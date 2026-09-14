# Lab 4

In Lab 1 you took a vehicle apart and found two wires. Cross them, and the vehicle that had been chasing the light fled it. Nothing else about it changed. In Lab 3, you opened one of those wires and found a neuron inside it, with a baseline and two connection strengths, and you were shown that the reading calls the same two numbers a *baseline* and a *weight*. This week, the vehicle becomes an animal. It is a small, soft-bodied thing something like a nematode worm. It is in a dish, with a head end that carries its senses, and a nervous system in layers. It has sensory cells, an interneuron that receives from all of them, and two groups of motor cells that drive its body one way or the other. Every number in that nervous system is on the screen, and you can change every one of them.

In this week's reading, we argued that good and bad are not properties the world hands over. They are verdicts an arrangement of cells assigns. The same molecule can be worth chasing or worth fleeing, depending on nothing but where the cell that detects it is wired. If it is wired to motor systems that lead the animal to approach the entity, then it is good. If wired to systems that flee, it is bad.

This lab makes you do the assigning. In Part 1 you flip a single switch and watch approach become avoidance. In Part 2 you are handed a truth table as a specification, and asked to build the animal that satisfies it, by setting its weights and its threshold by hand. In Part 3 you are handed four animals that are all bad at finding food, and asked whether the fault in each is in its wiring or in its chemistry. Then you will see that, because these animals' neural circuits are hard-wired, they cannot learn from changes. When the world changes, they cannot.

## Part 0: Opening the Simulation (≈3 minutes)

1. Open the simulation in your web browser: [The Bilaterian](https://jonwillits.github.io/bcogapp/#/m04-bilaterian). As before, it runs in any modern browser, and there is nothing to install.
2. Download the lab report Microsoft Word document. It is available here: [Lab 4 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/neural_circuits_affect_and_valence/bilaterian_lab/bilaterian_lab_report.docx) This document is what you will turn in to the course website.

The dish is the arena you know from the first three labs. It has walls and a rim, seen from above. The animal is the pale segmented thing moving across it. There are stimuli around the dish, and stimulus cues (information given off by the stimuli) are the colored glows on the floor. Each is a chemical, or a shadow, or a vibration, that falls off with distance from the bead at its center. A glow that is being eaten flashes a ring and vanishes; a glow that has simply drifted away fades out over a few seconds and reappears somewhere else. Watch the animal for a moment before you touch anything. A wave runs along its body from head to tail as it goes forward. Every so often it turns orange, backs up tail-first for a second or so, makes a deep bend, and sets off on a new heading. That reversal is most of what this animal does, and the reading's §4.3.3 says why.

There are four tabs along the top of the left panel. The rest of this section is a tour of the interface. You will be sent back to each tab when a step needs it.

### World

The *World* tab is the dish. Its **Scenario** menu loads one of seven set-ups, each named for the part of the lab that uses it. Each scenario decides which cues are in the dish, what they are called, and which of the animal's controls are locked. **Cue concentration** scales the plumes, the glows that come and go, and leaves the fixed features of the dish alone; it stays where you set it when you load another scenario or another animal. **Source to place on a click** decides which cue a left-click on the floor puts down; a right-click removes the nearest one. The **Reset** and **New seed** buttons work as they did in Labs 2 and 3: Reset replays the same run from the same seed with every control where you left it, and New seed draws a different run. The right panel lists what is in the dish, with a colored dot for each cue, and reports what the animal is getting done: **Cues reached per minute**, **Harm**, and, in the scenario that has a strip of copper, **Crossings of the strip**.

### Circuit

The *Circuit* tab is the animal's nervous system, and it is where Parts 1 and 2 happen. The picture on the right is a descendant of Lab 1's wiring diagram, with more in it. The sensory cells are at the top, one for each cue in the dish, labeled x₁, x₂ and so on, each glowing with its output. Lines run from them to a single **interneuron**, labeled y, in the middle. Each line carries a number, a *weight*, printed on it, green if the weight is positive and red if it is negative, and drawn thicker the more it is carrying right now, exactly as Lab 1 drew its connections. Beside the interneuron are its two other numbers: b₀, its *baseline*, and θ, its *threshold*. Below the interneuron the line continues to a small pill labeled **routing switch**, which says whether the interneuron's verdict goes to the **forward group** or the **reverse group**, the two groups of motor cells at the bottom. Those two groups inhibit each other, which is drawn as the red bars between them. Whichever is winning decides which way the wave runs along the body. Click the pill and the switch flips, where the scenario allows it.

The left panel holds the sliders: one weight per sensory cell, the baseline, the threshold, the routing switch as a menu, and the **activation function**, which is either the *threshold function* or the *sigmoid function* the reading names in §4.2.3. Controls a scenario has locked are printed rather than slid. A **Restore** button puts the wiring back to what the scenario started with, which you will want at least once.

The right panel's sections open and close by clicking their headings. **The arithmetic** prints the reading's equation with the live numbers in it, y = f(b₀ + b₁x₁ + b₂x₂ − θ), names the activation function being applied, and shows the input–output curve of that function with a dot for where the interneuron is right now. It also prints the line from Lab 3 saying that Lab 1's *connection strength* and *actuator bias* are the reading's *weight* and *baseline*: one number, two names. **The target function** shows the scenario's truth table, if it has one, with a column for what the animal currently does on each row and a check or a cross beside it, and counts the rows satisfied. **The decision boundary** is the reading's §4.2.5 figure, drawn live. **Steering** shows what each sensory cell has reported over the last few seconds, the interneuron's verdict and the animal's reversal rate over the same stretch, and which way the wave is running.

One line on the panel says where the scene is not being literal, and it is worth reading now: *the real worm uses a handful of interneurons where this shows one. One is enough to make the verdict.* Part 3 asks you about that.

### Chemistry

The *Chemistry* tab is for Part 3. The left panel has four sliders, named for what each does rather than for the molecule that does it: **pursuit**, **satiety and tone**, **arousal and vigilance**, and **relief**. Each is a *modulator*, in the reading's sense from §4.3.5: a chemical released into the tissue rather than into a single connection, that changes what the cells do with the messages they are already getting. Move one and the animal's behavior changes while every number on the Circuit tab stays exactly as it was. That is not a limitation of the display. It is the reading's claim, and Part 3 depends on it.

The right panel draws the reading's valence–arousal plane, with the chapter's five named states placed on it and a white dot for where the animal itself sits right now; the faint line behind the dot is where it has just been. Under it, a **Persistence** section reports how long the animal's current state has outlasted whatever set it, which modulator level is still decaying back toward its set-point, and whether the reverse group's loop onto itself is still running, and plots the four levels over the last few seconds.

### Worms

The *Worms* tab is Part 3's. It holds the healthy animal and five others, **W0** to **W4**, each loaded one at a time into the same dish, already a minute into its run so the scorecard has something to say. Opening the tab loads the healthy animal; loading any animal switches the World tab's scenario to *The diagnosis dish*, which is where all six live. The **Scorecard** on the right reports cues reached per minute, reversals per minute, the fraction of time spent in reverse, and the energy spent per cue reached, so the six can be compared without leaving the tab. W0 is a worked example with its fault explained on the panel. W1 to W4 keep theirs hidden until you press **Reveal faults**, which sits under *When you have committed*, and until then every number on their Circuit and Chemistry panels is hidden too. Leave this tab alone until Part 3.

## Part 1: Where Good and Bad Come From (≈15 minutes)

### Goal

The reading's §4.1.8 says that nothing in the world arrives labeled, and its §4.2.9 says where the label is actually put on. Before building anything, find out where value lives in this animal, by moving it.

### Instructions and What to Record

**Step 1 — The labeled line.** On the World tab, load **Part 1 — The labeled line**. There is one cue in the dish, food odor, and one sensory cell. Every control on the Circuit tab is locked except the routing switch. Let the animal run for a minute and watch how it gets to the food. It does not aim. Watch what happens as it heads toward the glow and what happens when it heads away from it, and look at the **Steering** section while you do: the reversal rate climbs when the sensory cell's trace is falling and sits near zero when it is rising.

- **Q1.** Describe how the animal finds the food, in your own words. Then answer this precisely, using §4.3.3 of the reading: what does this animal compare, in order to steer? Lab 1's vehicle compared one thing; this animal compares something else. Say what each compares and why the reading says the animal cannot do what the vehicle does.

**Step 2 — Flip the switch.** On the Circuit tab, click the **routing switch** on the diagram (or use the menu on the left) so that the verdict goes to the **reverse group**. Watch for another minute.

- **Q2.** What does the animal do now? Then look at the diagram and the arithmetic. List everything about the sensory cell, the weight, the baseline, the threshold and the interneuron's output that changed when you flipped the switch. Where in the animal is the difference between the version that chases food and the version that flees it? The reading's §4.2.9 has a name for this arrangement; use it, and say where it puts the label.
- **Q3.** So where is the value located? Say, for each of these, whether the goodness of the food odor lives there, and how you know from what you just did: in the molecule; in the sensory cell that detects it; in the wiring between that cell and the motor groups. Lab 1's crossed wires did the same thing to a vehicle. Say what is the same about the two demonstrations and what this one adds.

**Step 3 — The trade-off.** Load **Part 1 — Food beyond copper**. The dish now has two cues: food odor on the far side of a strip of copper, and the copper itself, which burns. Two sensory cells now feed the interneuron, and both weights are unlocked: b₁ from the food odor cell and b₂ from the copper cell. As shipped they are +1 and −1. The World tab's right panel counts **Crossings of the strip** and **Harm**, which is the burn. Run each setting for two minutes, pressing **Reset** between runs so the counts start from zero, and record the crossings and the harm each time. Then find two settings of your own: one where the animal crosses about once a minute, and one where it almost never crosses but still visibly flinches from the strip.

| Food weight b₁ | Copper weight b₂ | Crossings in 2 min | Harm in 2 min |
|---|---|---|---|
| +1 | −1 | | |
| +3 | −3 | | |
| +3 | −1 | | |
| +3 | −0.2 | | |
| your own | | | |
| your own | | | |

- **Q4.** Report your table. Two of the rows have the food weighed three times as heavily as the copper, and two have them weighed equally; say what decided whether the animal crossed. The reading's §4.1.9 says that in this situation nothing is a yes-or-no rule. Say what it is instead, and say why the setting where the copper weight is nearly zero is a poor way to make the animal cross, even though it works.
- **Q5.** Look at the diagram while the animal is near the strip. Both cells are firing, and one interneuron is receiving from both. The reading's §4.3.3 describes this exact case in the real worm. Name the circuit motif from §4.2.2 that this is, and say what the interneuron is doing that neither sensory cell can do on its own.

## Part 2: Build the Animal from the Truth Table (≈25 minutes)

### Goal

The reading's §4.1.9 wrote three target functions as truth tables and said nothing about how an animal could compute them. Its §4.2.4 then computed all three with one unit and two numbers. You are now going to do that with the animal running, so that a truth table satisfied on paper and an animal that feeds correctly are visibly the same achievement. The order is AND, then OR, then AND NOT, and the middle step is the one that teaches.

### Instructions and What to Record

**Step 1 — AND.** Load **Part 2 — AND**. The two cues are food odor and cool water, and the target, from the reading's table, is *feed when there is food odor AND the water is not too warm*. On the Circuit tab, **The target function** section shows the four rows, what the target says on each, what the animal currently does, and a count of rows satisfied. **The decision boundary** section draws the four combinations as points, blue where the target says act and orange where it says do not, over a background colored by what the current weights output. Read the text above and below that figure once, carefully. Every control is unlocked.

As shipped, the weights are +1 from food odor and 0 from cool water, the baseline is 0 and the threshold is 0.5. Watch the animal for a minute before changing anything. Food eaten where the water is warm counts as harm, and the World tab reports it.

- **Q6.** As shipped, which rows of the table are wrong, and what does the animal do in the dish that shows it? Then set the weights, the baseline and the threshold until all four rows are satisfied. Report the numbers you ended with. Write out the arithmetic for the row where both cues are present and for the row where only food odor is present, the way the panel prints it, and say what the threshold function does to each. The reading gives one setting of these numbers in §4.2.4; your setting need not be the same one, but say whether it is, and if it is not, why yours also works.
- **Q7.** With AND satisfied, watch the animal for two minutes. It arrives at every plume it can find. Describe what it does at a plume inside the cool water and what it does at a plume outside it, and say what the harm counter did. This is the whole point of the part in one observation: say in one sentence what the truth table and the dish are each telling you, and why they agree.

**Step 2 — OR, by one number.** Do not touch the wiring. On the World tab, load **Part 2 — OR**. The cues are now a shadow and a vibration, the target is *flee when there is a shadow OR a vibration*, and the routing switch has been set to the reverse group for you, because acting now means fleeing. The interneuron's weights, baseline and threshold are exactly as you left them in AND; the World tab says so. Watch the **decision boundary** and the table while you make the change.

- **Q8.** Change **one number** so that all four rows are satisfied. Which number, and to what? Describe what the boundary line did as you changed it, and what it did *not* do. Which two points changed sides? The reading's §4.2.5 says exactly this; quote or paraphrase its sentence about a shift and a rotation, and say what you saw that confirms it.
- **Q9.** Restore the AND setting with the **Restore** button, then achieve OR again by changing a *different* single number. There are two knobs that do it. Name both, say what each one is called on the diagram, and explain, using the arithmetic, why moving either one alone slides the same line. Then say what that tells you about whether the baseline and the threshold are really two different things.
- **Q10.** Watch the animal in the OR dish with the wiring set to AND (Restore, if you need to) and then with it set to OR, for a minute each. Every second spent in a shadow or a vibration counts as harm. Report the harm for each minute and describe the difference in what the animal does at the edge of a shadow when its wiring says OR.

**Step 3 — AND NOT.** Load **Part 2 — AND NOT**. The cues are food odor and the scent of something that eats us, and the target is *advance when there is food odor AND NOT the scent of something that eats us*. Food eaten where the scent is present counts as harm; you have been eaten. This one ships with the AND wiring.

- **Q11.** Satisfy all four rows and report your numbers. This target needed something that neither AND nor OR needed. Say what it was, and, using the reading's §4.2.4 account of NOT, say why no setting of positive weights could have done it. Then look at the boundary: which point is now on its own side of the line, and which way did the line have to tilt to put it there?
- **Q12.** The reading's §4.2.4 ends with a warning that is Lab 1's lesson restated: *the unit is not choosing anything, and it does not know what AND means.* You have now set the same unit to compute three different functions by changing numbers. Say where the logic is, in one sentence. Then say what would have to be true of the interneuron for the sentence "it knows what AND means" to be an accurate description, and whether anything you did put that in.

## Part 3: Same Diagram, Different Chemistry (≈20 minutes)

### Goal

The reading's §4.3.5 says the worm's wiring has been completely known for decades and its behavior still cannot be predicted from the diagram. Four animals, **W1** to **W4**, are all bad at reaching food. Each has a different thing wrong with it, and one of them has nothing wrong with it at all. For each, you have to say whether the fault lives in its wiring or in its chemistry, and defend the answer. Their panels hide every number until you have committed, so this is done by watching, by building a table, and by designing a test.

**Two things you are told in advance, because this part is about method.** First, one of the four is not broken, and deciding which is part of the work. Second, two of the four will look the same however long you watch them at the concentration the dish ships with, and the way out is to change the dish.

### Instructions and What to Record

**Step 0 — Build the tool first.** Load the healthy animal on the Worms tab and give it a minute on the Circuit tab, then a minute on the Chemistry tab. Then do two things to it, one at a time, and put each back afterward. First, on the Circuit tab, halve the weight from the food odor cell (the Restore button undoes it). Second, on the Chemistry tab, halve **pursuit**. Watch the animal and both panels each time.

- **Q13.** Fill in this table. For a fault in the wiring and a fault in the chemistry, say what you would expect to see on the Circuit panel, on the Chemistry panel, and in the dish. Some cells will say "nothing unusual", and those are the useful ones. Then answer the question the table raises: the two changes you just made produced the same behavior. Where, exactly, does a halved gain act, and where does a halved weight act? The reading's §4.3.5 and the Chemistry tab's own note both say where a modulator acts.

| A fault in the… | …looks like this on the Circuit panel | …on the Chemistry panel | …in the dish |
|---|---|---|---|
| Wiring (a weight, a switch, a threshold) | | | |
| Chemistry (a modulator level) | | | |

**A worked example.** Load **W0**, which is diagnosed for you. In the dish it flees every plume it finds and, if it wanders into one of the grey patches of decaying matter, crawls there rather than avoiding it. On the Circuit tab its routing switch reads *reverse group*, and every weight, the baseline and the threshold are the healthy values. On the Chemistry tab all four levels are healthy. So W0's fault is in the wiring, and the evidence is as much the healthy chemistry as the flipped switch. Notice that its whole verdict is inverted, not just its response to food: it is drawn toward the very thing a healthy animal avoids, by the same switch. A diagnosis is made by what is ruled out as much as by what is found.

**Step 1 — Watch.** Load each of **W1**, **W2**, **W3** and **W4** in turn. Give each two minutes, watching the dish and the Scorecard. Press **Reset** if you want to see the same two minutes again.

- **Q14.** Describe what each of the four does, and copy its scorecard. They do not all move the same way. Say, for each, whether the way it moves tells you what is wrong with it, and why or why not. At least two of them should be impossible to tell apart.

**Step 2 — Commit.**

- **Q15.** For each of the four, say whether you think the fault is in the wiring, in the chemistry, or nowhere, and give your reason from the Q13 table and from what you watched. Committing before you have all the evidence is the point; you will be asked to compare your guesses against the answers, not graded on them.

**Step 3 — Design the world that separates them.** Two of the four behave the same at the concentration the dish ships with. The reading gives you the way out, and this is the third time the course has asked for it: if two things behave the same, find the conditions under which they stop. The Q13 table tells you where each kind of fault acts, and the sensory cell has a ceiling of its own. Things you can change on the World tab: the **cue concentration**, and where the sources are, by clicking. Load each of the pair again after you change the dish; concentration stays where you set it.

- **Q16.** Say which two you could not separate, describe the test you designed and what you predicted before running it, and report what happened, with the scorecards. Then explain the result: why does a fault in the chemistry disappear when the cue is strong, while a fault in the wiring does not? Your answer should use the words *gain*, *ceiling* and *weight*, and it should say where each of the two faults acts.

**Step 4 — Reveal.** Press **Reveal faults**.

- **Q17.** For each of the four, state what was actually wrong and whether it lived in the wiring, in the chemistry, or nowhere. Compare against Q15: which did you get right, and for the ones you got wrong, what misled you?
- **Q18.** One of the four has nothing wrong with it. Which one, and what is different about it? The reading's §4.1.11 describes this animal exactly, with carbon dioxide. Explain why an animal that behaves differently from every other animal in the tab, with the same wiring as the healthy one, is nonetheless not broken. Then say what that does to the idea that a complete wiring diagram tells you what an animal will do.

**Step 5 — Persistence and the plane.** Load the healthy animal again and open the Chemistry tab. Watch the four level traces and the dot on the plane for a few minutes while the animal eats. Each meal kicks two levels up, and they decay back over a couple of minutes; each reversal is held by the reverse group's loop onto itself for about a second after the pulse that started it.

- **Q19.** The animal's state after a meal outlasts the meal. Where is that state being kept? The panel names two different ways a state can outlast its cause, on two different time scales. Describe both, and say, for each, whether anything has been written down anywhere. The reading's §4.2.8 has a sentence about this; find it and use it.
- **Q20.** Name the state the healthy animal sits nearest on the plane. Then, for two of the four controls, say which named neighboring state each one would move the animal toward and check by moving it. The reading's §4.3.6 gives a table of what each of four molecules does and where each moves an animal on this plane. Match each of the four controls to its molecule, and give your reason for each match from what the control does in the simulation.

## The Closer: What the Animal Cannot Do (≈7 minutes)

### Instructions and What to Record

Load **Closer — The world changes**. It is the healthy animal, with the healthy wiring, in a dish of food odor. But the food odor now comes from a toxin. Watch the harm counter on the World tab for two minutes.

- **Q21.** What does the animal do, and what does the harm counter do? Does the animal's behavior change at all over the two minutes? Say why it does not, using the reading's §4.2.12.
- **Q22.** Now fix it. It should take you a few seconds with the controls you have been using all hour; say what you did. Then answer this: what did you just do that the animal cannot do? Be exact about which numbers you changed and what would have had to happen inside the animal for those numbers to change by themselves.
- **Q23.** In Part 3, a hungry animal behaved differently from a fed one with nothing in its wiring moved. That is the animal changing its own behavior. Why is that not the same thing as what you did in Q22? The reading's Close says what the hungry worm keeps and what it does not; use it.
- **Q24.** A worm in a field has no sliders and no student. Say what would have to be added to this animal for it to do, by itself, what you did in Q22. Be as specific as you can about where in the diagram the addition would go and what it would have to be sensitive to. Module 5 is about the answer, and you have just asked its question.

## Completing the Lab Assignment

- Make sure you answer all the questions in the document bilaterian_lab_report.docx.
- Make sure you have added everyone's name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
