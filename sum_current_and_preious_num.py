previous_num = 0

for i in range(1, 11):
    x_sum = i + previous_num
    print("Current number: ", i, "Previous Number: ", previous_num, "Sum: ", x_sum )

    previous_num = i
