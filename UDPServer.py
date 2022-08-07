import socket
import random
import time
import serial
import re
from sklearn.svm import SVC
from sklearn.externals import joblib
import numpy as np
def main():
    model = joblib.load('svc.pkl.cmp')
    timer = 1
    permove = 100
    State = ["drop", "still", "raise"]
    wave = np.empty((0,2),int)
    n=1
    HOST = '127.0.0.1'
    PORT = 50007    
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("connected")
    with serial.Serial('/dev/cu.usbmodem141101',115200,timeout=1) as ser:
        while True:
            ser.write(str.encode('A'))
            c = ser.readline()
            DecodeC = c.decode()
            cReplaced = DecodeC.replace('\n','')
            if cReplaced == '':
                continue
            elif cReplaced == 'A':
                continue
            else:
                cReplaced = cReplaced.split(',')
                cReplaced = [int(i) for i in cReplaced]
                carray = np.array(cReplaced)
                wave = np.vstack((wave,carray))
                if timer == permove * n:
                    # メモ 要素数が100,2にならなかったら条件として弾いてもいいかもしれない。
                    wave = wave.reshape(1,200)
                    result = str(int(model.predict(wave)))
                    print(result)
                    wave = np.empty((0,2),int)
                    client.sendto(result.encode('utf-8'),(HOST,PORT))
                    n += 1
                timer += 1
        ser.close

if __name__=="__main__":
    main()