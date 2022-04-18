import sounddevice as sd
from scipy.io.wavfile import read

myarray = read('./sounds/recording0.wav', False)
myarray = read('./sounds/recording1.wav', False)
