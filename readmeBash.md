## Tutorial

https://mjrobot.org/2016/06/01/controlando-um-raspberry-pi-robo-pela-internet/comment-page-1/

## Instalando a biblioteca wiringpi

~~~bash
apt-get install wiringpi
~~~
## Lendo todo raspberry
~~~bash
gpio readall
~~~

## Configurando os pinos
gpio -g mode 18 pwm
ou
gpio mode 1 pwm   
