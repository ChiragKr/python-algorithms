Timestamp Depth First Search
============================

Using the timestamp-based approach, we record the _discovery time_ and _completion time_ (completion implies all descendants discovered) of every node. This helps us classify the various edges of the graph. Some edges form a tree, called the depth-first-search tree of G starting at the given root, and the edges in this tree are called **Tree edges**. The other edges of G can be divided into three categories:

* **Forward edges** : point from a node to one of its descendants in the DFS tree (but is not part of the DFS tree).
* **Back edges** : point from a node to one of its ancestors in the DFS tree.
* **Cross edges** : point from a node to a previously visited node that is neither an ancestor not a descendant.

classification done using following time comparision table 

| Edge-type    | start times         | end times       |
| -------------|:-------------------:|:---------------:|
| Tree edge    | start[u] < start[v] | end[u] > end[v] |
| Forward edge | start[u] < start[v] | end[u] > end[v] |
| Back edge    | start[u] > start[v] | end[u] < end[v] |
| Cross edge   | start[u] > start[v] | end[u] > end[v] |

These edge-types help us analyse the graph. For example, if the graph has no back edges then it does not contain cycles. In the code, directed graphs are considered.
Below is an example graph showing the timestamp at each node (start time/end time) and the different edges: 
![alt text](https://github.com/ChiragKr/python-algorithms/blob/master/depth_first_search3/example1.png "Graph example")
