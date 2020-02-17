from math import sqrt
from random import seed, randrange

def find_distance(a, b):
    '''
    Calculates the distance between two points a and b in 2d using pythagoras,
    returns the distance.
    '''
    diff_x = a[0]-b[0]
    diff_y = a[1]-b[1]
    return sqrt((diff_x)**2+(diff_y)**2)

n_clusters=3

lines = open('data/samples.csv', 'r').readlines()
points = []
for line in lines: points.append(tuple(map(float, line.strip().split(','))))

# Picks three random points to be initial centres of the clusters
seed(1)
cluster_centre = [points[randrange(len(points))], points[randrange(len(points))], points[randrange(len(points))]]

cluster_allocation = [None]*len(points)
iteration = 0
iters = 10
while iteration<iters:
    for index, point in enumerate(points):
        distance = [None] * n_clusters
        # Assign each data point to a cluster, specific to 3 clusters currently
        distance[0] = find_distance(point,cluster_centre[0])
        distance[1] = find_distance(point,cluster_centre[1])
        distance[2] = find_distance(point,cluster_centre[2])
        cluster_allocation[index] = distance.index(min(distance))
    # Update the centre of each cluster by setting it to the average of all points assigned to the cluster
    for i, cluster in enumerate(cluster_centre):
        cluster_points = [point for ind, point in enumerate(points) if cluster_allocation[ind] == i]
        av_x = sum([point[0] for point in cluster_points]) / len(cluster_points)
        av_y = sum([point[1] for point in cluster_points]) / len(cluster_points)
        cluster_centre[i] = (av_x, av_y)
    iteration = iteration+1

for i, cluster in enumerate(cluster_centre):
    cluster_points = [point for ind, point in enumerate(points) if cluster_allocation[ind] == i]
    print("Cluster " + str(i) + " is centred at " + str(cluster) + " and has " + str(len(cluster_points)) + " points.")

# Visualising the output of the algorithm
from matplotlib import pyplot as plt
for i in range(n_clusters):
    cluster_points = [point for ind, point in enumerate(points) if cluster_allocation[ind] == i]
    plt.scatter([point[0] for point in cluster_points], [point[1] for point in cluster_points])
plt.show()


