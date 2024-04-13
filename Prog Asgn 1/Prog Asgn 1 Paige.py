#This program is created to show a simple hotel billing system.
#TPaige98 1/30/21

def main():
    print('Welcome to Kings Kastle. The following will calculate the billing amount for your stay.')
    print()

    print('Enter the number of days for hotel stay:', end=' ')
    num_days = int(input())

    print('Enter the cost per day:', end=' ')
    cost_per_day = int(input())
    print()

    total = num_days * cost_per_day
    print('Your total will be', total, 'dollars!')
    print()

    print('Kings Kastle')

    print('   @..@ ')
    print('  (----) ')
    print(' ( >__< ) ')
    print('^^  ~~  ^^ ')
    print()
main()

