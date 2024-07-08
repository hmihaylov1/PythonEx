def check_palindrome(number):
    print("Given number: ", number)
    num = number

    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    if num == reverse_num:
        print("Yes, Number is palindrome")
    else:
        print("No, Number is NOT palindrome")


input_num = int(input("Enter a number to check: "))


check_palindrome(input_num)
