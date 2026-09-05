# Lab 3

In Lab 1 you took a vehicle apart and found a wiring diagram: a line running from a sensor to an actuator, with a number on it. In Lab 2 you watched a population of those vehicles evolve. This week you open one of those lines up, and find that it is a cell.

This week's reading looks at that cell three times: once as the answer to a problem, once as a function, and once as a physical machine with a running cost. The simulation does the same thing, in three tabs, and they are all the same cell. Change something in one tab and the other two change with it. Your job is to work out what each of the three views can tell you that the other two cannot — and then to use that to diagnose four vehicles that are all failing in the same way for four different reasons.

## Part 0: Opening the Simulation (≈3 minutes)

1. Open the simulation in your web browser: [The Neuron](https://jonwillits.github.io/bcogapp/#/m03-neuron). As before, it runs in any modern browser, and there is nothing to install.
2. Download the lab report Microsoft Word document. It is available here: [Lab 3 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/neurons_and_neural_communication/neuron_lab/neuron_lab_report.docx) This document is what you will turn in to the course website.

The pit and the vehicle are the ones you already know. What is new is the three tabs along the top:

- **World** — one vehicle in the pit, with lights that move. The connection between its sensor and its actuator is now a neuron with a length, and the panel reports how long the vehicle takes to react to something.
- **Unit** — that neuron as an input-output device: rates coming in, a strength on each connection, a total, and a rate going out. This is the description in §3.2 of the reading.
- **Membrane** — the same neuron as a piece of biology: a membrane, ion channels, the sodium-potassium pump, a voltage trace, and a counter showing what it is all costing in ATP. This is §3.3.

**One cell, three tabs.** Nothing is duplicated between them. If you break something on the Membrane tab, the Unit tab and the World tab are showing you the consequences.

The Membrane tab also has a small area marked **Things to try**. Nothing in this lab asks about anything in it, and nothing in your report depends on it. It is there because a neuron is a more interesting object than any one lab has room to ask about, and because some of you will read §3.3.5 of the chapter and want to see it happen.

## Part 1: Why a Neuron at All (≈15 minutes)

### Goal
The reading argues that neurons solved a specific problem, and that only some kinds of living thing had it. Before looking inside a neuron, find out what the problem was.

### Instructions
Open the **World** tab. Three controls matter here: **signal type** (a diffusing chemical, a graded electrical signal, or spikes), **body size** (which sets how far the signal has to travel), and **world speed** (how fast the lights move).

Run each of the following for about 30 seconds and record what the panel reports: the **reaction time**, the **travel time** it breaks out of that total, and the **lights collected**.

1. Diffusing chemical, small body, **slow** world.
2. Diffusing chemical, small body, **fast** world.
3. Spikes, small body, **fast** world.
4. Graded electrical, **largest** body, fast world.
5. Now a size sweep. The **body size** control sets how far the signal has to travel, and the panel names that distance. Set the signal to **diffusing chemical** and record the **travel time** at the smallest, middle and largest settings. Then do the same three settings with **spikes**. At the larger settings the diffusing signal will not arrive at all within the run; the panel still reports how long it would have taken, and that number is your answer.

### What to Record
- **Q1.** Report your four runs from steps 1–4 and your two size sweeps from step 5 as a table: signal type, body size, world speed, reaction time, travel time, lights collected.
- **Q2.** In the slow world, the vehicle signalling by diffusing chemical did fine. Given that, say precisely what is and is not wrong with chemical signalling. Your answer should make clear that "too slow" is only half of an answer.
- **Q3.** Look at the travel times in your two size sweeps. In one of them, doubling the distance roughly doubles the travel time. In the other, doubling the distance roughly *quadruples* it. Which is which? The reading explains why one of them behaves that way — give the explanation.
- **Q4.** In run 4 you sent a graded electrical signal down a long body. Describe what arrived at the far end, and what the vehicle did about it.
- **Q5.** Using Q1 to Q4, write one sentence stating the problem a neuron solves. Then say who has that problem and who does not, and why. The reading's table comparing plants, fungi and animals is what this question is about.

## Part 2: Taking the Cell Apart (≈21 minutes)

### Goal
Now open the cell. The **Unit** tab tells you what it computes. The **Membrane** tab tells you how it manages that physically. In every experiment below you throw one switch and look at all three tabs.

### Instructions and What to Record

**Step 1 — Reproduce the reading's example.** Open the **Unit** tab. Set the baseline to **5** spikes per second, the first connection to **+2**, and the second connection to **−3**. Set the first input to **10** spikes per second and the second to **0**.
- **Q6.** What output rate do you get? Now raise the second input to **5** without touching the first, and report the output. Then raise the second input to **15**. Write out the arithmetic the panel prints, say what number the arithmetic gives, and say what the panel actually reports as the output rate. Those two are not the same. Explain why not, and what a real cell is doing that the arithmetic alone does not capture.

**Step 1b — Look at the function itself.** Underneath the arithmetic is a small plot: the total arriving input along the bottom, the output rate up the side, and a dot showing where the cell is sitting right now. Watch the dot move as you change the sliders. Drive the inhibitory connection up until the dot runs off the bottom of the rising part, then drive the excitatory input up until the dot stops climbing.
- **Q7.** Describe the shape of that curve. It is flat at both ends and rising in between. Say what the flat part on the left means about the cell, and what the flat part on the right means. The reading gives a reason for each — give both. Then answer this: if the curve were a straight line the whole way, with no flat parts at all, what would this cell be doing that a real neuron cannot?

**Step 2 — The same output, two ways.** Leave the vehicle running and find the **time window** slider under the spike display. Slide it from one millisecond to one second and back.
- **Q8.** Describe what the output looks like at each end of that slider. At one end you are looking at something that is either there or not there. At the other you are looking at a number that can land anywhere in a range. Are those two competing descriptions of the neuron? Answer using what §3.2.5 of the reading says about time scales.

**Step 3 — Watch one spike.** Open the **Membrane** tab and let a single action potential run, using the step control if it goes by too fast. Three gate meters run beside the voltage trace: sodium activation, sodium inactivation, and potassium.
- **Q9.** Describe the order of events. Which gate opens first, which one closes during the spike, and which one is slow to arrive and slow to leave? Match each phase you describe to the rising and falling parts of the voltage trace.

**Step 4 — Turn off the pump.** Set the **sodium-potassium pump** to zero and let the simulation run for a simulated minute.
- **Q10.** Report what happened to the resting voltage, to the spikes, and to the ATP counter. The reading says a neuron doing nothing at all is still spending energy, and that what it is buying is readiness. Use what you just watched to explain that sentence.

**Step 5 — Block the sodium channels.** Restore the pump. Set the **voltage-gated sodium channel block** to its maximum, then give the cell the same input as before.
- **Q11.** What happened to the voltage at the cell body, and what arrived at the far end of the axon? Connect this directly to your Q4 answer: you have now seen the same failure twice, once as a design choice in Part 1 and once as a mechanism.

**Step 6 — Remove the refractory period.** Restore the sodium channels. Set **sodium inactivation recovery** to instant.
- **Q12.** What happened to the highest firing rate the cell could reach, and what happened to spikes travelling along the axon? The reading uses the refractory period to explain two separate things about neurons. Name both, and say which one you just watched break. Then look at the input–output curve from Q7. One of its two flat parts is now gone. Say which one, and why removing the refractory period is what removed it.

**Step 7 — Flip a sign.** Return to the **Unit** tab and change the second connection from inhibitory to excitatory, leaving every input exactly where it was.
- **Q13.** The vehicle's behaviour changed although nothing about its inputs changed. Explain what happened, using the reading's word **integration**. Then say why a cell that can only add would be less useful than one that can add and subtract.

## Part 3: Four Sick Neurons (≈25 minutes)

### Goal
Four vehicles — **N1**, **N2**, **N3** and **N4** — are all bad at finding light, and they are bad at it in ways that look the same from outside. Each one has a different thing wrong with it, and one of them has nothing wrong with it at all. Your job is to work out which is which.

**Two things you are being told in advance, because this part is about method rather than about catching you out.** First: **one of the four is not broken.** Deciding which one, and defending the choice, is part of the work. Second: **if you open a panel and everything on it looks normal, that is a result, not a dead end.** A cell can be perfectly healthy and still fail at a task, and a cell can compute exactly the wrong thing while every piece of its biology is in order.

### Instructions and What to Record

**Step 0 — Build the tool first.** Everything you did in Part 2 was a fault you caused on purpose, so you already know what each kind of fault looks like.
- **Q14.** Fill in this table from your Part 2 results. For each of the three tabs, say what a problem *at that level* would look like when you looked at each of the three tabs. Some cells will say "nothing unusual" — those are the useful ones.

| A problem in the… | …looks like this on the World tab | …on the Unit tab | …on the Membrane tab |
|---|---|---|---|
| World (the task itself) | | | |
| Unit (what the cell computes) | | | |
| Membrane (how the cell works) | | | |

**A worked example.** Before you start, open **N0**, which is diagnosed for you. In the World tab, N0 reacts to lights promptly but steers the wrong way. On the Unit tab, its arithmetic shows a strong negative connection where the task needs a positive one, so the cell is computing a perfectly good function that happens to be the wrong function. On the Membrane tab, everything is normal: the resting voltage is where it should be, the gates open in the right order, the spikes are full size, the ATP cost per spike is ordinary. **N0's fault is at the level of what the cell computes, and the evidence for that is as much the healthy membrane as the odd arithmetic.** Notice the shape of the reasoning: a diagnosis is made by what is *ruled out* as much as by what is found.

**Step 1 — Watch.** Put a single light in the middle of the floor and watch all four vehicles.
- **Q15.** Describe what each of N1, N2, N3 and N4 does. Then say whether behaviour alone lets you sort them, and why.

**Step 2 — Choose where to look, and commit.**
- **Q16.** For each of the four, say which tab you would open first and why, using your Q14 table. Then open it, and write down your diagnosis and your reason. Guessing is fine — committing to a guess before you have all the evidence is the point, and you will be asked to compare your guesses against the answers, not graded on them.

**Step 3 — Test the ones you cannot separate.** At least two of the four will still be ambiguous after Step 2. The reading gives you the way out: if two things behave the same, find the conditions under which they *stop* behaving the same. Things you can change: how fast the lights move, how many lights there are, how long the vehicle has to keep working without a rest, and the body size.
- **Q17.** Describe the test you designed, what you predicted before running it, and what happened. If your first test did not separate them, describe that one too and what you tried next.

**Step 4 — Reveal.** Press **Reveal faults**.
- **Q18.** For each of the four, state what was actually wrong and which of the three levels the fault lives at. Then compare against your Q16 answers: which did you get right, and for the ones you got wrong, what misled you?
- **Q19.** One of the four had nothing wrong with it. Which one, and why is a cell that fires very rarely not a broken cell? Your answer to this question is the beginning of Part 4.

## Part 4: What It Costs, and What Three Descriptions Are For (≈18 minutes)

### Instructions and What to Record

**Q20 — Do the arithmetic.** The **Membrane** tab reports what a single action potential costs in molecules of ATP. Open the **energy calculator** and give it the number of neurons in a human brain, which the panel supplies. Set the average firing rate to **10 spikes per second** — roughly what you have been watching all hour — and record the power the calculator returns, in watts. Then work backwards: adjust the firing rate until the power comes out at about twenty watts, which is what a real brain actually uses, and record the rate you needed.

**Q21 — What follows from it.** The rate you just recorded is very low. Say what it implies about how many neurons in a brain can be firing at any one moment, and give the reading's term for activity that thin. Then answer this: is a brain in which most neurons fired most of the time a *better* brain that evolution failed to build? Explain.

**Q22 — Why a fifth.** *Write this answer before reading the next question.* A human brain is about two percent of body weight and uses about twenty percent of the body's energy at rest. Write the best explanation you can for why humans invest that much. Give the argument you would defend.

**Q23 — And what was wrong with it.** Now the comparative figures. A human neuron costs roughly what a chimpanzee's neuron costs; what is unusual about a human brain is how many neurons are in it, not how expensive each one is. Given that, what was wrong with the explanation you wrote in Q22 — not with your reasoning, but with the question it was answering? If your Q22 answer treated twenty percent as an achievement, say what it should be read as instead.

**Q24 — Which vehicle is better.** In Part 1 you ran a vehicle that signalled by diffusing chemical, in a slow world, and it did fine — at a fraction of the energy cost. You also ran a spiking vehicle in a fast world. Which of the two is **better adapted**? Which is **better**? Explain why those are not the same question. Then apply the same reasoning to the figures in Q23: humans spend about a fifth of the body's resting energy on the brain, other primates about a tenth, and other mammals less than that. Is that a ranking of anything?

**Q25 — Two curves.** Go back to the **Unit** tab and switch on **Show measured**. The panel now draws two curves on the same axes: the one the arithmetic predicts, and the one measured from the membrane simulation as the cell actually fires. Describe where the two agree and where they part company. Then answer this: is the measured curve the *right* one, with the predicted curve a rough approximation of it? Or is that the wrong way to describe how the two are related? Use what the reading says in §3.3.4 about Hodgkin and Huxley's model of a neuron sitting beside the model in §3.2.7.

**Q26 — Which panel answers which question.** Here are four questions about a single neuron. For each one, name the tab that can answer it, and say why the other tab is silent.
- What will this cell do if a fourth input arrives at 20 spikes per second?
- How long after the voltage crosses threshold does it reach its peak?
- What happens to the vehicle if this connection changes sign?
- Why can this cell not fire a thousand times a second?

**Q27 — The switch that did nothing.** On the **Unit** tab there is a toggle marked *biological / artificial*. Flip it. Every word on the panel changes and not one number does, because the same arithmetic describes a neuron and the unit at the heart of an artificial neural network. Now open the **Membrane** tab and ask the same question of it.
- Where do the natural and the artificial version of this cell resemble each other, and where do they stop resembling each other? Be specific about which level each answer belongs to.
- The reading has a term for one function running in two completely different physical materials. Give it, and say why a single cell is a better demonstration of it than a whole brain would be.

**Q28 — Turn it on the simulation.** Nothing in the Membrane tab plays back a recorded spike. The shape you have been watching all hour is calculated, moment by moment, from equations Hodgkin and Huxley wrote in 1952 — and when they first used those equations, the curve that came out had the right shape, height, duration and travelling speed, none of which they had fitted the equations to. Why does that matter more than if they had fitted them? What would you be entitled to conclude in each case?

## Completing the Lab Assignment
- Make sure you answer all the questions in the document neuron_lab_report.docx.
- Make sure you have added everyone's name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
