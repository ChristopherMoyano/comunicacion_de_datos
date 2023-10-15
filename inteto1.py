#funcion xor
def xor(a,b):
    if(a==b):
        return 0
    else:
        return 1

c=[0,0,0,0,0]
contador=1
data="1010001101"
for input in data:
    input = int(input)
    for a in range(5):
        i=4-a
        if(i!=4 or i!=2 or i!=0):
            c[i]=c[i-1]
    c[0]=xor(input,c[4])
    print(c[0])
    c[2]=xor(c[0],c[1])
    print(c[2]) 
    c[4]=xor(c[0],c[3])
    print(c[4])
    print("step " + str(contador))
    print(c)
    contador=contador+1