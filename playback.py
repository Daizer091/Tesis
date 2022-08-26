import sounddevice as sd
import soundfile as sf

fs = 44100
array, smp_rt = sf.read('./prueba.wav', dtype='float32')
# myarray = read('./sounds/recording0.wav', True)
# myarray = numpy.array(myarray)
sd.play(array, smp_rt)
sd.wait()
