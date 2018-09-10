# -*- coding: utf-8 -*-
import turtle as tt ##Juan Pablo Arcila M,
from math import tan,pi,cos
tt.speed("fastest")
def poligonos(lados,longitud): #los que seran dibujados
    tt.seth(0)
    for i in range(lados):
        tt.forward(longitud) #left(x) rota la tortuga x grados a la izquierda, forward(y) mueve la tortuga y hacia donde apunta
        tt.left(360/lados)
    tt.seth(0) #reinicia la dirección de la tortuga
def apotema(n,s): #n lados de s longitud
    a=s/(2*tan(pi/n))
    return a
def poligono (lados,longitud,x,y):#los vertices de este serán los lugares donde se dibujen los poligonos de x lados y longitud y
    tt.penup()
    tt.goto(-longitud/2,-apotema(lados,longitud))
    tt.pendown()
    for i in range(lados):
        tt.penup()
        tt.forward(longitud)
        tt.pendown()
        poligonos(x,y)
        tt.left((i+1)*(360/lados)) #como la posicion de la tortgua fue reiniciada, hay que girarlo en cada paso más, para recuperar la dirección que tenia antes de reiniciarse con seth
    tt.done()
lados2=int(raw_input("de cuantos lados quiere los poligonos "))
tt.setup(800,800,0,0) #setup(ancho, alto, posicionX, posicionY)
tt.screensize(800,800)
tt.hideturtle()
poligono(4,2*apotema(lados2,20)/cos(pi/lados2)+50,lados2,20)