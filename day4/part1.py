import hashlib

puzzle ='yzbqklnj'

addon = 0

md5_as_dec = int('fffffffffffffffffffffffffff', 16) + 10

while md5_as_dec > int('fffffffffffffffffffffffffff', 16) :

    addon += 1

    whole = puzzle + str(addon)

    coded = whole.encode()

    hash_object = hashlib.md5(coded)

    md5_as_dec = int(hash_object.hexdigest(), 16)


print('final answer ', addon)




    


