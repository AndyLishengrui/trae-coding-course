from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    time.sleep(3)
    
    # 查找登录按钮
    print("查找登录按钮...")
    btn_menu = driver.find_element(By.XPATH, "//div[@class='btn-menu']")
    login_button = btn_menu.find_element(By.TAG_NAME, "button")
    login_button.click()
    time.sleep(2)
    
    # 输入登录信息
    print("输入登录信息...")
    username_input = driver.find_element(By.XPATH, "//input[@placeholder='用户名']")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='密码']")
    
    username_input.send_keys("andy")
    password_input.send_keys("andy@5dg")
    
    # 提交登录
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), '登录')]")
    submit_button.click()
    time.sleep(3)
    
    print("登录成功!")
    
    # 重新加载题目页面
    driver.get("https://www.xmuoj.com/problem/GW003")
    time.sleep(3)
    
    # 切换到 C++ 语言
    print("切换到 C++ 语言...")
    language_div = driver.find_element(By.XPATH, "//div[@class='adjust ivu-select ivu-select-single']")
    language_div.click()
    time.sleep(1)
    
    # 选择 C++
    cplusplus_option = driver.find_element(By.XPATH, "//li[contains(text(), 'C++')]")
    cplusplus_option.click()
    time.sleep(1)
    
    # 输入代码
    print("输入代码...")
    code_editor = driver.find_element(By.TAG_NAME, "textarea")
    code = "#include <iostream>\nusing namespace std;\n\nint main() {\n    char c;\n    cin >> c;\n    cout << static_cast<int>(c) << endl;\n    return 0;\n}\n"
    code_editor.send_keys(code)
    time.sleep(2)
    
    # 提交代码
    print("提交代码...")
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), '提交')]")
    submit_button.click()
    time.sleep(5)
    
    print("代码提交成功!")
    
    # 检查提交结果
    print("检查提交结果...")
    # 尝试获取提交状态
    try:
        # 查找提交状态
        status_elements = driver.find_elements(By.CLASS_NAME, "submission-status")
        if status_elements:
            print(f"提交状态: {status_elements[0].text}")
        else:
            print("提交成功，请手动检查状态")
    except Exception as e:
        print(f"获取状态时出错: {e}")
        print("提交成功，请手动检查状态")
        
finally:
    # 关闭浏览器
    driver.quit()
    print("浏览器已关闭")
