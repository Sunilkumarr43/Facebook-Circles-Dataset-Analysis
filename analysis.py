{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "78f231dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Graph with 4039 nodes and 88234 edges\n",
      "Average clustering coefficient: 0.6055467186200876\n"
     ]
    }
   ],
   "source": [
    "#Loading and Exploring the Data\n",
    "import networkx as nx\n",
    "\n",
    "   # Load the graph (assuming edge list format)\n",
    "G = nx.read_edgelist(\"facebook_combined.txt\", nodetype=int)\n",
    "\n",
    "   # Basic Stats\n",
    "print(nx.info(G))\n",
    "\n",
    "   # Clustering coefficient\n",
    "clustering = nx.average_clustering(G)\n",
    "print(f\"Average clustering coefficient: {clustering}\")\n",
    " \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "39dd4ba8",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Weakly Connected Components: 1\n"
     ]
    }
   ],
   "source": [
    "#a. Weakly Connected Components (WCC)\n",
    "# Convert undirected graph to directed graph\n",
    "G_directed = nx.DiGraph(G)\n",
    "\n",
    "# Now you can calculate the weakly connected components\n",
    "wcc = nx.number_weakly_connected_components(G_directed)\n",
    "print(f\"Number of Weakly Connected Components: {wcc}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "351e0196",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Strongly Connected Components: 1\n"
     ]
    }
   ],
   "source": [
    "#b. Strongly Connected Components (SCC)\n",
    "# Convert the undirected graph to directed\n",
    "G_directed = nx.DiGraph(G)\n",
    "\n",
    "# Now calculate SCC\n",
    "scc = nx.number_strongly_connected_components(G_directed)\n",
    "print(f\"Number of Strongly Connected Components: {scc}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "042b3c61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of triangles: 1612010\n"
     ]
    }
   ],
   "source": [
    "# Number of triangles\n",
    "triangles = nx.triangles(G)\n",
    "print(f\"Number of triangles: {sum(triangles.values()) // 3}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6644686e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Degree distribution\n",
    "degrees = [degree for node, degree in G.degree()]\n",
    "import matplotlib.pyplot as plt\n",
    "plt.hist(degrees, bins=50)\n",
    "plt.xlabel('Degree')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Degree Distribution')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "e9156414",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Diameter: 8\n"
     ]
    }
   ],
   "source": [
    "# Diameter\n",
    "diameter = nx.diameter(G)\n",
    "print(f\"Diameter: {diameter}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
