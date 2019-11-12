import numpy as np
from scipy.io.wavfile import read
from scipy.io.wavfile import write 
from scipy import signal
import matplotlib.pyplot as plt
import os

datasetpath = '/content/drive/My Drive/MM/Music Source sepration/music-source-separation-master'
processed_audio_path = '/content/drive/My Drive/MM/Music Source sepration/processed_audio'


for files in os.listdir():
	if files[-3:] == wav:
		(Frequency, data) = read('sample1.wav') # Reading the sound file. 
		b,a = signal.butter(5, 1000/(Frequency/2), btype='lowpass')
		filteredSignal = signal.lfilter(b,a,data)
		write(processed_audio_path+files, Frequency, filteredSignal)
