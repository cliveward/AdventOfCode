lightson = []

def main() :

    count = 1
       
    with open("data.txt", 'r' ) as file:

        while True:
            line = file.readline()
            print(line)
            print(corners(line))
            if "turn on" in line :
                turnon(changes(corners(line)))
            elif 'turn off' in line :
                turnoff(changes(corners(line)))
            elif 'toggle' in line:
                toggle(changes(corners(line)))
            print('line  ', count, ' done')
            print('number of lights on = ',len(lightson))
            print('   ')
            print('   ')

            count += 1

            if not line:
              break
    return len(lightson)

def corners(text):
    a = b = x = y = -1
    for char in ((text.replace(",", " "))).split() :
        if char.isdigit():
            if x != -1 :
                y = char
            elif b != -1 :
                x = char
            elif a != -1 :
                b = char
            else :
                a = char
            
    return [[a,b],[x,y]]

def changes(coords) :
    tochange = []
    count = 0
    for x in range(int(coords[0][0]), int(coords[1][0])+1) :
        for y in range(int(coords[0][1]), int(coords[1][1])+1) :
            tochange.append([x,y])
            count += 1
    print(count, '  sets of coordinates calculated')
    print(len(tochange))
    return tochange

def toggle(bulbs):
    for item in bulbs :
        if item in lightson :
            lightson.remove(item)
        else :
            lightson.append(item)

def turnoff(bulbs):
    for item in bulbs :
        if item in lightson :
            lightson.remove(item)

def turnon(bulbs):
    for item in bulbs :
        if not item in lightson :
            lightson.append(item)



print('number of lights on = ',main())
    
