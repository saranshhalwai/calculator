def pow(x: float, p: int):
    product = 1.0
    for i in range(0, p):
        product *= x

    return product


def fact(x: int):
    prod = 1
    for i in range(1, x + 1):
        prod *= i

    return prod


def ln(x: float):
    res = 0.0
    x -= 1
    for i in range(1, 10000):
        res += (-1.0 ** (i + 1)) * x ** i / i
    return res


def sin(x: float):
    res = 0.0
    for i in range(0, 40):
        res += ((-1) ** i) * (x ** (2 * i + 1)) / fact((2 * i + 1))

    return res


def add(x: float, y: float):
    return x + y


def subtract(x: float, y: float):
    return x - y


def multiply(x: float, y: float):
    return x * y


def divide(x: float, y: float):
    return x / y


def slesolver():
    coeff = [[0, 0, 0], [0, 0, 0]]
    print("1st eqn")
    coeff[0][0] = float(input("x*"))
    coeff[0][1] = float(input("+y*"))
    coeff[0][2] = float(input("="))
    print("\n2nd eqn")
    coeff[1][0] = float(input("x="))
    coeff[1][1] = float(input("+y*"))
    coeff[1][2] = float(input("="))
    D = coeff[0][0] * coeff[1][1] - coeff[0][1] * coeff[1][0]
    D1 = coeff[0][2] * coeff[1][1] - coeff[0][1] * coeff[1][2]
    D2 = coeff[0][0] * coeff[1][2] - coeff[1][0] * coeff[0][2]
    x = D1 / D
    y = D2 / D
    print(f"x={x}  y={y}")


def cos(x: float):
    res = 0.0
    for i in range(0, 40):
        res += (-1) ** i * x ** (i * 2) / fact(i * 2)

    return res


def tan(x: float):
    return sin(x) / cos(x)


def cot(x: float):
    return 1 / tan(x)


def sec(x: float):
    return 1 / cos(x)


def cosec(x: float):
    return 1 / sin(x)


def sqrt(x: float):
    i = 0
    res = 0.0
    arg = 1
    while i < 16:
        while True:
            if (res + arg) ** 2 > x:
                break

            res += arg

        arg /= 10
        i += 1
    return res

def quadeqnsolver(a : float, b: float, c: float):
    complex = False
    D = b ** 2 - 4 * a * c
    if (D < 0):
        complex = True
        D = 0 - D

    if not complex:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
        print(f"roots are:{x1}  {x2}")
    else:
        print(f"roots are {-b/(2*a)}+{sqrt(D)/(2*a)}  {-b/(2*a)}-{sqrt(D)/(2*a)}")


