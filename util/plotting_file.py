import matplotlib.pyplot as plt

x = [0.1, 0.2, 0.5, 0.7]
y1 = [9384, 58460, 4088, 1717]
y2 = [3889, 5887, 955, 381]
dot_names_y1 = ['9384', '58460', '4088', '1717']
dot_names_y2 = ['3889', '5887', '955', '381']
xtick_labels = ['(0.1,0.1,5)', '(0.2,0.2,0.2)', '(0.5,0.5,0.5)', '(0.7,0.7,0.7)']

# Plot the data as lines
plt.plot(x, y1, label='Djikstra', marker='o')
plt.plot(x, y2, label='Astar', marker='s')

# Add dot name annotations to both lines
for i, name in enumerate(dot_names_y1):
    plt.annotate(name, (x[i], y1[i]))
for i, name in enumerate(dot_names_y2):
    plt.annotate(name, (x[i], y2[i]))

# Set x-axis tick labels
plt.xticks(x, xtick_labels)

# Add legend and labels
plt.legend()
plt.xlabel(" Resolution")
plt.ylabel('Number of nodes')

# Display the plot
plt.show()
