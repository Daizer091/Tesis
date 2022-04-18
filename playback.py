import sounddevice as sd
from scipy.io.wavfile import read

fs = 44100
myarray = read('./sounds/recording0.wav', False)
sd.play(myarray, fs)
sd.wait()
