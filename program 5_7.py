"""
COMP.CS.100 The 5.7 Python program.
Creator: Rahele Ahmadian
Student id number: 151200445
"""


def main():
    # The bus schedule as a list, After asking a time from the user, find the location
    # in the list (index) that contains the time the next bus leaves. It is the time
    # the next bus departs. Print the next three bus departure times from that index
    # onwards, unless you are at the end of the table, print more times from the beginning
    # of the table, so that a total of three times are printed.

    bus_schedule = [630, 1015, 1415, 1620, 1720, 2000]
    time_given = int(input("Enter the time (as an integer): "))

    next_bus_index = 0
    for i, time in enumerate(bus_schedule):
        if time >= time_given:
            next_bus_index = i
            break

    print("The next buses leave:")
    # Print the next three bus departure times
    for _ in range(3):
        print(bus_schedule[next_bus_index % len(bus_schedule)])
        next_bus_index += 1



if __name__ == "__main__":
    main()
