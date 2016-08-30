import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import layout, widgetbox, gridplot
from bokeh.plotting import figure
from bokeh.charts import Bar
from bokeh.models import (ColumnDataSource, HoverTool, Text, Div, Circle,
                          SingleIntervalTicker, Slider, Button, Label, Range1d,
                           LabelSet, Label)
import numpy as np
import math


def make_today(col):
    return pd.to_datetime(col, infer_datetime_format=True)

calls = pd.read_csv('calls_one_day.csv')

calls['time'] = make_today(calls['vru_entry'])
calls.index = calls.time

calls = calls.sort_values(by='time')
del calls['time']
del calls['server']

now = pd.datetime.now()
#now = pd.datetime(2016, 8, 30, 14, 25, 10, 733298)
past = calls[calls.index < now]

q = past.loc[:,['q_time','q_exit', 'outcome', 'server_abv']]
q = q[(q['outcome'] == 'AGENT') 
      | ((q['q_time'] > 0) & (make_today(q['q_exit']) < now))]
     

def within_sla(row):
    if row['q_time'] <= 300:
        val = 1
    else:
        val = 0
    return val

def service(row):
    if row['outcome'] == "AGENT":
        ser = 1
    else:
        ser = 0
    return ser

q['sla'] = q.apply(within_sla, axis=1) 
q['ser'] = q.apply(service, axis=1)
q['sla20ma'] = pd.Series(q['sla']).rolling(window=20).mean()
q['ser20ma'] = pd.Series(q['ser']).rolling(window=20).mean()
q['q_time20ma'] = pd.Series(q['q_time']).rolling(window=20).mean()

total_calls = len(past.index)
total_queued = len(q.index)
q_percent = round((total_queued * 100) / total_calls, 1)
#total_q_over_sla = len(q[q['q_time'] > 300].index)

sla_today = round(q.sla.mean() * 100, 1)
ser_today = round(q.ser.mean() * 100, 1)

avg_current_sla = round(q.iloc[-1, 6] * 100, 1)
avg_current_ser = round(q.iloc[-1, 7] * 100, 1)
avg_current_wait = int(q.iloc[-1, 8])

avg_call_length = int(past.ser_time[past.ser_time > 0].mean())
total_call_time = past.ser_time.sum()

waiting = past[make_today(past['q_exit']) > now]
calls_waiting = len(waiting.index)
oldest_waiting = make_today(waiting['q_start']).min()
wait = (now - oldest_waiting).total_seconds()

if math.isnan(wait):
    longest_waiting = 0
else:
    longest_waiting = int(wait)
lw_sla = round((longest_waiting) / 3, 1)

q200 = q.tail(100)
service = figure(plot_width=1000, plot_height=500, title="Time in Queue - last 100 calls",
                 x_axis_type="datetime", x_axis_label="Time", y_axis_label="Queue time (seconds)")
service.line(x=q200.index, y=q200['q_time'], line_width=2, color='grey', alpha=0.6, legend="Q time")
service.circle(x=q200.index, y=q200['q_time'], size=5, color='grey', alpha=0.6, legend="Q time")
service.line(x=q200.index, y=300, line_width=2, line_dash=[2,2], color='red', alpha=0.8,
    legend="300 seconds")
service.line(x=q200.index, y=q200['q_time20ma'], line_width=4, color='teal', alpha=1,
    legend="Moving average 20")


q50 = q.tail(50)
bar = Bar(q50, 'server_abv', 
        title="Agents - last 50 calls", color='teal',
        width=350, height=300, legend=False,
        xlabel="Agent", ylabel="Calls",
        )

centre = [q_percent, lw_sla, avg_current_sla, avg_current_ser]
angle = []
percent = []

for c in centre:
    angle.append((3.6 * (100 - c)) + 90)
    percent.append('{0}%'.format(c))

wd = dict(
    xs = [1, 3, 5, 7],
    ys = [1, 1, 1, 1],
    t1 = ['Total calls today', 'Calls waiting', 'Answered within SLA', 'Abandoned in queue'],
    h1 = ['Calls received', 'Waiting now', 'Today', 'Today'],
    h2 = ['% q or service', 'Longest waiting', 'Current', 'Current'],
    n1 = [total_calls, calls_waiting, sla_today, ser_today],
    n2 = [total_queued, longest_waiting, avg_current_sla, avg_current_ser],    
    percent = percent,
    angle = angle
)

source = ColumnDataSource(wd)

w = figure(width=1350, height=300, x_range=Range1d(0,9), y_range=Range1d(0,2))
w.annular_wedge('xs', 'ys', inner_radius=0.25, outer_radius=0.4, source=source,
               end_angle_units='deg', start_angle_units='deg', direction='clock',
                start_angle=90, end_angle='angle', color="teal", alpha=0.9)
w.text('xs', 'ys', text='percent', text_font_size="14pt", source=source,
    text_align="center", text_baseline="middle", color='teal')
w.text('xs', 'ys', text='t1', source=source, text_font_size='16pt', 
    text_color='grey', x_offset=0, y_offset=-80,
    text_align="left", text_baseline="middle", color='teal')
w.text('xs', 'ys', text='h1', source=source, text_font_size='13', 
    text_color='grey', x_offset=70, y_offset=-30,
    text_align="left", text_baseline="middle", color='teal')
w.text('xs', 'ys', text='h2', source=source, text_font_size='13', 
    text_color='grey', x_offset=70, y_offset=10,
    text_align="left", text_baseline="middle", color='teal')
w.text('xs', 'ys', text='n1', source=source, text_font_size='14pt', 
    text_color='black', x_offset=70, y_offset=-10,
    text_align="left", text_baseline="middle", color='teal')
w.text('xs', 'ys', text='n2', source=source, text_font_size='14pt', 
    text_color='black', x_offset=70, y_offset=30,
    text_align="left", text_baseline="middle", color='teal')
w.xaxis.visible = False
w.xgrid.visible = False
w.yaxis.visible = False
w.ygrid.visible = False

'''
layout = layout([
        [w],
        [service, bar]
    ], sizing_mode='stretch_both')
'''
# make a grid
grid = gridplot([[w], [service, bar]])

curdoc().add_root(grid)
curdoc().title = "Calls"
