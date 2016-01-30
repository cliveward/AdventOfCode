box = [0,0,0]

paper = 0

def add_area(box):
      global paper
      box.sort()
      l = box[0] 
      w = box[1] 
      h = box[2]
      area = 3 * l * w + 2 * l * h + 2 * w * h
      paper = paper + area
      return

with open("sizes.txt", 'r' ) as file:
    num = paper = 0
    dig = 1
    box = []
     
    while True:

        c = file.read(1)
        if not c:
              
          print( "End of file" )
          break
 #input in form  lxwxh\n where some are 2-digit      
        if c != '\n' :
            if c == 'x' :
                # ==> l or w has been read  
                box.append(num)
                # so reset digit count
                dig = 1
                
            elif dig == 1 :
                #==> reading first (or only) digit  
                num = int(c)
                # reset digit count; next char will be x, \n or 2nd digit
                dig = 2
             
            else :
                # ==> we are on 2nd of double digit  
                num = num*10 + int(c)
                # so no need to reset digit count as next char will be x or \n
                #dig = 1
                  
        else :
            #==> h has been read so dimensions complete for one box  
            # so reset digit count
            dig = 1
            box.append(num)
                
        if len(box)==3:
              add_area(box)
              box =[]

print('Total area of paper needed is  ', paper, ' square feet')


        
    
