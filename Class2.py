class Iterator:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        if self.x <= bound:
            y = self.x
            self.x += 1
            return y
        else:
            raise StopIteration


bound = int(input("Bound: "))
_object = Iterator()
_iter = iter(_object)
for y in _iter:
    print(y, end=" ")


def parent_function():
    val_1 = int(input("\nValue 1: "))
    val_1 = val_1 ** 2
    global y
    y = 30

    def child_function():
        print(val_1 + y)

    child_function()


parent_function()
print(y)
