#coding= utf-8
from appium import webdriver

driver_caps = {}
driver_caps['platformName'] = 'Android'
driver_caps['platformVersion'] = '5.0'
driver_caps['deviceName'] = '192.168.226.101:5555'
driver_caps['automationName'] = 'Appium'
driver_caps['appPackage'] = 'com.gongzhidao.nobel'
driver_caps['appActivity'] = '.login.SplashActivity'
driver_caps['appWaitActivity'] = '.login.SplashActivity, .common.activity.MainActivity'
driver_caps['unicodeKeyboard'] = 'True'
driver_caps['resetKeyboard'] = 'True'
driver_caps['noReset'] = 'True'

android_driver = webdriver.Remote('http://localhost:4723/wd/hub', driver_caps)


def driver(xpath, wait=10):
    if xpath == 'close_app':
        android_driver.close_app()
    elif xpath == 'start_activity':
        try:
            android_driver.start_activity('com.gongzhidao.nobel', '.login.SplashActivity')
        except Exception:
            pass
    elif xpath == 'quit':
        android_driver.quit()
    else:
        android_driver.implicitly_wait(wait)
        try:
            elem = android_driver.find_element_by_xpath(xpath)
            return elem
        except Exception:
            elem = android_driver.find_element_by_id(xpath)
            return elem
