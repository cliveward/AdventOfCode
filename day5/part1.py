
def vowels(line) :
    #at least 3 vowels
    vow = ['a', 'e', 'i', 'o', 'u']
    total = 0
    for char in vow:
        if line.count(char) > 0 :
            total = total + line.count(char)
    if total > 2 :
        return True
    return

def double(line):
    #at least one letter that appears twice in a row
    for char in range(0,len(line)-1):
        if line[char] == line[char+1]:
            return True
            break
    return

def nobads(line) :
    #must not contain the strings ab, cd, pq, or xy
    nono = ['ab', 'cd', 'pq', 'xy']
    for char in range(0,len(line)-1):
        test = line[char] + line[char+1]
        if test in nono :
            return False
            break
    return True

nice = 0
text = ""

with open("data.txt", 'r' ) as file:

    while True:
        c = file.read(1)
        if not c:
          print( "End of file" )
          break
        
        if c != '\n' :
           text = text + c
        else :
            if vowels(text) and double(text) and nobads(text) :
                nice = nice + 1
            # initialise for next line of data    
            text = ""

print('There are ', nice, ' nice strings')   




  
