import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp 
from math import *
import turtle


t = turtle.Turtle()

t.speed(1)

t.color('magenta')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

t.penup()
t.goto(0, -40) 
t.color('black')

t.write("Yay it is working!", align="center", font=("Arial", 20, "normal"))

t.hideturtle()

turtle.done()




