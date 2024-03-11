"""
COMP.CS.100 The 7.13 Python program.
Creator: Rahele Ahmadian
Student id number: 151200445
"""
PRICES = {
        "milk": 1.09, "fish": 4.56, "bread": 2.10,
        "chocolate": 2.70, "grasshopper": 13.25,
        "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
        "bananas": 1.05, "Pepsi": 3.15, "pizza": 4.15,
    }

def main():

    def payload(key):
        return PRICES[key]

    for product in sorted(PRICES, key=payload):
        print(f"{product} {PRICES[product]:.2f}")

# The commands we want the program to execute begin here.
# Python requires there to be at least one command here.

if __name__ == "__main__":
    main()
