from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from pyecharts import options as opts
import pandas as pd

path = input('请输入文件路径')
name = input('请输入csv名称')
pf = pd.read_csv(path+"\\"+name+'.csv')

line = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, page_title='{}line'.format(name), width='1600px', height='600px'))

x_data = pf['日期'].to_list()
x_data.reverse()
line.add_xaxis(xaxis_data=x_data)
y_data = pf['收盘'].astype(float).tolist()
y_data.reverse()
line.add_yaxis(series_name='{}收盘价'.format(name), y_axis=y_data)


line.render(path+"\\"+'{}.html'.format(name))
