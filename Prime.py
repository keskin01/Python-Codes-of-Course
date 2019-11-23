number = int(input("Enter the number: "))

if number > 1:  # if number is 1 or 0 or negative these are not prime
    for i in range(2, number):  # i != number
        if (number % i) == 0:
            print(number, "is not a prime number")
            break  # We do not need more looping when we find any number that can divide the number
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")