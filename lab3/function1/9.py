from math import pi


def volume(R):
    return (4*pi*(R**3))/3


radius = int(input())
print(volume(radius))