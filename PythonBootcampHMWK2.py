# Homework
import math

# question 1
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        self.x1 = self.coor1[0]
        self.y1 = self.coor1[1]
        self.x2 = self.coor2[0]
        self.y2 = self.coor2[1]

        print(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5)

    def slope(self):
        self.x1 = self.coor1[0]
        self.y1 = self.coor1[1]
        self.x2 = self.coor2[0]
        self.y2 = self.coor2[1]

        print((self.y2 - self.y1) / (self.x2 - self.x1))


# test

'''
    c1 = (3, 2)
    c2 = (8, 10)

    myLine = Line(c1, c2)

    myLine.distance()

    myLine.slope()
'''

# question 2
class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius**2 * self.height

    def surface_area(self):
        circle_area = 2 * math.pi * self.radius ** 2
        rectangle_area = 2 * math.pi * self.radius * self.height

        return circle_area + rectangle_area

# test


'''
mycylinder = Cylinder(2, 3)
print(mycylinder.volume())
print(mycylinder.surface_area())
'''

# challenge questions

# question 1

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account owner: " + self.owner + "\nAccount amount: " + str(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} depossited in Account, you now have {self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("you dont have enough money")
            return self.balance
        else:
            self.balance = self.balance - amount
            print(f"youve taken out {amount}, you now have {self.balance}")

# testing


acct1 = Account("Jose", 100)

print(acct1)
print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
acct1.withdraw(50)
