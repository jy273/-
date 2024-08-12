import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Prior probability values
prior_probs = [0.3758, 0.3758, 0.2484]

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
        counts[i, 0] = (data.iloc[i, 0] / data.iloc[i, 3]) * prior_probs[0]
        counts[i, 1] = (data.iloc[i, 1] / data.iloc[i, 3]) * prior_probs[1]
        counts[i, 2] = (data.iloc[i, 2] / data.iloc[i, 3]) * prior_probs[2]
# 删除所有特征值都是0的行
counts = counts[~np.all(counts == 0, axis=1)]
# 计算后验概率
posterior_probs = counts / counts.sum(axis=1)[:, None]

# 输出先验概率值
print('先验概率值:\n', prior_probs)

# 输出后验概率值
print('贝叶斯公式输出的值:\n', posterior_probs)

# 输出特征的概率值
print('特征的概率值:\n', counts)

# 绘制柱状图
fig, ax = plt.subplots()
index = np.arange(3)
bar_width = 0.35
opacity = 0.8

rects1 = ax.bar(index, counts.mean(axis=0), bar_width,
                alpha=opacity, color='b',
                label='Mean probability')

rects2 = ax.bar(index + bar_width, counts.max(axis=0), bar_width,
                alpha=opacity, color='g',
                label='Max probability')

# 添加先验概率柱状图
rects3 = ax.bar(index, prior_probs, bar_width,
                alpha=opacity, color='r',
                label='Prior probability')

ax.set_xlabel('Feature')
ax.set_ylabel('Probability')
ax.set_title('Probability of Each Feature')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('UPDRS_ON', 'UPDRS_OFF', 'Yrs Since Diagnosis'))
ax.legend()

plt.tight_layout()
plt.savefig('概率柱状图.png')  # 保存图像为名为 概率柱状图.png 的文件
plt.show()

# 绘制折线图
plt.plot(counts[:, 0], label='UPDRS_ON')
plt.plot(counts[:, 1], label='UPDRS_OFF')
plt.plot(counts[:, 2], label='Yrs Since Diagnosis')

# 添加先验概率折线
# plt.plot(prior_probs, label='Prior probability', linestyle='--')

plt.legend()
plt.title('Bayesian Formula Output')
plt.savefig('贝叶斯公式.png')  # 保存图像为名为贝叶斯公式.png 的文件
plt.show()
plt.show()
