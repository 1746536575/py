from selenium.webdriver.common.by import By
from base.base_action_132 import BaseAction
class docuCenterPage(BaseAction):
    docuCenter_file_btn = By.XPATH, "//*[@id='knowledge-container']/div[2]/div[1]/div/div[2]"
    # 提示信息
    msg_info = By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[1]/div/button[2]/span"
    
    def click_docuCenter_file_btn(self):

        return self.click(self.docuCenter_file_btn)
        # return self.click(self.docuCenter_file_btn)
     

    # 获取提示信息
    def get_msg(self):
        return self.find_el(self.msg_info).text