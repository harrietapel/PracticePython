import numpy as np
import time 
import os
from matplotlib import pyplot as plt

n_samples = 30
n_data_points = np.logspace(2.0, 4.0, num=n_samples, dtype=int)
plain_time = np.zeros(n_samples)
numpy_time = np.zeros(n_samples)

for i, n_dp in enumerate(n_data_points):
    # Make multiple input files with coordinate points, ranging from 100 to 10,000 points
    points = np.random.uniform(-5,5,n_dp*2).reshape(n_dp,2)
    filename = "data/performance_" + str(n_dp) + ".csv"
    np.savetxt(filename, points, delimiter=",")

    # Measure time for clustering.py
    start = time.time()
    os.system('python clustering.py ' + filename)
    plain_time[i] = time.time() - start

    # Measure time for clustering_numpy.py
    start = time.time()
    os.system('python clustering_numpy.py ' + filename)
    numpy_time[i] = time.time() - start

# Plot and save results
plt.plot(n_data_points, plain_time, label='plain python')
plt.plot(n_data_points, numpy_time, label='numpy')
plt.legend()
plt.xlabel('Number of data points in input file')
plt.ylabel('Time for execution/s')
plt.xscale('log')
plt.savefig('performance.png')
