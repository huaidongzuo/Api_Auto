# -*- coding: utf-8 -*-
# author:hzuo
# 封装统计测试结果

from system.DBManage import LiteDB

def days_count():
    """
    以时间周期为维度去统计各项目的质量情况
    :return:
    """
    results = dict()
    dates = list()
    tests = list()
    errs = list()

    sqlite_db = LiteDB('test_results.db')
    dql_results = sqlite_db.query(f"""select * from test_cases where datetime>=datetime('now','start of day','-7 day') and datetime<=datetime('now','start of day','+1 day') ORDER BY datetime""")

    for result in dql_results:
        date = str(result['datetime'].split()[0])
        if date not in dates:
            dates.append(date)

    for date in dates:
        dql_results = sqlite_db.query(f"""SELECT count(*) as count from test_cases WHERE datetime like '{date}%'""")
        tests.append(dql_results[0]['count'])

        dql_results = sqlite_db.query(f"""SELECT count(*) as count from test_cases WHERE datetime like '{date}%' and result != 'passed'""")
        errs.append(dql_results[0]["count"])
    results.update({
        "dates" : dates,
        "tests" : tests,
        "errs"  : errs
    })
    return results

def team_count():
    """
        以项目团队为维度去统计各项目的质量情况
        :return:
    """
    results = dict()
    teams = list()
    tests = list()
    errs = list()

    sqlite_db = LiteDB('test_results.db')

    dql_results = sqlite_db.query("""SELECT team from test_cases group by team""")
    for i in dql_results:
        teams.append(i['team'])

    for i in teams:
        dql_results = sqlite_db.query(f"""SELECT count(*) as count from test_cases where team == '{i}'""")
        tests.append(dql_results[0]["count"])

        dql_results = sqlite_db.query(f"""SELECT count(*) as count from test_cases where team == '{i}' and result != 'passed'""")
        errs.append(dql_results[0]["count"])

    results.update({
        'teams' : teams,
        'tests' : tests,
        'errs'  : errs
    })

    return results