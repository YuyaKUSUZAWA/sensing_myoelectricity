import socket
import random
import time
import serial
import re
import math
from sklearn.svm import SVC
from sklearn.externals import joblib
import numpy as np
def main():
    HOST = '127.0.0.1'
    PORT = 50007    
    permove = 100
    n=1
    State = ["drop", "still", "raise"]
    timer = 1
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("connected")
    while True:
        if timer == permove * n:
            result = str(math.floor(random.random()*len(State)))
            client.sendto(result.encode('utf-8'),(HOST,PORT))
            n += 1
        timer += 1

if __name__=="__main__":
    main()