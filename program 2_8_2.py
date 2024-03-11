"""
Create a program that prints all the dates of a year which is not leap year.
"""


def main():

        for month in range(1, 13):
            if (month == 1 or month == 3 or month == 5 or month == 7
                     or month == 8 or month == 10 or month == 12):
                 for day in range(1, 32):
                     print(day, ".", month, ".", sep="")
            elif month == 4 or month == 6 or month == 9 or month == 11:
                 for day in range(1, 31):
                    print(day, ".", month, ".", sep="")
            elif month == 2:
                repetition_counter = 1
                while repetition_counter :
                    repetition_counter += 1
                    if repetition_counter % 4 == 0 :
                        for day in range(1, 30):
                            print(day, ".", month, ".", sep="")
                        break
                    else:
                        for day in range(1, 29):
                            print(day, ".", month, ".", sep="")
                        break


if __name__ == "__main__":
    main()