# -*- coding: utf-8 -*-
"""OOPs.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18t__7bdGkaGMG-m-8eE_7FaOD2wSJyvw
"""

# # 1. What are the five key concepts of Object-Oriented Programming (OOP)?
# Answer =
# Key Concepts of Object-Oriented Programming (OOP)
# 1.Encapsulation: Wrapping data (variables) and methods (functions) into a single unit (class), and restricting access using access modifiers.
# 2 .Abstraction: Hiding internal details and showing only essential features.
# 3.Inheritance: Allowing a class (child) to inherit properties and methods from another class (parent).
# 4.Polymorphism: Allowing methods to perform differently based on the object they are acting upon.
# 5. Association: Building relationships between classes, such as composition and aggregation.

# 2. Write a Python class for a Car with attributes for make, model, and year. Include a method to display
# the car's information.
# Answer =
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# 3. Explain the difference between instance methods and class methods. Provide an example of each.
# # Answer =
#  Difference Between Instance Methods and Class Methods
# Instance Methods: Operate on instance-level data and require an instance of the class. They use self as the first parameter.
# Class Methods: Operate on the class-level data and require the cls parameter. Use @classmethod decorator.

# 4. How does Python implement method overloading? Give an example.
# # Answer =
#  Python and Method Overloading
# Python does not support traditional method overloading. However, you can achieve similar behavior using default arguments or variable-length arguments.

# Example:

class Example:
    def method(self, a, b=None):
        if b:
            return a + b
        return a

obj = Example()
print(obj.method(5))        # 5
print(obj.method(5, 10))    # 15

# 5. What are the three types of access modifiers in Python? How are they denoted?
# Answer =


#  Access Modifiers in Python
# Public: Accessible everywhere. Denoted without an underscore (x).
# Protected: Accessible in the class and its subclasses. Denoted with a single underscore (_x).
# Private: Accessible only within the class. Denoted with double underscores (__x).

# 6. Describe the five types of inheritance in Python. Provide a simple example of multiple inheritance.
# # Answer =
#  Types of Inheritance in Python
# Single Inheritance: One child class inherits from one parent class.
# Multiple Inheritance: A class inherits from multiple parent classes.
# Multilevel Inheritance: A class inherits from another child class.
# Hierarchical Inheritance: Multiple classes inherit from a single parent class.
# Hybrid Inheritance: Combination of two or more types of inheritance.

# 7. What is the Method Resolution Order (MRO) in Python? How can you retrieve it programmatically?
# Answer =
#  Method Resolution Order (MRO)
# MRO defines the order in which classes are searched for methods and attributes in multiple inheritance. It is determined using the C3 Linearization Algorithm.

# Retrieve MRO Programmatically:

class A: pass
class B(A): pass
class C(B): pass

print(C.mro())  # [C, B, A, object]

# 8. Create an abstract base class Shape with an abstract method area(). Then create two subclasses
# Circle and Rectangle that implement the area() method.

# Answer =
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# 9. Demonstrate polymorphism by creating a function that can work with different shape objects to calculate
# and print their areas.
# Answer =
def print_area(shape):
    print(f"Area: {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(4, 6)

print_area(circle)       # Area: 78.5
print_area(rectangle)    # Area: 24

# 10. Implement encapsulation in a BankAccount class with private attributes for balance and
# account_number. Include methods for deposit, withdrawal, and balance inquiry.

# Answer =
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient balance!")

    def get_balance(self):
        return self.__balance

# 11. Write a class that overrides the __str__ and __add__ magic methods. What will these methods allow
# you to do?

# Answer =
class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Number: {self.value}"

    def __add__(self, other):
        return Number(self.value + other.value)

n1 = Number(5)
n2 = Number(10)
n3 = n1 + n2

print(n3)  # Number: 15

# 12. Create a decorator that measures and prints the execution time of a function.
# Answer =
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()  # Execution time: 2.0001 seconds

# 13. Explain the concept of the Diamond Problem in multiple inheritance. How does Python resolve it?
# Answer =
#  Diamond Problem and Python Resolution
# The Diamond Problem occurs in multiple inheritance when a class inherits from two classes that share a common ancestor.

# Python resolves it using the C3 Linearization Algorithm, which ensures that each class is called only once in a consistent order.

# Example:


class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())  # B (Based on MRO)
print(D.mro())  # [D, B, C, A, object]

# 14. Write a class method that keeps track of the number of instances created from a class.
# Answer =
class InstanceCounter:
    count = 0  # Class attribute to track instances

    def __init__(self):
        InstanceCounter.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.count

# Usage
obj1 = InstanceCounter()
obj2 = InstanceCounter()
print(InstanceCounter.get_instance_count())  # Output: 2

# 15. Implement a static method in a class that checks if a given year is a leap year.
# Answer =

class Utility:
    @staticmethod
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

# Usage
print(Utility.is_leap_year(2024))  # Output: True
print(Utility.is_leap_year(1900))  # Output: False
