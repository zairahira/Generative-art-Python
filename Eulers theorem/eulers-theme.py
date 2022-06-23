from turtle import *
from theme import set_theme
import random


def euler_curve(step_size, angle_step, n_steps):
        angle = 0
        for i in range(n_steps):
                right(angle)
                forward(step_size)
                angle+=angle_step

set_theme(tracer_value=2,hide_turtle=False)
euler_curve(step_size=5,  angle_step=0.66, n_steps=10000)

# tracer _value = how fast tracer moves

"""set_theme(tracer_value=1, hide_turtle=False)
euler_curve(step_size=40,  angle_step=1.00, n_steps=600)
"""

# try these arguments and see the curves.
"""
set_theme(tracer_value=10)
euler_curve(step_size=7,  angle_step=0.66, n_steps=10000)
"""

# try these arguments and see the curves.
""""
set_theme(tracer_value=10, hide_turtle=False)
euler_curve(step_size=3,  angle_step=1.99, n_steps=100000)

"""

tracer(True)
exitonclick()
