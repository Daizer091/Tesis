import os
import gc
import numpy as np
import librosa as ls
import librosa.display as display
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
gc.enable()

#Load auidos export list .wav
path='../Data set/Export Audios/Export Auidos'

file = os.listdir(path)
result = []

for i in file:
    if os.path.isfile(os.path.join(path, i)) and i.endswith('.wav'):
        result.append(i)
export_audio=np.array(result)
print(export_audio.shape)

#Load ambiental noise export list .wav
path='../Data set/Export Audios/Export Ruidos'

archivos = os.listdir(path)
result = []

for i in archivos:
    if os.path.isfile(os.path.join(path, i)) and i.endswith('.wav'):
        result.append(i)
export_ambi_noise=np.array(result)
print(export_ambi_noise.shape)

def spectrograms(x,sr,path_save,name_audio):
    print(name_audio)

    name=name_audio.split('.')

    Xstft=ls.stft(x[0],n_fft=1048)
    XstftdB=ls.amplitude_to_db(np.abs(Xstft))
    plt.figure(figsize=(25, 15))
    display.specshow(XstftdB, sr=sr, rasterized=False,cmap='inferno',n_fft=1048)
    path_save_name=path_save+name[0]+'_c1'+'.png'
    plt.savefig(path_save_name,bbox_inches='tight',pad_inches=0, metadata=None,transparent=True)
    plt.clf()
    plt.close('all')

    Xstft=ls.stft(x[1],n_fft=1048)
    XstftdB=ls.amplitude_to_db(np.abs(Xstft))
    plt.figure(figsize=(25, 15))
    display.specshow(XstftdB, sr=sr, rasterized=False,cmap='inferno',n_fft=1048)
    path_save_name=path_save+name[0]+'_c2'+'.png'
    plt.savefig(path_save_name,bbox_inches='tight',pad_inches=0, metadata=None,transparent=True)
    plt.clf()
    plt.close('all')

def audio_combination(x_name,y_name,x,y,x_sr,y_sr,path_save,combination):
    #x = Export Auidos
    #y = Export Ruidos
    #f = x+y or combination of audios

    name_1=x_name.split('.')
    name_2=y_name.split('.')

    name_f=name_1[0]+'_'+name_2[0]+'.wav'

    if x_sr == y_sr:
        sr = x_sr
    else:
        print('NameError:')
        sr='error'

    if x.shape == y.shape:
        f = x+y

    elif x.shape>y.shape:
        n=x.shape[1]-y.shape[1]
        zeros=np.zeros((2,n))
        y=np.concatenate((zeros,y),axis=1)
        f = x+y

    elif y.shape>x.shape:
        n=y.shape[1]-x.shape[1]
        zeros=np.zeros((2,n))
        x=np.concatenate((x,zeros),axis=1)
        f = x+y

    spectrograms(f,sr,path_save,name_f)

    if combination==True:
        write(path_save+name_f, sr, f.T)

path_save='T:/noise spectrograms/'
for i0 in export_audio[215:220]:
    x_path='../Data set/Export Audios/Export Auidos/'+i0
    for i1 in export_ambi_noise:
        y_path='../Data set/Export Audios/Export Ruidos/'+i1
        x ,x_sr=ls.load(x_path, sr=44100,mono=False)
        y ,y_sr=ls.load(y_path, sr=44100,mono=False)
        audio_combination(i0,i1,x,y,x_sr,y_sr,path_save,False)

        gc.collect()