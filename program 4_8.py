"""
program that prompts the user to select a geometric pattern (a square or a
rectangle) and to enter the required dimensions. The program prints the circumference
and area of the pattern to two decimal places.
COMP.CS.100 The 4.8 program.
Creator: Rahele Ahmadian
Student id number: 151200445
"""
import math
def square_circum(side):
    """Calculate the circumference of a square
    :param side: float, the dimension of square's side
    :return : float, the circumference of the square
    """
    return  4 * side

def square_area(side):
    """Calculate the surface area of a square
    :param side: float, the dimension of square's side
    :return : float, the surface area of the square
    """
    return  side ** 2

def rec_circum(side1, side2):
    """Calculate the circumference of a rectangle
    :param side1: float, the dimension of first side of the rectangle
    :param side2: float, the dimension of second side of the rectangle
    :return : float, the circumference of the rectangle
    """
    return  (side1 +side2) * 2

def rec_area(side1, side2):
    """Calculate the surface area of a rectangle
    :param side1: float, the dimension of first side of the rectangle
    :param side2: float, the dimension of second side of the rectangle
    :return : float, the surface area of the rectangle
    """
    return  side1 * side2

def cir_circum(radius):
    """Calculate the circumference of a circle
    :param radius: float, the radius of the circle
    :return : float, the circumference of the circle
    """
    return  math.pi * 2 * radius

def cir_area(radius):
    """Calculate the surface area of a circle
    :param radius: float, the radius of the circle
    :return : float, the surface area of the circle
    """
    return  math.pi * (radius ** 2)


def goodbye():
    """
    Prints Goodbye!
    :param : No parameter
    :return : No return value
    """
    print("Goodbye!")



def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """

    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            sq_side_value = True
            while sq_side_value:
                sq_side = float(input("Enter the length of the square's side: "))
                if sq_side > 0:
                    print(f"The circumference is {square_circum(sq_side):.2f}")
                    print(f"The surface area is {square_area(sq_side):.2f}")
                    print()
                    sq_side_value = False

                pass

        elif answer == "r":
            rec_side_value = True
            while rec_side_value:
                rec_side1 = float(input("Enter the length of the rectangle's side 1: "))
                if rec_side1 > 0:
                    rec_side2_value = True
                    while rec_side2_value:
                        rec_side2 = float(input("Enter the length of the rectangle's side 2: "))
                        if rec_side2 > 0 :
                            print(f"The circumference is {rec_circum(rec_side1, rec_side2):.2f}")
                            print(f"The surface area is {rec_area(rec_side1, rec_side2):.2f}")
                            print()
                            rec_side2_value = False
                            rec_side_value =False
                        else:
                            rec_side2_value = True

        elif answer == "c":
            cir_side_value = True
            while cir_side_value:
                circle_rad = float(input("Enter the circle's radius: "))
                if circle_rad > 0:
                    print(f"The circumference is {cir_circum(circle_rad):.2f}")
                    print(f"The surface area is {cir_area(circle_rad):.2f}")
                    print()
                    cir_side_value = False
                else:
                    cir_side_value = True

            pass

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

            # Empty row for the sake of readability.
            print()



def main():
    menu()
    goodbye()


if __name__ == "__main__":
    main()
