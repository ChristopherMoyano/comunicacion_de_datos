import os 
import time
nombres_carpetas = os.listdir('datos/') #busco los nombres de las carpetas donde tengo los archivos

#defino una funcion para buscar los nombres de todos los archivos en cada carpeta 
def buscar_archivo(ruta):
    archivos_texto = []
    archivos = os.listdir(ruta)
    for archivo in archivos:
        if archivo[-4:] == '.txt':
            archivos_texto.append(archivo)
    return archivos_texto

#funcion xor
def xor(a,b):
    if(a==b):
        return 0
    else:
        return 1


#codigo
#en cada carpeta busco los archivos de texto para realizar crc en cada uno de ellos
for carpeta in nombres_carpetas:
    ruta = 'datos/' +  carpeta
    archivos_texto = buscar_archivo(ruta)
    for texto in archivos_texto:
        with open(ruta + '/' + texto, 'r' ) as f: #abro el archivo
            print()
            print()
            print(texto) #imprimo el nombre de archivo en el que estoy realizando la accion
            c_aux=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #creacion de una variable auxiliar ya que los datos se imprimiran al reves y se guardaran en este
            c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #creacion de variable c donde se guardaran los datos en orden correcto
            data=f.read() #lectura del archivo de texto
            for input in data:

                input = int(input)
                #calculo de todas las funciones xor
                aux=xor(input,c_aux[15])
                aux_1=xor(aux,c_aux[4])
                aux_2=xor(aux,c_aux[11])
                #desplazamiento de datos por crc
                for a in range(16):
                    i=15-a
                    c_aux[i]=c_aux[i-1]
                #se reemplazan los datos correspondientes debido al crc con las funciones xor
                c_aux[0]=aux
                c_aux[5]=aux_1
                c_aux[12]=aux_2
                for i in range(16):
                    c[i] = c_aux[15-i]
            print(c) #impresion de resultado final 

