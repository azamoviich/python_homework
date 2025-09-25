###########
# Homework 1 (Circle Class)
###########
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


###########
# Homework 2 (Person Class)
###########
from datetime import date

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date  # birth_date as (year, month, day)

    def age(self):
        today = date.today()
        born = date(*self.birth_date)
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


###########
# Homework 3 (Calculator Class)
###########
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


###########
# Homework 4 (Shape and Subclasses)
###########
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


###########
# Homework 5 (Binary Search Tree Class)
###########
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        elif key > root.key:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)


###########
# Homework 6 (Stack Data Structure)
###########
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()


###########
# Homework 7 (Linked List Data Structure)
###########
class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = NodeLL(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None


###########
# Homework 8 (Shopping Cart Class)
###########
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())


###########
# Homework 9 (Stack with Display)
###########
class StackDisplay:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def display(self):
        print(self.stack)


###########
# Homework 10 (Queue Data Structure)
###########
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)


###########
# Homework 11 (Bank Class)
###########
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner, balance=0):
        self.accounts[account_number] = {"owner": owner, "balance": balance}

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number]["balance"] >= amount:
            self.accounts[account_number]["balance"] -= amount
        else:
            return "Insufficient funds or invalid account"

    def get_balance(self, account_number):
        return self.accounts.get(account_number, {}).get("balance", "Account not found")
