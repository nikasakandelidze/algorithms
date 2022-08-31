# Checking cycles in Undirected graph
There are 2 distinct ways that i know of for searching for loops in undirected graphs:
- DFS: Simply start iterating over all nodes of the graph using dfs and mark every visited node. If at some point
you encounter a node that is already marked as visited and it is not current node's parent than you found a cycle.
- Disjoint Set: Start creating Disjoint set data structure by unioning all the edges. If at some point in time as input
of unioin function comes pair of nodes that already have one and the same representator of connected components than you have found cycle

# Chechking cycles in Directed graph
- DFS: Simply start iterating over all nodes of the graph using dfs and mark/store every node you visit. If you see
node that is already marked/stored as visited but is current nodes neighbor you have found cycle
- Topologyc sort: Todo