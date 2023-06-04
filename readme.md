
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
