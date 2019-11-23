n_term = int(input("Enter the terms: "))
first_number = 0  # first element of series
second_number = 1  # second element of series
if n_term <= 0:
    print("Please enter positive number or do not enter 0")
elif n_term == 1:
    print("Fibonacci sequence:", first_number, end=" ")

else:
    print("Fibonacci sequence:", first_number, second_number, end=" ")  
    for i in range(2, n_term):
        temp = first_number + second_number
        print(temp, end=" ")
        first_number = second_number
        second_number = temp


