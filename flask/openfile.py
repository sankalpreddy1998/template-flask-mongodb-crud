from __future__ import print_function
import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import os
import csv
import librosa.display
import librosa.core


def visualise(x,test,n):

    counter = 0
    x=x.lower()
      
    fig = plt.figure(figsize=(25,60))
    for data in test:
        if counter<n:
            y, sr = librosa.load(os.path.join(test[-1], str(data)+".wav"))

            tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

            plt.subplot(n,1,counter+1)

            if x=='wave':
                librosa.display.waveplot(np.array(y),sr=sr, color='red')
            elif x=='specgram':
                specgram(np.array(y),Fs=sr)
            elif x=='log_power_specgram':
                 D = librosa.core.amplitude_to_db(np.abs(librosa.stft(y))**2, ref_power=np.max)
                 librosa.display.specshow(D,x_axis='time' ,y_axis='log')
                
            counter=counter+1
            
    plt.show()

  
test=[]
train=[]

folder_path = os.path.abspath('/home/gaurav/Desktop/datasets/')

test_path = os.path.join(folder_path,'Test')
train_path = os.path.join(folder_path,'Train')

f_train = open(os.path.join(folder_path,'test.csv'))
csv_train = csv.reader(f_train)
for row in csv_train:
    for element in row:
        if element=='ID':
            continue
        test.append(int(element))
test.append(test_path)


