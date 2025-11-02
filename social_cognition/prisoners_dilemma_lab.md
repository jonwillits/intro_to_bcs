# Social Cognition Lab: Theory of Mind, and Strategic Cooperation

### This Week’s Themes

This week, we explored how primate brains evolved to navigate complex social worlds.
Social cognition requires understanding other individuals 
— predicting their thoughts, intentions, and future behavior. 
This includes skills like imitation learning, perspective-taking, and theory of mind: 
the ability to represent what someone else knows, believes, or wants.

In this lab, you will explore these ideas by interacting with and analyzing simplified 
“social agents” in a repeated Prisoner’s Dilemma simulation. 
Even though the setting is simple, the strategic logic behind cooperation and competition 
is deeply relevant to real social behavior across species — including humans.

Why Games Help Us Study Social Minds

Primate social groups are full of conflicts, alliances, deception, trust, punishment, and cooperation.
Evolution favored brains that could:
- Track others’ past actions 
- Anticipate how others will respond 
- Learn from observation and imitation 
- Decide when to trust or defect 
- Adjust behavior based on social consequences

Game-theoretic scenarios like the Prisoner’s Dilemma let us explore these abilities in a controlled way. 
While real social life is far richer, this kind of model captures a core tension in social living.
Cooperating helps the group — but defection often benefits the individual in the short term. 
To succeed socially, brains must solve this tension.

### The Prisoner’s Dilemma (Quick Refresher)

In the Prisoner’s Dilemma, two agents simultaneously choose whether to:
- Cooperate (C)
- Defect (D)

|  | **Partner Cooperates**                  | **Partner Defects**                            |
|-------------------|-----------------------------------------|------------------------------------------------|
| **You Cooperate** | You both get a moderate reward          | You get the **sucker payoff** *(worst outcome)* |
| **You Defect**    | You get the **temptation payoff** *(best short-term outcome)* | You both get a low payoff |

Playing a prisoner's dilemma game for one turn thus encourages defection.
Since you do not know if they will cooperate or defect, it is in your self-interest to avoid being the sucker,
and to get the temptation payoff if you can get away with it.
But if your opponent also knows this, then they will also choose to defect, making mutual defection
the most likely outcome.
If only the two of you both cooperated, you would have both been better off!

In repeated interactions, cooperation _can_ emerge — if agents can remember which other agents are
likely to be cooperative and predict their behavior.

This turns the task into one requiring:
- Memory (What did others do before?)
- Theory of mind (What will they do next?)
- Learning (How should I adjust my strategy?)
- Social inference (Is someone trustworthy? Tit-for-tat? Exploitative?)

In this lab, you will:
1. Play the Prisoner’s Dilemma against AI agents using different social strategies.
2. Predict which strategies will succeed in different environments.
3. Observe how cooperation emerges (or collapses) in a population over generations.
4. Reflect on how this connects to social cognition in primates and humans.

### Running the lab
This week is another python program you need to download and install. To do this:
- Make sure you have python installed. If not, refer back to lab 1 instructions.
- Download [pd.zip](pd.zip)
- Unzip the file, it should create a folder called pd
- Inside the pd folder should be a file called pd.py. Run this file
  - For some of you, this was done by double-clicking
  - For others, you used your Terminal app (Mac) or Command Prompt app (Windows PC).
  Refer back to lab 1 for instructions.

## Part 1. Playing Against Individual Opponents (36 PTS)
In this section, you will play repeated Prisoner’s Dilemma games against different AI opponents.
Your goal is to discover how each opponent behaves and what strategy would work best against them.
Each opponent is following a particular strategy except one: Michael.
Michael is choosing his move randomly.

To play the game, select an opponent. Then choose COOPERATE or DEFECT.
Your opponent will also make a choice.
The result of the interaction will be shown on the right side of the screen,
following the rules in the payoff matrix the on the left side of the screen.
The ongoing tally of the points you and your opponents have received will show on the right.
The reset button will reset all the scores.
It will also erase the "memories" of your opponents about your play, if they have any.

### Important setup:
- Before beginning, make sure AI Noise = 0 in the simulation controls.
- Noise affects how reliably the AI follows its own strategy.
- The noise number is the probability their choice flips, after it is selected by their strategy.

### 1. Free Exploration (5 PTS)
Spend a few minutes playing against each AI opponent in the Play tab.
Try different behaviors — cooperate continually, defect early, cooperate then switch, etc.
As you play, keep notes on things that seem interesting or surprising.

Here are some light-touch guiding questions — you do not need to answer them formally yet:
- Does this opponent seem predictable or unpredictable? 
- Does it change behavior based on what you do? 
- Does it forgive you after you defect?
- Or does it “hold a grudge”?
	•	Does it ever defect first?
	•	Does it match your behavior, try to exploit you, or play completely randomly?

For each of the AIs (including Michael), write down three observations you had about your interactions.
Try to get a sense of each opponent like you would a real partner in a repeated interaction —
What kind of “personality” do they have? (5 PTS, 1 for each AI)

### 2. Identify Each Opponent’s Strategy (8 PTS)
Now that you’ve explored freely, test your mental model.
For each opponent except Michael:
- Based on your interactions, propose a hypothesis for that AI.
- Identify a set of move you could make that would test your hypothesis, and do it.
- How did your hypothesis fare? 
- If you are confident you were correct, move on. But if your hypothesis was incorrect,
repeat the process at least two times until you think you've figured that AI out or tried at least three times.
- Report back your hypotheses and how you tested them, and your final conclusions. (8 PTS, 2 for each AI)

### 3. Reason About Counter-Strategies (15 PTS)
Once you are done with part 2, you can view the AI descriptions to see an exact report of their strategies.
How did you do?

Now imagine you could design a perfect strategy to play against each AI.
For each AI (including Michael), describe:
- What would your best strategy be? (1 PT PER AI)
- Why would it work?  (1 PT PER AI)
- How well would it work? Would it work perfectly, or are there trade-offs?  (1 PT PER AI)

Some guiding thoughts to help you think strategically:
	•	Is it ever safe to always cooperate?
	•	When is defection worth the cost?
	•	How does the history of interactions matter?
	•	Can being “too clever” sometimes backfire?

## Part 2. Evolutionarily Stable Strategies (24 PTS)
In this section, you will shift from playing as an individual to observing how strategies compete in a population.

In biological or cultural evolution, an Evolutionarily Stable Strategy (ESS) is a strategy that, 
once common in a population, cannot be invaded by a rare alternative strategy — because it performs well against itself 
and against outsiders.

In social species (including primates and humans), cooperation can evolve 
— but only if it is stable against exploitation.

Here you will observe:
1. Which strategies thrive when they compete head-to-head.
2. Why some “winning” strategies are not stable.
3. How added noise changes which strategies succeed.

### Setup reminder:
- In this part, do not play manually.
- You will be using the "Tournament" tab at the top.
- Make sure that "AI Noise" is set to 0.

### 2.1 Predict Without Noise (8 pts)
This tab instantiates a round-robin tournament where each AI will play against each other AI's strategy,
including their own.

The results table will show you how many points each AI got against each other AI.

Prediction Task (4 pts)
Answer before running:
	1.	Which strategy do you predict will score highest overall? Why?
	2.	Which strategy do you predict will do worst? Why?
	3.	Do you think any strategy will tie? If so, which ones and why?
	4.	Which strategy do you think is evolutionarily stable in this environment? Explain.

Use what you learned in Part 1 — especially about reciprocity and punishment.

Now run the tournament.

Observation Task (2 pts)
Record:
	•	Final ranking of strategies (best → worst)
	•	Any surprising results

Reflection (2 pts)
Did the outcome match your prediction?
If not, what did you learn?

### 2.2 Add Noise (8 pts)

Now we introduce noise — randomness in action choice.

Noise is a way of modeling:
- Mistakes
- Miscommunication
- Perfect perception 
- “Emotional spur-of-the-moment” decisions
- Strategic attempts to be less predictable

Even smart strategies suffer if they cannot handle occasional errors.

Before running again: set
	•	AI Noise = 0.20


How do you think noise will change the results? Answer:
1. Which strategy will benefit most from noise? Why? (1 PT)
2. Which strategy will be harmed the most? Why? (1 PT)
3. Will the previous “best” strategy stay best? Or will rankings shift? (1 PT)

Run the tournament again.

Observation (2 pts)
Record:
- Final ranking (best → worst)
- Scores changed vs. before

Reflection (3 pts)

Answer:
	•	What changed, and why?
	•	Did Tit-for-Tat still perform well? If not, why might retaliation be risky in a noisy world?
	•	Which strategy appears most robust to noise?

In noisy environments, strategies that are too punitive or too trusting both suffer.
Real social environments are noisy — perception and communication are imperfect —
so stable cooperation must tolerate mistakes.

### 2.3 ESS Takeaways (8 pts, 2 PTS EACH)

Answer briefly:
	1.	What makes a strategy "evolutionarily stable" in repeated social interactions?
	2.	Why is “always defect” not stable in a repeated-interaction world?
	3.	Why is “nice but retaliatory” (like Tit-for-Tat) powerful without noise — but vulnerable with noise?
	4.	What real-world social behaviors resemble Tit-for-Tat?

## Evolution in a Social Ecology (37 PTS)

In the real world — and in primate societies — individuals do not interact randomly with the entire population.
They live in local neighborhoods:
- Families and kin groups 
- Stable alliances 
- Preferred social partners 
- Physical proximity (troops, troops, villages, dorms…)

These local structures change how cooperation evolves.
A strategy that works well in a "one-on-one" scenario might work less well complex interactions.
A strategy that cannot dominate a whole population might still survive in clusters, 
as long as cooperative partners remain near each other and defend against defectors.

In this section, you will explore these ideas using an evolution simulation, in the Simulation tab.

### Understanding the Evolution Simulation
In this part of the lab, you will explore how cooperation and competition evolve 
in a population of agents who repeatedly interact with their neighbors.

This simulation builds on the Prisoner’s Dilemma game, 
but instead of two individuals playing many rounds, 
an entire grid of agents plays many local games at once.

Each colored square in the grid represents an agent following a strategy 
(e.g., Always Cooperate, Tit-for-Tat, Always Defect, Random).
When the simulation begins, these four are assigned randomly to different squares.

**How the World Works**
- Each agent has up to four neighbors (up, down, left, right, unless they are on an edge or corner). 
- Each “turn,” every agent plays several rounds of the Prisoner’s Dilemma against each neighbor.
- Agents earn points based on the payoff matrix (cooperators can thrive together; defectors get ahead only in the short run).

**After Each Turn: Evolution Happens**
Once everyone has played, the simulation goes through three phases:
- _Competition_: Agents play repeated Prisoner’s Dilemma with neighbors and earn scores.
This represents social interactions and learning about partners.
- _Selection_: The worst-performing agents die. Low-fitness strategies disappear
- _Reproduction_: Empty spots are filled by copies of nearby successful agents.
One of the neighbors is randomly selected, or if no neighbors are alive, one of the four starting strategies is randomly selected. 
Successful strategies thus spread to neighboring squares.

This cycle repeats over generations, letting us see which strategies survive and spread.

### Why This is Interesting
Unlike the tournament (where everyone plays everyone), this world is local and spatial:
- Agents mostly interact with neighbors, not strangers.
- Clusters of cooperation can form — like “friendship circles,” families, or primate troops.
- Defectors can invade, but they also risk collapsing if surrounded by other defectors.

This models social ecology in primates and humans.
Real social groups evolve patterns of trust, betrayal, punishment, alliance, and forgiveness 
— not in isolation, but in networks.

### Simulation Controls
You will see buttons labeled:
- _Reset_: Creates a new random population
- _Compete/Selection/Reproduce_: A button that lets you go through each stage of the evolutionary algorithm step-by-step.
During competition, everyone plays PD with neighbors and earns points.
During selection, lowest-scoring individuals are removed.
During reproduction, neighboring strategies repopulate empty spaces.
- _Take Turn_: Runs all three steps once (Compete → Selection → Reproduce) in one step.
- _Run/Pause_: Automatically keeps stepping through turns.

You will also see controls to change:
- Rounds per Turn (how long agents interact before selection)
- Proportion to Keep (how harsh selection is)
- AI Noise (probability an agent “misplays”, mistakes the partner’s behavior, or randomly changes their move)

Important: In evolution, randomness is not noise — it is part of the ecology.
Noise models miscommunication, mistakes, misunderstandings, and messy real social life.

Once you understand the mechanics, 
move on to the next section where you will predict, run, and analyze the evolutionary outcomes.

### Setup
Go to the Simulation tab. Set:
- Rounds per Turn: 10
- Proportion to Keep: 0.50
- AI Noise: 0

Then click Reset.  This starts a new “generation 0” in a population of mixed strategies.

### 3.1 Predict the Ecology (6 pts)

Before pressing anything else, answer the following questions:
1. Which strategies do you predict will clump together into clusters? Why? (2 PTS)
2. Which strategies will struggle to form stable groups? Why? (2 PTS)
3. Do you expect any strategy to take over the whole map? If so, which one? If not, why not? (2 PTS)

Hint: Think about what happened in the tournament — then imagine many small tournaments happening at once, 
and winners reproducing locally.

### 3.2 Run & Observe (10 pts, 0.5 pts per cell in the 5x4 table described below)
Now run the simulation slowly, one step at a time, by pressing the "Compete" button:
- After pressing Compete, observe the scores of each agent.
- Then press the "Selection" button, and observe the selection process.
- Then press the "Reproduce" button, and observe the reproduction process.

Record snapshots at generations 0, 5, 10, and 20. For each snapshot, fill in:
- Generation #
- Which strategies dominate?
- Do cooperators form clusters?
- Any invasion events?
- Notes / surprises

### 3.3 Cooperative Pockets vs. Runaway Defection (6 pts)
Now just press the "Run" button and let the simulation go for a while. Watch how regions shift. 
Try to use the simulation to answer the following questions:
- Do cooperative clusters form? What conditions let cooperators do well? (1 PTS)
- Do defectors invade them? What conditions let defectors do well? (1 PTS)
- Can cooperators fight defectors off? (1 PT)
- Do defectors ever collapse because they exploit each other? (1 PT)
- Explain why cooperation sometimes survives locally even if it might lose globally. (1 PT)
- In your own words, what is the “ecological advantage” of cooperation in social species? (1 PT)

# 3.4 Add Noise (3 pts)
Now set AI Noise = 0.20 and press Reset, then repeat ~10 generations.

Questions:
1. Does noise weaken cooperative clusters, strengthen them, or both? Explain. (1 PTS)
2. Do you see more churn and instability? (1 PT)
3. How does noise affect defectors — do they spread more or less easily? Explain (1 PTS)

Hint: In real primate groups, misinterpreting a partner’s behavior can break alliances —
but never forgiving mistakes is also costly.

# 3.6 Key Takeaways (4 pts)
Answer briefly:
1. Why can cooperation evolve in local neighborhoods even if it wouldn’t dominate globally?
2. Why is it dangerous for defectors to cluster together?
3. How does occasional forgiveness help real social groups avoid destructive cycles?
4. We have been talking about this simulation as representing biological evolution.
But it could just as easily be used to model cultural evolution and imitation. Explain how that could be so.