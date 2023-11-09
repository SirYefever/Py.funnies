
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


# n = int(input())
# dct_tasks, dct_time = {}, {}
# for i in range(n):
#     lst = list(map(int, input().split()))
#     tasks, time  = lst[0], lst[1]
#     dct_tasks[f'{i + 1}'] = tasks
#     dct_time[f'{i + 1}'] = time
#
# dct_tasks = sorted(dct_tasks.items(), key=lambda x: x[1], reverse=True)
#
# ind1 = 0
# while ind1 < n:
#     ind2 = ind1
#     while ind2 > 0 and dct_tasks[ind2][1] == dct_tasks[ind2 - 1][1] and \
#         (dct_time[ind2] < dct_time[ind2 - 1] or \
#          dct_time[ind2] == dct_time[ind2 - 1] and \
#          int(dct_tasks[ind2][0]) < int(dct_tasks[ind2 - 1][0])):
#         dct_tasks[ind2], dct_tasks[ind2 - 1] = dct_tasks[ind2 - 1], dct_tasks[ind2]
#         ind2 -= 1
#     ind1 += 1
#
# for i in range(n):
#     print(dct_tasks[i][0], end=' ')
