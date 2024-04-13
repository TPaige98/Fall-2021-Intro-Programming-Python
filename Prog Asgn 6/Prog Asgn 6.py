#This program will determine the cost for a serving of a giant sub, serving's = 3 inches
#TPaige98 3/22/2021

def main():

    print("Hello and welcome to King's Sandwich")
    print("This program is designed to calculate the cost per serving of a giant sub based on inputs by the user")
    print()

    x = 1
    while x == 1:

        sub_length = float(input("Please enter the length of your sub in inches: "))
        sub_cost = float(input("Please enter the total cost of your sub in dollars: "))

        def numServings():
            sub_servings = sub_length / 3
            sub_servings = round(sub_servings)
            return sub_servings
        num_servings = numServings()

        def costPerServing():
            sub_cost_serving = sub_cost / num_servings
            return sub_cost_serving
        cost_per_serving = costPerServing()

        print()
        print('Your sub contains {} servings at a cost of ${:.2f} per serving!'.format(num_servings, cost_per_serving))
        loop_ans = input('If you would like to enter another sub, simply just type (Y) or (N): ')
        print()
        if loop_ans == 'N' or loop_ans == 'n':
            x = 0

main()
