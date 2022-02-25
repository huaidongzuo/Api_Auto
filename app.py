# -*- coding: utf-8 -*-
# 构建路由，通过web将测试结果图形化展示
# author:hzuo
from flask import Flask,render_template
from jinja2 import Environment,FileSystemLoader
from markupsafe import Markup
from pyecharts.globals import  CurrentConfig,ThemeType
from pyecharts import options as opts
from pyecharts.charts import Bar,Grid
from statistics.Conventional import days_count as dc
from statistics.Conventional import team_count as tc

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader('./templates'))
app = Flask(__name__,static_folder='./statics')

@app.route("/")
def day_count():
    data1 = dc()
    data2 = tc()

    title = "自动化测试数据监控"

    c1 = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(data1['dates'])
            .add_yaxis('测试用例',data1["tests"])
            .add_yaxis('异常用例',data1['errs'])
            .set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle="近七天自动化项目情况"))
    )

    c2 = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(data2["teams"])
            .add_yaxis("测试用例", data2["tests"])
            .add_yaxis("异常数量", data2["errs"])
            .set_global_opts(title_opts=opts.TitleOpts(title=title, pos_top="48%", subtitle="项目团队质量情况"),
                             legend_opts=opts.LegendOpts(pos_top="48%"), )
    )

    grid = (
        Grid()
            .add(c1,grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(c2, grid_opts=opts.GridOpts(pos_top="60%"))
    )

    return Markup(grid.render_embed())

if __name__ == '__main__':
    app.run(debug=True)