import matplotlib.pyplot as plt

# Data for plotting
x = [3, 1, 1, 3, 4, 5]
y = [2, 10, 20, 9, 16, 25]

# Create a line plot
plt.plot(x, y, marker='o', linestyle=':', color='r', label='y = x^2')

# Add title and labels
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show grid
plt.grid()

# Add a legend
plt.legend()

# Display the plot
plt.show()
