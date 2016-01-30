wires = {}


# a = []

def main():
    with open("data.txt", 'r') as file:

        while True:
            line = file.readline()

            if not line:
                break

            lineaslist = line.split()
            checkwire(lineaslist)

            find_target(lineaslist, 'a')
            find_target(lineaslist, 'lx')
            find_target(lineaslist, 'lw')
            find_target(lineaslist, 'lv')

            find_target(lineaslist, 'l')
            find_target(lineaslist, 'd')
            find_target(lineaslist, 'j')
            find_target(lineaslist, 'g')
            find_target(lineaslist, 'i')

        print(wires['a'], wires['lx'])


def andbit(text):
    if int(wires[text[2]]) == 0 and int(wires[text[0]]) == 0:
        return
    wires[text[4]] = int(wires[text[2]]) & int(wires[text[0]])


def assign(text):
    wires[text[2]] = text[0]


def checkwire(text):
    for item in text:
        if item.islower() and not item in wires:
            wires[item] = 0


def comp(text):
    if int(wires[text[1]]) == 0:
        return
    wires[text[3]] = ~int(wires[text[1]]) + 65536


def find_target(text, letter):
    if letter == text[-1]:
        print(text)


def left(text):
    wires[text[4]] = int(wires[text[0]]) << int(text[2])


def orbit(text):
    if int(wires[text[2]]) == 0 and int(wires[text[0]]) == 0:
        return
    wires[text[4]] = int(wires[text[2]]) | int(wires[text[0]])


def right(text):
    wires[text[4]] = int(wires[text[0]]) >> int(text[2])


main()
