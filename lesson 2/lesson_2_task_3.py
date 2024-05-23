import math
def square(side):
    square = side ** 2
    return math.ceil(square)
side = input ('Введите длину стороны квадрата: ')
side = float(side)    
print(square(side))
