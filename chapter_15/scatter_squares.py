import matplotlib.pyplot as plt

xVal = range(1,1001)
yVal = [x**2 for x in xVal]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(xVal, yVal, c=yVal, cmap=plt.cm.Greens, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0,1100,0,1100000])

plt.show()