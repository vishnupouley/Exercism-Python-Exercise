def triangle(a, b, c):
    return (a + b >= c > 0) and (b + c >= a > 0) and (a + c >= b > 0)

def equilateral(sides):
    a, b, c = sides
    return a == b == c and triangle(a, b, c)


def isosceles(sides):
    a, b, c = sides
    return (a == b or b == c or c == a) and triangle(a, b, c)


def scalene(sides):
    a, b, c = sides
    return (a != b and b != c and c != a) and triangle(a, b, c)
