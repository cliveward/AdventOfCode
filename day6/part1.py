
# this is a list comprehension
grid = [[0 for col_num in range(1000)] for row_num in range(1000)]
def main() :

    with open("data.txt", 'r' ) as file:

        for line in file.readlines() :

            if "turn on" in line :
                turn_on((corners(line)))
            elif 'turn off' in line :
                turn_off((corners(line)))
            elif 'toggle' in line:
                toggle((corners(line)))


    return lights_on(grid)

def corners(text):
    coords = []
    for num in ((text.replace(",", " "))).split() :
        if num.isdigit():
            coords.append(num)
    x, y, x1, y1 = coords

    return [[x,y],[x1,y1]]


def lights_on(array):
    total = 0
    for item in array :
        total = total + item.count(1)
    return total

def toggle(coords):
    for x in range(int(coords[0][0]), int(coords[1][0])+1) :
        for y in range(int(coords[0][1]), int(coords[1][1])+1) :
            grid[x][y] = not grid[x][y]

def turn_off(coords):
    for x in range(int(coords[0][0]), int(coords[1][0])+1) :
        for y in range(int(coords[0][1]), int(coords[1][1])+1) :
            grid[x][y] = False

def turn_on(coords):
    #count = 0
    for x in range(int(coords[0][0]), int(coords[1][0])+1) :
        for y in range(int(coords[0][1]), int(coords[1][1])+1) :
            grid[x][y] = True

print('number of lights on = ',main())

