# Kosaraju's Algorithm  

[Kosaraju](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm) is a linear time algorithm to find the strongly connected components of a directed graph.

first lets define strongly connected graphs:

a directed graph is a strongly connected graph if there is a path between all pairs of vertices, for example:

![graph2](https://github.com/neginkheirmand/Kosaraju-s-Algorithm/blob/master/images/graph2.png?raw=true)



this graph is a strongly connected graph because no matter which vertex you chose there will always be a path to any other vertex of the graph. 

for example, if you start from the vertex a0:

there will be a path to a3:

![graph2- a0-a3](https://github.com/neginkheirmand/Kosaraju-s-Algorithm/blob/master/images/graph2%20-%20a0-a3.png?raw=true)

  

to a2:

![graph2- a0-a2](https://github.com/neginkheirmand/Kosaraju-s-Algorithm/blob/master/images/graph2%20-%20a0-a2.png?raw=true)



and to a1:

![graph2 - a0-a1](https://github.com/neginkheirmand/Kosaraju-s-Algorithm/blob/master/images/graph2%20-%20a0-a1.png?raw=true)

these are only some of the existing paths.

Now you can probably tell what a strongly connected component is, its a node of the graph that can reach any other node of the directed graph.  

Another definition you will need to know is the transpose of a directed graph which is basically the same graph but with inverted edges or links.

the graph:

 ![graph3](https://github.com/neginkheirmand/Kosaraju-s-Algorithm/blob/master/images/graph3.png?raw=true)

transpose of the graph:

![graph3_T](https://github.com/neginkheirmand/Kosaraju-s-Algorithm/blob/master/images/graph3_T.png?raw=true)









You can find all graph images used in the Readme in the images folder, they were created using the [edotor site's](https://edotor.net/) graph creator. 

