# -*- coding: utf-8 -*-
# author: hzuo
#利用钩子函数将测试结果写入数据库，为统计测试结果做数据支持

import pytest
from system.DBManage import LiteDB


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item,call):
    out = yield
    sqlite_db = LiteDB('test_results.db')
    c = sqlite_db.cursor

    report = out.get_result()
    if report.when == 'call':
        if 'pytestmark' in item.function.__dict__:
            for i in item.function.pytestmark:
                if 'info' in i.__dict__.values():

                    values = (report.location[0],report.location[-1],item.originalname,report.outcome,i.__dict__["kwargs"]["team"], i.__dict__["kwargs"]["author"])
                    keys = ('caseId', 'testId', 'test_name', 'result','team','principal')
                    sqlite_db.into('test_cases', keys, values)
                else:
                    values = (report.location[0], report.location[-1], item.originalname, report.outcome)
                    keys = ('caseId', 'testId', 'test_name', 'result')
                    sqlite_db.into('test_cases', keys, values)

        else:

            values = (report.location[0], report.location[-1], item.originalname, report.outcome)
            keys = ('caseId', 'testId', 'test_name', 'result')
            sqlite_db.into('test_cases', keys, values)
