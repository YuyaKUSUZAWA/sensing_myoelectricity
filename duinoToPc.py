#coding utf-8
import serial
import re
def main():
    time = 0
    path = input('被験者名を入力してください\n')
    sample = int(input("サンプル数を入力してください(600>n)\n"))
    path += '.txt'
    permove = 100
    State = ["drop", "still", "raise"]
    n=0
    with serial.Serial('/dev/cu.usbmodem141101',115200,timeout=1) as ser:
        while time < sample:
            ser.write(str.encode('A'))
            c = ser.readline()
            DecodeC = c.decode()
            cReplaced = DecodeC.replace('\n','')
            if time == permove * n:
                print(State[n%3])
                n += 1
            if cReplaced == '':
                continue
            elif cReplaced == 'A':
                continue
            else:
                time += 1
                    # ファイルの作成、および編集
                with open(path, 'a') as f:
                    f.write(cReplaced + '\n')
        ser.close()

if __name__=="__main__":
    main()