#This program will determine the commission for a sales person's weekly sales.
#TPaige98 3/1/2021

def main():

    print("Hello and welcome to King's Komission!")
    print("This program is designed to calculate commission based on the user's inputs.")
    print()

    days = ('Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday')

    employee_name = input("Please enter your name: ")
    print()

    commission = 0
    total = 0

    for day in days:
       sales = float(input("Please enter your sales for {0}: ".format(day)))
       commission += sales * 0.1
       total += sales
    print()
    print('{} had total sales of ${:.2f} this week for a commission of ${:.2f}'.format(employee_name, total, commission))

    print('Thank you!')
main()