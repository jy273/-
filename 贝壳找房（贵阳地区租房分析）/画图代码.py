import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#绘制房源地址分布柱状图
file_path = '贝壳信息2.csv'
df = pd.read_csv(file_path)

house_address_counts = df['House_address'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=house_address_counts.index, y=house_address_counts.values, palette="viridis")
plt.title('房源地址分布柱状图')
plt.xlabel('地区')
plt.ylabel('数量', rotation=0)
plt.xticks(rotation=45, ha='right')

funnel_chart_file_path = '房源地址分布柱状图.png'
plt.savefig(funnel_chart_file_path)

funnel_chart_file_path


#绘制房源面积分布饼图
area_bins = [50, 80, 100, 120, float('inf')]
area_labels = ['50~80平方米', '81~100平方米', '101~120平方米', '120平方米以上']
area_grouped = pd.cut(df_user_uploaded_for_analysis['Area'], bins=area_bins, right=False, labels=area_labels).value_counts()


plt.figure(figsize=(8, 8))
plt.pie(area_grouped, labels=area_labels, autopct='%1.1f%%', startangle=140, colors=["blue", "green", "yellow", "red"])
plt.title('房源面积分布饼图')


pie_chart_file_path = '房源面积分布饼图.png'
plt.savefig(pie_chart_file_path)


pie_chart_file_path


#绘制不同户型房源数量统计柱形图
house_layout_counts = df['House_layout'].value_counts()

plt.figure(figsize=(10, 6))
house_layout_counts.plot(kind='bar', color='skyblue')
plt.title('不同户型房源数量统计')
plt.xlabel('户型')
plt.ylabel('数量')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plot_file_path = '不同户型房源数量统计.png'
plt.savefig(plot_file_path)

plt.show()

plot_file_path

#绘制租金分布折线图
plt.figure(figsize=(10, 6))
rent_counts = df_user_uploaded_for_analysis['Rent'].value_counts().sort_index()
rent_counts.plot(kind='line', marker='o', color='orange')
plt.title('租金分布折线图')
plt.xlabel('租金')
plt.ylabel('数量', rotation=0)
plt.grid(True)

line_chart_rent_new_color_new_label_file_path = '租金分布折线图.png'
plt.savefig(line_chart_rent_new_color_new_label_file_path)

plt.show()

line_chart_rent_new_color_new_label_file_path

#绘制各地区平均租金柱形图
plt.figure(figsize=(10, 6))
sns.barplot(x=areas, y=average_rents, palette="coolwarm")
plt.title('各地区平均租金')
plt.xlabel('地区')
plt.ylabel('平均租金 (元/月)')

plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#绘制不同类型的数量分布饼图
colors = ['#FF0000', '#0000FF']  # Red for "整租", Blue for "合租"
plt.figure(figsize=(8, 8))
plt.pie(df['数量'], labels=df['类型'], autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('不同类型的数量分布')
plt.show()

