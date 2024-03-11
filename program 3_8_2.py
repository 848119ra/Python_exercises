"""
COMP.CS.100 The 3.8.2 assignment
program which printing a box and checking the inputs
Creator: Rahele Ahmadian
Student id number: 151200445
"""

def print_box(horizontal_dimension, vertical_dimension, figure):
    """Printing a box looking shape.

    :param horizontal_dimension: int, the width of box.
    :param vertical_dimension: int, the height of box.
    :param figure: string, the shape of the character making the box.
    """
    for n in range(0, vertical_dimension):
        print(figure * horizontal_dimension)

def read_input(phrase):
    """reads the number entered by the user, checks that it is larger than zero,
    and returns it. The function also requests the user to enter a new input
    until the user enters a positive number.
    """
    read_length = True
    while read_length:
        length = int(input(phrase))
        if length > 0:
            return  length
            read_length = False


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()