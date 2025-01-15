class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_el(self, feature):
        return self.driver.find_element(*feature)

    def find_els(self, feature):
        return self.driver.find_elements(*feature)

    def click(self, feature):
        return self.find_el(feature).click()

    def input(self, feature, content):
        return self.find_el(feature).send_keys(content)

    def clear(self, feature):
        return self.find_el(feature).clear()

        # 定义一个方法，用于根据指定的特征和数字查找单个元素
    def find_ele_num(self, feature, digit):
        # 使用格式化字符串将数字插入到特征的第二个元素中
        return self.driver.find_element(feature[0], feature[1].format(str(digit)))

    # 定义一个方法，用于切换到指定的框架
    def switch_to(self, frame_feature):
        # 根据给定的框架特征找到框架元素，并切换到该框架
        return self.driver.switch_to.frame(self.find_el(frame_feature))

    # 定义一个方法，用于切换回默认的内容
    def switch_to_default(self):
        # 切换回默认的内容
        return self.driver.switch_to.default_content()

    # 定义一个方法，用于切换到最新打开的窗口
    def switch_window(self):
        # 获取所有窗口的句柄
        handlers = self.driver.window_handles
        # 切换到最后一个窗口
        return self.driver.switch_to.window(handlers[-1])


