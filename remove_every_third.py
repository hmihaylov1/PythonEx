def remove_third(sequence):
    position = 3 - 1
    idx = 0

    list = len(sequence)

    while list > 0:
        idx = (position + idx) % list

        print(sequence.pop(idx))
        list -= 1


seq = input("give me a sequesnce of numbers: ").split()
seq = [int(num) for num in seq]

print(remove_third(seq))
