ElementNumber = int(input("Eleman sayısı: "))
myList = []
for j in range(ElementNumber):
    number = int(input("number:"))
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            myList.append(number)
    else:
        continue
for x in range(len(myList)):
    print(myList[x], end=" ")
