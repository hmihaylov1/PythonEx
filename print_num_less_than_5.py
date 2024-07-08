# user_input = int(input("Enter a number: "))
#
# if user_input in a:
#     print("Number is in list A!")
# else:
#     print("Number NOT in A!")
#
# if user_input in b:
#     print("Number is in list B!")
# else:
#     print("Number NOT in B!")

a = input("Enter list A: ")
a = [int(x) for x in a]
b = input("Enter list B: ")
b = [int(y) for y in b]



set_a = set(a)
set_b = set(b)

new_list = set_a.intersection(set_b)

print(list(new_list))


