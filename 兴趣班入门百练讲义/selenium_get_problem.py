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
    
    # 等待页面加载
    time.sleep(5)  # 等待 5 秒让页面加载
    
    # 获取页面源代码
    page_source = driver.page_source
    print("\n页面源代码:")
    print(page_source)
    
    # 尝试获取题目内容
    print("\n尝试获取题目内容...")
    
    # 检查是否有登录按钮
    try:
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), '登录')]")
        print("发现登录按钮，准备登录...")
        
        # 点击登录按钮
        login_button.click()
        time.sleep(2)
        
        # 输入用户名和密码
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        
        username_input.send_keys("andy")
        password_input.send_keys("andy@5dg")
        
        # 提交登录
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), '登录')]")
        submit_button.click()
        time.sleep(3)
        
        # 重新获取页面
        page_source = driver.page_source
        print("\n登录后页面源代码:")
        print(page_source)
        
    except Exception as e:
        print(f"登录过程中出错: {e}")
        
finally:
    # 关闭浏览器
    driver.quit()
