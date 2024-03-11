"""
COMP.CS.100 The 6.12 Python program.
Creator: Rahele Ahmadian
Student id number: 151200445
"""
def count_abbas(text):
    """
    The function returns the number of abbas (meaning the string "abba") that the
    parameter string contains.

    :param text: str,  string to be investigated the number of abbas in it
    :return: int, the number of abbas
    """
    count = 0
    for i in range(len(text) - 3):
        if text[i:i+4] == "abba":
            count += 1

    return count
def main():
    print(count_abbas("abbabbabba"))
    print(count_abbas("barbapapa"))
# The commands we want the program to execute begin here.
# Python requires there to be at least one command here.

if __name__ == "__main__":
    main()
