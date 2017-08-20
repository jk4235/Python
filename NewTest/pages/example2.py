# coding: utf-8
from page import page
class Example2(page):
    element_location = {
        'dingdanchuli': "//android.widget.TextView[contains(@text,'订单处理')]"
    }

E2 = Example2()