from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, Patch, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool, 
  HoverTool,
)
from bokeh.models.widgets import CheckboxButtonGroup
from bokeh.io import output_file, show, vform
#from bokeh.plotting import figure, show, output_file, ColumnDataSource
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment
from numpy import random as rand
import numpy as np
import csv

#stuff to read Anthony's test data csv file
data = []
with open('noah_data.csv', newline='') as csvfile:
    next(csvfile)
    datareader = csv.reader(csvfile)
    for row in datareader:
        if float(row[7]) > 0: #only keep wells with positive values
            data.append(row)
#lat = 3, lon = 4, depth = 7
counties = {
    code: county for code, county in counties.items() if county["state"] == "ca" #Select State
}
cname = 'Los Angeles' #Name of county

county_xs = [county["lons"] for county in counties.values() if county['name'] == cname]
county_ys = [county["lats"] for county in counties.values() if county['name'] == cname]
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"] #we can set colors here for different types, not currently used
county_names = [county['name'] for county in counties.values() if county['name'] == cname]
print(county_names)

#This block of code assumes we look at one country a time. Fundamentally we can do more, so this picks out the first one.
xc = county_xs[0]
yc = county_ys[0]
x_well = [float(well[4]) for well in data] #pulls out longitude of wells
y_well = [float(well[3]) for well in data] #pulls out latitude of wells
depth = [float(well[7]) for well in data] #pulls out well depth
rate = [d/max(depth) for d in depth] #normalized depth, used to set alpha of points
well_colors = ['blue' for d in depth] #right now everyone is blue, but we can give different water types different colors

#Code to randomly generate test points
#N = 10
#L = len(xc)
#ind = [[rand.randint(0,L),rand.randint(0,L)] for n in range(N)]
#x_well = [rand.uniform(xc[coord[0]],xc[coord[1]]) for coord in ind]
#y_well = [rand.uniform(yc[coord[0]],yc[coord[1]]) for coord in ind]
#well_rates = rand.random_integers(1,6,N)/6
#well_colors = ['blue' if rand.uniform() > .5 else 'red' for rate in well_rates]
#print(well_colors)

source = ColumnDataSource(data=dict( #This source is for well data
    color=well_colors,
    depth=depth,
    rate=rate,
    xw = x_well,
    yw = y_well,
))
source_boarder = ColumnDataSource(data=dict( #This source is only for the county boarder patch
    x=xc,
    y=yc,
))
TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"

#Sets up google maps stuff
map_options = GMapOptions(lat=np.nanmedian(yc), lng=np.nanmedian(xc), map_type='terrain', zoom=9)
p = GMapPlot(x_range=DataRange1d(), y_range=DataRange1d(), plot_width=1500, plot_height=800, map_options=map_options, title="Water Wells")

patch = Patch(x='x',y='y', fill_color ='grey', line_width = 0, fill_alpha =0.25) #Draws the county patch
p.add_glyph(source_boarder,patch)
circ = Circle(x='xw',y='yw',size=10, line_alpha = 0.0, fill_color='color', fill_alpha='rate', name='wells') #Draws the wells
circ_r = p.add_glyph(source,circ)

#p.line(xc, yc, line_color='black', line_width=1.0)
#p.patches('x', 'y', source=source,
#          fill_color='color', fill_alpha=0.0,
#          line_color="black", line_width=0.5)
hover = HoverTool()
hover.renderers = [circ_r]
p.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool(), hover)

#hover.point_policy = "follow_mouse"
hover.tooltips = [
   # ("Name", "@name"),
    ("(Well Level)", "@depth ft"),
    ("(Water Type)", "@color"),
    ("(Long, Lat)", "(@xw, @yw)"),
]


output_file("california.html", title="california.py example")


checkbox_button_group = CheckboxButtonGroup( #Checkbox group, currently doesn't work. Still figuring out how callbacks work on Bokeh.
        labels=["Groundwater", "Recycled"], active=[0, 1])
show(vform(checkbox_button_group,p))
