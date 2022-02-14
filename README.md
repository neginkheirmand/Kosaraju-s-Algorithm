# Kosaraju's Algorithm  

[Kosaraju](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm) is a linear time algorithm to find the strongly connected components of a directed graph.

first lets define strongly connected graphs:

a directed graph is an strongly connected graph if there is a path between all pairs of vertices, for example:

![graph2](C:\Users\venus\Desktop\uni2\6th_SEMESTER\github\Kosaraju's Algorithm\images\graph2.png)



this graph is an strongly connected graph because no matter which vertex you chose there will always be a path to any other vertex of the graph. 

for example if you start from the vertex a0:

there will be a path to a3:

![graph2- a0-a3](C:\Users\venus\Desktop\uni2\6th_SEMESTER\github\Kosaraju's Algorithm\images\graph2- a0-a3.png)

  

to a2:

![graph2- a0-a2](C:\Users\venus\Desktop\uni2\6th_SEMESTER\github\Kosaraju's Algorithm\images\graph2- a0-a2.png)



and to a1:

![graph2 - a0-a1](C:\Users\venus\Desktop\uni2\6th_SEMESTER\github\Kosaraju's Algorithm\images\graph2 - a0-a1.png)

these are only some of the paths existent.

Now you can probably tell what a strongly connected component is, its a node of the graph that can reach any other node of the directed graph.  

Another definition you will need to know is the transpose of a directed graph which is basically the same graph but with inverted edges or links.

the graph:

 ![graph3](C:\Users\venus\Desktop\uni2\6th_SEMESTER\github\Kosaraju's Algorithm\images\graph3.png)

transpose of the graph:

![graph3_T](C:\Users\venus\Desktop\uni2\6th_SEMESTER\github\Kosaraju's Algorithm\images\graph3_T.png)









You can find all graph images used in the Readme in the images folder, they were created using the [edotor site's](https://edotor.net/) graph creator. 

