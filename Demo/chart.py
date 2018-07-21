import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(1,1,1)

ax1.set_xlabel('number')
ax1.set_ylabel('retes')
ax1.set_title("line chart")

ax1.plot([13, 14, 15, 16], [0.2, 0.8, 0.5, 0.4])
ax1.plot([13, 14, 15, 16], [0.3, 0.4, 0.7, 0.8])
plt.savefig('line_chart.jpg')
plt.show()