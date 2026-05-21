import requests
from bs4 import BeautifulSoup

# 尝试直接获取页面
def get_problem_content():
    url = "https://www.xmuoj.com/problem/GW003"
    
    try:
        # 设置请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        # 发送请求，忽略 SSL 验证
        response = requests.get(url, headers=headers, verify=False)
        response.encoding = 'utf-8'
        
        if response.status_code == 200:
            print("获取页面成功")
            print("页面内容:")
            print(response.text[:5000])  # 打印前 5000 字符
            
            # 尝试解析题目内容
            soup = BeautifulSoup(response.text, 'html.parser')
            print("\n解析结果:")
            print(soup.prettify()[:5000])
        else:
            print(f"获取页面失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    get_problem_content()
