# 123 -> x means that the signal 123 is provided to wire x.
#	x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
wires = [0,0,56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

def ass_or_com(text):
    print(text.split())
    aslist = text.split()
    print(aslist)
    if aslist[0].isdigit():
        print('number ',aslist[0])
        #assign(text)
    else :
        #combine(text)
       

def setwire(signal,letter):
    wires[ord(letter)-97] = signal

def readwire(letter) :
    return (wires[ord(letter)-97])
    
#setwire(120,'z')
#print(readwire('c'))


with open("data.txt", 'r' ) as file:


    #print(wires)

    while True:
        line = file.readline()
        ass_or_com(line)
        



        if not line:
          break
