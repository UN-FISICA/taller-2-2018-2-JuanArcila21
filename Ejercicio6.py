# -*- coding: utf-8 -*-
import turtle as tt #Juan Pablo Arcila M,
from math import tan,pi,cos,sin
entradafilas=int(raw_input("cuantas filas quiere "))
tt.screensize(4000,4000)
tt.speed("fastest")
def poligonos(lados,s): #poligonos de lado longitud s y lados "lados"
    tt.seth(0)
    for i in range(lados):
        tt.left(360/lados)
        tt.forward(s) #left(x) rota la tortuga x grados a la izquierda, forward(y) mueve la tortuga y hacia donde apunta
    tt.seth(0) #reinicia la dirección de la tortuga
def apotema(n,s): #n lados de s longitud
    a=s/(2*tan(pi/n))
    return a
def longitud(m):
    s=2*50*sin(pi/m)
    return s
def piramide(filas):
    j,i=1,0
    lados=filas+2
    c=lados #variable con lados fijos
    while i<filas:
        tt.penup()
        tt.seth(180)
        tt.forward(apotema(lados,longitud(lados))/2)
        tt.seth(0)
        tt.pendown()
        while j<=filas-i:
            
            poligonos(lados,longitud(lados))
            tt.penup()
            tt.forward(2*apotema(c,longitud(c))/cos(pi/c))
            tt.pendown()
            j+=1
        i+=1    
        tt.penup()
        tt.goto(i*(apotema(c,longitud(c))/cos(pi/c)),(2*i*apotema(c,longitud(c)))+10*i) #el circunradio es la apotema sobre el coseno de pi/lados
        tt.seth(0)
        tt.pendown()
        j=1
        lados-=1
    tt.done()

piramide(entradafilas)