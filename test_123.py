import time
import pytest

from base.base_analyze_149 import analyze_data
from login_page_123 import LoginPage
from utils.driver_utils import DriverUtils



class TestLogin:
    def setup_method(self):
        self.driver = DriverUtils.get_driver()
        self.login_page = LoginPage(self.driver)
        self.driver.get(' http://cal.apple886.com/')  # 打开目标网址

    def teardown_method(self):
        # 关闭浏览器
        time.sleep(5)  # 等待5秒以查看结果
        DriverUtils.quit_driver()
        # self.driver.quit()  # 关闭浏览器驱动

    @pytest.mark.parametrize("params", analyze_data("login_data123.json"))
    def test_login(self, params):
        # 依次处理输入数据
        for i in params["data"]:
            self.login_page.click_one_input(i)  # 输入相应的值
            self.login_page.click_jia_input()  # 提示用户输入密码
        self.login_page.click_login_btn()  # 点击登录按钮
        assert self.login_page.get_msg() == str(params["result"])
        print(self.login_page.get_msg())

        # assert "登录成功" in self.driver.page_source
# 初始化 Chrome 浏览器驱动
# driver = webdriver.Chrome()

# # 初始化 ActionChains 对象，用于模拟鼠标和键盘操作
# Action=ActionChains(driver)
# # 模拟鼠标右键点击用户名输入框
# Action.context_click(username_input).perform()


# 使用 By 来查找元素
# element_size = driver.find_element(By.XPATH, "//input[@type='text' and @class='el-input__inner']").size
# print(element_size)  # 打印元素的大小

# username_input.clear()
# username_input.send_keys("ckfang.admin")
# denglu_click = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/button"))
# )
# denglu_click.send_keys(Keys.ENTER)
#title = driver.title
#print(title)