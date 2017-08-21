#encoding=utf-8

import unittest
from findfile import find_file
from time import sleep
from driver.AndroidDriver import driver
from mainTest import operate_testcase


# def files(func):
#     def wapper(*args, **kwargs):
#         test_file_list = find_file('.', '.csv')
#         for f in test_file_list:
#             func(f)
#             sleep(2)
#             driver('close_app')
#             driver('start_activity')
#     return wapper


class TestCases(unittest.TestCase):

    # @files
    # def test_case(f):
    #     operate_testcase(f)

    def test_case(self):
        test_file_list = find_file('.', '.csv')
        for f in test_file_list:
            operate_testcase(f)
            sleep(2)
            driver('close_app')
            sleep(5)
            driver('start_activity')

    def tearDown(self):
        driver('quit')

if __name__ == '__main__':
    unittest.main()
