"""
A game of rock-paper-scissors for two players. In this game, both players use
one letter to tell whether they choose rock (R), paper (P) or scissors (S).
After this, the program shows the result. Paper beats rock, rock beats scissors
and scissors beat paper.
"""

def main():
    choice_1 = input("Player 1, enter your choice (R/P/S): ")
    choice_2 = input("Player 2, enter your choice (R/P/S): ")
    if choice_1 == "P":
        if choice_2 == "P":
            print("It's a tie!")
        elif choice_2 == "R":
            print("Player 1 won!")
        elif choice_2 == "S":
            print("Player 2 won!")
    elif choice_1 == "R":
        if choice_2 == "R":
            print("It's a tie!")
        elif choice_2 == "S":
            print("Player 1 won!")
        elif choice_2 == "P":
            print("Player 2 won!")
    elif choice_1 == "S":
        if choice_2 == "S":
            print("It's a tie!")
        elif choice_2 == "P":
            print("Player 1 won!")
        elif choice_2 == "R":
            print("Player 2 won!")
if __name__ == "__main__":
    main()