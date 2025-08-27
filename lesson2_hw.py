###########
#Homework 1 (Age Calculator)
###########
Name = input("Enter your name: ")
Year_you_born = int(input("Enter the year you were born: "))
Age = 2025 - Year_you_born
print(f"Hello, {Name}, you are {Age} years old!")
###########
#Homework 2 (Car Name)
###########
txt = 'LMaasleitbtui'
car1 = txt[::2]
car2 = txt[1::2]
print(car1, car2)
###########
#Homework 3 (Car Name)
###########
txt = 'MsaatmiazD'
car1 = txt[::2]
car2 = txt[::-1][::2]
print(car1, car2)
###########
#Homework 4 (Extract Residence Area)
###########
txt = "I'am John. I am from London"
word = txt.split()
Area = Area [-1]
print ("Residence Area :", Area)
###########
#Homework 5 (Reverse String)
###########
Text = input("Please input string")
Result = Text[::-1]
print("Results:", Result)
###########
#Homework 6 (Vowel Count)
###########
text = input("Enter a string: ")
vowels = "aeiou"
count = 0
for X in text:
    if X in vowels:
        count += 1
print("Number of vowels:", count)
###########
#Homework 7 (Max Number)
###########
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum value:", maximum)
###########
#Homework 8 (Palidrone)
###########
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
###########
#Homework 9 (Email)
###########
email = input("Enter your email: ")
at_index = email.find("@")
domain = email[at_index + 1:]
print("Domain:", domain)
###########
#Homework 10 (Password)
###########
import random
import string
length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(length))
print("Generated password:", password)












