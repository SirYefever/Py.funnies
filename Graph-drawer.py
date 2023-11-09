#requires a txt file with a structure:
#*argument value* *funvction value*
from matplotlib import pyplot as plt
from operator import itemgetter

f = open("TextFile1.txt").readlines()
data = [tuple(map(float, line.split())) for line in f]
x = list(map(itemgetter(0), data))
y = list(map(itemgetter(1), data))

#ploting our canvas
plt.plot(y, x)
#display the graph
plt.show()
