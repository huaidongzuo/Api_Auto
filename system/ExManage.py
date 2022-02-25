# -*- coding: utf-8 -*-
# author:hzuo
# 封装Excel读取测试数据的操作

import xlrd

class ExManage:

    def __init__(self,excel_name):
        self.__excel_name = excel_name


    def get_data(self,row_number,**kwargs):
        workbook = xlrd.open_workbook(filename=self.__excel_name)
        table =  workbook.sheet_by_index(0)
        keys = table.row_values(rowx=0)
        values = table.row_values(rowx=row_number)
        test_dics = dict(zip(keys,values))
        return test_dics










