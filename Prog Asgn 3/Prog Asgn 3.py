#this is a program that shows a simple payroll calculator.
#TPaige98 2/15/2021

def main():
    hours = [6.5, 8.75, 10.25, 0.0, 8.25]

    print("Hello and welcome to King's Kalcualtion's for the Payroll!")
    print("This program is designed to calculate payroll based on inputs by the user.")
    print()
    employee_first = input("Please enter your first name: ")
    employee_last = input("Please enter your last name: ")
    print()

    hours_sat = float(input("Please enter the hours worked today: "))
    hours.append(hours_sat)
    print()

    earned = sum(hours)
    print("Total hours worked this week: ", earned)
    print()

    wage = float(input("Please enter your hourly wage: "))

    days_off = hours.count(0.0)
    days_worked = len(hours) - days_off
    total_pay = earned * wage
    print()

    print('{} {} earned ${:.2f} for working {} days this week.'.format(employee_first, employee_last, total_pay, days_worked))

    print('Thank you!')
main()
