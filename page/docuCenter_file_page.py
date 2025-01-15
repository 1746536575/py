from selenium.webdriver.common.by import By
from base.base_action_132 import BaseAction
import os
import time
import pyautogui
class docuCenter_filePage(BaseAction):
      daoru_btn = By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/button[2]/span"
      shangchuan_btn = By.XPATH, "//div[@class='el-upload-dragger']"

      tiqu_btn = By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/button[2]"
      reflish_btn = By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/button[1]/span"

      def click_daoru_btn(self):
        return self.click(self.daoru_btn)
      def click_shangchuan_btn(self):
        return self.click(self.shangchuan_btn)
      def click_tiqu_btn(self):
        return self.click(self.tiqu_btn)

      def upload_file(self, filepath):
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
          except FileNotFoundError as fnf_error:
              print(f"文件未找到异常: {fnf_error}")
              raise
          except Exception as e:
              print(f"上传文件操作异常: {e}")
              raise
          else:
              return filepath
      
      def click_reflish_btn(self):
          time.sleep(2)
          return self.click(self.reflish_btn)
