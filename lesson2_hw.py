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

