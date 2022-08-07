import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import math
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

#データ整形フェイズ pandaの方が楽？
path = input("被験者名を再度入力してください\n")
path += ".txt"
# path = "python.txt"

State = ["drop", "still", "raise"]
permove = 100
data = []
with open(path, 'r') as f:
    while True:
        line = f.readline()
        if line == "":
            break
        s = line.replace('\n','').split(',')
        s = [int(i) for i in s]
        data.append(s)
    f.close
X = np.array(data)
sample = X.shape[0]
motion = int(sample/permove)
# 二次元配列をSVMに突っ込めないので、次元変換する。
X = X.reshape(motion,permove*2)
print(X)
reperiod = sample / (permove * len(State))
y = []
i = 0
while i < motion:
    species = i % 3 # 0~24は第一の姿勢以降同様...
    y.append(species)
    i+=1
#標準化フェイズおよびテストデータ採集フェイズ
#欠損値や異常値の考慮が必要
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=None)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

print(X_test.shape)
print(y_test)
#SVMフェイズ
model = SVC(kernel='linear', random_state=None)
model.fit(X_train_std, y_train)

pred_train = model.predict(X_train_std)
accuracy_train = accuracy_score(y_train, pred_train)
print('トレーニングデータに対する正解率: %.2f' % accuracy_train)

pred_test = model.predict(X_test_std)
accuracy_test = accuracy_score(y_test, pred_test)
print('テストデータに対する正解率: %.2f' % accuracy_test)

joblib.dump(model, path + '.pkl.cmp', compress=True)

# #表描画フェイズ
# plt.style.use('ggplot')

# X_combined_std = np.vstack((X_train_std, X_test_std))
# y_combined = np.hstack((y_train, y_test))

# fig = plt.figure(figsize=(13,8))
# plot_decision_regions(X_combined_std, y_combined, clf=model, res=0.02)
# plt.show()