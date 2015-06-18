__author__ = 'lionel'
import matplotlib.pyplot as plt


# The slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'black', 'lightskyblue', 'lightcoral']
explode = (0, 0, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

# autopct小数点位数 startangle 开始角度
plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.5f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.show()