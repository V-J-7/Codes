import matplotlib.pyplot as plt
import numpy  as np
x=list(range(1,35))
heights=[96.4,66.9,73.05,69.6,66.6,81.4,76.4,75.4,94.4,67.2,67,91.2,66.2,76.6,68.2,67,51.2,78.05,75.2,73.6,71.4,72,93.4,70.8,72,71.6,90,70.8,97.4,93.6,87.8,74.8,81.2,68.3]
values=list(range(678,711))
values.append(784)
colormap = plt.colormaps.get_cmap('Blues')
normalized_heights = np.array(heights) / max(heights)
colors = colormap(normalized_heights)
plt.bar(x, heights, tick_label=values, width=0.6, color=colors)
plt.xlabel("Roll numbers")
plt.ylabel("Percentages")
plt.xticks(x, values, rotation=45)
plt.show()
