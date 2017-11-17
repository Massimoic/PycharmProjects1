import random

def Ordenar(alist):
    alist[0] = int(alist[0])
    alist[1]= int (alist[1])
    if alist[0] > alist[1]:
        aux = alist[0]
        alist[0] = alist[1]
        alist[1] = aux

codigo = []
nturnos = 1
nturnos2=1
nturnos3=1
c = 0
b = 0
yaestan = []
gano=0
gano2=0
gano3=0
#ale
txt1=open("Resumen.txt","a")
#yi
txt2=open("Resumen.txt", "r")
#f
txt3=open("Resumen.txt","r+")

print("Bienvenidos a Megamente por Diego de la Puente y Massimo Imparato")
print("")

#instrucciones
print("************************************************************************************************************************")
print("* Instrucciones:                                                                                                       *")
print("* El objetivo del juego es determinar el número aleatorio que se crea, en la menor cantidad de intentos posibles.      *")
print("* El programa te indicará si un dígito está en su lugar correcto o que está en el código pero ubicado en otra posición.*")
print("* Los numeros se pueden repetir                                                                                        *")
print("* Para este nivel, solo estan permitidos los números del 0-5                                                           *")
print("* El maximo numero de intentos permitidos es de 10.                                                                    *")
print("************************************************************************************************************************")
for i in range(4):
    codigo.append(random.randint(0,5))

while nturnos <= 10:
    # maximos intentos 10
    print("")
    print("Turno:", nturnos)
    codadv = list(map(int, list(str(input("Ingresa codigo de 4 digitos:")))))
    # ingresar cuatro numero que se agregan a una lista
    print("")
    if len(codadv)==4:
        if codadv[0] == codigo[0] and codadv[1] == codigo[1] and codadv[2] == codigo[2] and codadv[3] == codigo[3]:
            # si todo el código esta bien
            print(" --------- Ganaste! --------- ")
            gano=gano+1
            codigo = []
            nturnos2= 1
            c = 0
            b = 0
            yaestan = []
            gano2=0
            print("")
            print("Nivel 2")
            print("")
            #instrucciones
            print("************************************************************************************************************************")
            print("* Instrucciones:                                                                                                       *")
            print("* Ingresar un numero de 4 digitos.                                                                                     *")
            print("* El programa te indicara si un digito está en su lugar correcto o que está en el código pero ubicado en otra posición.*")
            print("* Los numeros se pueden repetir                                                                                        *")
            print("* Para este nivel, solo están permitidos los números del 0-7                                                           *")
            print("* El máximo número de intentos es de 10.                                                                               *")
            print("************************************************************************************************************************")

            for i in range(4):
                codigo.append(random.randint(0,7))

            while nturnos2 <= 10:
                # maximos intentos 10
                print("")
                print("Turno:", nturnos2)
                codadv = list(map(int, list(str(input("Ingresa código de 4 digitos:")))))
                # ingresar cuatro numero que se agregan a una lista
                print("")
                if len(codadv)==4:
                    if codadv[0] == codigo[0] and codadv[1] == codigo[1] and codadv[2] == codigo[2] and codadv[3] == codigo[3]:
                        # si todo el codigo esta bien
                        print(" --------- Ganaste! --------- ")
                        gano2=gano2+1
                        codigo = []
                        nturnos3 = 1
                        c = 0
                        b = 0
                        yaestan = []
                        gano3=0
                        print("")
                        print("Nivel 3")
                        #instrucciones
                        print("************************************************************************************************************************")
                        print("* Instrucciones:                                                                                                       *")
                        print("* Ingresar un numero de 4 digitos.                                                                                     *")
                        print("* El programa te indicara si un digito esta en su lugar correcto o que esta en el código pero ubicado en otra posición.*")
                        print("* Los numeros se pueden repetir                                                                                        *")
                        print("* Para este nivel, solo están permitidos los numeros del 0-9.                                                          *")
                        print("* El máximo número de intentos es de 10.                                                                               *")
                        print("************************************************************************************************************************")
                        for i in range(4):
                            codigo.append(random.randint(0,9))

                        while nturnos3 <= 10:
                            # maximos intentos 10
                            print("")
                            print("Turno:", nturnos3)
                            codadv = list(map(int, list(str(input("Ingresa código de 4 digitos:")))))
                            # ingresar cuatro numero que se agregan a una lista
                            print("")
                            if len(codadv)==4:
                                if codadv[0] == codigo[0] and codadv[1] == codigo[1] and codadv[2] == codigo[2] and codadv[3] == codigo[3]:
                                    # si todo el codigo esta bien
                                    print("Ganaste")
                                    gano3=gano3+1
                                    break
                                for i in range(4):
                                    if codadv[i] == codigo[i]:
                                        # si el mismo elemento esta en la misma posicion
                                        c = c + 1
                                        yaestan.append(codadv[i])
                                        #para que no se repitan los valores en el de otro lugar
                                for i in range(4):
                                    if codadv[i] in codigo and codadv[i] not in yaestan:
                                            #si esta en el codigo pero en otro lugar
                                            b = b + 1
                                print("Hay", c, "números bien posicionados")
                                print("Hay", b, "números que se encuentran en el código pero que no están bien posicionados")
                                nturnos3 = nturnos3 + 1
                                # reicniciar lista y contadores
                                codadv.clear()
                                yaestan.clear()
                                b = 0
                                c = 0
                            elif len(codadv)>4:
                                print("Solo ingresa 4 digitos")
                            else:
                                print("No ingresaste 4 digitos")

                        if nturnos3 == 11:
                            print("")
                            print("Perdiste, el código era", codigo)
                        break
                    for i in range(4):
                        if codadv[i] == codigo[i]:
                            # si el mismo elemento esta en la misma posicion
                            c = c + 1
                            yaestan.append(codadv[i])
                            #para que no se repitan los valores en el de otro lugar
                    for i in range(4):
                        if codadv[i] in codigo and codadv[i] not in yaestan:
                                #si esta en el codigo pero en otro lugar
                                b = b + 1
                    print("Hay", c, "números bien posicionados")
                    print("Hay", b, "números que se encuentran en el código pero que no están bien posicionados")
                    nturnos2 = nturnos2 + 1
                    # reicniciar lista y contadores
                    codadv.clear()
                    yaestan.clear()
                    b = 0
                    c = 0
                elif len(codadv)>4:
                    print("Solo ingresa 4 digitos")
                else:
                    print("No ingresaste 4 digitos")

            if nturnos2 == 11:
                print("")
                nturnos2=10
                print("Perdiste, el código era", codigo)
            break
        for i in range(4):
            if codadv[i] == codigo[i]:
                # si el mismo elemento esta en la misma posicion
                c = c + 1
                yaestan.append(codadv[i])
                #para que no se repitan los valores en el de otro lugar
        for i in range(4):
            if codadv[i] in codigo and codadv[i] not in yaestan:
                    #si esta en el codigo pero en otro lugar
                    b = b + 1
        print("Hay", c, "números bien posicionados")
        print("Hay", b, "números que se encuentran en el código pero que no están bien posicionados")
        nturnos = nturnos + 1
        # reicniciar lista y contadores
        codadv.clear()
        yaestan.clear()
        b = 0
        c = 0
    elif len(codadv)>4:
        print("Solo ingresa 4 digitos")
    else:
        print("No ingresaste 4 digitos")

if nturnos == 11:
    print("")
    nturnos2=10
    nturnos3=10

    print("Perdiste, el código era", codigo)

archivo= txt2.readlines()
#leer las lineas del archivo y ponerlo en una lista

linea2=str(archivo[1])
linea2 = linea2.split(" ")
vecesjugadas=int(linea2[2])+1

linea3=str(archivo[2])
linea3=linea3.split(" ")
ganar=gano+int(linea3[2])

porcentaje=(ganar*100)/vecesjugadas

linea5=str(archivo[4])
linea5=linea5.split(" ")
alist=[linea5[4]]
alist.append(int(nturnos))
Ordenar(alist)
alist.pop(1)

linea8=str(archivo[7])
linea8 = linea8.split(" ")
vecesjugadas2=int(linea8[2])+1

linea9=str(archivo[8])
linea9=linea9.split(" ")
ganar2=gano2+int(linea9[2])

porcentaje2=(ganar2*100)/vecesjugadas2

linea11=str(archivo[10])
linea11=linea11.split(" ")
alist2=[linea11[4]]
alist2.append(int(nturnos2))
Ordenar(alist2)
alist2.pop(1)

linea14=str(archivo[13])
linea14 = linea14.split(" ")
vecesjugadas3=int(linea14[2])+1

linea15=str(archivo[14])
linea15=linea15.split(" ")
ganar3=gano3+int(linea15[2])

porcentaje3=(ganar3*100)/vecesjugadas3

linea17=str(archivo[10])
linea17=linea17.split(" ")
alist3=[linea17[4]]
alist3.append(int(nturnos3))
Ordenar(alist3)
alist3.pop(1)


txt1.write("Nivel 1"+("\n"))
txt1.write("Veces jugadas: "+str(vecesjugadas)+("\n"))
txt1.write("Veces ganadas: "+str(ganar)+("\n"))
txt1.write("Porcentaje de veces ganadas: "+ str(round(porcentaje,2))+"%"+("\n"))
txt1.write("Record de menor turnos: "+str(alist[0])+(" turnos")+("\n"))
txt1.write("\n")
txt1.write("Nivel 2"+("\n"))
txt1.write("Veces jugadas: "+str(vecesjugadas2)+("\n"))
txt1.write("Veces ganadas: "+str(ganar2)+("\n"))
txt1.write("Porcentaje de veces ganadas: "+ str(round(porcentaje2,2))+"%"+("\n"))
txt1.write("Record de menor turnos: "+str(alist2[0])+(" turnos")+("\n"))
txt1.write("\n")
txt1.write("Nivel 3"+("\n"))
txt1.write("Veces jugadas: "+str(vecesjugadas3)+("\n"))
txt1.write("Veces ganadas: "+str(ganar3)+("\n"))
txt1.write("Porcentaje de veces ganadas: "+ str(round(porcentaje3,2))+"%"+("\n"))
txt1.write("Record de menor turnos: "+str(alist3[0])+(" turnos"))

txt3.truncate()

txt1.close()
txt2.close()
txt3.close()
