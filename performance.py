import numpy as np
import timeit
import os
from matplotlib import pyplot as plt

n_samples = 20
n_data_points = np.logspace(2.0, 4.0, num=n_samples, dtype=int)
print('n_data_points', n_data_points)
plain_time = np.zeros(n_samples)
numpy_time = np.zeros(n_samples)
n_runs = 10

for i, n_dp in enumerate(n_data_points):
    # Make multiple input files with coordinate points, ranging from 100 to 10,000 points
    points = np.random.uniform(-5,5,n_dp*2).reshape(n_dp,2)
    filename = "data/performance_" + str(n_dp) + ".csv"
    np.savetxt(filename, points, delimiter=",")

    # Measure time for clustering.py
    plain_setup = 'from __main__ import filename; from clustering import cluster, plain_load'
    plain_code = 'points = plain_load(filename); cluster(points)'
    plain_time[i] = timeit.timeit(setup=plain_setup, stmt=plain_code, number=n_runs)

    # Measure time for clustering_numpy.py
    numpy_setup = 'from __main__ import filename; from clustering_numpy import cluster, numpy_load'
    numpy_code = 'points = numpy_load(filename); cluster(points)'
    numpy_time[i] = timeit.timeit(setup=numpy_setup, stmt=numpy_code, number=n_runs)

    os.remove(filename)

# Plot and save results
plt.plot(n_data_points, plain_time, label='plain python')
plt.plot(n_data_points, numpy_time, label='numpy')
plt.legend()
plt.title('Comparing cluster algorithm performance.')
plt.xlabel('Number of data points in input file')
ylabel = 'Time for '+ str(n_runs)+' executions/s'
plt.ylabel(ylabel)
plt.savefig('performance.png')
