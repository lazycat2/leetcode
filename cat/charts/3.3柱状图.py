from pyecharts import Bar, Pie,Grid
import pandas as pd
from pyecharts_javascripthon.dom import window
home_icon = "image://data:image/png;base64,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"

def switch_button():
    window.open('2.4_3.2各组出差费用组合图.html', '_self')

group01=[]
sheet0=pd.read_excel("./data_resources/3.3各组出差费用密度_拆.xls")
group02=sheet0["组名"].values.tolist()
for i in [ "售前组","领导组","销售组","硬件组","大数据云计算组",
          "软件组", "市场商务","综合管理"]:
    group01.append((i, sheet0[i].values.tolist()))
bar0 = Bar('各组出差费用密度', title_pos="10%")
for i in group01:
    if i[1] is not None:
        bar0.add(i[0],group02,i[1], xaxis_rotate=30, yaxis_name='出差数(元/人)', yaxis_name_pos='middle',yaxis_name_gap=50, legend_pos="40%", legend_top="2%", is_label_show=True,label_pos='inside', is_stack=True)
bar0.render("./all_charts/"+"3.3各组出差费用密度" + ".html")
# sheet1 = pd.read_excel("./data_resources/2.2每个组的出差天数柱状图和饼图.xls")
# group1 = sheet1["组名"].values.tolist()
# days1 = sheet1["出差天数（取整）"].values.tolist()
# pie1 = Pie('各组出差人天数比例', title_pos="55%")
# pie1.add('', group1, days1, radius=[45, 65], center=[65, 50], is_label_show=True, legend_pos="85%",
#          legend_orient="vertical", legend_top="20%", mark_point=['max'])
#
# bar0._option.get("toolbox").get("feature").update(
#     {
#         "myTool": {"show": True, "title": "switch", "icon": home_icon, "onclick": switch_button},
#     }
# )

# grid = Grid(width=1200)
# grid.add(bar0, grid_right="60%")
# grid.add(pie1, grid_left="70%")
# grid.render("./all_charts/" + "2.2_3.2各组出差人天数组合图" + ".html")