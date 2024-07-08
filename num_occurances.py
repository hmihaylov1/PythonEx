def occurrence(lst):
    return lst.count(19) == 2 and lst.count(5) >= 3


# Input handling
input_list = input("What is the list: ").split()
input_list = [int(num) for num in input_list]

print(occurrence(input_list))
