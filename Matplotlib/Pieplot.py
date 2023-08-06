import matplotlib.pyplot as plt

labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [200,130,240,180]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
neth = plt.axes()
#____data____
plt.pie(sizes,labels=labels, colors=colors,shadow=True)
plt.show()