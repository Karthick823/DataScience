import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure(figsize=(5,5))

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala')
performance = [10,8,6,4,2]
ab = [1,2,3,4,5]
neth= fig.add_subplot(111,projection="3d")
#neth.scatter(0.2,0.3,0.4)
neth.bar(objects, performance,ab)

plt.show()