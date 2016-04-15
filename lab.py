#Laboratorio 1 Redes De Computadores
#Profesor Carlos Gonzalez
#Ayudantes Maximiliano Perez - Pablo Reyes
#Alumno Joaquin Ignacio Villagra Pacheco

import numpy as np
from scipy.io.wavfile import read,write
import matplotlib.pyplot as p_time, p_frecuency

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style

from graph import *
from conv import *
from filt import *
from translator import *
from decoder import *

"""
2. Grafique la función de audio en el tiempo
3. Utilizando la transformada de fourier:
a. Grafique la señal en el dominio de la frecuencia
b. A la función en su frecuencia calcule la transformada de fourier inversa,
compare con la señal original.
4. En el dominio de la frecuencia:
a. Analice el espectro y determine los componentes de mayor amplitud.
b. Genere un nuevo espectro, truncando el resultado original en torno a la
amplitud máxima con un margen del 15%.
c. Calcule la transformada de fourier inversa y compare la señal generada con
la original.
"""

"""
timeGraphics FUNCTION: GRÁFICA DE LA SEÑAL EN EL DOMINIO DEL Tiempo
ENTRADA:
SALIDA:
"""
def timeGraphics(data, rate):
	timeDuration = len(data)/rate
	time    = linspace(0, timeDuration, len(data))    			#linspace(start,stop,number)
	p_time = f.add_subplot(1,1,1)		#Return evenly spaced numbers over a specified interval.
	p_time.set_title('Abs(audio)')
	p_time.set_xlabel('Tiempo [s]')
	p_time.set_ylabel('Amplitud [dB]')
	p_time.plot(time, data, "--")
	return p_time, f

"""
frecuencyGraphics FUNCTION: GRÁFICA DE LA SEÑAL EN EL DOMINIO DE LA FRECUENCIA
ENTRADA:
SALIDA:
"""
def frecuencyGraphics(data, rate):
	large = len(data)
	p_frecuency = f.add_subplot(2,1,1)
	k = arange(large)
	T = large/rate
	frq = k/T                       			#Two sides frequency range
	frq = frq[range(round(large/2))] 			#One side frequency range
	Y = fft(data)/large         				#Fast Fourier Transformation
	Y = Y[range(round(large/2))]
	p_frecuency.plot(frq,abs(Y),'r')
	p_frecuency.set_title('Gráficos de Frecuencia y Spectograma')
	p_frecuency.set_xlabel('Magnitud')
	p_frecuency.set_ylabel('Frecuencia [Hz]')
	return p_frecuency, f

#CUERPO DEL PROGRAMA
rate, info=read("beacon.wav")
#Graficando en el tiempo
p_time, f = timeGraphics(info, rate)
p_time.show()
#Graficando en la frecuencia
p_frecuency, f = frecuencyGraphics(info, rate)
p_frecuency.show()


"""
print(rate) #‪#‎FRECUENCIA‬ DE MUESTREO
plt.plot(info, "--")
plt.show()"""
