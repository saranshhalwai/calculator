import calc

print("1 - basic arithmetic\n2 - math functions\n3 - equation solvers")
i = int(input())
if (i == 1):
    print("1 - add(a+b)\n2 - subtract(a-b)\n3 - multiply(a*b)\n4 - divide(a/b)")
    i = int(input())
    if (i == 1):
        print(calc.add(float(input("a=")), float(input("b="))))

    elif (i == 2):
        print(calc.subtract(float(input("a=")), float(input("b="))))

    elif (i == 3):
        print(calc.multiply(float(input("a=")), float(input("b="))))

    elif (i == 4):
        print(calc.divide(float(input("a=")), float(input("b="))))

    else:
        print("really?")

elif (i == 2):
    print("1 - power(a^b)\n2 - square root\n3 - factorial(a!)\n4 - natural log(ln x)\n5 - sin x\n6 - cos x\n7 - tan "
          "x\n8 - cot x\n9 - sec x\n10 - cosec x")
    i = int(input())
    if i == 1:
        print(calc.pow(float(input("a=")), float(input("b="))))

    elif i == 2:
        print(calc.sqrt(float(input("number:"))))

    elif i == 3:
        print(calc.fact(int(input("a="))))

    elif i == 4:
        print(calc.ln(float(input("x="))))

    elif i == 5:
        print(calc.sin(float(input("x="))))

    elif i == 6:
        print(calc.cos(float(input("x="))))

    elif i == 7:
        print(calc.tan(float(input("x="))))

    elif i == 8:
        print(calc.cot(float(input("x="))))

    elif i == 9:
        print(calc.sec(float(input("x="))))

    elif i == 10:
        print(calc.cosec(float(input("x="))))

elif i == 3:
    print("1 - quadratic equation solver(ax^2+bx+c=0)\n2 - simultaneous linear equation(2)")
    i = int(input())
    if i == 1:
        calc.quadeqnsolver(float(input("a=")),float(input("b=")), float(input("c=")))

    elif i == 2:
        calc.slesolver()

else:
    print("No such option. Rerun.")
