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
    # 访问题目页面
    print("访问题目页面...")
    driver.get("https://www.xmuoj.com/problem/GW003")
    time.sleep(5)
    
    # 保存当前页面以查看结构
    with open("current_page.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("页面已保存到 current_page.html")
    
    # 查找登录按钮
    print("查找登录按钮...")
    
    # 尝试通过不同方式找到登录按钮
    try:
        # 方式 1: 通过文本内容查找
        login_buttons = driver.find_elements(By.TAG_NAME, "button")
        login_button = None
        for button in login_buttons:
            if "登录" in button.text:
                login_button = button
                break
        
        if login_button:
            print("找到登录按钮，点击...")
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
            submit_button = None
            for button in submit_buttons:
                if "登录" in button.text:
                    submit_button = button
                    break
            
            if submit_button:
                submit_button.click()
                time.sleep(3)
                print("登录成功!")
                
                # 重新访问题目页面
                driver.get("https://www.xmuoj.com/problem/GW003")
                time.sleep(3)
                
                # 切换到 C++ 语言
                print("切换到 C++ 语言...")
                language_div = driver.find_element(By.XPATH, "//div[@class='ivu-select']")
                language_div.click()
                time.sleep(1)
                
                # 选择 C++
                cplusplus_option = driver.find_element(By.XPATH, "//li[contains(text(), 'C++')]")
                cplusplus_option.click()
                time.sleep(1)
                
                # 输入代码
                print("输入代码...")
                # 找到代码编辑器
                code_editor = driver.find_element(By.TAG_NAME, "textarea")
                code = "#include <iostream>\nusing namespace std;\n\nint main() {\n    char c;\n    cin >> c;\n    cout << static_cast<int>(c) << endl;\n    return 0;\n}\n"
                code_editor.send_keys(code)
                time.sleep(2)
                
                # 提交代码
                print("提交代码...")
                submit_buttons = driver.find_elements(By.TAG_NAME, "button")
                submit_button = None
                for button in submit_buttons:
                    if "提交" in button.text:
                        submit_button = button
                        break
                
                if submit_button:
                    submit_button.click()
                    time.sleep(3)
                    print("代码提交成功!")
                else:
                    print("未找到提交按钮")
            else:
                print("未找到登录提交按钮")
        else:
            print("未找到登录按钮")
            
    except Exception as e:
        print(f"登录过程中出错: {e}")
        
finally:
    # 关闭浏览器
    driver.quit()
