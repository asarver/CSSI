# Chapter 15 and on

import copy

class Point(object):
    """represents a point in 2D space"""

def create_point(x, y):
    """create a point with coordinates x and y"""
    p = Point()
    p.x = x
    p.y = y
    return p

def add_coordinates(p):
    """add the x and the y coordinates of point p"""
    return p.x + p.y

class Circle(object):
    """represents a circle"""

def create_circle(origin, radius):
    """return a circle with the origin and radius"""
    c = Circle()
    c.origin = origin
    c.radius = radius
    return c

    
