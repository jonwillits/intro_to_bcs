# Lab 9: Symbolic Computation

The first part of this lab will be based on downloading and running the rock-paper-scissors game. Download and play
for a few minutes to see how you do before we start the lab questions. You can find the game at:
[rock_paper_scissors.zip](rock_paper_scissors.zip). Unzip the directory and then run the run.py file in your terminal.
You may need to install the Pillow library for python if you havent already. using: "python -m pip install Pillow" on 
windows or "python3 -m pip install Pillow" on MacOS.

## 1. Initial Attempt to Win (14 PTS TOTAL)

### 1.1. Play the game (7 PTS)
Restart the game, and have each member in your group play for 30 rounds. Record how well each person did. (5 PTS)

### 1.2. Discuss Your Strategies (7 PTS)
Discuss with your group what strategy you might have been using. Did anybody find a successful strategy? 
Whose strategy was the best?

## 2. Algorithmic Comparison

### 2.1. Algorithmic Description (30 PTS)
In your group, try to identify three distinct algorithms you can follow to choose what move you make. 
Write each algorithm down as an explicit sequence of steps that someone else could follow, such that their move and your move would be identical
After your first algorithm, test your algorithm with someone from a different group (or with your TA) to make sure it is a clear set of rules.
- Algorithm 1 (10 PTS):
- Algorithm 2 (10 PTS):
- Algorithm 3 (10 PTS):

### 2.2. Algorithm Performance (6 PTS)
Reset your game. 
Have each person in your group follow one of the algorithms for 30 moves and record how well each algorithm performs.
- Algorithm 1 (2 PTS):
- Algorithm 2 (2 PTS):
- Algorithm 3 (2 PTS):

## 3. Identifying the AIs Strategy (35 PTS TOTAL)
Can you identify the AI’s strategy? Here are some hints:
- The AI is not cheating (i.e. it doesn’t know what you choose before it makes its choice).
- The AI is never doing anything random or probabilistic in any way.
Its choices are always purely deterministic based on what you had done on previous turns.

Use the scientific method to try to figure it out.
- Identify a hypothesis about the algorithm the AI is using, as a sequence of steps. (3 PTS)
- Explicitly state how you will test your hypothesis (1 PT).
- Test the hypothesis by using if it does what you think it should over a 30 round game (or less, if you need less to disprove the hypothesis). (1 PT)
- Summarize your conclusions. What was right or wrong about your hypothesis? (2 PTS)

Refine your hypothesis and go through the steps again. Do this for five hypotheses.

### 3.1. Hypothesis 1 (7 PTS):
- Hypothesis:
- Method:
- Results
- Conclusion

### 3.2. Hypothesis 2 (7 PTS):
- Hypothesis:
- Method:
- Results
- Conclusion

### 3.3. Hypothesis 3 (7 PTS):
- Hypothesis:
- Method:
- Results
- Conclusion

### 3.4. Hypothesis 4 (7 PTS):
- Hypothesis:
- Method:
- Results
- Conclusion

### 3.5. Hypothesis 5 (7 PTS):
- Hypothesis:
- Method:
- Results
- Conclusion

## 4. Explanation as Symbolic Computation (15 PTS TOTAL)
The AI’s strategy and your own strategies can be thought of as a symbolic computational system as described in this week’s reading. 
Choose the strategy that you hypothesized that most accurately predicted the AI’s behavior, and answer the following questions about that strategy.

### 4.1. What is a symbol (i.e., what is its definition according to the reading), and what was the set of specific symbols being used by the AI. In other words, what are all the pieces of information that needed to be represented by the program? (5 PTS)
### 4.2. What rules did the program have for manipulating those symbols? (5 PTS)
### 4.3. Define syntax and semantics, and explain in specific reference to this AI program, what those two words mean. What was the “syntax” of the symbolic computational program? What was the “semantics” of the program? (5 PTS)