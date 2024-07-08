from datetime import date

current_date = date.today()
current_year = current_date.year

name = input("Hello, please enter your name: ")
age = int(input("How old are you?: "))
year = current_year - age + 100

print(year) 