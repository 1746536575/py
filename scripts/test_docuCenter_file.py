import time
import pytest

from base.base_analyze_149 import analyze_data
from page.docuCenter_file_page import docuCenter_filePage
from utils.driver_utils import DriverUtils

class TestLogin:
    def setup_method(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.docuCenter_file_page = docuCenter_filePage(self.driver)
        self.driver.get('https://llm-assistant-test1.pg-internal.aiadtech.cn/management/docuCenter/file/index?knowledgeId=147719906346033152&name=FC-%25E5%25A4%25A9%25E7%258C%25AB-%25E5%25B9%25B3%25E5%258F%25B0--20241111150610&isPublished=true')  # 打开目标网址
        time.sleep(2)
    def teardown_method(self):
        # 关闭浏览器
        time.sleep(5)  # 等待5秒以查看结果
        DriverUtils.quit_driver()
        # self.driver.quit()  # 关闭浏览器驱动


    def teardown_class(self):
        DriverUtils.set_switch(False)
        DriverUtils.get_driver().get_screenshot_as_file("./screenshot/bj.png")
        DriverUtils.quit_driver()

    def test_shangchuan(self):
        # 输入用户名和密码并进行登录
        self.docuCenter_file_page.click_daoru_btn()
        self.docuCenter_file_page.click_shangchuan_btn()

        # 验证文件路径
        file_path = r"D:\1.txt"  # 文件路径

        # 传入 driver 初始化 docuCenter_filePage 对象
        upload_page = docuCenter_filePage(self.docuCenter_file_page.driver)  # 确保传入 driver

        try:
            uploaded_file = upload_page.upload_file(file_path)  # 调用上传函数
            print(f"文件上传成功: {uploaded_file}")
        except Exception as e:
            print(f"文件上传失败: {e}")
            assert False, f"文件上传失败: {e}"  # 失败时断言
        self.docuCenter_file_page.click_tiqu_btn()