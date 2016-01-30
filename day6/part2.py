grid = []

def main() :

    generate_grid(1000)

         
    with open("data.txt", 'r' ) as file:

        while True:
            line = file.readline()
            if "turn on" in line :
                turnon((corners(line)))
            elif 'turn off' in line :
                turnoff((corners(line)))
            elif 'toggle' in line:
                toggle((corners(line)))

            if not line:
              break
    return lightson(grid)

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

def generate_grid(size):
    
    for rowcount in range (size):
        col = []
        for colcount in range(size):
            col.append(0)
        grid.append(col)

def lightson(array):
    total = 0
    for block in array :
        for bulb in block :
            total = total + int(bulb)

    return total   
    
def toggle(coords):
    for x in range(int(coords[0][0]), int(coords[1][0])+1) :
        for y in range(int(coords[0][1]), int(coords[1][1])+1) :
            grid[x][y] = grid[x][y] + 2

def turnoff(coords):
    for x in range(int(coords[0][0]), int(coords[1][0])+1) :
        for y in range(int(coords[0][1]), int(coords[1][1])+1) :
            if grid[x][y] > 0 :
                grid[x][y] = grid[x][y] - 1


def turnon(coords):
    #count = 0
    for x in range(int(coords[0][0]), int(coords[1][0])+1) :
        for y in range(int(coords[0][1]), int(coords[1][1])+1) :
            grid[x][y] = grid[x][y]+1

print('total brightness of lights = ',main())
    
