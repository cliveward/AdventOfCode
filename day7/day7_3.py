wires = {}
#a = []

def main():
    for cycle in range(4) :
                
        with open("data.txt", 'r' ) as file:

            while True:
                line = file.readline()
                
                if not line:
                    break

                lineaslist = line.split()
                checkwire(lineaslist)

                if lineaslist[0].isdigit() :
                    assign(lineaslist)
                elif lineaslist[0] == 'NOT' :
                    comp(lineaslist)
                elif lineaslist[1] == 'AND' :
                    andbit(lineaslist)
                elif lineaslist[1] == 'OR' :
                    orbit(lineaslist)
                elif lineaslist[1] == 'RSHIFT' :
                    right(lineaslist)
                elif lineaslist[1] == 'LSHIFT' :
                    left(lineaslist)

            print(wires['a'], wires['lx'])

                              

def andbit(text) :
    if int(wires[text[2]]) == 0 and int(wires[text[0]]) == 0 :
        return
    wires[text[4]] = int(wires[text[2]]) & int(wires[text[0]])

def assign(text):
    wires[text[2]] = text[0]

def checkwire(text):

    for item in text :
        if item.islower() and not item in wires :
            wires[item] = 0

def comp(text) :
    if int(wires[text[1]]) == 0 :
        return
    wires[text[3]] = ~int(wires[text[1]]) + 65536

def left(text) :
    wires[text[4]] = int(wires[text[0]]) << int(text[2])

def orbit(text) :
    if int(wires[text[2]]) == 0 and int(wires[text[0]]) == 0 :
        return
    wires[text[4]] = int(wires[text[2]]) | int(wires[text[0]])

def right(text) :
    wires[text[4]] = int(wires[text[0]]) >> int(text[2])
    
     

main()

