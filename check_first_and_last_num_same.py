def first_last_same(given_list):
    print("Given List: ", given_list)

    first_num = given_list[0]
    last_num = given_list[-1]

    if first_num == last_num:
        print("Inshalla they are the same")
    else:
        print("Nope, they are not the same")

input_list = input("Please give me a list of numbers: ").split()

input_list = [int(x) for x in input_list]

# Call the function without the print statement
first_last_same(input_list)
