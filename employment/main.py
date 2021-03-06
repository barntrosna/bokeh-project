import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import layout, widgetbox
from bokeh.models import (ColumnDataSource, HoverTool, Text, Div, Circle,
                          SingleIntervalTicker, Slider, Button, Label, Range1d)

from bokeh.plotting import figure

# read data from csv
sub = pd.read_csv('subsectors2.csv', index_col='date', parse_dates=True)

years = list(range(2006, 2016))
sources = {}
# build a list of data sources - one for each year
for year in years:
    subyr = sub[sub.index.year==year]
    sources[year] = ColumnDataSource(data=dict(
        x=subyr.temp_pct,
        y=subyr.change2006,
        size=subyr.both / 750,
        sector=subyr.sector,
        numbers=subyr.both,
        change=subyr.change2006,
        temp=subyr.temp_pct,
        color=subyr.color,
    ))

# build plot
p = figure(plot_width=800, plot_height=600, title="Employment ",
    tools=['pan', 'wheel_zoom', 'reset']
    )
p.x_range = Range1d(0, 45)
p.y_range = Range1d(-60, 100)

# create object for circle glyphs so we can change the source
cir = p.circle('x', 'y', 
            size='size', color='color', alpha=0.7
            )
# add hover tooltip
hover = HoverTool(tooltips=[
        ("Sector", "@sector"),
        ("Numbers", "@numbers"),
        ("% Change", "@change"),
        ("% Non-Permanent", "@temp")
        ],
        renderers = [cir]
        )
p.add_tools(hover)

p.xaxis.ticker = SingleIntervalTicker(interval=10)
p.xaxis.axis_label = "Percentage of temporary workers"
p.yaxis.ticker = SingleIntervalTicker(interval=20)
p.yaxis.axis_label = "Percentage change since 2006"

# show the year as a label on the chart
label = Label(x=30, y=-50, text=str(years[0]), text_font_size='70pt', text_color='#cccccc')
p.add_layout(label)

# set initial data to first year
initial = 2006
cir.data_source.data = sources[initial].data
label.text = str(initial)

# update callback when slider value changes
# label and source for cir updated
def slider_update (attrname, old, new):
    year = slider.value
    label.text = str(year)
    cir.data_source.data = sources[year].data

# add slider
slider = Slider(start=years[0], end=years[-1], value=years[0], step=1, title="Year")
slider.on_change('value', slider_update)

layout = layout([
    [p],
    [slider],
], sizing_mode='scale_width')

curdoc().add_root(layout)
curdoc().title = "Employment"
