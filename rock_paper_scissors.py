import sys


def rps(p1, p2):
    if p1 == p2:
        print("It is a tie!")
    elif p1 == 'r':
        if p2 == 's':
            print("Rock WINS")
        else:
            print("Paper WINS!")
    elif p1 == 's':
        if p2 == 'p':
            print("Scissors WINS")
        else:
            print("Rock WINS")
    elif p1 == 'p':
        if p2 == 'r':
            print("Paper WINS")
        else:
            print("Scissors WINS")
    else:
        print("Invalid input, try again!")
    sys.exit()


player_1 = input("Player 1, choose: ")
player_2 = input("Player 2, choose: ")

print(rps(player_1, player_2))

