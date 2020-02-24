import numpy as np
import timeit
import os
from matplotlib import pyplot as plt

n_samples = 20
n_data_points = np.logspace(2.0, 4.0, num=n_samples, dtype=int)
print('n_data_points', n_data_points)
plain_time = np.zeros(n_samples)
numpy_time = np.zeros(n_samples)

def plain_load(filename):
    points = []
    with open(filename, 'r') as source_file:
        lines = source_file.readlines()
        for line in lines: 
            points.append(tuple(map(float, line.strip().split(','))))
    return points

def np_load(filename):
    with open(filename, 'r') as source_file:
        points = np.genfromtxt(source_file, dtype=float, delimiter=',')
    return points


for i, n_dp in enumerate(n_data_points):
    # Make multiple input files with coordinate points, ranging from 100 to 10,000 points
    points = np.random.uniform(-5,5,n_dp*2).reshape(n_dp,2)
    filename = "data/performance_" + str(n_dp) + ".csv"
    np.savetxt(filename, points, delimiter=",")

    # Measure time for clustering.py
    plain_setup = 'from __main__ import filename, plain_load; from clustering import cluster; points = plain_load(filename)'
    plain_code = 'cluster(points)'
    plain_time[i] = timeit.timeit(setup=plain_setup, stmt=plain_code, number=10)

    # Measure time for clustering_numpy.py
    numpy_setup = 'from __main__ import filename, np_load; from clustering_numpy import cluster_np; points = np_load(filename)'
    numpy_code = 'cluster_np(points)'
    numpy_time[i] = timeit.timeit(setup=numpy_setup, stmt=numpy_code, number=10)

# Plot and save results
plt.plot(n_data_points, plain_time, label='plain python')
plt.plot(n_data_points, numpy_time, label='numpy')
plt.legend()
plt.xlabel('Number of data points in input file, (logarithmic scale)')
plt.ylabel('Time for execution/s')
plt.xscale('log')
plt.savefig('performance.png')
