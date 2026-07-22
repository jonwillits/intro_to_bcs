# Reinforcement Learning Lab
In this lab, you’ll use the game of rock–paper–scissors 
to explore how reinforcement learning works in theory, algorithms, and the brain. 
You’ll see how simple associations fail when outcomes are delayed, 
how prediction errors guide learning, and how habits and goals shape behavior.

### Rules of Rock–Paper–Scissors
Just in case you're not familiar with it, rock–paper–scissors is a simple two-player game. 
Each player simultaneously chooses one of three options:
- Rock (a closed fist)
- Paper (an open hand)
- Scissors (two fingers extended)

The winner is determined as follows:
- Rock beats Scissors (rock “crushes” scissors)
- Scissors beats Paper (scissors “cut” paper)
- Paper beats Rock (paper “covers” rock)
- If both players choose the same option, it is a tie.

The game is often played in repeated rounds, 
where players may try to predict or outguess their opponent’s next move.
Over repeated rounds, you can keep score of how many times you've won, lost, 
or tied (had the same move) as your opponent.

Although it looks like a children’s game, 
rock–paper–scissors is also a very simple model of real-world decision-making. 
It is a zero-sum game with three possible actions, 
where each action dominates one option but is vulnerable to another. 
This cyclical structure captures many everyday situations in which success depends 
not on finding a single “best” strategy, but on anticipating what others will 
do and adapting over time. 

For example, companies compete by adjusting prices against rivals, 
sports teams adjust plays in response to their opponents, and 
animals shift between strategies like fighting, fleeing, or signaling 
depending on context. 
In all these cases, the optimal choice changes depending on what others are doing, 
just as in rock–paper–scissors. That makes the game a useful miniature model 
for studying how learning, prediction, and adaptation work.

### Part 1: Classical and Operant Conditioning in RPS (15 pts)
Imagine you are learning to play RPS against a friend.
1.	Classical conditioning: Suppose you notice that whenever your opponent taps the table twice, 
they are about to throw “rock.” 
How does this fit the structure of classical conditioning (CS, US, CR)? (6 pts — 2 each)
2.	Operant conditioning: You win a round by throwing paper. 
How does this reinforce your behavior, and what behavior is reinforced? (5 pts)
3.	Explain why classical conditioning alone (pairing cues with moves) might not be enough to master RPS. (4 pts)

### Part 2: Hebb and the Temporal Credit Assignment Problem (15 pts)
Now suppose your opponent plays with a hidden rule: 
they always repeat their move from two rounds ago.
1.	Why would Hebbian learning (simple “things that fire together wire together”) have trouble learning this rule? (5 pts)
2.	Describe the temporal credit assignment problem in this scenario: which past move should be credited with leading to your win? (5 pts)
3.	Imagine you tried to learn by reinforcing every move you made before a win. What problems would this cause? (5 pts)

### Part 3: Prediction Error and Learning Algorithms (15 pts)
Suppose you’re now using an error-driven rule to learn.
1. Define prediction error in your own words. In RPS terms, what’s the prediction and what’s the error? (5 pts)
2. Was the outcome better than expected, worse than expected, or just as expected?
How would this affect what you predict or do the next time you face a similar situation? (5 pts)
3. Explain how temporal difference learning could help you learn longer-range patterns (like “two turns ago”) more efficiently than Hebb. (5 pts)

### Part 4: Brains, Dopamine, and Neuromodulators (20 pts)
Now imagine the RPS game is being played inside your brain.
1.	When you expect to win but lose, dopamine neurons dip. How does this change future action tendencies in the basal ganglia’s Go (D1) and No-Go (D2) pathways? (6 pts — 3 each)
2.	Why do researchers describe dopamine as a prediction error signal rather than just a “pleasure chemical”? (5 pts)
3.	What roles might serotonin (patience, avoidance) and norepinephrine (surprise, arousal) play while you’re deciding on your next RPS move? (6 pts — 3 each)
4.	Which brain structures best map onto the actor (choosing moves) and the critic (evaluating outcomes)? (3 pts)

### Part 5: Habits, Goals, and Addiction in RPS (15 pts)
Finally, let’s think about how repeated play might shape behavior.
1.	Suppose you always open with “rock,” even when it stops working.
Explain from a neuroscientific perspective, using the concepts we've discussed, how and why that might happen. (5 pts)
2.	Compare this to goal-directed play, where you adjust dynamically to your opponent’s last few moves.
Which brain system supports this? (5 pts)
3.	Addiction can be thought of as the reinforcement system being hijacked.
Imagine if a player received an artificial dopamine “burst” every time they threw “scissors,” no matter the outcome. 
What would happen to their strategy over time? (5 pts)