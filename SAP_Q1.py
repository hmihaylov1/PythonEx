def mostCommon(lst):
    most_common = {}

    for item in lst:
        if item in most_common:
            most_common[item] += 1
        else:
            most_common[item] = 1
    common = max(most_common, key=most_common.get)
    return common


input_list = input("Please give me a list: ").split()

print(mostCommon(input_list))
