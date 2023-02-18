import colorgram
import random
import turtle
from turtle import Turtle, Screen


class ColorPalette:

    def __init__(self):
        self.color_list = []

    #
    def extract_colors(self, image, color_count):
        print("Selecting colors...")
        color_set = colorgram.extract(image, color_count)
        for color in color_set:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            new_color = (r, g, b)
            self.color_list.append(new_color)

    def pick_random_color(self):
        return random.choice(self.color_list)


class CircleGrid:
    def __init__(self):
        self.coordinates = []

    def get_coordinates(self, radius, columns, rows, dot_method):
        coordinates = []
        if dot_method:
            for row in range(rows):
                for column in range(columns):
                    # Coordinates are adjusted to center array of dots on the canvas:
                    x = ((row * radius) * 4) - (((rows - 1) * 4 * radius) / 2)
                    y = (((column * radius) * 4) - (((columns - 1) * 4 * radius) / 2) - radius)
                    coordinate = (x, y)
                    coordinates.append(coordinate)
            self.coordinates = coordinates
        else:
            for row in range(rows):
                for column in range(columns):
                    # Coordinates are adjusted to center array of dots on the canvas:
                    x = ((row * radius) * 4) - (((rows - 1) * 4 * radius) / 2)
                    y = (((column * radius) * 4) - (((columns - 1) * 4 * radius) / 2) - radius)
                    coordinate = (x, y)
                    coordinates.append(coordinate)
            self.coordinates = coordinates


class Circle:
    def __init__(self):
        self.radius = None
        self.color = None
        self.coordinate = None
        self.offset = 0

    def draw_filled_circle(self, speed, pensize):
        turtle.hideturtle()
        turtle.speed(speed)
        turtle.pensize(pensize)
        turtle.penup()
        turtle.setposition(self.coordinate)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.circle(self.radius)
        turtle.penup()
        turtle.end_fill()

    def draw_circle(self, speed, pensize):
        turtle.hideturtle()
        turtle.speed(speed)
        turtle.pensize(pensize)
        turtle.penup()
        turtle.setposition(self.coordinate)
        turtle.pencolor(self.color)
        turtle.right(self.offset)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()


class Dot:
    def __init__(self):
        self.diameter = None
        self.color = None
        self.coordinate = None
        self.offset = 0

    def draw_dot(self, speed):
        turtle.hideturtle()
        turtle.speed(speed)
        turtle.penup()
        turtle.setposition(self.coordinate)
        turtle.pendown()
        turtle.dot(self.diameter, self.color)
        turtle.penup()

