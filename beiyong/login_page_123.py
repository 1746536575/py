from selenium.webdriver.common.by import By
from base.base_action_132 import BaseAction

class LoginPage(BaseAction):
    # 用户名 输入框
    one_input = By.ID, "simple{}"
    # 密码 输入框
    jia_input = By.XPATH, "//*[@id='simpleAdd']"
    # 登录 按钮
    login_btn = By.XPATH, "//*[@id='simpleEqual']"
    # 提示信息
    msg_info = By.XPATH, "//*[@id='resultIpt']"


    # 输入用户名
    def click_one_input(self,num):
        return self.find_ele_num(self.one_input,num).click()
        # return self.find_el(self.username_input).send_keys(username)

    # 输入密码
    def click_jia_input(self):
        return self.click(self.jia_input)
        # return self.find_el(self.password_input).send_keys(password)

    # 点击登录按钮
    def click_login_btn(self):
        return self.click(self.login_btn)
        # return self.find_el(self.login_btn).click()

    # 获取提示信息
    def get_msg(self):
        return self.find_el(self.msg_info).get_attribute("value")
