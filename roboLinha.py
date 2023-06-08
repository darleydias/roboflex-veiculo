import RPi .GPIO as GPIO
import time
import getch 
import os

GPIO.setmode(GPIO.BOARD) # considera a numeração dos pinos
GPIO_gatilho = 10
GPIO_eco = 22
GPIO.setup(GPIO_gatilho,GPIO.OUT)
GPIO.setup(GPIO_eco,GPIO.IN)

# MAPEAMENTO DOS PINOS

F_DIREITA = 16 
F_ESQUERDA = 11
T_DIREITA = 18
T_ESQUERDA = 13

def setupMotor():
    GPIO.setup(F_DIREITA,GPIO.OUT)
    GPIO.setup(F_ESQUERDA,GPIO.OUT)
    GPIO.setup(T_DIREITA,GPIO.OUT)
    GPIO.setup(T_ESQUERDA,GPIO.OUT)

def moveFrente():
    GPIO.output(F_DIREITA,GPIO.HIGH)
    GPIO.output(F_ESQUERDA,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(F_DIREITA,GPIO.LOW)
    GPIO.output(F_ESQUERDA,GPIO.LOW)
    time.sleep(0.005)   
def moveDireita():
    GPIO.output(F_ESQUERDA,GPIO.HIGH)    GPIO.output(F_ESQUERDA,GPIO.LOW)

def lerTecla():
    while true:
        tecla = getch.getch()
        if tecla == 'i':
            moveFrente()
        if tecla == 'p':
            paraTudo()
def lerDistancia(dist):
        GPIO.output(GPIO_gatilho,False)
        time.sleep(1)
        GPIO.output(GPIO_gatilho,True)
        time.sleep(0.00001)
        GPIO.output(GPIO_gatilho,False)
        inicio=time.time()
        while GPIO.input(GPIO_eco)==0:  
                inicio=time.time()
        while GPIO.input(GPIO_eco)==1: 
                stop = False
                tempoParado=time.time()
                transcorrido=tempoParado - inicio
                distancia = ((transcorrido * 34000)/2)
                if (distancia > dist): 
                        stop = True
        return stop
try:
        while(True):
                if lerDistancia(20):
                        setupMotor()
                        moveFrente()
                else:
                        paraTudo()
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()

                       
    time.sleep(0.4)
    GPIO.output(F_ESQUERDA,GPIO.LOW)
def moveEsquerda():
    GPIO.output(F_DIREITA,GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(F_DIREITA,GPIO.LOW)
def paraTudo():
    GPIO.output(F_DIREITA,GPIO.LOW)
    GPIO.output(F_ESQUERDA,GPIO.LOW)
    GPIO.output(F_DIREITA,GPIO.LOW)
