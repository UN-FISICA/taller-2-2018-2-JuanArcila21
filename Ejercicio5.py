# -*- coding: utf-8 -*-
import turtle as tt ##Juan Pablo Arcila M,
from math import tan,pi,cos
entradafilas=int(raw_input("cuantas filas quiere "))
tt.screensize(4000,4000)
tt.hideturtle()
tt.speed("fastest")
def poligonos(lados): #poligonos de lado longitud 20 y lados "lados"
    tt.seth(0)
    for i in range(lados):
        tt.left(360/lados)
        tt.forward(10) #left(x) rota la tortuga x grados a la izquierda, forward(y) mueve la tortuga y hacia donde apunta
    tt.seth(0) #reinicia la dirección de la tortuga
def apotema(n): #n lados de 20 longitud
    a=20/(2*tan(pi/n))
    return a
def piramide(filas):
    j,i=1,0
    lados=filas+2
    hola=lados
    while i<filas:
        while j<=filas-i:
            poligonos(lados)
            tt.penup()
            tt.forward(2*apotema(hola)/cos(pi/hola))
            tt.pendown()
            j+=1
        i+=1    
        tt.penup()
        tt.goto(i*(apotema(hola)/cos(pi/hola)),(2*i*apotema(hola))+10*i) #el circunradio es la apotema sobre el coseno de pi/lados
        tt.seth(0)
        tt.pendown()
        j=1
        lados-=1
    tt.done()

piramide(entradafilas)