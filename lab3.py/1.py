#1
class StringProcessor:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

# Пример использования
sp = StringProcessor()
sp.getString()
sp.printString()


#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

# Пример
sq = Square(5)
print("Square area:", sq.area())


#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Пример
rect = Rectangle(4, 6)
print("Rectangle area:", rect.area())




#4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Пример
p1 = Point(2, 3)
p2 = Point(5, 7)
p1.show()
p1.move(1, 1)
p1.show()
print("Distance:", p1.dist(p2))



#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New balance: {self.balance}")

# Пример
acc = Account("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150)  # Попытка снять больше, чем есть




