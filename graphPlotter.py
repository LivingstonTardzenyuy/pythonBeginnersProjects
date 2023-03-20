import matplotlib.pyplot as plt

x1=[2,4,5]
y1=[2,3,6]

x2=[1,2,3,4]
y2=[1,2,3,4]

plt.plot(x1,y1, label="Line-1")

plt.plt(x2,y2, label="Line-2")

plt.xlabel('x axis')

plt.ylabel('y axis')

plt.title('Demo graph')

plt.legend()

plt.show()