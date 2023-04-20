from time import sleep
import math

def delay(formula, millisec, num):
  sleep(millisec / 1000)
  return formula(num)

a = int(input())
b = int(input())
print(f'Square root of {a} after {b} seconds is {delay(lambda x : math.sqrt(x), b, a)}')