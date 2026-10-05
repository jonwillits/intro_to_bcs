# Lab 7

Lab 5 ended with an animal whose weights could change by themselves, and with one thing it still could not do. Its single interneuron drew a single line. Module 4 said that no setting of one unit's weights computes exclusive or, and Lab 5's learning rule could not get there either, because a rule can only move the weights that exist.

This week the animal is a fish, and it has a layer of units between its receptors and its output. The fish holds its place in a murky stream, facing into the current. Smells drift down to it one at a time. Each smell is a pair of numbers, the responses of two kinds of receptor. The fish's network turns that pair into **evidence**, the evidence is compared with a **criterion**, and the fish either darts to cover or stays to feed. Then the outcome arrives, whatever the fish did: an eel lunges, or a harmless sucker drifts past. With learning switched on, every weight changes a little by Lab 5's rule.

One idea runs through every part of the lab. **How well the fish can tell an eel from a sucker lives in its weights. Where it draws the line between fleeing and staying lives in its chemistry.** The reading calls the first *sensitivity* and the second the *criterion*, and says they are different kinds of thing to change. In Part 1 one unit draws one line. In Part 2 you move the criterion and the sensitivity separately, and then diagnose four fish. In Part 3 you build a hidden layer by hand and then hand it to a rule. In Part 4 you solve one problem three ways. In Part 5 the fish learns the individuals in a small pool too well, and then is taken somewhere its training never covered. The closer brings in a new predator.

This lab is longer than the others: plan on about two hours. Almost none of that is waiting.

## Part 0: Opening the Simulation (≈5 minutes)

1. Open the simulation in your web browser: [Fish](https://jonwillits.github.io/bcogapp/#/m07-fish). It runs in any modern browser, and there is nothing to install.
2. Download the lab report Microsoft Word document. It is available here: [Lab 7 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/pattern_recognition/fish_lab/fish_lab_report.docx) This document is what you will turn in to the course website.

### The stream

The fish faces up the screen, and the pale specks moving down the screen are the current. A smell arrives as a loose cloud of colored specks carried on that current: **pink specks for receptor A's response, and green specks for receptor B's**. The more specks of a color, the stronger that response. Right behind the smell comes a pale morsel of food.

When the smell reaches the fish, the fish does one of two things. It **darts to cover**, into the weed behind the large rock at the right, or it **stays**. Then the outcome arrives. An eel lunges to the place where the fish was, or a sucker is carried harmlessly past. A red ring means the fish was struck. A green ring means it fed.

The block of text at the top of the stream reports each encounter, one fact to a line: the count, the smell, the evidence and the criterion, what the fish did, what was there, and which of the reading's four outcomes that makes it (*Hit*, *Miss*, *False alarm* or *Correct rejection*).

### Running it

One encounter takes about four seconds. That is right for watching and far too slow for learning, which takes hundreds or thousands of encounters. So beside the play button there are two buttons: **Skip ahead 100 encounters** and **Skip ahead 1,000 encounters**. They run the stream forward without drawing it. Nothing is left out, presses add up, and a skip takes about a second. **Whenever a step says "run 1,000 encounters", press Skip ahead.** Watch live only where a step asks you to.

**Every scenario loads with learning switched off.** The switch, **Learning on**, is at the top of the Learning tab. If you skip ahead and nothing has changed, check it first.

**Reset** starts the run again from the same seed, with every control where you left it and the weights back where the run started. **New seed** gives a different stream, and, where the starting weights are drawn at random, different starting weights. The scene opens on a random seed, so your numbers will be close to your neighbor's and not identical.

### The five tabs

- **World** has the **Scenario** menu, with one entry for each part of this lab, and on the right a list of what is in the stream and a scorecard.
- **Network** has every weight, and on the right the lab's main instrument, **the feature space**: receptor A across, receptor B up, one dot for each recent encounter. Dots are blue where the outcome happened (an eel was there) and orange where it did not. The shading is the output unit's prediction for every possible smell, and **the white line is the decision boundary**. Below it are a diagram of the network and **the learning curve**, which plots percent wrong against encounters.
- **Learning** has the switch, the learning rate, the choice of who sets the hidden weights, and the rule's arithmetic with live numbers.
- **Decision** has the criterion, two of Lab 4's modulators, and the signal detection instruments.
- **Fish** loads the animals you will diagnose in Part 2.

## Part 1: One Line Will Do (≈12 minutes)

### Goal

The reading's §7.2.2 turns the fish's problem into a picture: every smell is a point in a feature space, and telling an eel from a sucker means dividing that space. §7.2.3 says the simplest thing that can divide it is one unit, which draws one straight line. Draw that line by hand, and then let the rule draw it.

### Instructions and What to Record

**Step 1 — The fish before it has any weights.** On the World tab, load **Part 1 — One line will do**. This fish has no hidden units. Its two receptors connect straight to its output unit, and both weights are zero. Watch ten encounters and read the text block for each one.

- **Q1.** What did the fish do on every encounter? The verdict is taken by comparing the evidence with the criterion, and the fish darts when the evidence is at or above it. Read both numbers from the text block and explain what you saw. Which two of the four outcomes occurred, and which two never did? Would you call this fish good at detecting eels?

**Step 2 — Draw the line by hand.** Open the Network tab. On the feature space, the encounters you watched have landed in two clouds. On the left, under **The output unit**, set **weight b₁ — from receptor A**, **weight b₂ — from receptor B** and **baseline b₀** until the white line runs between the two clouds, with the blue cloud on the blue side. Then change one weight and watch the line. Change the baseline and watch it again. Finally, open the Decision tab, move the **criterion**, and look at the line once more. Put the criterion back at 0.

- **Q2.** Where does each cloud sit: which receptor responds more strongly to an eel, and which to a sucker? Report the two weights and the baseline you settled on, and the percent wrong on the test set that the learning curve prints. What is the sign of each weight, and why does that make sense for these two clouds?
- **Q3.** What did changing a weight do to the line? What did changing the baseline do? What did moving the criterion do? The reading's §7.2.3 describes all three in one sentence about turning and sliding, and says which part of a unit is its evidence and which is its criterion. Say which is which. Then say what *linear separability* means, from §7.2.2, and whether these two clouds have it.

**Step 3 — Let the rule draw it.** On the Network tab, press **Restore the wiring this scenario started with**. On the Learning tab, switch **Learning on**. Press **Skip ahead 100 encounters** three times, and after each press record the weights and the test set's percent wrong.

| After | Weight from A | Weight from B | Baseline | Test set, percent wrong |
|---|---|---|---|---|
| 100 encounters | | | | |
| 200 encounters | | | | |
| 300 encounters | | | | |

- **Q4.** Report your table. Did the rule arrive at the same numbers you chose by hand? Did it arrive at a line that does the same job? Explain how two different sets of weights can both be right. Then run 700 more encounters and look at the weights again. They are still growing, although the test set was already nearly perfect. Why would a rule keep moving weights that already get every answer right? Look at the shading on either side of the line for a hint.
- **Q5.** On the Learning tab, **The arithmetic** prints Φ = a − p for the output unit, and a line under it says where the target came from. Copy that line out. This is Lab 5's Prediction setting, unchanged. What is *a* here, what is *p*, and when was *p* made? The reading's §7.2.7 says a network's target "need not come from a teacher". Where does this fish's target come from?

**Step 4 — When the clouds overlap.** On the World tab, set **How much smells vary** to 0.15, press **Reset**, and run 1,000 encounters. Record the test set's percent wrong. Do the same at 0.20. Set it back to 0.06 when you are done.

| How much smells vary | Test set, percent wrong after 1,000 encounters |
|---|---|
| 0.06 (from Step 3) | |
| 0.15 | |
| 0.20 | |

- **Q6.** Report your table. Look at the feature space at 0.20. Is there any straight line that would put every eel on one side and every sucker on the other? Is there any curved one? The rule is working exactly as it did in Step 3. So what is the source of the remaining errors, and could more training remove them? The reading's §7.1.4 opens with the sentence that explains it.

## Part 2: Jumpy or Blind? (≈28 minutes)

### Goal

When the two clouds overlap, some errors are unavoidable, and the fish has a choice about which kind to make. The reading's §7.1.4 separates two things that percent correct mixes together: **sensitivity**, measured as *d′*, and the **criterion**. Move each one by itself, find the criterion that suits this fish's life, and then work out what is wrong with four fish from their behavior alone.

### Instructions and What to Record

**Step 1 — Move the criterion.** Load **Part 2 — Jumpy or blind?** This is the same stream with smells that vary more, and the fish arrives already trained: its weights are locked, and learning is locked off. Open the Decision tab. **The evidence** shows two histograms on one axis, the evidence the fish's output unit gives 1,000 encounters with an eel and 1,000 without, with the criterion as a white line. **The scorecard** below it counts the four outcomes on those 2,000 encounters. Record the scorecard with the **criterion** at 0, then at −0.50, then at +0.50.

| Criterion | Hits | Misses | False alarms | Correct rejections | Hit rate | False-alarm rate | Percent correct | d′ |
|---|---|---|---|---|---|---|---|---|
| 0 | | | | | | | | |
| −0.50 | | | | | | | | |
| +0.50 | | | | | | | | |

- **Q7.** Report your table. When you lowered the criterion, which two counts went up together? Why can the fish not have more hits without more false alarms? Now say what did *not* move: look at the two histograms, at d′, and at the white line on the Network tab's feature space. The reading's §7.1.4 says moving the criterion "leaves sensitivity exactly where it was", and gives the reason. What is the reason?

**Step 2 — Move it with chemistry.** Put the criterion back at 0. Raise **arousal and vigilance** to 3, and read the line **effective criterion** and the scorecard. Compare them with your −0.50 row. Put arousal back at 1 and lower **satiety and tone** to 0.4. Then open the Network tab and look at the fish's weights. Put both modulators back at 1.

- **Q8.** What did each modulator do to the effective criterion, and to the four counts? Did either one change a weight, a histogram, or d′? In Lab 4 these same two modulators changed how readily a worm reversed, with no change to its wiring. The reading's §7.3.6 says what the criterion's physical counterpart is in a neuron, and what changes it. Say what it is. Then say what would have to change in this fish for its d′ to change.

**Step 3 — The best criterion.** The fish's criterion should depend on what each outcome is worth to it. On the Decision tab, under **What each outcome is worth**, the menu is set to **The fish’s stakes**: a correct rejection is a mouthful of food (+1), a false alarm or a hit earns nothing, and a miss is a strike (−20). The scorecard's last line, **Energy per 100 encounters**, applies those stakes to the four counts. Move the criterion to each value in the table and record that number. Then switch the menu to **The reading’s example**, which is §7.1.4's worked example (a false alarm costs 15 and a miss costs 1), and do it again.

| Criterion | Energy per 100, the fish's stakes | Energy per 100, the reading's example |
|---|---|---|
| −1.50 | | |
| −1.00 | | |
| −0.75 | | |
| −0.50 | | |
| 0 | | |
| +0.50 | | |
| +0.75 | | |
| +1.00 | | |

- **Q9.** Report your table. Which criterion earned the most under each set of stakes? The By hand box calls a criterion below zero *liberal* and one above zero *conservative*. Which is best for the fish, and which for the reading's example, and why does each make sense? Under the fish's stakes, compare percent correct at a criterion of 0 with percent correct at the criterion that earns the most. The reading says accuracy is "the wrong measure" in a situation like this. Use your numbers to say why. (The **Score this criterion** button runs 500 fresh encounters and plots the result. Try it a few times at one criterion. Why do its points scatter when the scorecard's number does not?)
- **Q10.** Switch back to **The fish’s stakes** and set **How often an eel is upstream** to 80%. Find the criterion that now earns the most. Then set it to 20% and find it again. Which way did the best criterion move as eels became more common, and why? Set it back to 50% and the criterion back to 0.

**Step 4 — Four fish.** Open the Fish tab. **Healthy** is the fish you have been using. **F1** to **F4** are four more, each in the same stream, facing the same 2,000 test encounters. **Each differs from the healthy fish in exactly one way.** Until you press **Reveal**, their weights, their criterion, their chemistry and their histograms are hidden. What you have is what an experimenter would have: the four counts.

For each fish, press its button and copy **The four counts**. Type them into the **By hand** box beside them, which works out the hit rate, the false-alarm rate, d′ and the criterion's position from four counts, by the formula it prints. Then, **before you press Reveal**, write down what you think is different about that fish: is its criterion too low, is its criterion too high, or is its sensitivity poor? Do all four before you reveal any of them.

| Fish | Hits | Misses | False alarms | Correct rejections | Percent correct | d′ | Criterion | Your diagnosis, before Reveal |
|---|---|---|---|---|---|---|---|---|
| Healthy | | | | | | | | — |
| F1 | | | | | | | | |
| F2 | | | | | | | | |
| F3 | | | | | | | | |
| F4 | | | | | | | | |

- **Q11.** Report your table and your four diagnoses. Then press **Reveal** on each fish and say what the one change was, and whether you had it right.
- **Q12.** F2 and F3 both miss many eels, and their percent correct is nearly the same. Which number in your table tells them apart, and how? One of these fish could be put right by a meal. The other could not be put right by any change of criterion. Say which is which, and what the second one would need. This is the difference in the lab's title.
- **Q13.** After Reveal, look at F3 on the Network tab. Its weights are as large as the healthy fish's. What is different about them, and what has that done to the white line and to the two histograms? The reading's §7.2.4 describes an expert whose space has been "stretched" along the dimension that matters. In those terms, what has gone wrong in F3?
- **Q14.** F1 and F4 give nearly the same counts. Reveal says F1's fault lies in its chemistry, and that F4 is "not broken". Load F4 and switch on **This fish’s stream**, and read its **Energy per 100 encounters** on the Decision tab. Then load **Healthy**, set **How often an eel is upstream** to 80% by hand, and read the healthy fish's. Which fish does better in that stream? So was F4's criterion a fault? What does this say about calling an animal "too jumpy" from its behavior alone?
- **Q15.** The reading's §7.1.4 describes two people taking a face memory test. Type the first person's counts into the By hand box: 42 hits, 8 misses, 8 false alarms, 42 correct rejections. Then the second's: 49, 1, 25, 25. Record d′, the criterion and percent correct for each. The reading says both have a d′ of about 2.0. What do you get for each? What differs between the two people, and which of the four fish does the second person most resemble?

## Part 3: Ripe or Rotting (≈30 minutes)

### Goal

The reading's §7.1.6 describes fruit that either of two smells alone marks as ripe, and both together mark as rotting. No single smell says anything about it. See one unit fail at this, build the reading's hidden layer by hand, and then find out what a rule needs in order to build one itself.

### Instructions and What to Record

**Step 1 — One unit fails.** Load **Part 3 — Ripe or rotting**. The verdict now goes to **eat**, and the outcome the fish predicts is that the fruit nourishes. There are four kinds of thing in the stream, one in each corner of the feature space. Switch **Learning on** and run 1,000 encounters, twice. After each, look at the white line and read the test set's percent wrong. Then switch on **Show each kind’s average (its prototype)**, which marks the average smell of the things that nourish and the average smell of the things that do not.

- **Q16.** What did the line do, and where did the percent wrong end up after each 1,000 encounters? Module 4 said a single unit cannot compute exclusive or. Use the feature space to say why: where are the two blue clouds, and where would one line have to go? Then look at the two crosses. Where are they? The reading's §7.2.5 says what follows for any model that keeps one prototype for each category. What follows?

**Step 2 — Build the hidden layer by hand.** Switch learning off. On the Network tab, set **Number of hidden units** to 2 and the **activation function** to **threshold function (a hard step)**. Then set these nine numbers, which are the reading's network from §7.2.6. Open **Hidden unit 1** and **Hidden unit 2** on the left to find their sliders.

| Unit | Weight from the first input | Weight from the second input | Baseline b₀ |
|---|---|---|---|
| Hidden unit 1 (from receptors A and B) | 1 | 1 | −0.5 |
| Hidden unit 2 (from receptors A and B) | −1 | −1 | 1.5 |
| The output unit (from hidden units 1 and 2) | 1 | 1 | −1.5 |

Look at the feature space, at the two small squares on **the diagram** (each shows one hidden unit's own output over the whole smell space; point at one to shade the feature space with it), and at **the hidden-activity space** below, which draws every encounter by the output of the two hidden units instead of by the two receptors.

- **Q17.** Fill in the table below for the four typical smells, working each unit out by hand: a unit fires (1) when its weighted sum plus its baseline is at or above zero. Check your last column against what the fish does. Which logical function from Lab 4 does each of the three units compute?

| Smell (A, B) | What it is | Hidden unit 1 | Hidden unit 2 | Output unit | Eat? |
|---|---|---|---|---|---|
| (0.15, 0.15) | twig or leaf | | | | |
| (0.85, 0.15) | ripe fruit, first kind | | | | |
| (0.15, 0.85) | ripe fruit, second kind | | | | |
| (0.85, 0.85) | rotting fruit | | | | |

- **Q18.** The reading's §7.2.6 reads this network in three ways. You have just done the first. For the second: describe the feature space now. How many white lines are there, whose are they, and what shape is the region where the fish eats? For the third: in the hidden-activity space, where does each of the four kinds land, and which two land together? How many lines does the output unit need in *that* space? The reading says the three readings "describe one fact". What is the fact?

**Step 3 — Hand it to the rule.** On the Learning tab, under **Who sets the hidden weights?**, choose **Pass the error back**. Your hand-built network is kept. Leave the activation function on the threshold function, switch **Learning on**, and run 1,000 encounters. Watch the hidden units' sliders on the Network tab, and under **The arithmetic** on the Learning tab read the lines for **Hidden unit 1**, especially **its slope, f′(net)**. Then, on the Network tab, change the activation function to **sigmoid function (an S-shaped curve)**; on the Learning tab press **Start from new random weights**; and run 2,000 encounters.

- **Q19.** With the threshold function, did any hidden weight move? What did the slope read, and what did the hidden unit's Φ read? With the sigmoid, what changed? The reading's §7.2.7 says each unit's share of the error is "scaled by how much its output would change if its input changed". Use that phrase to explain both results. Why can a hard step not pass an error back?
- **Q20.** From the Learning tab, with the sigmoid running, copy the four lines under **Hidden unit 1** that end in *Φ = slope · weight · output's Φ*, with their numbers. The output unit's Φ comes from the world: the outcome minus the prediction. Where does a hidden unit's Φ come from? The reading names the problem this solves, and the lab prints the name on this panel. Give the name, and say how it differs from the credit problem of Lab 5's corridor.

**Step 4 — How many hidden units?** Stay on **Pass the error back** with the sigmoid and learning on. For each row of the table, set **Number of hidden units**, which starts a new network from random weights. Run 1,000 encounters, and a second 1,000 if the test set is not yet at 5% wrong or better. Record what the test set reached. Then press **New seed** and do it again, three seeds for each row.

| Hidden units | Seed 1: test set, percent wrong | Seed 2 | Seed 3 |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 4 | | | |
| 6 | | | |

- **Q21.** Report your table. Which sizes never solved it, which solved it some of the time, and which every time? A run with two hidden units that sticks has not broken; it has settled somewhere that the rule cannot improve from. Why would more hidden units make that less likely? (If none of your two-unit runs stuck, or none solved it, press New seed a few more times until you have seen both.)
- **Q22.** Take a two-unit run that solved the problem and look at the hidden-activity space. Which two kinds landed together? Compare with a neighbor's. In some runs it is the two ripe fruits, as in the network you built by hand. In others it is the twig and the rotting fruit. Explain why *either* arrangement lets the output unit finish the job with one line. What does this tell you about whether a problem has one right hidden layer?

**Step 5 — A built-in receptor.** Set **Number of hidden units** back to 0. Under **Built-in receptors** on the Network tab, switch on **Both together: x₁ · x₂**. With learning on, run 300 encounters. Then switch it off, switch on **Distance from the ideal strength** instead, and run 1,000.

- **Q23.** What happened with each built-in receptor, with no hidden layer at all? Look at the diagram: what has the fish gained? The reading's §7.2.2 says that with the right features "the hard problems of §7.1.6 become easy", and describes exactly this third input. Explain in terms of the feature space why one unit can now do it. Why did the other receptor not help?

## Part 4: Built In, Wired at Random, or Learned (≈22 minutes)

### Goal

The reading's §7.2.2 ends by saying the features a hard problem needs "can be learned, wired at random, or built in". Solve one problem all three ways, and find out what each way costs.

### Instructions and What to Record

**Step 1 — Built in.** Load **Part 4 — Built in, wired at random, or learned**. Fruit now arrives with smells all over the feature space, and it nourishes only when both receptors respond at about the right strength: the blue dots form a disk in the middle. This is the reading's island. With no hidden units, switch **Learning on** and run 1,000 encounters. Then switch on **Distance from the ideal strength**, press **Skip ahead 100 encounters** until the test set is at 5% wrong or better, and count the presses. Then switch it off, switch on **Both together** instead, and run 1,000.

- **Q24.** Report the test set's percent wrong with no built-in receptor, how many encounters *Distance from the ideal strength* needed, and what *Both together* managed. What shape is the decision boundary when the fish succeeds? In Part 3 these two receptors did the opposite: one solved the problem and the other did nothing. The reading's §7.2.9 calls an assumption built into a system "a bet about the task". What is each receptor a bet on?

**Step 2 — Wired at random.** Switch both built-in receptors off. On the Learning tab choose **Fixed at random**. The hidden weights are now drawn once and never change, and only the output unit learns. For each row, set **Number of hidden units, fixed at random** as near to the number as the slider allows, run 1,000 encounters with learning on, and record the test set's percent wrong. Then switch on **Sparse: about one unit in ten active at once** and do each again.

| Hidden units, fixed at random | Percent wrong, not sparse | Percent wrong, sparse |
|---|---|---|
| 2 | | |
| 10 | | |
| 50 | | |
| 200 | | |

- **Q25.** Report your table. No hidden weight was learned in any of these runs. So how can 200 random units solve a problem that 2 random units cannot? The reading's §7.2.7 names this idea and says what it costs. Give the name and the cost. What did *Sparse* do to your numbers, and what does the line under the diagram, *For the smell now, … of 200 hidden units are active*, read with it on and with it off?
- **Q26.** The **Fixed at random** card names an animal whose brain is wired like this, and then says something it does not claim. Copy both sentences. Why does the lab bother with the second one?

**Step 3 — Learned.** On the Learning tab choose **Pass the error back**. For each row, set **Number of hidden units** on the Network tab, and press **Skip ahead 1,000 encounters** up to five times, stopping when the test set reaches 5% wrong or better. Record how many encounters that took, or the percent wrong after 5,000 if it never got there, and describe the boundary.

| Hidden units | Encounters to reach 5% wrong (or percent wrong after 5,000) | Shape of the boundary |
|---|---|---|
| 3 | | |
| 4 | | |
| 6 | | |

- **Q27.** Report your table. What shape can three units draw around a disk, and why is that the best three lines can do? Which size was the smallest that solved it for you? This route may fail on a given seed where a neighbor's succeeds; compare.
- **Q28.** You have now solved the island three ways. Fill in the table, and then answer: which route was fastest, which needed the fewest units, and which needed nothing to be known about the problem in advance? The reading's §7.2.14 lists ways that knowledge can be built into a pattern recognition system before any learning starts, and gives two reasons that building *everything* in is a bad idea. Which of its ways is each of your first two routes? Give the two reasons, and say which of your three routes escapes them.

| Route | Hidden units used | Encounters needed | What had to be in place before learning began |
|---|---|---|---|
| Built in: *Distance from the ideal strength* | | | |
| Wired at random: 50 sparse units | | | |
| Learned: *Pass the error back* | | | |

## Part 5: The Eels It Has Smelled (≈22 minutes)

### Goal

A network's score on the examples it learned from is not the score that matters. The reading's §7.2.12 separates a training set from a test set, and then separates both from inputs unlike anything in training. Produce each of those two failures, and try two repairs.

### Instructions and What to Record

**Step 1 — A small pool.** Load **Part 5a — The eels it has smelled**. The fish now lives in a small pool with six residents, three eels and three suckers. Each individual has a smell of its own, and the fish encounters the same six again and again. The fish has eight hidden units, and the rule sets all of its weights. Switch **Learning on** and press **Skip ahead 1,000 encounters** five times. The learning curve has two lines. The line labeled **recent training encounters** is percent wrong on the last 300 encounters as they arrived. The **test set** line is percent wrong on 200 encounters with eels and suckers the fish has never smelled. Record both after 1,000, 3,000 and 5,000. Then switch on **Show the test set**.

| After | Training, percent wrong | Test set, percent wrong | Encounters per individual, on average |
|---|---|---|---|
| 1,000 encounters | | | |
| 3,000 encounters | | | |
| 5,000 encounters | | | |

- **Q29.** Report your table. Which line ended lower? (In about one seed in six the two end close together. If yours did, press **New seed**, switch learning on, and run it again.) Describe the feature space: how many clusters of filled dots are there, and where does the white line run among them? Where are the hollow dots it gets wrong? The reading's §7.2.12 has a name for fitting the training examples "including the accidents in them". Give it, and say what the accidents are in this pool.

**Step 2 — What closes the gap.** Each row below changes one thing from Step 1. Changing the number of hidden units, the pool, or the source starts a new network; check that learning is on, run 5,000 encounters, and record both lines. For the last row, change **Where the encounters come from** to *a stream*, in which every encounter is a new individual.

| Setting | Training, percent wrong | Test set, percent wrong | Gap |
|---|---|---|---|
| 6 individuals, 8 hidden units (from Step 1) | | | |
| 6 individuals, 2 hidden units | | | |
| 24 individuals, 8 hidden units | | | |
| 60 individuals, 8 hidden units | | | |
| a stream, 8 hidden units | | | |

- **Q30.** Report your table. Did a smaller network close the gap? Did a larger pool? Did a stream? A common remedy for a network that fits its training set too closely is a smaller network. Say what your table shows about where the trouble came from in this pool. Why can a fish in a stream not fit its training encounters too closely, however many hidden units it has?

**Step 3 — Grown near.** Load **Part 5b — Downstream**. This fish has no hidden units. Every eel and sucker it encounters while it learns passes close by, so every smell is strong. The learning curve now has two test sets: a **near test set**, and a **far test set** of eels and suckers a long way off, whose smells are diluted to three tenths of their strength. Switch **Learning on**, press **Skip ahead 100 encounters** three times, and record both lines. Switch on **Show the test set** and find the far test set on the feature space. Then run 2,000 more and record both again.

- **Q31.** Report the near and far test sets' percent wrong after 300 encounters and after 2,300. Where on the feature space are the far smells, and on which side of the white line? About half of the far test set is suckers. So which far animals is the fish getting right, and which is it getting wrong? Did more training help? Why not?

**Step 4 — Taken downstream.** On the World tab, press **Go downstream**. Everything the fish now encounters is far off. The button also switches learning off, so that what you see is what the fish learned upstream. Watch a dozen encounters, reading the text block and the **Harm taken** on the World tab's scorecard.

- **Q32.** What did the fish do when an eel's smell reached it, and what happened next? Explain the failure with the feature space. Near the fish, an eel differs from a sucker in two ways at once: its smell has a larger share of A, and more A in total. Which of those two differences survives being diluted, and which one did the fish's line come to depend on? The reading's §7.2.12 names generalization to "inputs unlike anything in training", and §7.1.7 names the demand this fish has failed. Give both names.

**Step 5 — Two repairs.** Press **Go back upstream**. Before each of the runs below, press **Reset** and check that **Learning on** is switched on; going downstream switched it off.

*Train on the change.* Switch on **Learn from every distance**, so that half the fish's encounters are near and half far, and run 2,000 encounters. Record both test sets. Switch it off again.

*Build it in.* Switch on **Proportion of A (a built-in receptor)**, which responds to the share of the smell that is A, whatever its strength. Run 1,000 encounters, near only, and record both test sets. Then switch on **Proportion only (receptors A and B disconnected)** as well, run 2,000, and record them again.

| Repair | Near test set, percent wrong | Far test set, percent wrong |
|---|---|---|
| None (from Step 3) | | |
| Learn from every distance | | |
| Proportion of A, beside A and B, near only | | |
| Proportion only, near only | | |

- **Q33.** Report your table. Which repairs worked? The reading's §7.2.9 says how artificial networks "mostly get there" when the change is one of size or angle, and calls the question of whether that is enough for animals "a live dispute". Which of your repairs is that method, and which is the other side of the dispute?
- **Q34.** The third row is the surprising one. The fish was given a receptor that distance cannot fool, and it still failed far away. With that receptor switched on beside A and B, the fish had two ways to tell a near eel from a near sucker, and both worked perfectly on everything it encountered. Why did it have no reason to prefer the one that also works downstream? What had to be taken away before it used the proportion? Under the switch is a sentence about real fish. Copy it out, and say why it is there.

## The Closer: A New Predator (≈10 minutes)

### Instructions and What to Record

Load **Closer — A new predator**. The fish has six hidden units, set by passing the error back. The stream has three **phases**, and you move between them with the buttons on the World tab. In phase 1 the stream holds eels and suckers. In phase 2 they leave, and a pike and a chub arrive: the pike lunges, and the chub is harmless. Changing phase changes the stream and nothing about the fish. The learning curve plots two test sets throughout, an **eel and sucker test set** and a **pike and chub test set**.

**Step 1 — One after the other.** Switch **Learning on** and run 1,000 encounters in phase 1. Record both test sets. Press **Go to phase 2**, run 100 encounters, and record both. Run 900 more and record both. Switch on **Show the test set** and look at where the eel and sucker dots now sit. Then press **Go to phase 3: An eel comes back**, and watch the next encounter.

| | Eel and sucker test set, percent wrong | Pike and chub test set, percent wrong |
|---|---|---|
| After phase 1 (1,000 encounters) | | |
| Phase 2, after 100 encounters | | |
| Phase 2, after 1,000 encounters | | |

- **Q35.** Report your table. After phase 1 the fish had never encountered a pike or a chub. A fish with no information about them would be wrong about half the time. Yours was wrong far more often than that. On the World tab, compare the typical smells of the four animals, and explain what the fish did with a pike and with a chub, and why.
- **Q36.** What happened to the eel and sucker test set during phase 2, and how quickly? It did not drift back to half wrong. Where did it end, and why there? What happened when the eel came back? The reading's §7.2.10 names this, describes a network that answered "ones problems as if they were twos problems", and says the cause "is the same property that makes the network useful". Give the name, and explain the cause using this fish's weights.

**Step 2 — Both at once.** Press **Reset**, which returns to phase 1 and to the starting weights. Run 1,000 encounters in phase 1 again. Now switch on **Eels and suckers stay around**, press **Go to phase 2**, and run 1,000 encounters. Record both test sets.

- **Q37.** Report both numbers. The fish, the network and the rule are the same as in Step 1. What was different, and why was that enough? The reading says "the trigger is learning in sequence". It also says what people retain of an old list after mastering a new one, and how that compares with a network. What is the comparison, and which later module takes up how brains manage it?
- **Q38.** Open the Learning tab and read the line at the foot of the left panel about backpropagation and brains. Copy it out. This lab has run that rule in a fish for two hours. Say what the lab has shown the rule can do, and what you would be wrong to conclude about real fish from that. The reading's §7.3.7 is where the question is taken up.
- **Q39.** Return to the idea from the top of this handout: sensitivity lives in the representation, and the criterion lives in the chemistry. For each of the following, say which of the two it changed, and how you could tell from an instrument in the scene: (a) raising *arousal and vigilance* in Part 2; (b) F3's weights; (c) adding two hidden units in Part 3; (d) switching on *Distance from the ideal strength* in Part 4; (e) going downstream in Part 5. One of these changed what the world sent the fish and nothing inside the fish. Which, and what happened to its sensitivity anyway?

## Completing the Lab Assignment

- Make sure you answer all the questions in the document fish_lab_report.docx.
- Make sure you have added everyone's name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
