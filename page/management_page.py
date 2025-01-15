from selenium.webdriver.common.by import By
from base.base_action_132 import BaseAction

class managementPage(BaseAction):
    
    docuCenter_btn = By.XPATH, "//*[@id='app']/div/div[2]/div[1]/ul/li[5]/span"

    msg_info = By.XPATH, "//*[@id='knowledge-container']/div[1]/div[3]/span"
    
    def click_docuCenter_btn(self):
        return self.click(self.docuCenter_btn)
    def get_msg(self):
        return self.find_el(self.msg_info).text