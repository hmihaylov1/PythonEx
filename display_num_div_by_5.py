def num_div_by_5(list):
    print("Given list: ", list)

    for num in list:
        if num % 5 == 0:
            print(num)


input_list = input("Please input a list of numbers: ").split()
input_list = [int(x) for x in input_list]

num_div_by_5(input_list)
