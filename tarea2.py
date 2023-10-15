#funcion xor
def xor(a,b):
    if(a==b):
        return 0
    else:
        return 1

c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
contador=1
f = open ('dataset1/data_150.txt', 'r')
data=f.read()
for input in data:
    input = int(input)
    c[0]=xor(input,c[15])
    c[5]=xor(c[0],c[4])
    c[12]=xor(c[0],c[11])
    print("step " + str(contador))
    print(c)
    for a in range(16):
        i=15-a
        if(i!=5 or i!=12 or i!=0):
            c[i]=c[i-1]
    contador=contador+1
f.close()


