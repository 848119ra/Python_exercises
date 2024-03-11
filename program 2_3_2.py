"""
This program will calculate the multiplication
table for a given number until it reaches a result
that is more than 100.
"""

def main():
    number = int(input("Choose a number: "))
    multiply = 0
    repetition_counter = 1
    while repetition_counter:
        multiply = repetition_counter * number
        print(repetition_counter, "*", number, "=", multiply)
        repetition_counter += 1
        if multiply >= 100:
            break


if __name__ == "__main__":
    main()