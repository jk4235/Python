# coding: utf-8
from page import page

class Example(page):
    element_location = {
        'paiban':"//android.widget.TextView[contains(@text,'排班')]"
    }


E1 = Example()