import csv
import bertOA
import numpy as np
import pickle

analyCSVpath = "data/倾向性分析数据集.csv"  # 已评分数据集(CSV文件)路径

def classi(score):  # 根据评分分成四类
    score = float(score)
    if (score >= 0 and score < 0.25):
        return [1,0,0,0]
    if (score >= 0.25 and score < 0.5):
        return [0,1,0,0]
    if (score >= 0.5 and score < 0.75):
        return [0,0,1,0]
    if (score >= 0.75 and score < 1):
        return [0,0,0,1]

fp2 = open(analyCSVpath, 'r', encoding='utf-8')
analyCSV = csv.reader(fp2)
data = []  # 读入内容
for i in analyCSV:
    data.append((i[1],classi(i[2])))

def partitioningData(data):
    random_order = np.array(range(len(data)))
    np.random.shuffle(random_order)
    train_data = [data[j] for i, j in enumerate(random_order) if i % 10 != 0]
    valid_data = [data[j] for i, j in enumerate(random_order) if i % 10 == 0]
    return train_data, valid_data

train_data, valid_data=partitioningData(data)
model=bertOA.train(train_data, valid_data)
pickle.dump(model, open('model.pkl', 'wb'), protocol=2)