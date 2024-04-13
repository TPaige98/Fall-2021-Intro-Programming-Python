# This program is designed to ask the user to specify a file in the current directory.
# TPaige98 4/12/2021.

import os


def main():
    filename = input("Please enter the filename: ")         # user prompts to gather data and info
    foldname = input("Please enter the folder name: ")
    filepath = os.path.join(foldname, filename)
    nfile = open(filepath, "r")

    count = 0
    characters = 0
    dataline = 0
    for line in nfile:           # For loop which allows the program to read all the variables and not just one.
        count = count + len(line.split())
        characters = characters + len(line)
        dataline += 1

    print()
    print("The total number of words is: {:d}".format(count))               # print statements putting together
    print("The total number of characters is: {:d}".format(characters))     # the variables from the for loop.
    print("The total number of lines is: {:d}".format(dataline))

    nfile.close()


main()
