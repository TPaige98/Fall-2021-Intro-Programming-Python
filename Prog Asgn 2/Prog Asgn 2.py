#This program is created to show a simple currency converter
#TPaige98 2/8/2021

def main():
    print("Hello and welcome to King's Konverter for converting currencies!")
    print()

    dollar = float(input('Enter the amount of US dollars to be converted: '))
    euro = dollar * 0.82781
    rupee = dollar * 72.8852
    pesos = dollar * 20.0576

    print()
    print('Your amount of ${:.2f} US dollars is equivalent to {:.2f} euros, {:.2f} rupees, {:.2f} pesos.'.format(dollar, euro, rupee, pesos))
    print()
    print('Thank you, and please come again for all of your konverting needs!')

main()