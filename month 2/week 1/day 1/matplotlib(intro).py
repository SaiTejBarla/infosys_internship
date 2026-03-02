import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data1 = np.random.normal(0,1,100)
data2 = np.random.normal(0,2,100)

plt.hist(data1, bins=20, alpha=0.5, label='Data 1')
plt.hist(data2, bins=20, alpha=0.5, label='Data 2')
plt.legend()
plt.title('Histogram of Two Datasets')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
