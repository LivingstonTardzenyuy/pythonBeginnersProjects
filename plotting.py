import matplotlib.pyplot as plt

x1=[1,2,3,4,5,6,7]
y1=[1,2,3,4,5,6,7]

plt.plot(x1, y1, color='purple', linestyle='dashed', linewidth=3, markerfacecolor='blue', markersize=12)

plt.ylim(1,8)           #select the range from 1 to 8
plt.xlim(1,8)

plt.xlabel("X-xis")
plt.ylabel('Y-axis')

plt.title("Quadratic graph")



plt.show()