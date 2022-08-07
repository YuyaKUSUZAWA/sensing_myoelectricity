    #coding utf-8
import numpy as np
import matplotlib.pyplot as plt
def main():
    # path = input("被験者名を再度入力してください\n")
    # path += ".txt"
    data = []
    with open("Yuya_kusuzawa.txt", 'r') as f:
        while True:
            line = f.readline()
            if line == "":
                break
            s = line.replace('\n','').split(',')
            s = [int(i) for i in s]
            data.append(s)
        f.close
        data = np.array(data)
        n = 0
        x0 = np.empty((100,0),int)
        x1 = np.empty((100,0),int)
        x2 = np.empty((100,0),int)
        y0 = np.empty((100,0),int)
        y1 = np.empty((100,0),int)
        y2 = np.empty((100,0),int)
        while n < 60:
            p = 100 * n
            if n % 3 == 0:
                x0 = np.hstack((x0, data[p:p + 100,[0]]))
                y0 = np.hstack((y0, data[p:p + 100,[1]]))
            elif n % 3 == 1:
                x1 = np.hstack((x1, data[p:p + 100,[0]]))
                y1 = np.hstack((y1, data[p:p + 100,[1]]))
            else:
                x2 = np.hstack((x2, data[p:p + 100,[0]]))
                y2 = np.hstack((y2, data[p:p + 100,[1]]))
            n += 1
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(x0,y0,c='red', label='drop')
    ax.scatter(x1,y1,c='green', label='still')
    ax.scatter(x2,y2,c='blue', label='raise')

    ax.set_title('myoelectricity')
    ax.set_xlabel('biceps')
    ax.set_ylabel('triceps')
    ax.legend(loc='upper right')
    plt.show()

if __name__=="__main__":
    main()