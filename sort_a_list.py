def sorted_list(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


input_string = input("Give me a list of integers separated by spaces: ")
list_to_sort = list(map(int, input_string.split()))  # Convert input to list of integers

print(sorted_list(list_to_sort))
