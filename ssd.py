def toBinary(n):
    binary_array = []
    while n > 0:
        binary_array.append(n % 2)
        n = n // 2
    return binary_array[::-1]

def point_doubling (point:tuple, b, p):
    x1, y1 = point
    if p == 0:
        m = (3*(x1**2) + b)/(2*y1)
        x3 = (m**2 - 2*x1)
        y3 = (m*(x1 - x3) - y1)
        return (x3, y3)
    y_coordinates_mod = ((3 * (x1**2) + b) % p)
    x_coordinates_inverse_mod = pow((2 * y1), -1, p)
    m = (y_coordinates_mod * x_coordinates_inverse_mod) % p

    x3 = (m**2 - (2 * x1)) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

def point_addition(point_1:tuple, point_2:tuple, b, p):
    if point_1 == point_2:
        return point_doubling(point_1, b, p)
    
    x1, y1 = point_1
    x2, y2 = point_2

    if p == 0:
        m = (y2 - y1)/(x2 - x1)
        x3 = (m**2 - x1 - x2)
        y3 = (m*(x1 - x3) - y1)
        return (x3, y3)

    y_coordinates_mod = ((y2 - y1) % p)
    x_coordinates_inverse_mod = pow((x2 - x1), -1, p)
    m = (y_coordinates_mod * x_coordinates_inverse_mod) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

def successive_doubling(k:int, point:tuple, b, p) -> tuple:
    k_binary = toBinary(k)
    result = point
    for i in range(1, len(k_binary)):
        result = point_doubling(result, b, p)
        if k_binary[i] == 1:
            result = point_addition(result, point, b, p)
    return result
## COMPUTATION ##
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# p = int(input("p: "))
# point = int(input("x: ")), int(input("y: "))
# k = int(input("k: "))
a = 1
b = 0
c = -2
p = 0
point = (3,5)
k = 7

print(f'E: y^2 = {a}x^3 + {b}x + {c}')
print(f'Point: P = {point}')
print(f'{k}P = {successive_doubling(k, point, b, p)}')


