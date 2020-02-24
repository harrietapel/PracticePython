import json
from clustering import cluster

# Reading the JSON files
with open('data/cities.json', 'r') as json_file:
    cities_as_string = json_file.read()
cities = json.loads(cities_as_string)

with open('data/libraries.json', 'r') as json_file:
    libs_as_string = json_file.read()
libs = json.loads(libs_as_string)

# Combining the two files and saving it into its own JSON file
combined = {}
pts = []
for city in cities:
    combined[city['name']] = {'population':city['population']}
    n_books = 0
    for lib in libs:
        if lib['city']==city['name']:
            n_books += lib['books'] 
    combined[city['name']]['books'] = n_books
    pts.append(tuple((city['population'], n_books)))

with open('data/combined.json', 'w') as outfile:
    json.dump(combined, outfile, indent=4)

# Calling the cluster code
cluster_centre, cluster_allocation = cluster(pts, iters=10)

for i, cluster in enumerate(cluster_centre):
    cluster_points = [point for ind, point in enumerate(pts) if cluster_allocation[ind] == i]
    print("Cluster " + str(i) + " is centred at " + str(cluster) + " and has " + str(len(cluster_points)) + " points.")
