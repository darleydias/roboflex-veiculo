import serial
import pynmea2
import time

def parseGPS(dados):
        dados = dados.decode("utf-8") 
        if 'GGA' in dados:
                print(dados)
                msg = pynmea2.parse(dados)
                print ("Timestamp]:",msg.timestamp)
                lat = str(msg.lat)+str(msg.lat_dir)
                lat = lat.replace('.','')
                print ("latitude:",lat)
                longi = str(msg.lon)+ str(msg.lon_dir)
                print ("Longetude:",longi)
                altitude = str(msg.altitude) + str(msg.altitude_units)
                print ("Altitude:",altitude)

serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
while True:
        try:
                dados = serialPort.readline()
                parseGPS(dados)
        except serialPort.SerialException as e:
                print("Device error:{}".format(e))


