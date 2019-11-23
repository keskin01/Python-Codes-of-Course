class MyClass:
    def __init__(self, param_1, param_2):  # init = initiate
        self.Name = param_1
        self.ID = param_2

    def printed(self):
        print("'printed' Function of 'MyClass' class print your object attr: ", self.ID, self.Name)


class MyChildClass_1(MyClass):
    def __init__(self, param_3, param_1=None, param_2=None):
        super().__init__(param_1, param_2)
        # super() function that will make the child class inherit all the methods and properties from its parent
        self.Age = param_3

    def printed(self):
        print("'printed' Function of 'MyChildClass_1' class print your object attr: ", self.ID, self.Name, self.Age)


FirstObject = MyClass("Ömer", 5801)  # create an object
SecondObject = MyChildClass_1("Muhammed", 2403, 22)
FirstObject.printed()
SecondObject.printed()
