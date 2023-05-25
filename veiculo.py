# capturar pontos do aplicativo ponto inicial 
# ponto final da reta 
# a = (48.11617185, 11.743858785932662)
# b = (48.116026149999996, 11.743938922310974)

# pontos obtidos do aplicativo. 
pontoInicial = (-48.11627385, -11.743858785942662)
pontoFinal = (-48.11627385, -11.743858785942662)
#pip install geographiclib

from geographiclib.geodesic import Geodesic
import time

while 1:
        # pegar do GPS
        coordAtual = (-48.11617200, -11.743858785932862)
        calculoAtual = Geodesic.WGS84.Inverse(*coordAtual, *pontoFinal)
        distAtual = calculoAtual["s12"] # in [m] (meters)
        time.sleep(1)
        print(distAtual)


result = Geodesic.WGS84.Inverse(*a, *b)
distance = result["s12"] # in [m] (meters)
bearing = result["azi1"] # in [°] (degrees)


print(distance)
print(bearing)