#For example:

 #   qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

def pair(line) :
    #  It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    print('pair   ', text)    
    for char in range(0,len(line)-2):
         poss = line[char] + line[char+1]
         for char2 in range(char+2,len(line)-1):
             print('poss ', poss, '  line[char2] + line[char2+1]  ',  line[char2] + line[char2+1])
             if line[char2] + line[char2+1] == poss :
                 print('match')
                 return True
    return

def double(line):
       # It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

    for char in range(0,len(line)-3):
        if line[char] == line[char+2]:
            return True
            break
    return

text = 'vhqrbbbqjkmqj'

if double(text) and pair(text) :
    print('nice')
else:
    print('naughty')
