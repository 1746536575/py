# 1. 导包
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui

# 从 selenium.webdriver.chrome.service 模块导入 Service 类，并重命名为 ChromeService
from selenium.webdriver.chrome.service import Service as ChromeService

# 从 webdriver_manager.chrome 模块导入 ChromeDriverManager 类
from webdriver_manager.chrome import ChromeDriverManager
# 创建一个 ChromeOptions 对象，用于配置 Chrome 浏览器的启动选项
options = webdriver.ChromeOptions()
# 添加一个启动参数，允许访问不安全的本地主机
options.add_argument("--allow-insecure-localhost")
# 添加一个启动参数，将指定的不安全来源视为安全的，这里使用了 http://your-unsecure-url

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)




# 2. 创建浏览器驱动对象
# driver = webdriver.Chrome()

# 3. 打开主页
driver.get('https://llm-assistant-test1.pg-internal.aiadtech.cn/login')
# 最大化窗口，以便更好地查看页面内容
driver.maximize_window()
# 设置隐式等待时间为10秒
driver.implicitly_wait(10)

# 4. 等待用户名输入框可见并输入用户名
username_input = driver.find_element(By.XPATH, "//input[@type='text' and @class='el-input__inner']")
username_input.send_keys("ckfang.admin")
# # 初始化 ActionChains 对象，用于模拟鼠标和键盘操作
# Action=ActionChains(driver)
# # 模拟鼠标右键点击用户名输入框
# Action.context_click(username_input).perform()


# 使用 By 来查找元素
# element_size = driver.find_element(By.XPATH, "//input[@type='text' and @class='el-input__inner']").size
# print(element_size)  # 打印元素的大小
# 5. 等待密码输入框可见并输入密码

password_input = driver.find_element(By.XPATH, "//input[@type='password' and @class='el-input__inner']")
password_input.send_keys("123456")

# 6. 暂停3秒以查看结果
time.sleep(2)
# username_input.clear()
# username_input.send_keys("ckfang.admin")
denglu_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/button"))
)
# denglu_click = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div/button")
denglu_click.send_keys(Keys.ENTER)
# denglu_click.click()
#title = driver.title
#print(title)
wendang_click = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[1]/ul/li[5]/span")
wendang_click.click()

# keyong_xiala_click = driver.find_element(By.XPATH, "//*[@id='knowledge-container']/div[1]/div[2]/div/div/div[1]/input")
# keyong_xiala_click.click()
#
# ceshituandui_click = driver.find_element(By.XPATH, "//span[text()='测试团队B']")
# ceshituandui_click.click()
#
# ceshituandui_click = driver.find_element(By.XPATH, "//span[text()='测试团队A']")
# ceshituandui_click.click()


# wendang_one_click = driver.find_element(By.XPATH, "//*[@id='knowledge-container']/div[2]/div[1]/div/div[2]")
# wendang_one_click.click()
time.sleep(2)
wendang_one_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id='knowledge-container']/div[2]/div[1]/div/div[2]"))
)
wendang_one_click.click()
# keyong_click= driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[1]/div/button[1]/span")
# keyong_click.click()
#
# queding_click = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div/footer/div/button[2]")
# queding_click.click()
daoru_click =driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/button[2]/span")
daoru_click.click()

time.sleep(2)
shangchuan_click = driver.find_element(By.XPATH, "//div[@class='el-upload-dragger']")
shangchuan_click.click()



import os
def uploadWinFile(filepath):
    '''
    通过Windows系统上传文件
    '''
    # 检查文件是否存在
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"文件未找到: {filepath}")

    try:
        time.sleep(1)  # 等待对话框加载，确保时间足够
        pyautogui.write(filepath)  # 输入文件绝对路径
        time.sleep(1)  # 等待输入完成
        pyautogui.press('enter', presses=2)  # 按2次回车键
    except Exception as e:
        print(f"上传文件操作异常: {e}")
        raise
    else:
        return filepath

# 使用示例
if __name__ == '__main__':
    file_path = r"D:\1.txt"  # 文件路径
    uploadWinFile(file_path)  # 调用上传函数
time.sleep(5)
tiqu_click = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/button[2]")
tiqu_click.click()
#time.sleep(5)
#driver.refresh()
time.sleep(10)
# 7. 关闭驱动
driver.quit()