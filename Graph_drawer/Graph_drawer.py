#fill the "x and y values.txt" with argument & function values
#syntax for txt file:
#argumen_value fuction_value
from matplotlib import pyplot as plt
from operator import itemgetter

f = open("x and y values.txt").readlines()
data = [tuple(map(float, line.split())) for line in f]
x = list(map(itemgetter(0), data))
y = list(map(itemgetter(1), data))

#ploting our canvas
plt.plot(y, x)
#display the graph
plt.show()
