def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
        # f(1)=f(1)+f(0) 1+0
        # f(2)=f(1)+f(1) 1+1
        # f(3)=f(2)+f(1) (1+1)+(1+0)
        # f(4)=f(3)+f(2) ((1+1)+1)+(1+1)


nterms = int(input("Len of Fibonacci Seq: "))
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:", end=" ")
    for i in range(nterms):
        print(recursive_fibonacci(i), end=" ")
