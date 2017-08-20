# coding: utf-8
from driver.AndroidDriver import driver

class page(object):
    element_location = {}
    def find_elem(self,str):
        return driver(self.element_location[str])