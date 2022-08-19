# Disjoint set data structure / union-find algorithm
This algorithm is perfect to use in cases where we need to deal with:
- any kind of operations with connected components
- check whether two verticies are connected in single connected component
- address connectivity problem in any kind of network ( social networ, computer network, etc)
- Check for cycles in undirected graphs

# algorithm idea
Each connected component has one "representative" node, so if we need to understand if two nodes are connected
we should check whether or not these nodes have one and the same representative.

Let's assume for simplicity that all the cases where we'll need union find algorithm will deal with input data of next type:
[(node1, node2), (node3, node4)....]. 
we'll first need to perform union operation on all of the edges ( node1 <-> node2 ), and after it check components for connectivity. 

We'll need to implement 2 functions:
- union: gets two nodes (edge) as an input and updates state of data structure
- find: gets two nodes as an input and tell us whether or not they are connected
