#This program is showing a simple shipping calcualtor
#TPaige98 2/22/2021

def main():

    print("Hello and welcome to King's Shipping Kalculations!")
    print("This program is designed to calculate shipping cost based on inputs by the user")
    print()
    pur_price = float(input("Please enter the cost of you purchase: "))
    print()

    if pur_price <= 100:
        shipping = 10.00
    elif pur_price <= 300:
        shipping = 8.00
    elif pur_price <= 500:
        shipping = 5.00
    else:
        shipping = 0.00

    total = pur_price + shipping

    print("Your purchase of ${:.2f} has incurred a shipping charge of ${:.2f} for a total price of ${:.2f}".format(pur_price, shipping, total))
    print()
    print("Thank you for using King's Shipping Kalculations!")
main()