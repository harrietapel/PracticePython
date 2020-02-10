from math import *
from random import *

n_clusters=3

lines = open('data/samples.csv', 'r').readlines()
points = []
for line in lines: points.append(tuple(map(float, line.strip().split(','))))

# Picks three random points to be initial centres of the clusters
cluster_centre = [points[randrange(len(points))], points[randrange(len(points))], points[randrange(len(points))]]

cluster_allocation = [None]*len(points)
iteration = 0
while iteration<10:
    for i in range(len(points)):
        p = points[i]
        distance = [None] * 3
        # Assign each data point to a cluster.
        distance[0] = sqrt((p[0]-cluster_centre[0][0])**2 + (p[1]-cluster_centre[0][1])**2)
        distance[1] = sqrt((p[0]-cluster_centre[1][0])**2 + (p[1]-cluster_centre[1][1])**2)
        distance[2] = sqrt((p[0]-cluster_centre[2][0])**2 + (p[1]-cluster_centre[2][1])**2)
        cluster_allocation[i] = distance.index(min(distance))
    # Update the centre of each cluster by setting it to the average of all points assigned to the cluster
    for i in range(3):
        cluster_points = [point for ind, point in enumerate(points) if cluster_allocation[ind] == i]
        new_mean = (sum([point[0] for point in cluster_points]) / len(cluster_points), sum([point[1] for point in cluster_points]) / len(cluster_points))
        cluster_centre[i] = new_mean
    iteration = iteration+1

for i in range(3):
    cluster_points = [point for ind, point in enumerate(points) if cluster_allocation[ind] == i]
    print("Cluster " + str(i) + " is centred at " + str(cluster_centre[i]) + " and has " + str(len(cluster_points)) + " points.")


# Visualising the output of the algorithm
from matplotlib import pyplot as plt
for i in range(3):
    cluster_points = [point for ind, point in enumerate(points) if cluster_allocation[ind] == i]
    plt.scatter([point[0] for point in cluster_points], [point[1] for point in cluster_points])
plt.show()
