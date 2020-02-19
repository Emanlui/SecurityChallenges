import pickle

with open('donotshare.p', 'rb') as f:
    o = pickle.load(f)

print(o)

outstr = ''
for line in o:
    print(line)
    print("--------------")
    for char,n in line:
        outstr += char*n
        #print(n)
        #print(char)
    outstr += '\n'
print (outstr)