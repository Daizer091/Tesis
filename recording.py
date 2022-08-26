import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate 44100 CD standatdize, 48000 Dvd standatdize 96000 Dvd Blue-ray
duration = 5  # Duration of recording

myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished

# Write a NumPy array as a WAV file.
write('./sounds/recording1.wav', fs, myrecording)

sd.wait()
    