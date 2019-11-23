while 1:
    def factorial(x):
        result = 1
        temp = x
        if temp >= 0:
            while temp > 0:
                result *= temp
                temp -= 1
            return result  # return to fact
        else:
            print("Please dont enter negative number")


    def combination(n, r):
        if n and r > 0:

            h = factorial(n) // (factorial(r) * factorial(n - r))
            print(h)
        else:
            print("Please dont enter negative number")


    combination(int(input("n: ")), int(input("r: ")))

    user = input("Continue 'Yes' or 'No'? : ")
    if user == "Yes":
        continue
    elif user == "No":
        print("Exit the system")
        break
    else:
        print("System Error and Exit")
        break
