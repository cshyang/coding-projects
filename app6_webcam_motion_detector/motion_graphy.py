from motion_detector import df
from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type='datetime', width=500, height=100, sizing_mode="stretch_both")
p.title.text= "Motion Graph"
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks= 1

p.quad(left= df["Start"], right= df["End"], bottom= 0, top= 1, color='green')
output_file = "motion_graph.html"

show(p)