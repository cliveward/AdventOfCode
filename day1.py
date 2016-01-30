houses = 0
x = y = 0

def countnew


def findhouse(input):
    
    for character in input:
        if character == "^":
            y = y + 1
        elif character == ">":
            x = x + 1
	elif character == "v":
            y = y - 1
        elif character == ">":
            x = x + 1

    return x, y

input = ""

print( x )
print( y )
