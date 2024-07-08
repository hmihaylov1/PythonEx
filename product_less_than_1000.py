def solution(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2


result = solution(40, 30)
print("The result is:", result)
