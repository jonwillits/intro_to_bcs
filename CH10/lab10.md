# Lab 10: Connectionism and Neural Networks

## 1. Symbolic vs. Connectionist perspective (11 PTS TOTAL)

### 1.1. What are three things that make the connectionist and symbolic perspectives different? (3 PTS)

### 1.2. Comparing behaviorism to the symbolic and connectionist perspectives. 
- What are two ways that behaviorism is similar to, and two ways it is different from, the symbolic perspective (4 PTS)
- What are two ways that behaviorism is similar to, and two ways it is different from, the connnectionist perspective? (4 PTS)

# 2. Connectionist Rock-Paper-Scissors (46 PTS)
Previously, you played a symbolic AI that played rock-paper-scissors.
Now, answer the following questions about how the program would have to be different to be implemented as a connectionist program.

## 2.1. Next-move Prediction (19 PTS TOTAL)
Imagine a neural network that was trying to predict what your next move was going to be.
What would the model need to be like? 

- 2.1.1. What information would need to be represented in the input and output layers? (4 PTS)
- 2.1.2. Would the network need a "hidden" layer? Why or why not? (2 PTS)
- 2.1.3. Would the network need a "recurrent" layer? Why would one help? Is there a way you can represent the problem without one? (6 PTS)
- 2.1.4. Describe how a "Hebbian Learning" vs. an "Error Driven Learning" version of this model would be different. (4 PTS)
- 2.1.5. Would such a prediction model need to be good at winning rock-paper-scissors? Why or why not? If not, what would you need to add (3 PTS)

## 2.2. Predict the next best move (19 PTS TOTAL)
Now imagine a model that is trying to predict the correct next move to take.
What would that model need to be like? Answer the same five questions as above.
- 2.2.1. What information would need to be represented in the input and output layers? (4 PTS)
- 2.2.2. Would the network need a "hidden" layer? Why or why not? (2 PTS)
- 2.2.3. Would the network need a "recurrent" layer? Why would one help? Is there a way you can represent the problem without one? (6 PTS)
- 2.2.4. Describe how a "Hebbian Learning" vs. an "Error Driven Learning" version of this model would be different. (4 PTS)
- 2.2.5 Would such a learning model need to be good at winning rock-paper-scissors? Why or why not? If not, what would you need to add (3 PTS)

## 2.3. Comparison to symbolic model. (8 PTS)
What are 2 ways in which these neural network models would be similar to, and different from, the symbolic model we used last week.

# 3. Classifier Playground (43 PTS TOTAL)
The following questions all involving using this website: [Tensorflow Playground](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.33221&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false ).
On this website, you can play around with neural networks to better understand hwo they work.

To start off, make the following changes to the webpage:
- In the section marked data, click on and activate the bottom left picture (with an orange cloud of points in the top left and a blue cloud in the bottom right)
- In the middle where it says "2 Hidden Layers", click the minus button twice so that there are 0 hidden layers.

We now have a neural network that we can use to simulate a situation where you are trying to classify a set of inputs into one of two categories.
Each input is shown as a dot in the figure under the word "OUTPUT", with the color representing its category.
You can imagine this as analogous to many situations, such as "Should I eat this?".
In this situation the blue dots mean "yes, I want to eat it" and orange dots mean "no, I don't want to eat it".
The position of each dot in the graph represents the value of that input in terms of two properties X1 and X2.
X1 (the position of a dot on the horizontal axis) might represent how tasty something is. 
A score of +6 means really tasty, and a score of -6 means really not tasty.
X2 (the position of the dot on the vertical axis) might represent how healthy something is (+6 to -6).

What we are trying to do is see if the neural network can learn to classify whether you should eat it in terms of these two features.
In this case, we can see that tge things we want to eat (the blue dots) are things that are either really tasty, or really healthy, or both.
The things we don't want to eat (the orange dots) are things that are either really not tasty.
The two categories are "linearly separable", meaning we can divide the two categories with a line in the 2D feature space.
This means that a simple, single layer neural network will be able to learn to categorize each input as blue/yes or orange/no.

The background color of output graph shows you the current classification boundary of the network based on its current (random) weights.
The orange background shows the items the network thinks the answer should be "no".
The blue background shows where the network thinks the answer should be "yes"

## 3.1. Training single layer networks (5 PTS)
Verify that the neural network can learn the linearly separable category by pressing the "play" button.  How did the weights change, and
how does their change make sense? (5 PTS)

### 3.1.1. Dataset 2 (4 PTS TOTAL)
Now choose the dataset from the top right corner (blue in the top left and bottom right, orange in the bottom left and top right).
- Try to interpret what these inputs "mean", the same way we said for the earlier case that yes meant "tasty and/or healthy = yes" and "not tasty and/or not healthy = no".
Feel free to change the definitions of the features to something other than healthy/tasty that makes sense. (3 PTS)
- Can the single layer network learn this grouping? Explain?  (3 PTS)

### 3.1.2. Dataset 3 (4 POINTS TOTAL)
Now choose the dataset from the top left corner (circle of blue in the middle, circle of orange around it).
- Try to interpret what these inputs "mean", the same way we said for the earlier case that yes meant "tasty and/or healthy = yes" and "not tasty and/or not healthy = no".
Feel free to change the definitions of the features to something other than healthy/tasty that makes sense.  (2 PTS)
- Can the single layer network learn this grouping? Explain?  (3 PTS)

## 3.2. Adding 1 hidden layer (9 POINTS TOTAL)
Stay on the circle dataset 3.
- Add a single hidden layer, with two hidden units. Train Dataset 3. Can it solve the problem now? Explain. (2 POINTS)
- Continue to add hidden units (just units, not more layers) until it can solve the problem. How many did you need? (2 POINTS)
- What pattern did you notice for when it can solve the problem? Hint: In class we talked about two interpretations of hidden layers and what they do. (2 POINTS)
- Given your explanation, how many hidden units do you think you should need to solve Dataset 2? Why (2 POINTS)
- Test your guess. Were you right? (1 POINT)
14
## 3.3. Spiral dataset (9 POINTS)
- Now select the spiral dataset. Can you come up with an interpretation of this dataset? (2 POINTS)
- Train this dataset until you find an architecture that can solve the problem. Report what you find. (4 POINTS)
Feel free to add more units or more layers. You can also change the input features.
This changes the input to some nonlinear transformation of X1 and X2. For example, X1^2 will be a positive input when 
X1 is either really positive or really negative, but not near 0. Sin(X1) will make X1 alternate between positive and negative values rhythmically.
- If you find a network that works, can you explain anything about why it succeeded? (3 POINTS)

## 3.4. Overfitting (9 POINTS)
Stay on your best trained version of the spiral dataset, and click the "show test data" button on the bottom right.
This shows additional data points that follow the rules of the dataset but which did not exist in the training set. This is 
what we call a "test set", and we can use it to see if the model was really learning the underlying rule, or was just overfitting to the specific items
in your dataset.
- How did the model do on the test items? (2 POINTS)
- Can you find anything systematic about test items that it succeeded on and failed on? (2 POINTS)
- What does the model's performance on these test items say about the debate between the connectionist approach and the symbolic approach? (5 POINtS)

