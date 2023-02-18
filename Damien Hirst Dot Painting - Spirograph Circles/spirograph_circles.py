# Spirograph Circles:

# Module Imports:

import turtle
from circles import Circle
from circles import ColorPalette
from turtle import Turtle, Screen

# Turtle Settings:

turtle.colormode(255)  # changes the color mode for the turtle module to RGB
turtle = Turtle()
turtle.hideturtle()
turtle_speed = "fastest"

# Painting Configuration:

circle_radius = 100
circle_offset = 0.1
cycles = int(360 / circle_offset)
number_of_colors = 100
based_on_image = "color_image.png"
pen_size = 0

# Draw Painting:

colors = ColorPalette()
colors.extract_colors(based_on_image, number_of_colors)

print("Painting your picture...")

for cycle in range(cycles):
    circle = Circle()
    circle.radius = circle_radius
    circle.coordinate = (0, 0)
    circle.color = colors.pick_random_color()
    circle.offset = circle_offset
    circle.draw_circle(turtle_speed, pen_size)

print("Drawing finished.  Enjoy!")

screen = Screen()
screen.exitonclick()
