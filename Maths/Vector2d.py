import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Operator Overlaods

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other, self.y + other)
    
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other, self.y - other)
    
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x * other.x, self.y + other.y)
        return Vector(self.x * other, self.y * other)

    def __turediv__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x / other.x, self.y / other.y)
        return Vector(self.x / other, self.y / other)
    
    # Reverse multiply
    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return self.x == other and self.y == other


def dot(vec1, vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y


def angle_between(vec1, vec2):
    return math.acos(dot(vec1, vec2))


def lenght_sqr(vec):
    return vec.x ** 2 + vec.y ** 2


def dist_sqr(vec1, vec2):
    return lenght_sqr(vec1 - vec2)


def length(vec):
    return math.sqrt(lenght_sqr(vec))


def dist(vec1, vec2):
    return length(vec1 - vec2)


def normalize(vec):
    vec_lenght = length(vec)

    if vec_lenght < 0.00001:
        return Vector(0, 1)
    
    return Vector(vec.x / vec_lenght, vec.y / vec_lenght)

# I don't understand what anything does below this comment - I really suck at maths.

def reflect(incident, normal):
    return incident - dot(normal, incident) * 2.0 * normal


def negate(vec):
    return Vector(-vec.x, -vec.y)


def find_right(vec):
    return Vector(-vec.y, vec.x)


def find_left(vec):
    return negate(find_right(vec))