#----1----#

a= ("preetipreethbhcbdnbdhbnjsjfuhrpreeti")
d= {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# for i,j in d:


print(d)



#----2----#

#compress string 
#Input = aabbccaaaafffeiii
#Output = a2b2c2a4f3e1


a = "aabbccaaaafffeiii"

def compress(n):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else: 
            d[i] = 1
    # return d
    x= ""
    for i, j in d.items():
        x += f"{i}{j}"
    return x


result = compress(a)  
print(result)



#----3----#

def compress(s):
    x= len(s)
    new_s= ""
    count = 1
    for i in range(x-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            new_s += (s[i] + str(count))
            count = 1

    new_s += (s[-1] + str(count))
    return new_s

result = compress(a)
print(result)