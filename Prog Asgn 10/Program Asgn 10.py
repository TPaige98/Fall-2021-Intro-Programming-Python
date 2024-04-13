# This program will calculate the shipping cost based on the total purchase price.
# TPaige98 4/26/2021

def main():
    print("This program will calculate the shipping cost based on "
          "the total purchase price,\n")

    while True:
        try:
            company = input('Please enter the company name: ')
            if company == '':
                raise ValueError('Company name cannot be left blank')
            break
        except ValueError as excpt:
            print(excpt)

    while True:
        try:
            cost = float(input("Please enter in the purchase price: "))
            break
        except ValueError:
            print('Please enter the purchase price in the following format: 55.55')

    if cost <= 100.00:
        shipping = 10.0
    elif cost <= 300.00:
        shipping = 8.0
    elif cost <= 500.00:
        shipping = 5.0
    else:
        shipping = 0.0

    total = cost + shipping

    print("At a purchase price of ${:.2f}, the shipping cost will be ${:.2f},"
          " with a final total of ${:.2f}.".format(cost, shipping, total))
    print('{}, thank you for shopping with us!'.format(company))

main()