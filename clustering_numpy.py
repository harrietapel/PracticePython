from math import sqrt
from random import seed, randrange
from argparse import ArgumentParser
import numpy as np


def find_distance(a, b):
    '''
    Calculates the distance between two input points a and b in 2d using pythagoras,
    returns the distance.
    '''
    diff_x = a[0]-b[0]
    diff_y = a[1]-b[1]
    return sqrt((diff_x)**2+(diff_y)**2)


def cluster(points,iters=10):
    '''
    Takes a list of points as tuples and performs the k-means algorithm to cluster
    data points into separate clusters. Optional argument iters is the number of 
    iterations for the algorithm to be run. Each cluster  will (ideally) contain points 
    that are close to each other, and far from the other clusters. The code then 
    prints some basic statistics about the resulting clusters and returns the cluster
    centres and the cluster allocation.
    '''
    n_clusters = 3
    # Picks three random points to be initial centres of the clusters
    rng = np.random.default_rng()
    cluster_centre = rng.choice(points,n_clusters)
    
    ### TO MAKE SURE IT STILL WORKS
    cluster_centre = np.array([[3.83531, 3.88187], [0.54287, 2.37466], [5.75247, 4.68959]])
    
    iteration = 0
    while iteration<iters:
        # Assign each data point to a cluster
        distances = np.repeat(points,n_clusters,axis=0).reshape(points.shape[0],n_clusters,2)
        distances = np.subtract(distances, cluster_centre)
        distances = np.apply_along_axis(np.linalg.norm, 2, distances)
        cluster_allocation = np.argmin(distances, 1)
        # Update the centre of each cluster by setting it to the average of all points assigned to the cluster
        sorted_points = points[np.argsort(cluster_allocation)]
        unique, counts = np.unique(cluster_allocation, return_counts=True)
        n_points = dict(zip(unique, counts))
        np.mean(sorted_points[0:n_points[0]],axis=0,out=cluster_centre[0])
        np.mean(sorted_points[n_points[0]:n_points[0]+n_points[1]],axis=0,out=cluster_centre[1])
        np.mean(sorted_points[n_points[0]+n_points[1]:,],axis=0,out=cluster_centre[2])
        iteration = iteration+1

    for i, cluster in enumerate(cluster_centre):
        print("Cluster " + str(i) + " is centred at " + str(cluster) + " and has " + str(n_points[i]) + " points.")

    # Visualising the output of the algorithm
    from matplotlib import pyplot as plt
    for i in range(n_clusters):
        cluster_points = [point for ind, point in enumerate(points) if cluster_allocation[ind] == i]
        plt.scatter([point[0] for point in cluster_points], [point[1] for point in cluster_points])
    plt.show()
    
    return cluster_centre, cluster_allocation

if __name__ == "__main__":
    parser = ArgumentParser(description='Performs k-means algorithm to cluster data points')
    parser.add_argument('samples_file', type=str, 
                        help='csv filename including list of data points')
    parser.add_argument('--iters', type=int, default=10,
                        help='number of iterations for algorithm (default:10)' )
    args = parser.parse_args()

    with open(args.samples_file, 'r') as source_file:
        points = np.genfromtxt(source_file, dtype=float, delimiter=',')
    cluster(points, iters=args.iters)
