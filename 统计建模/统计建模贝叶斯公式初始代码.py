import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取文件数据
filename = 'C:/Users/金煜/PycharmProjects/scientificProject2/file.xlsx'
data = pd.read_excel(filename, usecols=[11, 12, 13, 14])

# 检查数据列名
if 'Handedness' in data.columns:
    data = data.drop('Handedness', axis=1)

# 将空值替换为0
data = data.fillna(0)

# 使用贝叶斯公式
counts = np.zeros((data.shape[0], 3))
for i in range(data.shape[0]):
    if data.iloc[i, 0] != 0 and data.iloc[i, 1] != 0 and data.iloc[i, 2] != 0 and data.iloc[i, 3] != 0:
        counts[i, 0] = data.iloc[i, 0] / data.iloc[i, 3]
        counts[i, 1] = data.iloc[i, 1] / data.iloc[i, 3]
        counts[i, 2] = data.iloc[i, 2] / data.iloc[i, 3]

# 绘制二维图像
plt.plot(counts[:, 0], label='UPDRS_ON')
plt.plot(counts[:, 1], label='UPDRS_OFF')
plt.plot(counts[:, 2], label='Yrs Since Diagnosis')
plt.legend()
plt.show()
plt.plot(counts[:, 0], label='UPDRS_ON')
plt.plot(counts[:, 1], label='UPDRS_OFF')
plt.plot(counts[:, 2], label='Yrs Since Diagnosis')
plt.legend()
plt.savefig('贝叶斯公式.png')  # 保存图像为名为 plot.png 的文件
plt.show()