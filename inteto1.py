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
    
    aux=xor(input,c[4])
    aux_2=xor(aux,c[1])
    aux_3=xor(aux,c[3])
    for a in range(5):
        i=4-a
        c[i]=c[i-1]
    c[0]=aux
    c[2]=aux_2
    c[4]=aux_3
    print("step " + str(contador))
    print(c)
    contador=contador+1