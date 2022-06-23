from ctypes.wintypes import RGB
from turtle import *

def set_theme(canvas_width = 1000,
                            canvas_height = 1000,
                            #canvas_color = (232/255,  210/255,  210/255),
                            canvas_color = (0,0,0),
                            #pen_color = (94/255, 71/255, 69/255),
                            pen_color = (255/255,255/255,255/255),
                            thickness = 1,
                            speed_value = 0,
                            tracer_value=False,
                            hide_turtle = False
):

                            setup(canvas_width, canvas_height)
                            bgcolor(canvas_color)
                            color(pen_color)
                            width(thickness)
                            speed(speed_value)
                            tracer(tracer_value)

                            if hide_turtle:
                                hideturtle()