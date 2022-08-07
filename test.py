import socket
import random
import time
import serial
import re
from sklearn.svm import SVC
from sklearn.externals import joblib
import numpy as np
def main():
    timer = 1
    base_time = time.time()
    n = 1
    permove = 100
    now = 0
    print("connected")
    while now <= 1:
        current_time = time.time()
        now = current_time - base_time
        # print(now)
        if timer == permove * n:
            n += 1
            print(timer)
        timer += 1

if __name__=="__main__":
    main()