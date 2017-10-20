from math import sqrt


def get_roots(a, b, c):
    def root1(a, b):
        root1 = int(((-1 * b) - sqrt(discriminant)) // (2 * a))
        return root1

    def root2(a, b):
        root2 = int(((-1 * b) + sqrt(discriminant)) // (2 * a))
        return root2

    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return root1(a, b), None
    else:
        return root1(a, b), root2(a, b)
