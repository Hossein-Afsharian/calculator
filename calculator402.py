import math

while True:
    op=input("enter op( sin , cos , tan , cot , factorial , sqrt, + , - , * , / ,) or off:")
    if op == "off":
        break

    if op=="sin":
        a=float(input("meghdar sin:"))
        r=(math.sin(math.radians(a)))

    if op=="cos":
        a = float(input("meghdar cos:"))
        r = (math.cos(math.radians(a)))

    if op=="tan":
        a = float(input("meghdar tan:"))
        r = (math.tan(math.radians(a)))

    if op=="cot":
        a = float(input("meghdar cot:"))
        x = (math.tan(math.radians(a)))
        r = 1/x

    if op=="factorial":
        a = int(input("meghdar factorial:"))
        r = (math.factorial(a))

    if op=="sqrt":
        a = float(input("meghdar sqrt:"))
        if a<0:
           r = "error"
        else:
           r = (math.sqrt(a))

    if op=="+":
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        r = a+b
    if op=="-":
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        r = a-b
    if op=="*":
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        r = a*b
    if op=="/":
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        if b == 0:
            r = "error"
        else:
            r =a/b

    print (r)
