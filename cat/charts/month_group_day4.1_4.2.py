from pyecharts import Bar, Line, Grid
import pandas as pd

sheet0 = pd.read_excel("./data_resources/4.1各月出差天数.xls")
month0 = sheet0["2018年"].values.tolist()
days0 = sheet0["出差天数"].values.tolist()
line0 = Line('各月出差人天数比例', title_pos="10%")
line0.add('2018年月份',month0,days0, yaxis_name = '出差数(天)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="35%",is_label_show = True,label_text_size = 10,mark_point = ['max'])

group = []
sheet1 = pd.read_excel("./data_resources/4.2各月每个组出差天数统计表格.xls")
dates1 = sheet1["2018年月份"].values.tolist()
for i in ["综合管理", "领导组", "硬件组", "销售组", "售前组",
          "市场商务", "软件组", "大数据云计算组"]:
    group.append((i, sheet1[i].values.tolist()))

bar1 = Bar('各月各组出差人天数排名',title_pos="65%")
for i in group:
    bar1.add(i[0], dates1, i[1], label_text_size=6,yaxis_name = '出差数(天)',yaxis_name_pos = 'middle',yaxis_name_gap = 40,legend_pos="85%",legend_orient="vertical", is_stack=True,bar_category_gap='10%')
bar1.render("./all_charts/" + "4.2各月每个组出差天数" + ".html")


grid = Grid(width=1200)
grid.add(line0, grid_right="55%")
grid.add(bar1, grid_left="55%")
grid.render("./all_charts/"+"4.1_4.2各月各组出差人天数组合图"+".html")