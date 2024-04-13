#This program is designed to take comma delimited input entered by the user and create a table out of it. The table is desgined to improve readability.
#TPaige98 3/29/2021

def main():
    print("This program prints out the total inventory value")
    print()
    inv_num = input("Enter name of product, then enter the number of products, then enter the cost of the products: ")
    invList = inv_num.split(",")
    '''print statement for entering the comma delimited input'''

    inventoryList = []
    for i in invList:
        inventoryList.append(i.strip().title())
    print(inventoryList)
    print()
    '''takes the list and deletes spaces that are not needed'''

    sum = 0
    for i in range(len(inventoryList))[0::3]:
        invfloat = float(inventoryList[i + 1])
        pricefloat = float(inventoryList[i + 2])
        totalinv = float(pricefloat * invfloat)
        print('{:19} {:^6} {:^8.2f} ${:>6.2f}'.format(inventoryList[i], invfloat, pricefloat, totalinv))
        sum = totalinv + sum
    '''variables allowing for calculations and print statement forming the table'''

    print()
    print("The value of the entire inventory is ${:.2f}.".format(sum))
    '''print statement showing the total inventory in dollars'''

main()

'''
Input
CD-R 100 disc,  25, 14.00 ,DVD-R 50 disc,10, 10.00 ,  HDMI cable 3ft,12, 4.00 ,Flash Drive 32GB  ,16, 9.00 ,   Laptop Cooling Pad  ,10, 25.00

Ending display:

CD-R 100 disc		  25	 14.00 	 $350.00
DVD-R 50 disc		  10	 10.00 	 $100.00
HDMI cable 3ft		  12	  4.00 	 $ 48.00
Flash Drive 32GB	  16	  9.00 	 $144.00
Laptop Cooling Pad	  10	 25.00 	 $250.00

The total value of the inventory is $892.00.
'''