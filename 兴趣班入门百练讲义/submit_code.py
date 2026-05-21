import requests
import json

# 创建会话
session = requests.Session()
session.verify = False  # 忽略 SSL 验证

# 登录信息
login_url = "https://www.xmuoj.com/api/auth/login"
submit_url = "https://www.xmuoj.com/api/submissions"

# 用户信息
user_data = {
    "username": "andy",
    "password": "andy@5dg"
}

# 代码信息
code_data = {
    "problem_id": "GW003",
    "language": "C++",
    "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    char c;\n    cin >> c;\n    cout << static_cast<int>(c) << endl;\n    return 0;\n}\n"
}

try:
    # 登录
    print("正在登录...")
    login_response = session.post(login_url, json=user_data)
    print(f"登录状态码: {login_response.status_code}")
    print(f"登录响应: {login_response.text}")
    
    if login_response.status_code == 200:
        print("登录成功!")
        
        # 提交代码
        print("\n提交代码...")
        submit_response = session.post(submit_url, json=code_data)
        print(f"提交状态码: {submit_response.status_code}")
        print(f"提交响应: {submit_response.text}")
        
        if submit_response.status_code == 200:
            print("代码提交成功!")
        else:
            print("代码提交失败")
    else:
        print("登录失败")
        
        # 尝试其他登录路径
        print("\n尝试其他登录路径...")
        other_login_urls = [
            "https://www.xmuoj.com/api/login",
            "https://www.xmuoj.com/auth/login",
            "https://www.xmuoj.com/login"
        ]
        
        for url in other_login_urls:
            print(f"尝试登录到: {url}")
            other_login_response = session.post(url, json=user_data)
            print(f"状态码: {other_login_response.status_code}")
            print(f"响应: {other_login_response.text}")
            
            if other_login_response.status_code == 200:
                print("登录成功!")
                break
                
except Exception as e:
    print(f"发生错误: {e}")
