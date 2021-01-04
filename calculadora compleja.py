#Calculadora compleja
import tkinter 
#from tkinter import * lo metes antes al comando pa que jale
from math import *
import array as arr
import matplotlib.pyplot as plt
import numpy as np
ventana = Tk()
frame=Frame(ventana)


#funcion que pasa cuando oprimes el boton
def funcion():
    #rr resultado real
    #ri resultado imaginario
    w=1.0
    
    a=9*w
    b=2*w
    c=3*w
    d=8*w

    miz1=z1.get()
    miz2=z2.get()
    mide1=len(miz1)
    mide2=len(miz2)

    imaginario=miz1.find("i")
    imaginario2=miz2.find("i")

    #primer numero
    if miz1=="-i":
        #print("es -1i")
        a=0
        b=-1
    elif miz1=="i":
        #print("es +1i")
        a=0
        b=1
    elif imaginario!=-1:
        #print("z1 tiene imaginario en",imaginario,"mide",mide1)
        if miz1[0]=="-":
            signomas=miz1.find("+")
            if signomas!=-1:
                #print("signo mas se encuentra en",signomas)
                a=float(miz1[0:signomas])
                b=float(miz1[signomas:mide1-1])
            else:    
                copy=miz1[1:mide1]
                siggno=copy.find("-")
                
                siggno=siggno+1
                a=float(miz1[0:siggno])
                b=float(miz1[siggno:mide1-1])
        else:
            signomas=miz1.find("+")
            signomenos=miz1.find("-")
            if signomas!=-1:
                if signomenos!=-1:
                    a=float(miz1[0:signomas])
                    b=float(miz1[signomas:mide1-1])
                elif miz1[0]=="+":
                    a=float(miz1[0:mide1])
                    b=0
                else:
                    a=float(miz1[0:signomas])
                    b=float(miz1[signomas:mide1-1])
            elif signomenos!=-1:
                a=float(miz1[0:signomenos])
                b=float(miz1[signomenos:mide1-1])
            else:
                a=0
                b=float(miz1[0:mide1-1])
    else:
        #print("z1 no hay imaginario")
        a=w*float(miz1)
        b=0.0

    #segundo numero
    if miz2=="-i":
        #print("es -1i")
        c=0
        d=-1
    elif miz2=="i":
        #print("es +1i")
        c=0
        d=1
    elif imaginario2!=-1:
        #print("z1 tiene imaginario en",imaginario,"mide",mide2)
        if miz2[0]=="-":
            signomas=miz2.find("+")
            if signomas!=-1:
                #print("signo mas se encuentra en",signomas)
                c=float(miz2[0:signomas])
                d=float(miz2[signomas:mide2-1])
            else:    
                copy=miz2[1:mide2]
                siggno=copy.find("-")
                siggno=siggno+1
                c=float(miz2[0:siggno])
                d=float(miz2[siggno:mide2-1])
        else:
            signomas=miz2.find("+")
            signomenos=miz2.find("-")
            if signomas!=-1:
                if signomenos!=-1:
                    c=float(miz2[0:signomas])
                    d=float(miz2[signomas:mide2-1])
                elif miz2[0]=="+":
                    c=float(miz2[0:mide2])
                    d=0
                else:
                    c=float(miz2[0:signomas])
                    d=float(miz2[signomas:mide2-1])
            elif signomenos!=-1:
                c=float(miz2[0:signomenos])
                d=float(miz2[signomenos:mide2-1])
            else:
                c=0
                d=float(miz2[0:mide2-1])
    else:
        #print("z1 no hay imaginario")
        c=w*float(miz2)
        d=0.0

    if miz2 == "0":
        c=0.0
        d=0.0
        print("Numero 2 es igual a cero")
    
    print("\n")
    print("a vale: ",a)
    print("b vale: ",b)
    print("c vale: ",c)
    print("d vale: ",d)

    aw=a
    bw=b
    if suma.get()==True:
    	#print("Sumare")
        rrsuma.set(a+c)  
        risuma.set(b+d) 
        label22=Label(ventana,text="Suma= ")
        label22.grid(row=13,column=1)
        label21=Label(ventana,textvariable=rrsuma)
        label21.grid(row=13,column=2) 
        label23=Label(ventana,text="+i")
        label23.grid(row=13,column=3)
        label24=Label(ventana,textvariable=risuma)
        label24.grid(row=13,column=4)

    if conjugado.get()==True:
    	#print("Hare el conjugado")
        rrconjugado.set(a)
        riconjugado.set(b*(-1))
        label25=Label(ventana,text="Conjugado= ")
        label25.grid(row=14,column=1)
        label26=Label(ventana,textvariable=rrconjugado)
        label26.grid(row=14,column=2)
        label27=Label(ventana,text="+i")
        label27.grid(row=14,column=3)
        label28=Label(ventana,textvariable=riconjugado)
        label28.grid(row=14,column=4)

    if resta.get()==True:
        #print("Resta")
        rrresta.set(a-c)
        riresta.set(b-d)
        label29=Label(ventana,text="Resta= ")
        label29.grid(row=15,column=1)
        label30=Label(ventana,textvariable=rrresta)
        label30.grid(row=15,column=2)
        label31=Label(ventana,text="+i")
        label31.grid(row=15,column=3)
        label32=Label(ventana,textvariable=riresta)
        label32.grid(row=15,column=4)
#--------------------------------------------------Todo bien hasta aqui con las funciones-------------------
    if raiz.get()==True:
        #print("Raiz")
        angulo=DoubleVar()
        magnitud=DoubleVar()
        rrraiz.set(c)
        riraiz.set(d)
        magnitud=sqrt(pow(c,2)+pow(d,2))
        label33=Label(ventana,text="F.Cartesiana= ")
        label33.grid(row=16,column=1)
        if c>=0.0:
            if c==0.0:
                if d>=1:
                    angulo=90
                if d==0.0:
                    angulo=0.0
                if d<1:
                    angulo=270

            elif    c>0.0:
                if  d>=0.0:
                    #print("Primer cuadrante")
                    angulo=degrees(atan(d/c))  #calcular el arctan y pasarlo a angulo
                if d<0.0:
                    #print("Cuarto cuadrante")
                    angulo=360 - degrees(atan(d/(c*-1))) 

        if c<0.0:
            if d>=0.0:
                #print("Segundo cuadrante")
                angulo=180 - degrees(atan((d*-1)/c)) 
            if d<0.0:
                #print("Tercer cuadrante")
                angulo=180 + degrees(atan((d*-1)/(c*-1))) 
        
        var=StringVar()
        var.set(angulo)
        var2=StringVar()
        var2.set(magnitud)

        #print(angulo)
        label50=Label(ventana,text="Todas las raices:")
        label50.grid(row=25,column=1)
        #print(magnitud)
        label34=Label(ventana,textvariable=var2)
        label34.grid(row=16,column=2)
        label35=Label(ventana,text="<")
        label35.grid(row=16,column=3)
        label36=Label(ventana,textvariable=var)
        label36.grid(row=16,column=4)
        


  

        #ensenar las raices
        print("-----------------------------------------------------------")
        print("\nValores de las raices\n")
        cuenta = 0 
        min=DoubleVar()
        min=n.get()
        valor=DoubleVar()
        angulod=np.empty(40)

        for i in range(n.get()):
            valor=magnitud
            angulod[i]=(float(angulo+360*i))/(n.get())
            print('Z',i,'=',valor,'^1/',min,'<',angulod[i])
            cuenta= cuenta + 1

        #aqui empieza todo------------------------------------------------
        noxx=np.empty(20)
        noyx=np.empty(20)
        angulodd=np.empty(40)
        va=n.get()
        #print(va) si no agregas en float no sale nada 
        if va==0: 
            print("no se hace la division")
            raiz33=1
        else:
            raiz33=float(1)/va
        magnitudd=sqrt(pow(c,2)+pow(d,2))
        magnituddd=pow(magnitudd,raiz33)
        
        
        if c>=0.0:
            if c==0.0:
                if d>=1:
                    angulo=90
                if d==0.0:
                    angulo=0.0
                if d<1:
                    angulo=270
            elif    c>0.0:
                if  d>=0.0:
                    #print("Primer cuadrante")
                    angulo=degrees(atan(d/c))  #calcular el arctan y pasarlo a angulo
                if d<0.0:
                    #print("Cuarto cuadrante")
                    angulo=360 - degrees(atan(d/(c*-1))) 
        if c<0.0:
            if d>=0.0:
                #print("Segundo cuadrante")
                angulo=180 - degrees(atan((d*-1)/c)) 
            if d<0.0:
                #print("Tercer cuadrante")
                angulo=180 + degrees(atan((d*-1)/(c*-1))) 

        for i in range(20):
            noxx[i]=0.0
            noyx[i]=0.0
        for i in range(n.get()):
            angulodd[i]=(float(angulo+360*i))/(n.get()) #el angulo es perfecto
            #EN el caso de sen y cos acepta los valores en radianes, y como tengo los angulos lo pasare a radianes
            noxx[i]=magnituddd*float(cos(angulodd[i]*(pi/180)))
            #print'angulo y',noxx[i],'de', angulodd[i]
            noyx[i]=magnituddd*float(sin(angulodd[i]*(pi/180)))
            #print'angulo x',noyx[i],'de', angulodd[i]
        #para ver cuales datos ingresaron
        print('\nValores de las raices en Forma cartesiana\n')
        for i in range(n.get()):
            print('Raiz',i,'=',noxx[i],'+i',noyx[i])
            #print'Valor y',i,'=',noyx[i]
        plt.scatter(noxx,noyx,color="green")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada y")
        plt.title("Raices de Z2")
        plt.grid(True)
        plt.show()

   


    if multiplicacion.get()==True:
        #print("Multiplicando")
        rrmultiplicacion.set(a*c-b*d)  
        rimultiplicacion.set(a*d+b*c) 
        label38=Label(ventana,text="Multiplicacion= ")
        label38.grid(row=18,column=1)
        label39=Label(ventana,textvariable=rrmultiplicacion)
        label39.grid(row=18,column=2) 
        label40=Label(ventana,text="+i")
        label40.grid(row=18,column=3)
        label41=Label(ventana,textvariable=rimultiplicacion)
        label41.grid(row=18,column=4)

    if elevado.get()==True:
    	#print("Elevando")
        aa=a
        bb=b
        #print(n.get())
        rrel=aa*aa-bb*bb
        riel=aa*bb+bb*aa
        copyrrel=rrel
        copyriel=riel
        conta=n.get()-2
        for i in range(conta):
            rrel=aa*copyrrel-bb*copyriel
            riel=aa*copyriel+bb*copyrrel
            copyrrel=rrel
            copyriel=riel
   
        rrelevado.set(rrel)  
        rielevado.set(riel) 
        label42=Label(ventana,text="Elevado= ")
        label42.grid(row=19,column=1)
        label43=Label(ventana,textvariable=rrelevado)
        label43.grid(row=19,column=2) 
        label44=Label(ventana,text="+i")
        label44.grid(row=19,column=3)
        label45=Label(ventana,textvariable=rielevado)
        label45.grid(row=19,column=4)

    if entre.get()==True:
    	#print("Dividiendo")
        aa=a
        bb=b
        cc=c
        dd=d
        if(cc == 0 and dd== 0):
        	label46=Label(ventana,text="Dividir no es posible")
        	label46.grid(row=20,column=1)
        else:
        	rient=(bb*cc-aa*dd)/(cc*cc-(-dd*dd))
	        rrent=(cc*aa-(-dd*bb))/(cc*cc-(-dd*dd))
	        rrentre.set(rrent)
	        rientre.set(rient)
	        label46=Label(ventana,text="Dividiendo= ")
	        label46.grid(row=20,column=1)
	        label47=Label(ventana,textvariable=rrentre)
	        label47.grid(row=20,column=2) 
	        label48=Label(ventana,text="+i")
	        label48.grid(row=20,column=3)
	        label49=Label(ventana,textvariable=rientre)
	        label49.grid(row=20,column=4)


    if distancia.get()==True:
    	#print("distancia")
        aa=a
        bb=b
        cc=c
        dd=d
        realrest1=aa-(cc)
        imarest1=bb-(dd)
        resultadoval=sqrt(pow(realrest1,2)+pow(imarest1,2))
        rrdistancia.set(resultadoval)
        label46=Label(ventana,text="Distancia= ")
        label46.grid(row=21,column=1)
        label47=Label(ventana,textvariable=rrdistancia)
        label47.grid(row=21,column=2) 
	

def graficas():

    if suma.get()==True:
        xre=[a.get(),c.get(),rrsuma.get()]
        yim=[b.get(),d.get(),risuma.get()]
        plt.scatter(xre,yim,color="red")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada y")
        plt.title("Suma de No. Complejos")
        plt.grid(True)
        plt.show()

    if entre.get()==True:
        #print("entre")
        xre=[a.get(),c.get(),rrentre.get()]
        yim=[b.get(),d.get(),rientre.get()]
        plt.scatter(xre,yim,color="blue")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada y")
        plt.title("Division de 2 numeros")
        plt.grid(True)
        plt.show()

    if multiplicacion.get()==True:
        xre=[a.get(),c.get(),rrmultiplicacion.get()]
        yim=[b.get(),d.get(),rimultiplicacion.get()]
        plt.scatter(xre,yim,color="blue")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada y")
        plt.title("Multiplicacion de No. Complejos")
        plt.grid(True)
        plt.show()

    if resta.get()==True:
        xre=[a.get(),c.get(),rrresta.get()]
        yim=[b.get(),d.get(),riresta.get()]
        plt.scatter(xre,yim,color="red")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada y")
        plt.title("Resta de No. Complejos")
        plt.grid(True)
        plt.show()

    if conjugado.get()==True:
        xconjugado=[rrconjugado.get(),a.get()]
        yconjugado=[b.get()*-1,b.get()]
        plt.scatter(xconjugado,yconjugado,color="green")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada y")
        plt.title("Conjugado del Complejo")
        plt.grid(True)
        plt.show()

    if raiz.get()==True:
        print("-")
        noxx=np.empty(20)
        noyx=np.empty(20)
        angulodd=np.empty(40)
        va=n.get()
        #print(va) si no agregas en float no sale nada 
        print(a.get())
        print(aw.get())
        if va==0: 
            print("no se hace la division")
            raiz33=1
        else:
            raiz33=float(1)/va
        magnitudd=sqrt(pow(a.get(),2)+pow(b.get(),2))
        magnituddd=pow(magnitudd,raiz33)
        
        
        if a.get()>=0.0:
            if a.get()==0.0:
                if b.get()>=1:
                    angulo=90
                if b.get()==0.0:
                    angulo=0.0
            elif    a.get()>0.0:
                if  b.get()>=0.0:
                    #print("Primer cuadrante")
                    angulo=degrees(atan(b.get()/a.get()))  #calcular el arctan y pasarlo a angulo
                if b.get()<0.0:
                    #print("Cuarto cuadrante")
                    angulo=360 - degrees(atan(b.get()/(a.get()*-1))) 
        if a.get()<0.0:
            if b.get()>=0.0:
                #print("Segundo cuadrante")
                angulo=180 - degrees(atan((b.get()*-1)/a.get())) 
            if b.get()<0.0:
                #print("Tercer cuadrante")
                angulo=180 + degrees(atan((b.get()*-1)/(a.get()*-1))) 
        for i in range(20):
            noxx[i]=0.0
            noyx[i]=0.0
        for i in range(n.get()):
            angulodd[i]=(float(angulo+360*i))/(n.get()) #el angulo es perfecto
            #EN el caso de sen y cos acepta los valores en radianes, y como tengo los angulos lo pasare a radianes
            noxx[i]=magnituddd*float(cos(angulodd[i]*(pi/180)))
            #print'angulo y',noxx[i],'de', angulodd[i]
            noyx[i]=magnituddd*float(sin(angulodd[i]*(pi/180)))
            #print'angulo x',noyx[i],'de', angulodd[i]
        #para ver cuales datos ingresaron
        print('Valores de las raices en Forma cartesiana')
        for i in range(n.get()):
            print('Raiz',i,'=',noxx[i],'+i',noyx[i])
            #print'Valor y',i,'=',noyx[i]
        plt.scatter(noxx,noyx,color="green")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada y")
        plt.title("Raices de Z1")
        plt.grid(True)
        plt.show()

    if elevado.get()==True:
        #print("elevadoo")
        xre=[a.get(),rrelevado.get()]
        yim=[b.get(),rielevado.get()]
        plt.scatter(xre,yim,color="blue")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada y")
        plt.title("Z1 elevado a la n")
        plt.grid(True)
        plt.show()

    if distancia.get()==True:
        #print("distancia")
        xre=[a.get(),c.get()]
        yim=[b.get(),d.get()]
        plt.plot(xre,yim,'-',color="blue")
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada y")
        plt.title("Distancia entre 2 puntos")
        plt.grid(True)
        plt.show()




#titulo y tamano de ventana
ventana.title('Calculadora Compleja')
ventana.geometry("600x550") 
label1=Label(ventana,text="Ingrese los valores")
label1.grid(row=1,column=3)

#Primer numero complejo
label2=Label(ventana,text="Z1=")
label2.grid(row=2,column=1)
z1=StringVar()
caja=Entry(ventana,textvariable=z1)
caja.grid(row=2,column=2)

#Segundo numero complejo
label4=Label(ventana,text="Z2=")
label4.grid(row=3,column=1)
z2=StringVar()
caja3=Entry(ventana,textvariable=z2)
caja3.grid(row=3,column=2)

#para ingresar el valor de n
label6=Label(ventana,text=" n=")
label6.grid(row=4,column=1)
n=IntVar()
caja5=Entry(ventana,textvariable=n)
caja5.grid(row=4,column=2)
label10=Label(ventana,text="n -> no. entero")
label10.grid(row=4,column=3)

#Configuracion del boton
boton = Button(ventana, text ="Resultado",command=funcion)
boton.grid(row=5,column=3)

boton2 = Button(ventana, text ="Graficar",command=graficas)
boton2.grid(row=5,column=4)

#Hasta aqui todo perfecto------------------------------------------------------------------------------------------

label11=Label(ventana, text="Elegir con click")
label11.grid(row=6,column=1)

#Impresion de datos 
suma = BooleanVar()
suma.set(False) #set check state
chk=Checkbutton(ventana, text='Z1 + Z2', var=suma)
chk.grid(column=2, row=7)

conjugado = BooleanVar()
conjugado.set(False) #set check state
chk2=Checkbutton(ventana, text='Conjugado Z1', var=conjugado)
chk2.grid(column=3, row=7)

resta = BooleanVar()
resta.set(False) #set check state
chk3=Checkbutton(ventana, text='Z1 - Z2', var=resta)
chk3.grid(column=2, row=8)

raiz = BooleanVar()
raiz.set(True) #set check state
chk4=Checkbutton(ventana, text='Raiz n de Z2', var=raiz)
chk4.grid(column=3, row=8)

multiplicacion = BooleanVar()
multiplicacion.set(False) #set check state
chk5=Checkbutton(ventana, text='Z1 por Z2', var=multiplicacion)
chk5.grid(column=2, row=9)

elevado = BooleanVar()
elevado.set(False) #set check state
chk=Checkbutton(ventana, text='Z1 a la n', var=elevado)
chk.grid(column=3, row=9)

entre = BooleanVar()
entre.set(False) #set check state
chk=Checkbutton(ventana, text='Z1/Z2', var=entre)
chk.grid(column=2, row=10)

distancia = BooleanVar()
distancia.set(False) #set check state
chk=Checkbutton(ventana, text='d(Z1,Z2)', var=distancia)
chk.grid(column=3, row=10)

label26=Label(ventana,text="")
label26.grid(row=11,column=1)
label25=Label(ventana,text="Resultados:")
label25.grid(row=12,column=1)


#Hasta aqui todos los datos para ingresar--------------------------------------------------
a=DoubleVar()
b=DoubleVar()
c=DoubleVar()
d=DoubleVar()
aw=DoubleVar()
bw=DoubleVar()
#Creacion de los valores de resultados
rrsuma= StringVar(ventana, "0")
risuma= StringVar(ventana, "0")
rrconjugado= StringVar(ventana, "0")
riconjugado= StringVar(ventana, "0")
rrresta= StringVar(ventana, "0")
riresta= StringVar(ventana, "0")
rrraiz=StringVar(ventana, "0")
riraiz=StringVar(ventana, "0")
rrmultiplicacion=StringVar(ventana, "0")
rimultiplicacion=StringVar(ventana, "0")
rrelevado=StringVar(ventana,"0")
rielevado=StringVar(ventana,"0")
rrentre=StringVar(ventana,"0")
rientre=StringVar(ventana,"0")
rrdistancia=StringVar(ventana,"0")
ridistancia=StringVar(ventana,"0")

ventana.mainloop()