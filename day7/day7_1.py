# 123 -> x means that the signal 123 is provided to wire x.
#	x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.

signal1 = '5 -> x'

signal2 = '3 -> z'

signal3 = 'x AND y -> z'


signal = '123'

signal2 = '11'

text = '123 -> x'
for item in text.split() :
    #print(int(item))

    if item.isdigit :
        print('number = ',item)



with open("data.txt", 'r' ) as file:

    while True:
        line = file.readline()

        for item in line.split() :
            #print(int(item))

            if item.isalpha :
                print('alpha = ',item)
            elif item.isdigit :
                print('number = ',int(item))



        if not line:
          break

