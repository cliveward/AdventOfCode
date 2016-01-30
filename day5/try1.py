text = 'dvszwmarrgswjxmb'

#A nice string is one with all of the following properties:
#    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

#For example: ugknbfddgicrmopn is nice


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
    #    It does not contain the strings ab, cd, pq, or xy
    nono = ['ab', 'cd', 'pq', 'xy']
    for char in range(0,len(line)-1):
        test = line[char] + line[char+1]
        if test in nono :
            return False
            break

    return True


if vowels(text) and double(text) and nobads(text) :
    print('nice')

else :
    print('naughty')




  
