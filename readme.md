
# PADRAO MEGA + RASP

### Balança: https://www.usinainfo.com.br/blog/balanca-arduino-com-celula-de-peso-e-hx711-tutorial-calibrando-e-verificando-peso/

Sketch:
~~~Arduino
#include "HX711.h"
#include "LiquidCrystal_I2C.h";
 
#define DT A1
#define SCK A0
 
HX711 escala;
 
LiquidCrystal_I2C lcd(0x27, 16, 2);
 
void setup() {
  escala.begin (DT, SCK);
 
  lcd.init();
  lcd.backlight();
 
  Serial.begin(9600);
  Serial.print("Leitura do Valor ADC:  ");
  Serial.println(escala.read());   // Aguada até o dispositivo estar pronto
  Serial.println("Nao coloque nada na balanca!");
  Serial.println("Iniciando...");
  escala.set_scale(397930.55);     // Substituir o valor encontrado para escala
  escala.tare(20);                // O peso é chamado de Tare.
  Serial.println("Insira o item para Pesar");
}
 
void loop() {
  lcd.setCursor(4, 0);
  lcd.print("USINAINFO");
  lcd.setCursor(0, 1);
  lcd.print("Peso: ");
  lcd.print(escala.get_units(20), 3);
  lcd.println(" kg  ");
  delay(1000);
}
~~~

### Controle de motores: https://www.robocore.net/tutoriais/motor-dc-arduino-ponte-h-l298n
Componente: L298N

Sketch: 

~~~Arduino

/*******************************************************************************
* Modulo L298N Primeiros Passos (v1.0)
* 
* Rampa de aceleracao e desaceleracao de dois motores utilizando o driver L298N.
* Os motores irao acelerar de 0 rpm ate a sua rotacao maxima e entao reduzir a 
* velocidade ate parar, com o mesmo intervalo de tempo. Entao os motores irao 
* rotacionar no sentido contrario com a mesma aceleracao e desaceleracao.
* 
* Copyright 2019 RoboCore.
* Escrito por Giovanni de Castro (05/04/2019).
* 
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version (<https://www.gnu.org/licenses/>).
*******************************************************************************/

//declaracao dos pinos utilizados para controlar a velocidade de rotacao
const int PINO_ENA = 6; 
const int PINO_ENB = 5;

//declaracao dos pinos utilizados para controlar o sentido do motor
const int PINO_IN1 = 4; 
const int PINO_IN2 = 3;
const int PINO_IN3 = 8;
const int PINO_IN4 = 7;

int i = 0; //declaracao da variavel para as rampas

const int TEMPO_ESPERA = 1000; //declaracao do intervalo de 1 segundo entre os sentidos de rotacao do motor

const int TEMPO_RAMPA = 30; //declaracao do intervalo de 30 ms para as rampas de aceleracao e desaceleracao

void setup() {

  //configuração dos pinos como saida
  pinMode(PINO_ENA, OUTPUT); 
  pinMode(PINO_ENB, OUTPUT);
  pinMode(PINO_IN1, OUTPUT);
  pinMode(PINO_IN2, OUTPUT);
  pinMode(PINO_IN3, OUTPUT);
  pinMode(PINO_IN4, OUTPUT);

  //inicia o codigo com os motores parados
  digitalWrite(PINO_IN1, LOW); 
  digitalWrite(PINO_IN2, LOW);
  digitalWrite(PINO_IN3, LOW);
  digitalWrite(PINO_IN4, LOW);
  digitalWrite(PINO_ENA, LOW);
  digitalWrite(PINO_ENB, LOW);

}

void loop() {

  //configura os motores para o sentido horario
  digitalWrite(PINO_IN1, LOW); 
  digitalWrite(PINO_IN2, HIGH);
  digitalWrite(PINO_IN3, LOW);
  digitalWrite(PINO_IN4, HIGH);

  //rampa de aceleracao
  for (i = 0; i < 256; i=i+10){ 
    analogWrite(PINO_ENA, i);
    analogWrite(PINO_ENB, i);
    delay(TEMPO_RAMPA); //intervalo para incrementar a variavel i
  }

  //rampa de desaceleracao
  for (i = 255; i >= 0; i=i-10){ 
    analogWrite(PINO_ENA, i);
    analogWrite(PINO_ENB, i);
    delay(TEMPO_RAMPA); //intervalo para incrementar a variavel i
  }

  delay(TEMPO_ESPERA); //intervalo de um segundo

  //configura os motores para o sentido anti-horario
  digitalWrite(PINO_IN1, HIGH); 
  digitalWrite(PINO_IN2, LOW);
  digitalWrite(PINO_IN3, HIGH);
  digitalWrite(PINO_IN4, LOW);

  //rampa de aceleracao
  for (i = 0; i < 256; i=i+10){ 
    analogWrite(PINO_ENA, i);
    analogWrite(PINO_ENB, i);
    delay(TEMPO_RAMPA); //intervalo para incrementar a variavel i
  }

  //rampa de desaceleracao
  for (i = 255; i >= 0; i=i-10){ 
    analogWrite(PINO_ENA, i); 
    analogWrite(PINO_ENB, i);
    delay(TEMPO_RAMPA); //intervalo para incrementar a variavel i
  }

  delay(TEMPO_ESPERA); //intervalo de um segundo
  
}
~~~


# Pesquisando 

## pyfirmata - ligando arduino no raspberry

https://www.youtube.com/watch?v=q7u5KUM94Uc

## Gravando no esp32 lora

## Seguidor de linha

https://blog.eletrogate.com/robo-seguidor-de-linha-tutorial-completo/

## Configuração gnss

https://defcon007.medium.com/using-a-gps-module-neo-7m-with-raspberry-pi-3-45100bc0bb41


u-blox 8 GNSS modules
zed f9p GNSS module
https://www.waveshare.com/wiki/ZED-F9P_GPS-RTK_HAT
mosaicHAT

https://pt.aliexpress.com/item/1005004605528964.html?spm=a2g0o.detail.1000060.1.af9f2a6clLqqwV&gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.291025.0&scm_id=1007.13339.291025.0&scm-url=1007.13339.291025.0&pvid=04b76dcb-2a8e-444a-90a2-40a24a2ef91e&_t=gps-id%3ApcDetailBottomMoreThisSeller%2Cscm-url%3A1007.13339.291025.0%2Cpvid%3A04b76dcb-2a8e-444a-90a2-40a24a2ef91e%2Ctpp_buckets%3A668%232846%238113%231998&pdp_npi=3%40dis%21BRL%21377.34%21354.68%21%21%21%21%21%402103244616852799388806622e4992%2112000029803075829%21rec%21BR%21&gatewayAdapt=glo2bra


Giroscopio e acelerometro
https://www.youtube.com/watch?v=JTFa5l7zAA4
https://www.youtube.com/watch?v=L5QIFnurucU
https://capsistema.com.br/index.php/2022/06/06/mpu6050-com-raspberry-pi-pico-acelerometro-giroscopio-e-temperatura/



Biblioteca para cáculo de azinute
https://pypi.org/project/geopy/

Instalei os módulos geopy e outros mas não reconhecia quando executava o arquivo xxx.py
Era porque instalei o módulo sem root
errado => pip3 install geopy 
certo =>  sudo pip3 install geopy 



# Python-NEO-6M-GPS-Raspberry-Pi
Script Python para NEO-6M GPS no Raspberry Pi
## 1. Ligações
![Image of Yaktocat](https://raspberrytips.nl/wp-content/uploads/2016/12/UBOLX-NEO-6M-RPI-600x274.png)
![Image of Yaktoc2at](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png)
![Image of Yaktoc2at2](./gps-neo-6m-board-schematic.png)
![Image of Yaktoc2at2](./00532_Raspberry_Pi_NEO-6M_GPS-Modul_-_Schaltplan.png)
## 2. Dependências
* pip installed.
```
sudo apt-get install python-pip
```
* you will need pynmea2.
```
sudo pip install pynmea2

```
* You need the GPS software
```
sudo apt-get install gpsd gpsd-clients python-gps minicom
```
sudo apt-get install gpsd
sudo apt-get install gpsd-clients
sudo apt-get install minicom
sudo apt-get install python-gps
sudo apt-get install gpsd-tools:armhf
sudo apt-get install gpsd-clients:armhf 
sudo apt-get install gpsd-tools gpsd-clients
...
## 3. Configurando serviços
* Serial port modify cmdline.txt:
```
sudo nano /boot/cmdline.txt
```
and replace all with the following lines:
```
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
```
* Configurações de boot:
```
sudo nano /boot/config.txt
```
acrescentar oa final:
```
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
init_uart_baud=9600
```
* reinicie o sistema:
```
sudo reboot now
```
* configurar o boundrate para 9600 rate:
```
stty -F /dev/ttyAMA0 9600
```
* Conectando o dispositivo com o GPS Software 

sudo systemctl enable gpsd.socket
sudo systemctl start gpsd.socket 
sudo cgps -s
```
## 4. Rodando no terminal
```
cgps -s
```
* Criando arquivo python
```
sudo python Neo6mGPS.py
```
O Script pode levar até 20 min para encontrar sinal. 
## 5. Examplo de código
```
~~~python
import serial
import pynmea2
def parseGPS(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude:
%s %s" %
(msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,m
sg.altitude_units)
serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
while True:
    str = serialPort.readline()
    parseGPS(str)
~~~
```
```

è preciso matar o processo e adicionar a ferramenta de gps no sispositivo

```
sudo killall gpsd
sudo nano /etc/default/gpsd
```
Edite o arquivo /etc/default/gpsd  e adicione o dispositivo na porta serial

```
DEVICES="/dev/ttyAMA0"
```
* Restart the Software
```
sudo systemctl enable gpsd.socket
sudo systemctl start gpsd.socket 
sudo cgps -s
