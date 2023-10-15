#funcion xor
def xor(a,b):
    if(a==b):
        return 0
    else:
        return 1

c_aux=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
contador=1
f = open ('dataset1/data_150.txt', 'r')
data=f.read()
for input in data:
    input = int(input)
    aux=xor(input,c_aux[15])
    aux_1=xor(aux,c_aux[4])
    aux_2=xor(aux,c_aux[11])
    for a in range(16):
        i=15-a
        c_aux[i]=c_aux[i-1]
    c_aux[0]=aux
    c_aux[5]=aux_1
    c_aux[12]=aux_2
    for i in range(16):
        c[i] = c_aux[15-i]
    print("step " + str(contador))
    print(c)
    contador=contador+1
f.close()


