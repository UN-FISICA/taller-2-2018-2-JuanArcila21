# -*- coding: utf-8 -*-
import turtle as tt ##Juan Pablo Arcila M,
from math import tan,pi,cos
entradafilas,entradapoligonos=int(raw_input("cuantas filas quiere ")),int(raw_input("de cuantos lados quiere los poligonos "))
tt.hideturtle()
tt.screensize(4000,4000)
tt.speed("fastest")
def poligonos(lados): #poligonos de lado longitud 20 y lados "lados"
    tt.seth(0)
    for i in range(lados):
        tt.left(360/lados)
        tt.forward(20) #left(x) rota la tortuga x grados a la izquierda, forward(y) mueve la tortuga y hacia donde apunta
    tt.seth(0) #reinicia la dirección de la tortuga
def apotema(n): #n lados de 20 longitud
    a=20/(2*tan(pi/n))
    return a
def piramide(filas,lados):
    j,i=1,0
    while i<filas:
        while j<=filas-i:
            poligonos(lados)
            tt.penup()
            tt.forward(4*apotema(lados)/cos(pi/lados))
            tt.pendown()
            j+=1
        i+=1    
        tt.penup()
        tt.goto(2*i*(apotema(lados)/cos(pi/lados)),4*i*apotema(lados)+10*i) #el circunradio es la apotema sobre el coseno de pi/lados
        tt.seth(0)
        tt.pendown()
        j=1
    tt.done()

piramide(entradafilas,entradapoligonos)
