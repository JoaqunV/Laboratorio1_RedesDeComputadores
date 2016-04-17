#Laboratorio 1 Redes De Computadores
#Profesor Carlos Gonzalez
#Ayudantes Maximiliano Perez - Pablo Reyes
#Alumno Joaquin Ignacio Villagra Pacheco

import numpy as np
from numpy import linspace, arange
from scipy.io.wavfile import read, write
from scipy.fftpack import fft
from scipy.fftpack import ifft
import matplotlib.pyplot as plt

"""
timeGraphics FUNCTION: GRÁFICA DE LA SEÑAL EN EL DOMINIO DEL TIEMPO
ENTRADA
	# Data -> audio data captured from
	# rate -> audio time
	# nameExit -> Output file name
SALIDA: #NONE
"""
def timeGraphics(data, rate, nameExit="graficoTiempo"):
	timeDuration = len(data)/float(rate)
	time    = linspace(0, timeDuration, len(data)) #linspace(start,stop,number)
	plt.plot(time, data,"--") #al agregar "--" ubuntu deja de tirar error con la cantidad de datos
	plt.title(nameExit)
	plt.xlabel("Time [s]")
	plt.ylabel("Amplitude [dB]")
	plt.savefig(nameExit+".png")
	plt.show()
	return
"""
frecuencyGraphics FUNCTION: GRÁFICA DE LA SEÑAL EN EL DOMINIO DE LA FRECUENCIA
ENTRADA
	# data -> audio data captured from
	# rate -> audio time
	# nameExit -> Output file name
SALIDA: fourierTransform
"""
def frecuencyGraphics(data, rate, nameExit="graficoFrecuencias"):
	channel = data.T[0] # this is a two channel soundtrack, I get the first track
	normalizedChannel = [(ele/2**8.)*2-1 for ele in channel] # this is 8-bit track, normalizedChannel is now normalized on [-1,1)
	fourierTransform = fft(normalizedChannel) # calculate fourier transform (complex numbers list)
	realSymetry = len(fourierTransform)/2  # you only need half of the fft list (real signal symmetry)
	plt.plot(abs(fourierTransform[:(realSymetry-1)]),'r')
	plt.title(nameExit)
	plt.xlabel("Frequency")
	plt.ylabel("Amplitude")
	plt.savefig(nameExit+".png")
	plt.show()
	return fourierTransform

"""
inverseTransformGraphics FUNCTION: GRÁFICA DE LA SEÑAL EN EL DOMINIO DEL TIEMPO - ANTITRANSOFORMADA DE FOURIER
ENTRADA
	# data -> audio data captured from
	# rate -> audio time
	# fourierSignal -> previously transformed data
	# nameExit -> Output file name
SALIDA: #NONE
"""
def inverseTransformGraphics(data, rate, fourierSignal, nameExit="Anti Transformed"):
	lenSignal = len(data)
	timeDuration = lenSignal/float(rate)
	time     = linspace(0, timeDuration, lenSignal) #linspace(start,stop,number)
	transfor = ifft(fourierSignal*lenSignal,lenSignal)
	plt.plot(time,transfor,"--")
	plt.title(nameExit)
	plt.xlabel("Time [s]")
	plt.ylabel("Amplitude [dB]")
	plt.savefig(nameExit+".png")
	plt.show()
	return 

"""
findMaxValue FUNCTION: DETERMINA EL INDICE DEL VALOR MAXIMO DE UN ARREGLO DE DATOS.
ENTRADA
	# array: evaluate data array
SALIDA: index
"""
def findMaxValue(array):
	value = max(array)
	for index in range(len(array)):
		if array[index] == value:
			return index

"""
setNewRangeData FUNCTION: DETERMINA EL NUEVO CONJUNTO DE DATOS A GRAFICAR.
ENTRADA
	# array:   evaluate data array
	# porcent: data considered percentaje
SALIDA: #NONE
"""
def setNewRangeData(array, porcent, nameExit="Transformed with restricted data"):
	indexOfMaxValue 	=  findMaxValue(array)
	deltPercentage 		=  int(len(array)*porcent/100) 
	floorIndexOfArray   =  indexOfMaxValue - deltPercentage
	ceilingIndexOfArray =  indexOfMaxValue + deltPercentage
	newRangeData 	    =  array[floorIndexOfArray:ceilingIndexOfArray]
	plt.title(nameExit)
	plt.xlabel("Frequency")
	plt.ylabel("Amplitude")
	plt.plot(newRangeData)
	plt.savefig(nameExit+".png")
	plt.show()
	return newRangeData

"""
inverseTransformGraphics FUNCTION: ANTITRANSOFORMADA DE FOURIER SIMPLE
ENTRADA
	# fourierSignal -> previously transformed data
	# nameExit -> Output file name
SALIDA: #NONE
"""
def simpleInverseTransformGraphics(fourierSignal, nameExit="Anti Transformed with restricted data"):
	transfor = ifft(fourierSignal)
	plt.plot(transfor)
	plt.title(nameExit)
	plt.xlabel("Time [s]")
	plt.ylabel("Amplitude [dB]")
	plt.savefig(nameExit+".png")
	plt.show()
	return transfor

#CUERPO DEL PROGRAMA
rate, information = read("beacon.wav")
#Graficando en el tiempo
timeGraphics(information, rate)
#Graficando en la frecuencia
fourierTransform = frecuencyGraphics(information, rate)
#Graficando AntiTransformada
inverseTransformGraphics(information, rate, fourierTransform)
#Graficando transformada de Fourier restringiendo el conjunto de datos.
newData = setNewRangeData(fourierTransform, 15)
#Obteniendo anitransformada de los datos restringidos.
newSignal = simpleInverseTransformGraphics(newData)
#Escribo los datos en un archivo .wav para comparar el sonido de los datos truncados vs originales
write("beaconWithRestrictedData.wav",rate,newSignal)







