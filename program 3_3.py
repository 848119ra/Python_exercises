"""
COMP.CS.100 The first Project
program which allows someone to follow the amount they jog and analyzes
the average length of jogging during those days modified by user.
Creator: Rahele Ahmadian
Student id number: 151200445
"""

def main():
    lazy_day = 0
    sum_running_length = 0

    # getting the number of days from that person
    number_of_days = int(input("Enter the number of days: "))
    for repetition_counter in range(1, number_of_days + 1):
        running_length = float(input(f"Enter day {repetition_counter} running length: "))
        if running_length == 0:
            lazy_day += 1
            if lazy_day == 3:
                print("\nYou had too many consecutive lazy days!")
                break
        else:
            lazy_day = 0
            sum_running_length += running_length
    mean_length = sum_running_length / number_of_days
    if lazy_day != 3:
        if mean_length < 3.00:
            print(f"\nYour running mean of {mean_length:.2f} km was too low!")
        elif mean_length >= 3.00:
            print(f"\nYou were persistent runner! With a mean of {mean_length:.2f} km.")


if __name__ == "__main__":
    main()
