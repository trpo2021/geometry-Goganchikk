from math import sqrt
import math


class Circle:
    """
    DOCSTRING: Circle class
    """

    def __init__(self, x, y, r):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        """
        DOCSTRING: Calc area
        INPUT: Radius
        OUTPUT: Area
        """
        return math.pi * self.r * self.r

    def perimeter(self):
        """
        DOCSTRING: Calc perimeter
        INPUT: Radius
        OUTPUT: Perimeter
        """
        return 2 * math.pi * self.r


def calc_intersection(x1, y1, r1, x2, y2, r2):
    """
    DOCSTRING: Calculating a intersection of figures
    INPUT: Coordinates and radius
    OUTPUT: 'No intersection of figures' or 'There is an intersection of figures'
    """
    cen_dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if not cen_dist:
        return "No intersection of figures" if r1 != r2 else "There is an intersection of figures"
    else:
        return "No intersection of figures" if cen_dist > r1 + r2 else "There is an intersection of figures"


def get_input():
    """
    DOCSTRING: Input validation
    INPUT: Coordinates and radius
    OUTPUT: Numbers
    """
    while True:
        try:
            reply = int(input('Enter a number: '))
            return reply
        except:
            print('Its not a number, try again!')
            continue


def main():
    r1 = get_input()
    r2 = get_input()
    x1 = get_input()
    y1 = get_input()
    x2 = get_input()
    y2 = get_input()

    c1 = Circle(r1, x1, y1)
    c2 = Circle(r2, x2, y2)

    print("Area for first circle:", c1.area())
    print("Perimeter for first circle:", c1.perimeter())
    print("Area for second circle:", c2.area())
    print("Perimeter for second circle:", c2.perimeter())

    print(calc_intersection(x1, y1, r1, x2, y2, r2))


main()