"""
the game Zip Boing, The first player says 1, the next one 2 and so forth.
The game is called Zip Boing because every time the next number is divisible
by 3 the player has to say "zip" and divisible by 7 say "boing", divisible
by both the numbers "zip boing".
"""

def main():
    number = int(input("How many numbers would you like to have? "))
    for repetition_counter in range(1, number + 1):
        if repetition_counter % 3 == 0 and repetition_counter % 7 == 0:
            print("zip boing")
        elif repetition_counter % 3 == 0:
            print("zip")
        elif repetition_counter % 7 == 0:
            print("boing")
        else:
            print(repetition_counter)


if __name__ == "__main__":
    main()