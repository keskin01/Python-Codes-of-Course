def factorial(x):
    result = 1
    temp = x
    if temp >= 0:
        while temp > 0:
            result *= temp  # result=result*temp
            temp -= 1  # temp=temp-1
        print(x, "! =", result)
    else:
        print("Please dont enter negative number")


factorial(int(input("x: ")))
