# import pi from math package to use it in the calculation of the the volume of sphere
from math import pi


def vol_of_sphere(d):
    r = d / 2
    return 4 / 3 * pi * r ** 3


d = 12
print(vol_of_sphere(d))
