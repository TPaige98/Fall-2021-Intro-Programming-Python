#This program is designed to calculate payroll data based on inputs by the user
#TPaige98 4/5/2021



def main():
    fname = []
    lname = []
    hours = []
    rate = []

    firstName = input("Please enter first name or "
                        "press enter to quit!: ")          #priming read

    while firstName != "":              #while loop that also allows user to quit at end
        fname.append(firstName.strip().upper())
        lastName = input("Please enter last name: ")
        lname.append(lastName.strip().upper())
        hours.append(float(input("Please enter hours worked: ")))
        rate.append(float(input("Please enter rate of pay: ")))
        print()
        firstName = input("Please enter first name or press enter to quit!: ")

    print()
    for x in range(len(fname)):         #spaced out statement showing the final outcome
        print('{:7} {:7} {:^6.2f} {:^8.2f} ${:>4.2f}'
              .format(fname[x], lname[x], hours[x], rate[x], (hours[x] * rate[x])))

main()