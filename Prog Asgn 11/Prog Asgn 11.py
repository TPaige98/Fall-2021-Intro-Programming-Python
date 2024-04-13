# This is a program involving reading files and working with dictionaries. Making changes to these things.
# TPaige98 5/3/2021

def state_cap(capitals):
    for state, capital in capitals.items():
        print('{}, {}'.format(state, capital))


def main():

    capitals = {}
    file = open("States.txt", "r")
    for x in file:
        split_x = x.strip().split(",")
        capitals[split_x[0]] = split_x[1]

    state_cap(capitals)
    print()

    del capitals['Ontario']
    capitals['Alaska'] = 'Juneau'
    capitals['Oklahoma'] = 'Oklahoma City'
    capitals['Wyoming'] = 'Cheyenne'
    print()

    state_cap(capitals)

    with open("StateCapitals.txt", 'w') as file:
        for state, capital in capitals.items():
            file.write('{},{}\n'.format(state, capital))


main()
