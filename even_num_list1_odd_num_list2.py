def even1_odd2_list(list1, list2):
    print("List 1:", list1)
    print("List 2:", list2)

    new_list = []

    for num in list1:
        if num % 2 != 0:  # Add odd numbers from list1
            new_list.append(num)

    for num in list2:
        if num % 2 == 0:  # Add even numbers from list2
            new_list.append(num)

    return new_list


# Input lists as strings
input_list1 = input("Input List 1: ").split(', ')
input_list2 = input("Input List 2: ").split(', ')

# Convert input strings to integers
input_list1 = [int(x) for x in input_list1]
input_list2 = [int(y) for y in input_list2]

# Call the function with integer lists and store the result
result_list = even1_odd2_list(input_list1, input_list2)

# Print the resulting list
print("Resulting List:", result_list)
s