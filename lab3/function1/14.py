from math import pi


def volume(R):
    return (4*pi*(R**3))/3


radius = int(input())
k1 = volume(radius)


def gramm(grams):
    ounces = 28.3495231 * grams
    return ounces


n = int(input())
k2 = gramm(n)


def temperature(f):
    C = (5/9) * (f-32)
    return C


f = int(input())
k3 = temperature(f)

z = k1*k2*k3
print(z)