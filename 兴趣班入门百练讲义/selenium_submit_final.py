from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置 Chrome 选项
chrome_options = Options()
# 注释掉无头模式，以便查看浏览器操作
# chrome_options.add_argument('--headless')
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
    
    # 查找右上角登录按钮
    print("查找右上角登录按钮...")
    login_button = driver.find_element(By.XPATH, "//div[@class='btn-menu']/button")
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
    language_select = driver.find_element(By.XPATH, "//div[@class='ivu-select']")
    language_select.click()
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
    time.sleep(3)
    
    print("代码提交成功!")
    
    # 检查提交结果
    print("\n检查提交结果...")
    time.sleep(5)
    
    # 保存提交后的页面
    with open("submission_result.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("提交结果已保存到 submission_result.html")
    
finally:
    # 等待用户查看
    input("按 Enter 键关闭浏览器...")
    # 关闭浏览器
    driver.quit()
