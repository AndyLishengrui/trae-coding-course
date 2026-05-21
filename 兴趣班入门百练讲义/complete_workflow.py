from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-certificate-errors')  # 忽略证书错误

# 启动浏览器
driver = webdriver.Chrome(options=chrome_options)

try:
    # 访问登录页面
    print("访问登录页面...")
    driver.get("https://www.xmuoj.com")
    time.sleep(3)
    
    # 查找登录按钮
    print("查找登录按钮...")
    try:
        # 尝试通过不同方式找到登录按钮
        login_buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in login_buttons:
            if "登录" in button.text:
                login_button = button
                break
        
        if 'login_button' in locals():
            print("点击登录按钮...")
            login_button.click()
            time.sleep(2)
            
            # 输入用户名和密码
            print("输入登录信息...")
            
            # 尝试找到输入框
            username_input = driver.find_element(By.XPATH, "//input[@placeholder='用户名']")
            password_input = driver.find_element(By.XPATH, "//input[@placeholder='密码']")
            
            username_input.send_keys("andy")
            password_input.send_keys("andy@5dg")
            
            # 提交登录
            submit_buttons = driver.find_elements(By.TAG_NAME, "button")
            for button in submit_buttons:
                if "登录" in button.text:
                    submit_button = button
                    break
            
            submit_button.click()
            time.sleep(3)
            
            print("登录成功!")
            
    except Exception as e:
        print(f"登录过程中出错: {e}")
    
    # 访问题目页面
    print("\n访问题目页面...")
    driver.get("https://www.xmuoj.com/problem/GW003")
    time.sleep(5)
    
    # 尝试获取题目描述
    print("\n尝试获取题目描述...")
    
    # 保存页面源代码到文件，以便分析
    with open("problem_page.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    
    print("页面源代码已保存到 problem_page.html")
    
    # 尝试查找题目描述部分
    try:
        problem_description = driver.find_element(By.CLASS_NAME, "problem-content")
        print("\n题目描述:")
        print(problem_description.text)
    except Exception as e:
        print(f"获取题目描述失败: {e}")
        
    # 尝试查找代码编辑器
    print("\n查找代码编辑器...")
    try:
        # 切换到 C++ 语言
        language_select = driver.find_element(By.XPATH, "//select[@name='language']")
        for option in language_select.find_elements(By.TAG_NAME, "option"):
            if "C++" in option.text:
                option.click()
                break
        
        # 输入代码
        code_editor = driver.find_element(By.TAG_NAME, "textarea")
        code = "#include <iostream>\nusing namespace std;\n\nint main() {\n    // 这里将根据题目要求编写代码\n    return 0;\n}"
        code_editor.send_keys(code)
        
        # 提交代码
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), '提交')]")
        submit_button.click()
        
        print("代码已提交!")
        
    except Exception as e:
        print(f"提交代码失败: {e}")
        
finally:
    # 关闭浏览器
    driver.quit()
