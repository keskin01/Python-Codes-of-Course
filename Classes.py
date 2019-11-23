# class Ornek:
#     def __init__(self, name, age, sname):
#         self.name = name
#         self.age = age
#         self.SurName = sname
#
#
# omer = Ornek("Ömer", 22, "Keskin")
# samet = Ornek("Samet", 23, "Mert")
# print(omer.age, samet.SurName, omer.SurName)
# omer.SurName = "Kaya"
# print(omer.age, samet.SurName, omer.SurName)


class Complex:

    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return self.real + other.real, self.imaginary + other.imaginary

    def __sub__(self, other):
        return self.real - other.real, self.imaginary - other.imaginary

    def __mul__(self, other):
        return self.real * other.real - self.imaginary * other.imaginary, self.imaginary * other.real + self.real * other.imaginary

    def __truediv__(self, other):

        x, y, z, t = self.real, self.imaginary, other.real, other.imaginary
        r = float(z ** 2 + t ** 2)
        return (x * z + y * t) / r, (y * z - x * t) / r


number1 = Complex(int(input("Self Real Part: ")),
                  int(input("Self Imaginary Part: ")))  # number1 is obj of Complex class
number2 = Complex(int(input("Other Real Part: ")),
                  int(input("Other Imaginary Part: ")))  # number1 is obj of Complex class
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)

# class IEEE:
#     def __init__(self, birth, year, name, sname, p):
#         self.BirthYear = birth
#         self.Year = year
#         self.Name = name
#         self.SurName = sname
#         self.Password = p
#
#     def age(self):
#         return self.Year - self.BirthYear
#
#     def name(self):
#         if self.Name == "Ömer" or "Muhammed" or "Muhammed Ömer":
#             return 1
#         else:
#             return False
#
#     def surname(self):
#         if self.SurName == "Keskin":
#             return True
#         else:
#             return False
#
#     def password(self):
#         if "omer" in self.Password:
#             return True
#         else:
#             return False
#
#
# Object_1 = IEEE(1997, 2019, "Ömer", input("Surname: "), input("Your Password: "))
# print(Object_1.age(), Object_1.name(), Object_1.surname(), Object_1.password())

# class Calender:
#     def __init__(self, fday, lday, month, year, weekday, index):
#         self.FirstDay = fday
#         self.LastDay = lday
#         self.Month = month
#         self.Year = year
#         self.DayOfWeek = weekday
#         self.IndexOfDay = index
#     def General(self):
#         self.FirstDay = 1
#         self.Year = 2019
#         self.DayOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
#     def January(self):
#         self.Month = "January"
#         self.IndexOfDay = 0
#     def February(self):
#         self.Month = "February"
#         self.IndexOfDay = 3
#         if self.Year%4==0:
