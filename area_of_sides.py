from math import *

def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    n = round(((number_of_sides * (circle_radius ** 2)) / 2) * (sin(radians(360 / number_of_sides))), 3);
    return (n);

print(area_of_polygon_inside_circle(4, 5))
