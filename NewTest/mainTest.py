# encoding: utf-8
import csv
import codecs
from driver.AndroidDriver import driver
from selenium.webdriver.remote.webelement import WebElement


def operate_testcase(filepath):
    with codecs.open(filepath) as csvfile:
        filename = filepath.split('.')[0]
        print filename
        #filename = filename.encode('utf-8')
        steps = csv.DictReader(csvfile)

        for step in steps:
            try:
                if step['action'] == 'is_in':
                    try:
                        driver(step['xpath'])
                        if step['paras'] == 'yes':
                            print filename + ' test is ok!'
                        else:
                            print filename + ' test is not ok!'
                    except Exception:
                        if step['paras'] == 'yes':
                            print filename + ' test is not ok!'
                        else:
                            print filename + ' test is ok!'
                    finally:
                        return

                if step['wait'] == '':
                    target_elem = driver(step['xpath'])
                else:
                    target_elem = driver(step['xpath'], int(step['wait']))
                if step['paras'] == '':
                    getattr(WebElement, step['action'], 'wrong func name!')(target_elem)
                else:
                    getattr(WebElement, step['action'], 'wrong func name!')(target_elem, step['paras'])
            except Exception as e:
                print step['xpath']
                print e
                print filename + ' ' + step['﻿element_name'] + ' is not ok!'
                return
        print filename + ' test is ok!'
