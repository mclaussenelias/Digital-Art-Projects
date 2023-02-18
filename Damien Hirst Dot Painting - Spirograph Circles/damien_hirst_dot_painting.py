# Damien Hirst Dot Painting:

# Module Imports:

import turtle
from circles import Circle
from circles import Dot
from circles import ColorPalette
from circles import CircleGrid
from turtle import Turtle, Screen

# Turtle Settings:

turtle.colormode(255)
turtle = Turtle()
turtle.hideturtle()
turtle_speed = "fastest"

# Painting Configuration:

circle_radius = 7
dot_method = True  # If False, circle draw method will be used instead
circle_fill = False  # Setting only honored if dot_method = False
number_of_columns = 15
number_of_rows = 15
number_of_colors = 50
based_on_image = "color_image.png"
pen_size = 0  # Setting only honored if dot_method = False

# Draw Painting:

colors = ColorPalette()
colors.extract_colors(based_on_image, number_of_colors)

circle_grid = CircleGrid()
circle_grid.get_coordinates(circle_radius, number_of_columns, number_of_rows, dot_method)

print("Painting your picture...")

for coordinate in circle_grid.coordinates:
    if dot_method:
        dot = Dot()
        dot.diameter = circle_radius * 2
        dot.color = colors.pick_random_color()
        dot.coordinate = coordinate
        dot.draw_dot(turtle_speed)
    else:
        circle = Circle()
        circle.radius = circle_radius
        circle.color = colors.pick_random_color()
        circle.coordinate = coordinate
        if circle_fill:
            circle.draw_filled_circle(turtle_speed, pen_size)
        elif not circle_fill:
            circle.draw_circle(turtle_speed, pen_size)

print("Painting finished.  Enjoy!")

# Check for centering of dots within canvas:

# turtle.setposition(0, 0)
# turtle.showturtle()

screen = Screen()
screen.exitonclick()


