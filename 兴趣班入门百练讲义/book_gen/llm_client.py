import os
import requests
import json
import time
from openai import OpenAI
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions

class LLMClient:
    def __init__(self, api_key=None, base_url=None, model=None):
        # 1. Setup Doubao (Primary)
        self.doubao_api_key = os.getenv("DOUBAO_API_KEY", "7a315dcf-8ffc-4653-9c5d-b9e7cbd51ce6")
        self.doubao_base_url = "https://ark.cn-beijing.volces.com/api/v3"
        self.doubao_model = "rpi-20251204210214-h26bj" # Updated based on user request
        
        self.doubao_client = OpenAI(
            api_key=self.doubao_api_key,
            base_url=self.doubao_base_url
        )
        
        # 2. Setup Gemini (Fallback)
        self.gemini_key = os.getenv("GEMINI_API_KEY")
        self.gemini_ready = False
        if self.gemini_key:
             try:
                genai.configure(api_key=self.gemini_key)
                self.gemini_model_name = "gemini-flash-latest" 
                # self.gemini_model_name = "gemini-2.0-flash" 
                self.gemini_ready = True
             except:
                print("Gemini config failed.")

        print(f"LLM Client initialized. Primary: Doubao ({self.doubao_model}) | Secondary: Gemini ({self.gemini_ready})")

    def _call_doubao(self, prompt, retries=1):
        for i in range(retries):
            try:
                response = self.doubao_client.chat.completions.create(
                    model=self.doubao_model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant. Please output strictly in JSON format."},
                        {"role": "user", "content": prompt}
                    ],
                    stream=False
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"[Doubao] Error: {e}")
                if "429" in str(e) or "limit" in str(e).lower():
                    time.sleep(2)  # Short sleep for rate limit
                    continue
                break # Non-retryable error
        raise Exception("Doubao failed")

    def _call_gemini(self, prompt, retries=1):
        if not self.gemini_ready:
            raise Exception("Gemini not configured")
            
        for i in range(retries):
            try:
                model = genai.GenerativeModel(self.gemini_model_name)
                response = model.generate_content(
                    prompt,
                    generation_config={"response_mime_type": "application/json"}
                )
                return response.text
            except Exception as e:
                print(f"[Gemini] Error: {e}")
                if "429" in str(e) or "Quota" in str(e) or "503" in str(e):
                    time.sleep(10) # Longer sleep for Gemini
                    continue
                break
        raise Exception("Gemini failed")

    def _call_llm(self, prompt):
        # Strategy: Try Doubao first (Primary), then Gemini (Secondary)
        
        # Attempt 1: Doubao
        try:
            content = self._call_doubao(prompt, retries=2)
            return self._parse_json(content)
        except Exception as e:
            print(f"Primary (Doubao) failed: {e}. Switching to Secondary (Gemini)...")
            
        # Attempt 2: Gemini
        try:
            content = self._call_gemini(prompt, retries=2)
            return self._parse_json(content)
        except Exception as e:
            print(f"Secondary (Gemini) failed: {e}.")
            
        raise Exception("All LLM providers failed.")

    def _parse_json(self, content):
        try:
            # Cleanup Markdown wrappers
            clean_content = content.replace('```json', '').replace('```', '').strip()
            return json.loads(clean_content)
        except json.JSONDecodeError:
            # Fallback: try to find first { and last }
            start = content.find('{')
            end = content.rfind('}')
            if start != -1 and end != -1:
                return json.loads(content[start:end+1])
            raise

    def generate_content(self, problem_data):
        prompt = f"""
你是一名专业的算法竞赛教练。请根据以下题目，生成教材内容。

【题目标题】: {problem_data.get('title')}
【题目描述】: {problem_data.get('description')}
【输入描述】: {problem_data.get('input_description')}
【输出描述】: {problem_data.get('output_description')}
【样例】: {problem_data.get('samples')}
【提示】: {problem_data.get('hint', '')}

请以JSON格式返回：
1. analysis: 解题思路 (Markdown)
2. code: C++标准代码 (包含头文件, Google Style)

JSON Format:
{{
  "analysis": "...",
  "code": "..."
}}
"""
        return self._call_llm(prompt)
