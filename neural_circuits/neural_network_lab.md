# Lab 4: Neurons and the Neural Computation

All of the questions below deal with the neural network simulation program available at:
https://trinket.io/pygame/8d83ddd53d?toggleCode=true . Press the “Run” button to start the simulation. 
The code is available for those who are interested in looking at it, but you shouldn’t need it to answer the questions.

The simulation is of a simple 4-neuron neural network, with 2 input units, 1 bias unit, and 1 output unit. 
The simulation demonstrates how you can use a network like this to do logical computation. 
In this simulation, the network starts off with random weights, and so doesn’t perform the logical computations very well. 
You can use the “train” buttons at the bottom to train the network. 
Train 1x exposes the network to each input-output pairing one time.
Thia is a total of 4 learning experiences, since there are four input output pairs in each logical truth table. 
We call this 1 training “epoch” (usually pronounced more like “epic”, although some people say “ee-pock”). 
Train 10x exposes the network to each input-output pairing ten times (or 10 epochs), and 100x does 100 epochs. 
As you click the train button you will see the network improve its calculation of these functions. 
You can use the reset button to go back to random weights and start over.
 
In the top right corner, you will see a truth table. 
The truth table defaults to showing the logical function AND, and its inputs and outputs. 
This table also shows the network’s current predicted output for each input. 
You can click on the “AND” text to toggle the truth table to different functions.
For each function you can see the network’s prediction for the outputs given its current weighted connections.
 
In the bottom left/middle of the simulation, you see the neural network itself. 
At any given time, it shows one set of inputs (the nodes x1 and x2 will be filled in with either a 1 or a 0). 
You can see each weighted connection from the inputs and bias to the output.
You can also see the network’s output value, which will be the same as for that input in the truth table. 
You can click on different inputs in the truth table and that will change which input is displayed in the network. 
You can also click on the values of the weights in the network, and manually change them to your own values.
 
The top left corner shows the “sigmoid” (also called logistic) activation function.
The sigmoid function starts with the neuron's net input, the sum of each input and bias multiplied by their weights.
The net input is converted to a value between 0 and 1. 
The orange vertical line represents the current level of net input, and the orange horizontal line represents the net output.
 
The bottom right corner shows a graphical representation of the four inputs, and what their outputs should be (green if 1, red if 0). 
As the network trains, you will see a yellow line appear in that space, representing the decision boundary for the network. 
For every input on one side of the boundary, the network is guessing 1.
For every input on the other side of the boundary, the network is guessing 0.
 
Play around with the simulation a bit, then try to answer the following questions.

## 1. Set the network to the AND logical function, and press the Reset button. (38 PTS TOTAL)

### 1.1. Initial state of the untrained neural network (10 POINTS, 2 EACH)
- write out the network's current "model" equation of the AND relationship (y = b0 + b1*x1 + b2*x2, but subbing in the b-values) 
- In a table like below, write out the network's prediction for each combination of inputs

**LOGICAL "AND"**

| x1 | x2 | y | y' |
|----|----|---|---|
| 0  | 0  | 0 |   |
| 0  | 1  | 0 |   |
| 1  | 0  | 0 |   |
| 1  | 1  | 1 |   |

- Look at the figure in the bottom right of the simulation window.
It shows the four inputs as points, using color to depict the correct output category for those inputs.
It also shows the current decision boundary, determined by the current weights.
Describe where the boundary is relative to the four points and how it divides them.
- Does it get all members of each category on different sides of the line?
- How does the decision boundary need to change in order to do so?

### 1.2. Now train the network for 1 epoch (12 POINTS, 3 EACH)
- write the new prediction table

**LOGICAL "AND"**

| x1 | x2 | y | y' |
|----|----|---|---|
| 0  | 0  | 0 |   |
| 0  | 1  | 0 |   |
| 1  | 0  | 0 |   |
| 1  | 1  | 1 |   |

- write the new model equation.
- how have the weights changed?
- Given your understanding of “error-driven learning” explained in class and in the reading, why does the change make sense? (5 PTS)
- How has the decision boundary changed?

### 1.3. Now train the network until it is performing well on the AND function (y' close to 1 when the answer should be 1, and close to 0 when the answer should be zero). (16 POINTS, 2 EACH)
- How many epochs you had to train the network to achieve this performance?
- Rewrite the equation with the parameter values.
- Describe how has the decision boundary has changed.
- Describe how have the weights changed?
- Do the values of the weights make sense to you given the function that is being performed?
- How do the weights for the inputs (b1 and b2) compare to one another, and why does this make sense?
- How do the weights for the inputs compare to the weight for the bias (b0) and why does this make sense?
- Can you make a general statement about what the relationship between the weights for the inputs and the weights for the bias need to be, in order for neurons to compute an AND function?

## 2. Now, change the network to the OR function, but DO NOT reset the network. (29 POINTS TOTAL)

### 2.1. How does the network that was trained on the AND function do on the OR function? Explain why its performance makes sense. (2 PTS)

### 2.2. Now reset the weights back to random values. How does the network perform now, and why does that make sense? (3 PTS) 

### 2.3 Train the network until it achieves good performance on the OR function. (18 POINTS, 3 EACH)
- How many epochs did it take to achieve good performance?
- Write out the equation for the well-performing OR network (like you did in 1b).
- How have the weights changed? Do the values of the weights make sense to you given the function that is being performed?
- How do the weights for the inputs (b1 and b2) compare to one another, and why does this make sense?
- How do the weights for the inputs compare to the weight for the bias (b0) and why does this make sense?
- Can you make a general statement about what the relationship between the weights for the inputs and the weights for the bias need to be, in order for neurons to compute an OR function?

### 2.4 Compare the AND and OR network (6 POINTS, 2 EACH)
- Rewrite the AND and the OR equations here next to each other.
- Describe the difference between the two equations. Can you explain how their differences make sense? (10 PTS)
- Compare the two decision boundaries. How are they different, and how does the difference make sense?

## 3. Now, change the network to the XOR function, and reset the network, but do not train it. (31 POINTS TOTAL)

### 3.1. The XOR Problem (11 POINTS)
- The xor problem is a famous issue with neural networks, as it is hard to solve with certain kinds of neural networks.
Can you think of three situations where you need to learn that some outcome (y) depends on either one thing (x1) or another thing (x2),
BUT NOT BOTH, being true in order for y to be true? (6 POINTS)
- Can you describe why it might be harder, in general, to learn or represent XOR relationships compared to AND or OR relationships? (5 POINTS)

### 3.2. How does the network perform now, and why does that make sense? (4 PTS, 2 EACH)
- How does the network perform before training?
- Where is the decision boundary, and how does it need to change to correctly classify all four sets of inputs. 

### 3.3. Train the network for as many epochs as it took to solve the AND or OR dataset. (9 POINTS, 3 EACH)
- How have the weights changed?
- How has the decision boundary changed?
- How has the performance changed?

### 3.4. Train it for 10x as many epochs as you did previously.
- The network will still be performing poorly. Explain why. Try to use the decision boundary graphic in your explanation. Note the large number of points here. Please try to give this a thoughtful answer (10 POINTS).
