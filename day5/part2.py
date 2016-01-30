def pair(line) :
    #  It contains a pair of any two letters that appears
    #at least twice in the string without overlapping
    for char in range(0,len(line)-2):
         poss = line[char] + line[char+1]
         for char2 in range(char+2,len(line)-1):
             if line[char2] + line[char2+1] == poss :
                 
                 return True
                 
    return

def double(line):
    # It contains at least one letter which repeats with
    #exactly one letter  in between them, xyx, abcdefeghi 
    for char in range(0,len(line)-2):
        if line[char] == line[char+2]:
            return True
            
    return

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
            if pair(text) and double(text) :
                nice = nice + 1
            # initialise for next string    
            text = ""

print('There are ', nice, ' nice strings')   




  
