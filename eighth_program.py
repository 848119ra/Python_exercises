"""
Program that asks how much purchases cost and the amount of paid money and then
prints the amount of change. To simplify the program, only 1, 2, 5 and 10 euros
are offered as change. It is assumed that the paid amount is always euros, i.e.
no cents are paid besides euros. It is further assumed that the paid amount is
always at least 1 euro.
"""

def main():
    # How much purchases cost?
    string_purchase = input("Purchase price: ")
    purchase = int(string_purchase)
    # Amount of paid money
    string_money = input("Paid amount of money: ")
    money = int(string_money)
    if money > purchase:
        change = money - purchase
        ten_euro = change // 10
        change = change - ten_euro * 10
        five_euro = change // 5
        change = change - five_euro * 5
        two_euro = change // 2
        change = change - two_euro * 2
        one_euro = change // 1
        change = change - one_euro * 1
        print("Offer change:")
        if ten_euro > 0:
            print(str(ten_euro) + " ten-euro notes")
        if five_euro > 0:
            print(str(five_euro) + " five-euro notes")
        if two_euro > 0:
            print(str(two_euro) + " two-euro coins")
        if one_euro > 0:
            print(str(one_euro) + " one-euro coins")
    elif money == purchase:
        print("No change")
    elif money < purchase:
        print("No change")
if __name__ == "__main__":
    main()