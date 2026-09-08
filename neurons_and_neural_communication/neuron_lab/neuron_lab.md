# Lab 3

In Lab 1, you took a vehicle apart and found a wiring diagram. There were lines running from sensors to actuators, with numbers telling you how strongly the sensors drove the actuators. In Lab 2 you watched a population of those vehicles evolve, with those numbers changing as they were inherited and mutated, because certain combinations of numbers led to more offspring. This week you open one of those lines up, and find that it is a neuron, and that we can understand more about it by considering what we have learned in this module about neurons.

This week's reading looks at a neuron three times. First, as the answer to a problem. Second, as a function. And third, as a physical machine with a running cost. The simulation does the same thing, in three tabs. Change something in one tab and the other two change with it. Your job is to work out what each of the three views can tell you that the other two cannot. And then, to use that to diagnose four vehicles that are all failing in the same way, for four different reasons.

## Part 0: Opening the Simulation (≈3 minutes)

1. Open the simulation in your web browser: [The Neuron](https://jonwillits.github.io/bcogapp/#/m03-neuron). As before, it runs in any modern browser, and there is nothing to install.
2. Download the lab report Microsoft Word document. It is available here: [Lab 3 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/neurons_and_neural_communication/neuron_lab/neuron_lab_report.docx) This document is what you will turn in to the course website.

The arena and the vehicle are the ones you already know. There is one vehicle in the arena, and lights that move. What is new is the four tabs along the top. The first three are the same two neurons described three ways; the fourth loads the vehicles we use in Part 3 of the lab.

### World

The *World* tab shows the options and information that are relevant to the computational level. When the World tab is selected, the panel below it shows you the options about the world that you can change. As before, you can change the number of lights, the speed of the lights, reset the simulation, and pick a new random seed. In the vehicle being shown on the screen there are, as before, a left and a right light sensor. And as before, each sensor is connected to a left and right actuator.

What is new in this lab is that the connections between them are neurons. Each sensor sends spikes at a rate that depends on how close it is to a light, and two fully realized actuator neurons integrate those spikes and drive the actuators, as a function of the connection strengths.

To show how the distance a signal must travel affects reaction time, this lab lets you change the length of each actuator neuron’s axon, which runs from the neuron to its actuator, using the *Sensor-to-actuator distance* slider in the World tab. A longer axon means a slower reaction.

When the World tab is selected, the World Information panel on the right is displayed. This info panel shows you the current reaction time of the vehicle, information about *The neural signal*, the *Lights*, and a *Motion Comparison*.

### Neurons

The Neurons tab displays the options for the two actuator neurons, and the information about the vehicle’s neural system as a whole, described at the algorithmic level.

Under the LEFT/RIGHT buttons, the Neurons panel shows the Sensor Neuron Activity. This shows the firing rate of the two sensor neurons, labelled x₁ for the left sensor and x₂ for the right. The “Where the inputs come from” option menu allows you to control whether the sensor neurons are firing due to the actual presence of lights, or firing under your control. If you set it to “the sliders below”, then the sensor neurons stop responding to the lights, and just activate at whatever level you set the sliders to. This is to let you have direct control over those neurons if you want.

Below that are sliders controlling the connection strength between the sensor neurons and the actuator neurons. The vehicle has **two** actuator neurons, one for each actuator, and each has three numbers of its own: a baseline firing rate b₀ (how fast it fires when nothing is arriving), and two connection strengths, b₁ from the left sensor and b₂ from the right. A positive strength is an excitatory connection, drawn green; a negative one is inhibitory, drawn red, as in Lab 1. That is six numbers, three for each actuator neuron. The picture at the top of the right panel draws them the way Lab 1 did. There are two sensors above, two actuators below, and the two actuator neurons between them, each receiving one straight line from the sensor on its own side and one crossed line from the sensor on the other side.

You can change which neuron is being displayed in two ways. First, you can click a neuron in the picture on the right to make the sliders on the left and the instruments below it belong to the one you clicked. You can also click the LEFT or RIGHT buttons on the left panel to change which actuator neuron is being displayed. 

You can change each neuron’s base firing rate and the connection strength of each sensor by moving the sliders with the corresponding labels. The *Mirror this wiring to the right/left neuron* button gives the other neuron the same wiring seen from its own side: the same baseline, with the two connection strengths swapped, so a crossed connection stays crossed.

Below the picture, the right panel shows, for the selected neuron: the arithmetic the reading uses, y = b₀ + b₁x₁ + b₂x₂, printed with the live numbers in it; the output firing rate actually measured from the neuron over the last second, which is not always what the arithmetic says; a line saying that Lab 1's *connection strength* and *actuator bias* are the reading's *weight* and *baseline*; a plot of output rate against total input, with a dot for where the neuron is right now and two curves, one predicted by the arithmetic and one measured; and the neuron's spike train over the last stretch of time, with the *Time window for the output* slider on the left setting how long a stretch.

### Membrane

The *Membrane* tab shows the same two actuator neurons as pieces of biology, described at the implementational level. The four jobs the Neurons tab named — input surface, integrator, output line, junction — are done here by four named parts: dendrites, a soma, an axon and a synapse. Watch the picture on the right when you switch from the Neurons tab to this one. It does not change shape, but each job turns into the part that does it. This is the description in §3.3 of the reading.

**The Membrane tab runs the whole scene in slow motion.** An action potential lasts about a millisecond, and you are meant to watch one happen, so when you open the tab the simulation runs ten times slower than life, and fifty times slower if you ask. The vehicle in the arena is on the same clock, so it will have all but stopped. It has not frozen. A badge over the arena says what speed you are at, and has three buttons: *real time*, *10× slow* and *50× slow*. Press *real time*, there or on the panel, whenever you want the vehicle to drive again. Two of the experiments in Part 2 need a real minute of driving, and the instructions say so when they do.

The left panel, under the LEFT/RIGHT buttons, has five groups of controls:

- **Simulation Speed.** A slider from real time to two hundred times slower than life, the three speed buttons, and *step one spike*, which runs the simulation just far enough for the selected neuron to fire once.
- **Lesions — damage the neurons.** Four ways to damage a neuron: *Sodium-potassium pump power*, *Sodium channels blocked*, *How fast sodium channels reset* (from normal to instant), and *Current injected into the neuron*. These act on *both* actuator neurons at once, the way a drug reaches the whole animal; only the wiring on the Neurons tab is set one neuron at a time. *Restore healthy membrane* puts all four back.
- **Equations.** *Show the equations* is off to begin with. It reveals the equations the simulation is calculating, and says whose they are and when they were written. The gate meters on the right are those equations without the algebra.
- **Brain Energy Calculator.** For Part 4.
- **Things to try.** A control that nothing in this lab asks about; see the end of this section.

The right panel, *Neuron Information*, is divided into sections you can open and close by clicking their headings: **The parts**, the two-neuron picture with the parts named and a line for each job saying which part does it; **Voltage trace**, the voltage across the membrane of the selected neuron, in millivolts against milliseconds, with buttons for how many milliseconds to show; **The gates**, three bars; **Ions and the pump**, the ions crossing the membrane as arrows sized by how much is crossing, with the pump drawn as its own machine; **Spikes and conduction**, the voltage at the cell body and at the far end of the axon, and how many spikes reached each in the last second; **Concentrations**, sodium and potassium inside and outside the cell, and the reversal potentials computed from them; and **Energy (ATP)**, the pump's work, counted cycle by cycle. Some sections start closed; open them when a step asks for them.

### Diagnosis

The *Diagnosis* tab is for Part 3. Under *Load a vehicle* it holds the healthy vehicle and five others, N0 to N4, each with its own two neurons and its own world. Loading one replaces the vehicle in the arena, and the World, Neurons and Membrane tabs then show that vehicle's neurons. Each loads already three-quarters of a minute into its run, so what you see is how it drives once it has been driving for a while; *Reset* replays the same run from that point. The panel on the right shows a **Scorecard** for the loaded vehicle — lights per minute, energy per light, lights collected, run time — so the four can be compared without leaving the tab. N0 is a worked example with its fault explained on the panel. N1 to N4 keep theirs hidden until you press **Reveal faults**, which sits under *When you have committed*; Part 3 tells you when. Leave this tab alone until then.

### One cell, three views

Nothing is duplicated between the three views. If you break something on the Membrane tab, the Neurons tab and the World tab are showing you the consequences. Switching between the Neurons tab and the Membrane tab also swaps one vocabulary for another, since the four jobs become the four parts that do them. Watching that swap happen is worth a moment on its own.

The Membrane tab also has a small area marked **Things to try**. Nothing in this lab asks about anything in it, and nothing in your report depends on it. It is there because a neuron is a more interesting object than any one lab has room to ask about, and because some of you will read §3.3.5 of the chapter and want to see it happen.

## Part 1: Why a Neuron at All (≈15 minutes)

### Goal
The reading argues that neurons solved a specific problem, and that only some kinds of living thing had it. Before looking inside a neuron, find out what the problem was.

### Instructions
Open the **World** tab. Three controls matter here: **signal type** (a diffusing chemical, a graded electrical signal, or spikes), **sensor-to-actuator distance** (which sets how far the signal has to travel — the vehicle is drawn the same size whatever it says, and what changes is the *travel* time in the World Information panel), and **world speed** (how fast the lights move; the **slow** and **fast** buttons set the two speeds this part uses).

A light counts as collected when the vehicle *catches* it — drives into it while moving at least as fast as the light is moving. A light that runs into a vehicle that is sitting still, or streaks past one that could never have kept up, bounces off and is not counted.

Run each of the following for about 30 seconds and record what the World Information panel reports: the **reaction time**, the **travel time** it breaks out of that total, and the **lights collected**. Press **Reset** before each run so the light count starts from zero; your other settings stay where you put them.

1. Diffusing chemical, shortest distance, **slow** world.
2. Diffusing chemical, shortest distance, **fast** world.
3. Spikes, shortest distance, **fast** world.
4. Graded electrical, **longest** distance, fast world.
5. Now a distance sweep. The **sensor-to-actuator distance** control sets how far the signal has to travel, and the panel names that distance. Set the signal to **diffusing chemical** and record the **travel time** at the smallest, middle and largest settings. Then do the same three settings with **spikes**. At the larger settings the diffusing signal will not arrive at all within the run; the panel still reports how long it would have taken, and that number is your answer.

### What to Record
- **Q1.** Report your four runs from steps 1–4 and your two distance sweeps from step 5 as a table: signal type, distance, world speed, reaction time, travel time, lights collected. (Lights collected varies from run to run, and a difference of one or two lights means little. The comparison that matters is between signal types within one world: runs 2 and 3.)
- **Q2.** In the slow world, the vehicle signalling by diffusing chemical did fine. Given that, say precisely what is and is not wrong with chemical signalling. Your answer should make clear that "too slow" is only half of an answer.
- **Q3.** Look at the travel times in your two distance sweeps. Each step of the sweep is a thousand times the distance. For one signal type, each step takes about a thousand times as long. For the other, each step takes about a *million* times as long. Which is which? The reading explains why the second one behaves that way — give the explanation.
- **Q4.** In run 4 you sent a graded electrical signal a long way. Describe what arrived at the far end (the *Arrives at the far end* line in The neural signal section tells you), and what the vehicle did about it.
- **Q5.** Using Q1 to Q4, write one sentence stating the problem a neuron solves. Then say who has that problem and who does not, and why. The reading's table comparing plants, fungi and animals is what this question is about.

## Part 2: Taking the Cell Apart (≈21 minutes)

### Goal
Now open the cell. The **Neurons** tab tells you what it computes. The **Membrane** tab tells you how it manages that physically. In every experiment below you throw one switch and look at all three tabs.

### Instructions and What to Record

**Step 1 — Reproduce the reading's example.** Open the **Neurons** tab. Make sure the **LEFT** neuron is selected — the banner at the top of the panel says which. Under *Wiring*, set the baseline b₀ to **5** spikes per second, the first connection strength b₁ (from the left sensor) to **+2**, and the second, b₂ (from the right sensor), to **−3**. Under *Sensor Neuron Activity*, set the first input x₁ to **10** spikes per second and the second, x₂, to **0** — moving an input slider switches the inputs from the vehicle's sensors to the sliders, and the panel says so. (The vehicle carries on driving on whatever the neurons put out; it will drive oddly for the rest of this step, which is fine.)
- **Q6.** What output rate does the panel measure? Now raise the second input to **5** without touching the first, and report the output. Then raise the second input to **15**. For each of the three, write out the arithmetic the panel prints, say what number the arithmetic gives, and say what the panel actually reports as the *measured* output rate. Those two are not the same — at these totals the measured rate is well below the arithmetic, and in the third case it is a few spikes rather than none. Explain why not, and what a real cell is doing that the arithmetic alone does not capture.

**Step 1b — Look at the function itself.** Underneath the arithmetic is a small plot: the total arriving input along the bottom, the output rate up the side, and a dot showing where the cell is sitting right now. It draws two curves. The dashed one is what the arithmetic predicts. The solid orange one was measured from the membrane simulation, by sweeping the input and counting spikes — leave it for now; it is Q25's. Watch the dot move as you change the sliders. Raise x₂, the input on the inhibitory connection, until the dot runs off the bottom of the rising part, then set x₂ back to 0 and raise x₁ as far as it goes: the dot climbs more and more slowly. The sliders cannot push the cell all the way to the top of the curve; the curve itself shows where it would go.
- **Q7.** Describe the shape of the measured curve. It is flat on the left, rising in the middle, and levelling off on the right. Say what the flat part on the left means about the cell, and what the levelling-off on the right means. The reading gives a reason for each — give both. Then answer this: if the curve were a straight line the whole way, with no flat parts at all, what would this cell be doing that a real neuron cannot?

**Step 2 — The same output, two ways.** Leave the vehicle running and find the **Time window for the output** slider, under *Output Options*; the spike display it changes is at the bottom of the right panel. Slide it from one millisecond to one second and back.
- **Q8.** Describe what the output looks like at each end of that slider. At one end you are looking at something that is either there or not there. At the other you are looking at a number that can land anywhere in a range. Are those two competing descriptions of the neuron? Answer using what §3.2.6 of the reading says about time scales.

**Step 3 — Watch one spike.** Before this step, go back to the Neurons tab and set **Where the inputs come from** back to the vehicle's sensors, so the neuron is being driven by the world again. Then open the **Membrane** tab. It opens in slow motion, ten times slower than life, and the vehicle all but stops — that is the time scale, not a fault; the badge over the arena names it. Let a single action potential run, using **50× slow** or **step one spike** if it goes by too fast. Under the voltage trace, *The gates* section shows three meters: sodium activation, sodium inactivation, and potassium.
- **Q9.** Describe the order of events. Which gate opens first, which one closes during the spike, and which one is slow to arrive and slow to leave? Match each phase you describe to the rising and falling parts of the voltage trace.

**Step 4 — Turn off the pump.** Press **real time** first — a simulated minute in slow motion is ten real ones. Then, under *Lesions*, set **Sodium-potassium pump power** to zero and let the simulation run for a simulated minute (a real minute on a clock is fine; the *Run time* line in the World tab's Motion Comparison section keeps count). Open the *Concentrations* and *Energy (ATP)* sections on the right so you can watch them.
- **Q10.** Report what happened to the resting voltage, to the spikes, and to the ATP counter. The reading says a neuron doing nothing at all is still spending energy, and that what it is buying is readiness. Use what you just watched to explain that sentence.

**Step 5 — Block the sodium channels.** Restore the pump (the *Restore healthy membrane* button does it). Set **Sodium channels blocked** to 100%, then, on the Neurons tab, set x₁ to **10** with the slider so the cell is getting a steady input. The *Spikes and conduction* section on the Membrane tab reports what reaches the far end of the axon.
- **Q11.** What happened to the voltage at the cell body, and what arrived at the far end of the axon? Connect this directly to your Q4 answer: you have now seen the same failure twice, once as a design choice in Part 1 and once as a mechanism.

**Step 6 — Remove the refractory period.** Restore the sodium channels. Set **How fast sodium channels reset** to instant, go back to the Neurons tab, and look at the measured curve from Q7 again.
- **Q12.** The curve has changed at both ends. Say what changed at the low-input end and what changed at the high-input end. The reading uses the refractory period to explain two separate things about neurons. Name both, and say which one you just watched change. Then say why letting the sodium channels reset instantly is what changed the top of the curve.

**Step 7 — Change what a connection does.** Return to the **Neurons** tab and set **Where the inputs come from** back to the vehicle's sensors. In the **LEFT** neuron, set b₂ — the connection from the right sensor, the one that crosses — to **−2**, so that it is inhibitory, and press **Mirror this wiring to the right neuron**. Watch the vehicle for a moment. Then set b₂ back to **+2** in the left neuron only, and watch again; then mirror it across once more, and watch again.
- **Q13.** The vehicle's behavior changed although nothing about its inputs changed. Explain what happened, using the reading's word **integration** — and say why flipping the connection in one neuron turned the vehicle, while flipping it in both changed which way it went. Then say why a cell that can only add would be less useful than one that can add and subtract. Finally, look at the *synaptic input* arrow in the Membrane tab's *Ions and the pump* section before and after you flip that connection. Flipping it did not change which neurotransmitter arrives. Using §3.3.5 of the reading, say what it did change, and explain how the same neurotransmitter can excite one cell and inhibit another.

## Part 3: Four Sick Neurons (≈25 minutes)

### Goal
Four vehicles — **N1**, **N2**, **N3** and **N4** — are all bad at finding light, and they are bad at it in ways that look the same from outside. Each one has a different thing wrong with it, and one of them has nothing wrong with it at all. Your job is to work out which is which.

**Two things you are being told in advance, because this part is about method rather than about catching you out.** First: **one of the four is not broken.** Deciding which one, and defending the choice, is part of the work. Second: **if you open a panel and everything on it looks normal, that is a result, not a dead end.** A cell can be perfectly healthy and still fail at a task, and a cell can compute exactly the wrong thing while every piece of its biology is in order.

### Instructions and What to Record

**Step 0 — Build the tool first.** Everything you did in Part 2 was a fault you caused on purpose, so you already know what each kind of fault looks like.
- **Q14.** Fill in this table from your Part 2 results. For each of the three tabs, say what a problem *at that level* would look like when you looked at each of the three tabs. Some cells will say "nothing unusual" — those are the useful ones.

| A problem in the… | …looks like this on the World tab | …on the Neurons tab | …on the Membrane tab |
|---|---|---|---|
| World (the task itself) | | | |
| Neurons (what the cell computes) | | | |
| Membrane (how the cell works) | | | |

**A worked example.** Before you start, open **N0**, which is diagnosed for you. In the World tab, N0 reacts to lights promptly but steers the wrong way. On the Neurons tab, its arithmetic shows a strong negative connection where the task needs a positive one, so the cell is computing a perfectly good function that happens to be the wrong function. On the Membrane tab, everything is normal: the resting voltage is where it should be, the gates open in the right order, the spikes are full size, the ATP cost per spike is ordinary. **N0's fault is at the level of what the cell computes, and the evidence for that is as much the healthy membrane as the odd arithmetic.** Notice the shape of the reasoning: a diagnosis is made by what is *ruled out* as much as by what is found.

**Step 1 — Watch.** Open the **Diagnosis** tab and load each of the four in turn. Each loads with its own world, already three-quarters of a minute into its run, so what you see is how it drives once it has been driving for a while; **Reset** replays the same run from that point. Give each one a minute, watching the arena and the Scorecard.
- **Q15.** Describe what each of N1, N2, N3 and N4 does. They will not all *move* the same way — one charges, one creeps, one sits and lunges. Say whether the way each one moves tells you *what is wrong with it*, and why or why not.

**Step 2 — Choose where to look, and commit.**
- **Q16.** For each of the four, say which tab you would open first and why, using your Q14 table. Then open it, and write down your diagnosis and your reason. Guessing is fine — committing to a guess before you have all the evidence is the point, and you will be asked to compare your guesses against the answers, not graded on them.

**Step 3 — Test the ones you cannot separate.** At least two of the four will still be ambiguous after Step 2. The reading gives you the way out: if two things behave the same, find the conditions under which they *stop* behaving the same. Things you can change: how fast the lights move (the World tab's speed control, and its **slow** button), how many lights there are, how long the neuron has to keep working without a rest (the Neurons tab's input sliders, pushed up and left there), and the sensor-to-actuator distance. The World tab's *Motion Comparison* section shows how fast the lights move beside how fast the vehicle can go.
- **Q17.** Describe the test you designed, what you predicted before running it, and what happened. If your first test did not separate them, describe that one too and what you tried next.

**Step 4 — Reveal.** Press **Reveal faults**.
- **Q18.** For each of the four, state what was actually wrong and which of the three levels the fault lives at. Then compare against your Q16 answers: which did you get right, and for the ones you got wrong, what misled you?
- **Q19.** One of the four had nothing wrong with it. Which one, and why is a cell that fires very rarely not a broken cell? Look at its **energy per light** on the Diagnosis tab's Scorecard beside the other three's, and beware of one of them: a broken pump is a cheap pump. Your answer to this question is the beginning of Part 4.

## Part 4: What It Costs, and What Three Descriptions Are For (≈20 minutes)

### Instructions and What to Record

**Q20 — Do the arithmetic.** The **Membrane** tab reports what a single action potential costs in molecules of ATP, for the cell in front of you. Open the **Brain Energy Calculator** on the same tab. It does *not* use that number — it uses a published figure for a whole cortical neuron, and it says why on its face; read that line. The number of neurons in a human brain is supplied. Set the average firing rate to **10 spikes per second** — roughly what you have been watching all hour — and record the power the calculator returns, in watts. Then work backwards: adjust the firing rate until the power comes out at about twenty watts, which is what a real brain actually uses, and record the rate you needed.

**Q21 — What follows from it.** The rate you just recorded is very low. Say what it implies about how many neurons in a brain can be firing at any one moment, and give the reading's term for activity that thin. Then answer this: is a brain in which most neurons fired most of the time a *better* brain that evolution failed to build? The reading gives two reasons the answer is no, and only one of the two is about energy — give both. Finally, most of us have heard that people use only ten percent of their brains. Using the number you just computed, say what is false in that claim, and what nearby true thing the claim appears to be a mangled version of.

**Q22 — Why a fifth.** *Write this answer before reading the next question.* A human brain is about two percent of body weight and uses about twenty percent of the body's energy at rest. Write the best explanation you can for why humans invest that much. Give the argument you would defend.

**Q23 — And what was wrong with it.** Now the comparative figures. A human neuron costs roughly what a chimpanzee's neuron costs; what is unusual about a human brain is how many neurons are in it, not how expensive each one is. Given that, what was wrong with the explanation you wrote in Q22 — not with your reasoning, but with the question it was answering? If your Q22 answer treated twenty percent as an achievement, say what it should be read as instead.

**Q24 — Which vehicle is better.** In Part 1 you ran a vehicle that signalled by diffusing chemical, in a slow world, and it did fine. The reading, not the app, tells you what a chemical signal costs; take it that the chemical vehicle was far cheaper to run. You also ran a spiking vehicle in a fast world. Which of the two is **better adapted**? Which is **better**? Explain why those are not the same question. Then apply the same reasoning to the figures in Q23: humans spend about a fifth of the body's resting energy on the brain, other primates about a tenth, and other mammals less than that. Is that a ranking of anything?

**Q25 — Two curves.** Go back to the **Neurons** tab and look again at the plot under the arithmetic, which draws two curves on the same axes: the dashed one the arithmetic predicts, and the solid one measured from the membrane simulation as the cell actually fires. Describe where the two agree and where they part company. Then answer this: is the measured curve the *right* one, with the predicted curve a rough approximation of it? Or is that the wrong way to describe how the two are related? Use what the reading says in §3.3.4 about Hodgkin and Huxley's model of a neuron sitting beside the model in §3.2.8.

One caution, and it matters. §3.2.9 of the reading describes a much larger claim about what the simple model leaves out: that a neuron's branching input surface computes enough on its own that a single cortical cell may be better understood as a small network several layers deep. **The simulation in front of you cannot show that claim at all**, because the cell it models has no branching input surface. Say what the two curves do establish, and what they do not.

**Q26 — Which panel answers which question.** Here are four questions about a single neuron. For each one, name the tab that can answer it, and say why the other two tabs are silent.
- What will this cell do if a third input arrives at 20 spikes per second?
- How long after the voltage crosses threshold does it reach its peak?
- What happens to the vehicle if this connection changes sign?
- Why can this cell not fire a thousand times a second?

Then one more, which is the point of the four questions above. Those four make the three levels look like three separate compartments, each minding its own business. §3.3.9 of the reading says something stronger: the levels are *separable but not independent*, and the implementational level sets terms the levels above it have to respect. You produced an example of exactly that in Q21 and Q22 — an energy budget, which is an implementational fact, deciding how many neurons can be firing at once, which is a fact about the algorithm. Explain that example in your own words, and say what it costs the picture of three tidy compartments.

**Q27 — Turn it on the simulation.** Nothing in the Membrane tab plays back a recorded spike. The shape you have been watching all hour is calculated, moment by moment, from equations Hodgkin and Huxley wrote in 1952 — and when they first used those equations, the curve that came out had the right shape, height, duration and travelling speed, none of which they had fitted the equations to. Why does that matter more than if they had fitted them? What would you be entitled to conclude in each case?

## Completing the Lab Assignment
- Make sure you answer all the questions in the document neuron_lab_report.docx.
- Make sure you have added everyone's name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
