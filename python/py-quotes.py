def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# source
# geeksforgeeks - Fibonacci
# code
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
# source
# geeksforgeeks - Factorial
# code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# source
# w3schools - Python Classes/Objects
