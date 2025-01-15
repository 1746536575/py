import time
import pytest
import logging
from base.base_analyze_149 import analyze_data
from page.management_page import managementPage
from page.docuCenter_page import docuCenterPage
from utils.driver_utils import DriverUtils

class TestLogin:
    def setup_method(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.management_page= managementPage(self.driver)
        self.docuCenter_page = docuCenterPage(self.driver)
        self.driver.get('https://llm-assistant-test1.pg-internal.aiadtech.cn/management/callLog')  # 打开目标网址
        time.sleep(2)
    def teardown_method(self):
        # 关闭浏览器
        time.sleep(5)  # 等待5秒以查看结果
        DriverUtils.quit_driver()
        # self.driver.quit()  # 关闭浏览器驱动

    def test_in_docuCenter(self):
            # 点击文档中心按钮
            self.management_page.click_docuCenter_btn()

            # 验证是否跳转到正确的页面
            assert self.management_page.get_msg() == "发布状态"
            print(self.management_page.get_msg())
            # 点击文件按钮
            time.sleep(2)
            logging.info("waiting for 2 seconds")
            self.docuCenter_page.click_docuCenter_file_btn()

            # 验证文件按钮的消息
            assert self.docuCenter_page.get_msg() == "发布"
            print(self.docuCenter_page.get_msg())
        