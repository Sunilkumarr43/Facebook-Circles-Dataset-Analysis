Facebook Circles Dataset Analysis

Overview

This project performs network analysis on an anonymized Facebook dataset, focusing on nodes (Facebook users) and edges (connections between users). The dataset contains information about the friendship circles and the structure of the network, allowing for insights into connected components, clustering, and shortest path lengths.

Dataset Description

Nodes: 4039 users
Edges: 88,234 connections (friendships)
WCC: Weakly Connected Components, all nodes are part of one component when ignoring edge directionality.
SCC: Strongly Connected Components (when considering edge directionality).
Clustering Coefficient: A measure of how likely friends of a user are to be friends with each other.
Triangles: A group of three mutually connected users.
Diameter: The longest shortest path between two nodes.


Requirements

The project requires Python and the following libraries:

networkx: For network analysis
matplotlib: For plotting graphs
numpy (optional): For numeric computations
You can install the required libraries using pip:

bash
pip install networkx matplotlib

File Structure

analysis.py: The main Python script that loads the dataset and performs the analysis.
facebook_combined.txt: The dataset in edge list format.
README.md: This file, describing the project.
requirements.txt: A list of dependencies.

Usage
Load the dataset: The dataset is assumed to be in facebook_combined.txt. You can replace this with any graph dataset in the edge list format.
Run the analysis: Run the analysis.py script to perform various network analysis tasks such as calculating connected components, triangles, clustering coefficient, and more.

bash
python analysis.py
Output
The script will print basic statistics about the graph:

Number of nodes and edges
Number of connected components (for undirected graphs)
Number of triangles
Clustering coefficient
Degree distribution plot
Diameter of the graph (longest shortest path)
Code Snippet (Example Usage)


Here is an example code snippet from the analysis.py file that loads the dataset and calculates basic statistics:

python
import networkx as nx
import matplotlib.pyplot as plt

# Load the graph from the edge list
G = nx.read_edgelist("facebook_combined.txt", nodetype=int)

# Basic statistics
print(nx.info(G))

# Clustering coefficient
clustering = nx.average_clustering(G)
print(f"Average clustering coefficient: {clustering}")

# Number of connected components
wcc = nx.number_connected_components(G)
print(f"Number of Weakly Connected Components: {wcc}")

# Plot degree distribution
degrees = [degree for node, degree in G.degree()]
plt.hist(degrees, bins=50)
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()


Further Analysis
You can expand on the project by:

Community detection: Identify communities or clusters of users.
Centrality analysis: Calculate node centrality to identify key players in the network.
Graph visualization: Use tools like matplotlib or pygraphviz to visualize the network.