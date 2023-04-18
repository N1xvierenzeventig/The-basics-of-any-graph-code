import random
import matplotlib.pyplot as plt
x = []
y = []
f = [i*10 for i in range(11)]
f2 = [i*20 for i in range(11)]
x_axis = 0
for i in range(100):
    y_axis = random.randint(1,200)
    x.append(x_axis)
    y.append(y_axis)
    x_axis += 1


print(x)
print(y)
plt.plot(x,y, "g.--", label="2x")
plt.title("Random Graph", fontdict={"fontname": "Garamond", "fontsize":20})
plt.xlabel("X", fontdict={"fontname": "Garamond", "fontsize":10})
plt.ylabel("Y", fontdict={"fontname": "Garamond", "fontsize":10})
plt.xticks(f)
plt.yticks(f2)
plt.legend()
plt.show()
