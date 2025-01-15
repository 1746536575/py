from selenium.webdriver.common.by import By
from base.base_action_132 import BaseAction

class LoginPage(BaseAction):
    # 用户名 输入框
    username_input = By.XPATH, "//input[@type='text' and @class='el-input__inner']"
    # 密码 输入框
    password_input = By.XPATH, "//input[@type='password' and @class='el-input__inner']"
    # 登录 按钮
    login_btn = By.XPATH, "//*[@id='app']/div/div[2]/div/button"
    # 提示信息
    msg_info = By.XPATH, "//span[text()='查询']"


    # 输入用户名
    def input_username(self, content):
        return self.input(self.username_input, content)
        # return self.find_el(self.username_input).send_keys(username)

    # 输入密码
    def input_password(self, content):
        return self.input(self.password_input, content)
        # return self.find_el(self.password_input).send_keys(password)

    # 点击登录按钮
    def click_login_btn(self):
        return self.click(self.login_btn)
        # return self.find_el(self.login_btn).click()

    # 获取提示信息
    def get_msg(self):
        return self.find_el(self.msg_info).text
