def remove_char(word, n):
    print(word)
    # n = int(n)
    try:
        n = int(n)
    except ValueError:
        return "Please enter a valid number"
    x = word[n:]
    return x


print(remove_char(word=input("enter a word: "), n=input("how many char do you want to remove: ")))
