# Write your solution here
from math import sqrt

#Pythagorean theorem: a^2 + b^2 = c^2, where c = hypotenuse
def hypotenuse(leg1: float, leg2: float):
    hypotenuse = sqrt(leg1**2 + leg2**2)
    return hypotenuse

if __name__ == "__main__":
    print(hypotenuse(3,4)) # 5.0
    print(hypotenuse(5,12)) # 13.0
    print(hypotenuse(1,1)) # 1.4142135623730951