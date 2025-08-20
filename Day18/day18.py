"""
Name: Day 18 - The Hirst Painting Project
Date: August 19, 2025
Author: Sanika Surose
"""

import turtle
from turtle import *
import random
import colorgram

# Extract colors
colors = colorgram.extract('painting_inspo.jpg', 64)
rgb_colors = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colors]

# Set up turtle
cursor = Turtle()
cursor.shape("classic")
cursor.speed("fastest")
turtle.colormode(255)

# Move to starting position
cursor.penup()
cursor.goto(-175, 175)

# Start drawing dots
dot_count = 8
for row in range(dot_count):
    for col in range(dot_count):
        color = random.choice(rgb_colors)
        cursor.dot(20, color)
        cursor.forward(50) # move right
    # move one row down and go back to start of row position
    cursor.backward(50 * dot_count)  # move back to left
    cursor.right(90)
    cursor.forward(50)  # move down
    cursor.left(90)

# Keep at bottom, needs to happen
screen = Screen()
screen.setup(width=700, height=700)
screen.exitonclick()