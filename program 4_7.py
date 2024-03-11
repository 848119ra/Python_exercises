"""
COMP.CS.100 The 4.7 Python program.
Creator: Rahele Ahmadian
Student id number: 151200445
Implement a program that asks the user for two input values:the amount of lottery balls (or numbers)
andthe drawn balls (or numbers). And then prints the probability of getting a jackpot with
only one coupon.
"""
# factoriel function
def foo(an_int):
    """Calculates the factoriel of an integer number
    :param an_int: int, the given number
    :return fact_int: int, the factoriel of the given number
    """
    fact_int = 1
    if an_int == 0:
        fact_int = 1
    else:
        i = 1
        while i <= an_int:
            fact_int = i * fact_int
            i += 1

    return fact_int

# function for calculating the probability of getting a jackpot with only one
# coupon (1 divided with the number of different lottery lines)
def lottlines_jackpot(all_num, drawn_num):
    """Calculating the probability of getting a jackpot with only one coupon,
    :param all_num: int, the the number of balls in a lottery
    :param drawn_num: int, the number of the predicted balls
    :return lottery_lines: int, how many different lottery lines existed in total in lottery
    """
    # how many different lottery lines existed in total in lottery
    lottery_lines = foo(all_num) // (foo(all_num - drawn_num) * foo(drawn_num))
    return lottery_lines


def main():
    lottery_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))
    if lottery_balls < 0 or drawn_balls < 0 :
        print("The number of balls must be a positive number.")
    elif drawn_balls > lottery_balls:
        print("At most the total number of balls can be drawn.")
    else:
        print(f"The probability of guessing all {drawn_balls} balls correctly is 1/", lottlines_jackpot(lottery_balls, drawn_balls), sep="" )







if __name__ == "__main__":
    main()
