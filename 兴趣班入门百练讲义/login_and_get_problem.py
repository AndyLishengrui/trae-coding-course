import requests
from bs4 import BeautifulSoup
import json

# 登录并获取题目内容
def login_and_get_problem():
    # 登录信息
    login_url = "https://www.xmuoj.com/api/auth/login"
    problem_url = "https://www.xmuoj.com/problem/GW003"
    
    # 用户信息
    user_data = {
        "username": "andy",
        "password": "andy@5dg"
    }
    
    # 创建会话
    session = requests.Session()
    session.verify = False  # 忽略 SSL 验证
    
    try:
        # 登录
        print("正在登录...")
        login_response = session.post(login_url, json=user_data)
        print(f"登录状态码: {login_response.status_code}")
        print(f"登录响应: {login_response.text}")
        
        if login_response.status_code == 200:
            print("登录成功!")
            
            # 获取题目页面
            print("\n获取题目页面...")
            problem_response = session.get(problem_url)
            problem_response.encoding = 'utf-8'
            
            print(f"题目页面状态码: {problem_response.status_code}")
            print("\n题目页面内容:")
            print(problem_response.text)
            
            # 尝试查找 API 调用
            print("\n尝试查找 API 调用...")
            # 检查是否有 JavaScript 中的 API 调用
            if 'api' in problem_response.text:
                print("发现可能的 API 调用")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    login_and_get_problem()
