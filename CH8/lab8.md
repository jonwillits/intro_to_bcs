# Lab 8: Computational Mind

## 1. Algorithms (20 points total)

### 1.1. Sorting algorithm (10 PTS)
In your group, create a google spreadsheet that has the numbers 1 through 10 in a random order in cells A1 through A10. 
Leave columns B though E empty. 
In column F, write out precise steps that outline an algorithm a person can follow to sort the numbers into lowest to highest order 
In other words, step to take to end up with 1 in A1, and 10 in A10. 
Your algorithm should specify where to start, which numbers to compare, and which numbers to move in order to complete the sort. 

Your algorithm needs to follow these rules:
1. You can only compare two numbers at a time.
2. You can only move a number one spot (i.e., cell) at a time.
3. When comparing two numbers, assume that your algorithm will know which number is greater than or less than the other.
4. When writing a step of the algorithm, your algorithm should specify locations rather than general statements. For example, your starting step could say “Start in A2” but cannot say “Start with the highest number”.  

Paste your algorithm below.

### 1.2. Testing your algorithm (10 PTS)
Once you are done with a, turn to a group near you and swap algorithms. 
Take turns having each group follow the other group’s instructions, to see if your group can “break” their algorithm.
Don’t be generous; follow their instructions literally with as little interpretation as possible. 
After each group has gone, fix your algorithm if it needs fixing. 
In your lab report, note how well your algorithm worked, and if it broke, what were its problems and how did you fix it.

## 2. Algorithmic Complexity (40 points total)

### 2.1. Complexity Theory (10 points)
Complexity theory is the study of how complex algorithms are, and how efficient they can be in various circumstances. 
Let’s test the efficiency of your algorithm. 
First, each person in your group should put your numbers in different random orders in different columns on the worksheet. 
Second, each person should follow the steps of your algorithm, counting exactly how many individual steps and operations were needed to perform your algorithm. 
Compare your results and write them in here. 

### 2.2. Best and Worst Case? (10 PTS)
Is there a relationship between the structure of the data (e.g. ordering of numbers) and the number of steps needed for the sorting algorithm? Explain.
Is the number of steps your algorithm must take to sort the numbers different if the numbers are:
- in a random order?
- already sorted in the correct order?
- sorted in reverse order?

### 2.3. Big O Notation (10 PTS)
An algorithm’s complexity can be described in a more general way using a notion called “big O notation”. 
In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows. 
In general terms, an algorithm that has n inputs, and runs in some constant multiple of n steps, is said to be O(n), and runs in “linear” time. 
This is a good algorithm, because it scales slowly with input size. An algorithm with n inputs that runs in n2 steps, is said to be O(n2), and runs in quadratic time. 
That’s less good. An algorithm that is O(nc), where c is a really big number, will be really inefficient if n is bad. 
Other common big O scores are O(log(n)) and O(n*log(n)). 
What is your algorithm’s big O score? Show your work and specify the number of steps to solve and the number of inputs.

### 2.4. Explain the Big O Score (10 points)
Explain what factors you think contributed to your algorithm’s score. 
Be sure to discuss what you think the impact of your starting point, comparison method, and swap method was for your score.

## 3. Automata Theory (40 points total)

### 3.1. Finite state machines (15 points)
Finite state machine (FSM) can be used to describe the steps to get a snack from a vending machine. 
Draw a state transition diagram that includes a start state, transition states, and an end state for getting Cheetos or Oreos from a vending machine. 
Assume that the code to select Cheetos is B9, and the code for Oreos is A9. Both snacks cost $1. 

### 3.2. FSM end states (5 points)
What are the end states for this FSM? Note, your machine may not have any, if your machine resets. 

### 3.3. FSM transition rules (5 points)
What are the transition rules for each state (i.e. for each state, what happens for a given kind of input)? 

### 3.4. FSM vs. Pushdown automata (15 points total)
- An FSM cannot recognize palindromes such as racecar (a palindrome is the same read backwards or forwards). But a push-down stack can! Brainstorm what steps would be necessary to determine whether a word is a palindrome. List the steps you brainstormed for recognizing a palindrome below. (5 PTS)
- What steps might be particularly problematic for an FSM, but not a push-down automaton? (5 PTS)
- What is the most important difference between the FSM and the push-down automaton for recognizing palindromes? (5 PTS)
