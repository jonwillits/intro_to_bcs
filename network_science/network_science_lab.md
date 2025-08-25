# Lab 11: Network (Neuro)Science

## 1. Creating Networks (44 PTS)
You have identified 26 different areas in the brain (we will label these with letters from A to Z).
You have conducted a series of studies to see which areas activate together in different tasks. 
You want to create a functional network diagram of the brain based on your work.

### Network 1:
First, you run a series of studies using visual stimuli and observe sets of co-activations (in square brackets). 
If you assume that co-activation means connection (and that all connections are bidirectional), 
draw the visual processing network that these studies as a group suggest: (8 PTS)

\[B, D, K] \[A, J, K] \[A, K, M] 

### Network 2:
Now, you run a series of studies using auditory stimuli and get a different set of co-activations.  
Draw this network as well. (8 PTS)

\[C, I, R] \[G, I, R] \[G, I, O] \[C, M, O]

Compare this network with the one you drew above. 
Are there any points of connection (assume that a letter label always refers to the same brain area, across experiments)? 
Where? (2 PTS)

### Network 3:
Now draw the graphs associated with a motor task (like very carefully manipulating small objects with your hands). (6 PTS)

\[E, F, M] \[F, N, S] \[F, P, S] \[P, Q] \[H, S] \[H, X]

Are there any connections between network 1 and network 3? What about network 2 and network 3? (4 PTS)

### Network 4:
Finally, draw the graph associated with a language task: (8 PTS)

\[E, M, O] \[E, F, M] \[E, L, M] \[E, L, U] \[E, U, W] \[U, V] \[W, Z] \[F, Z] \[Z, T] \[V, Y]

Describe the connections between Network 4 and Networks 1, 2, and 3. (6 PTS)


## 2. Analyzing the Networks (38 PTS TOTAL)
Now, let's analyze our networks.

### 2.1. Calculating Network Degree (k) (10 PTS)
Calculate the degree of each node in the “whole brain”.
Remember, the degree is just a number representing how many other nodes a given node is connected to. 
For nodes that appear in more than one subnetwork, make sure to count up connections across all the networks.

| Node | Degree |
|------|--------|
| A    |        |
| B    |        |
| C    |        |
| D    |        |
| E    |        |
| F    |        |
| G    |        |
| H    |        |
| I    |        |
| J    |        |
| K    |        |
| L    |        |
| M    |        |
| N    |        |
| O    |        |
| P    |        |
| Q    |        |
| R    |        |
| S    |        |
| T    |        |
| U    |        |
| V    |        |
| W    |        |
| X    |        |
| Y    |        |
| Z    |        |

### 2.2. Calculating Degree (k) Distribution (10 PTS)
Now create a chart of the k distribution (to make it easier, we will just count rather than do probabilities, which are more typical). 
Remember that k refers to the degree, so we are creating a chart of how often each degree appears in the network.

| K | Frequency of k in network |
|------|--------|
| 1    |        |
| 2    |        |
| 3    |        |
| 4    |        |
| 5    |        |
| 6    |        |
| 7    |        |

### 2.3. Network Architecture (10 PTS TOTAL)
- Which of the following network architectures does our network resemble? Why? (4 PTS)
![network_structures.png](images/network_structures.png)

- Which nodes are good candidates for being network hubs based on this metric? (1 PT)
- What are likely provincial hubs in your brain network? Provincial hubs act as hubs within a module. (1 PT)
- What are likely connector hubs? Connector hubs serve to connect different modules to one another. (1 PT)
- Can we identify properties like a network's architecture type, which nodes are hubs, and what kinds of hubs they are based on measures of degree alone? (3 PTS)

### 2.4. Experimenting on the network (8 PTS TOTAL)
Now, imagine you asked participants to do an experiment consisting of a series of tasks one after the other, cycling through visual to auditory to motor to language and back to a (different kind of) visual task, etc.
- If you were able to use something like transcranial magnetic stimulation (TMS) to disrupt the function of one of the non-hub nodes during this experiment, what might happen?  (4 PTS)
- What if you disrupted a single provincial hub?  (2 PTS)
- What about a single connector hub? (2 PTS)

## 3. Network Neuroscience vs. Neural Networks (18 PTS)
What are 3 similarities and 3 differences between the neural network approach we discussed previously, and the network neuroscience approach we are discussing this week?
