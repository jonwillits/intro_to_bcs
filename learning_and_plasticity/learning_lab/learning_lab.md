# Lab 5

Lab 4 ended with an animal walking into poison. The world had changed — the food odor now came from a toxin — and the animal's weights had not, so it kept approaching for as long as you let it. Then you fixed it in a few seconds, by moving one number, and the last question asked what would have to be added to the animal for it to do that for itself. In Lab 4 you were the only thing in the room that could change a weight.

This week that job is taken away from you and handed to a rule. It is the same animal in the same dish, with the same sensory cells, the same interneuron, and the same two motor groups. One thing has been added: the weights can now change by themselves. Your new job is choosing what a weight change is allowed to depend on.

That turns out to be the whole question. This week's reading describes four kinds of learning, and says that what separates them is not what they change, since all four change a weight. What separates them is how much of the world has to reach that weight before it will move. In Part 1 you hand the weights to the simplest rule there is and find out why that does not save the animal. In Part 2 you run a real experiment that tells two rules apart, and then try all four kinds of learning on one problem. In Part 3 you watch credit travel backward across a delay. The closer shows that a learned response that has faded away has not been unlearned.

## Part 0: Opening the Simulation (≈3 minutes)

1. Open the simulation in your web browser: [Learning](https://jonwillits.github.io/bcogapp/#/m05-learning). As before, it runs in any modern browser, and there is nothing to install.
2. Download the lab report Microsoft Word document. It is available here: [Lab 5 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/learning_and_plasticity/learning_lab/learning_lab_report.docx) This document is what you will turn in to the course website.

Everything you learned to read in Lab 4 is still here and still means what it meant. The rest of this section covers what is new.

### Skip ahead, and why you will need it

**Learning in this dish takes minutes, not seconds.** A weight can only change when something happens to the animal, and the animal reaches something only two or three times a minute. So at the bottom of the screen, beside the play button, there are two new buttons: **Skip ahead 1 min** and **Skip ahead 3 min**. They run the dish forward without drawing it, which takes about a second on any computer. Nothing is left out. Every weight, every counter and every plot records straight through the skip, exactly as if you had watched it. Presses add up, so two presses of *Skip ahead 3 min* is six minutes.

**Whenever a step says "run for three minutes", press Skip ahead rather than waiting.** Watch live when a step asks you to watch. The speed control also now goes up to 8×, if you would rather watch a run go by quickly.

**Reset is different this week.** It starts the run again from the same seed, with every slider, switch and rule choice where you left it, and it puts **the weights back where the run started**. That is what lets you change one setting and compare two runs. If you set a weight by hand on the Circuit tab, that counts as a new starting value.

### World

The *World* tab's **Scenario** menu now lists six set-ups: *Part 1a*, *Part 1b*, *Part 2a*, *Part 2b*, *Part 3*, and the *Closer*. Some scenarios have controls of their own, which appear on this tab when you load them: buttons to move between **phases**, an **interval** slider, a switch or two. On the right, a new readout called **What the world does** says, in a line or two, what reaching each thing in the dish currently does to the animal. Several scenarios change that while you watch, so check it rather than trusting your memory. Below it the scorecard reports **Meals per minute**, **Harm**, and, where the dish has marked sites, **Sites touched** and **Touched and found nothing**.

### Circuit

The *Circuit* tab is Lab 4's, with one section added at the top of the right panel: **The weight trace**. It plots every weight over the last five minutes of the run. The bottom axis is run time in minutes and seconds, a white line marks where the run started, and a dotted line marks the value each weight started at. Under the plot, each weight is printed as *at the start 1.00 · now 1.82*. This plot is the instrument the whole lab is read through. The weight sliders on the left are still live, and you will see them move by themselves.

### Learning

The *Learning* tab is new. Every connection the rule is allowed to move changes by the same arithmetic:

> Δbᵢ = η · xᵢ · Φ

The change in a weight is that connection's own input, xᵢ, times a **third factor**, Φ, scaled by the **learning rate**, η. The left panel's main control is a set of four cards that decide **what supplies Φ**: **Coincidence**, **Prediction**, **Teacher**, or **Verdict**. These are the reading's four kinds of learning, from §5.2.7, and each card says what it needs. Most scenarios hold the rule at one setting and grey out the rest. Below the cards are the **learning rate η** slider, and, where a scenario uses them, the **eligibility trace window** and the **discount γ**. At the bottom are two switches under **Bounds**, **Weakening** and **Competition**. **Both are off when you begin, on purpose.**

The right panel shows what the rule is doing. **The arithmetic** prints the equation above for every connection, with the live numbers in it. **The signal trace** plots Φ over the last minute, whatever Φ currently is. Other sections appear in the scenarios that need them.

### Chemistry

The *Chemistry* tab has Lab 4's four modulators, still named for what they do. One thing has been added, and this time it is named for its molecule: **dopamine — the broadcast signal**. It is not a slider, because it is not a level you set. It is a number the animal generates, and a plot on the right shows it over the last minute. Lab 4 made you work out which molecule each control was. The reading's §5.3.7 names this one outright, so the panel does too.

## Part 1: Let the Weights Change (≈18 minutes)

### Goal

The reading's §5.2.1 gives the oldest and simplest rule for changing a weight: Hebb's rule, Δb₁ = ηx₁y. In this lab it is the **Coincidence** setting, where the third factor is y, the receiving cell's own output. Find out what it does, and then find the three things the reading's §5.2.3 says it cannot do.

### Instructions and What to Record

**Step 1 — The failure.** On the World tab, load **Part 1a — Let the weights change**. This is Lab 4's last dish exactly: the food odor marks a toxin, and the animal's one weight, b₁, is 1.00. **Leave b₁ where it is for this first run.** Open the Circuit tab and watch the weight trace and the b₁ slider for about a minute. Nobody is touching the slider. Then go to the World tab, note the **Harm**, press **Skip ahead 3 min**, and note it again. Finally, go to the Learning tab, untick **Learning on**, press **Reset**, skip ahead the same four minutes, and record the harm once more. Tick **Learning on** again when you are done.

| | b₁ at the start | b₁ after 4 minutes | Harm after 4 minutes |
|---|---|---|---|
| Learning on | | | |
| Learning off | | | |

- **Q1.** Report your table. With the rule switched on, what did the weight do, and did it ever go down? What did the harm counter do, and how did it compare with the run where nothing could change? Lab 4's closer asked what would have to be added to the animal for it to fix itself, and the obvious answer was "let its weights change". Say what this run shows about that answer.
- **Q2.** Look at the rule on the Learning tab, Δb₁ = η · x₁ · Φ with Φ = y, and at the numbers in **The arithmetic** while the animal is near a plume. Say in words what has to be true at a connection for its weight to grow. Then say what is missing: what would the rule have to be sensitive to, in order to do this animal any good? The reading's §5.2.3 has a sentence that says it exactly; find it and use it.
- **Q3.** Press Reset and open the Chemistry tab. Watch the **Dopamine** plot while the animal eats a few poisoned meals. What does the signal do at each meal? The panel says what a value above zero, below zero and at zero means. So something in this animal does register that things went badly. Explain why that makes no difference to the weight in this scenario. What is the rule listening to instead?

**Step 2 — What coincidence does.** Load **Part 1b — Salt, then food**. The places marked by the pale glow are salt, which this animal ignores: look at the Circuit tab and you will see its weight, b₂, is 0. When the animal happens to touch a salt site, the salt lingers for a second and a half and dissolves, and food arrives there. The food-odor connection, b₁, is innate, and the rule cannot move it; it is drawn as a dashed line on the weight trace. Watch the dish and the weight trace together for a minute or two, until the animal has eaten a few times. Then skip ahead three minutes. When the salt weight has stopped climbing, go to the World tab, make sure **Source to place on a click** reads *salt*, and click the floor somewhere far from the animal to put down a patch of salt with no food under it. Watch what the animal does about it.

- **Q4.** Describe what happened to the salt weight: what it started at, roughly how much it gained at each of the first few meals, what happened once it passed the threshold θ = 0.35, and where it ended. How did the naive animal find salt sites at first, and how does it find them now? What did it do about the patch of salt you placed? This is the reading's rat and tone from §5.2.2, in a dish. Say which part of the dish plays the tone, which plays the food, and what plays the connection that strengthened.
- **Q5.** The salt weight grew slowly at first and then very fast. Use the rule to explain the change of pace. What starts happening once salt alone can make the interneuron fire, and why does that make the weight grow faster still? The reading's §5.3.5 names this kind of process, and says what such processes do.

**Step 3 — The learning rate.** On the Learning tab, find **One occasion, by hand** in *The arithmetic* section. It multiplies the learning rate on the slider by two firing rates you type in, and it starts with both at 40, the reading's own example. Read the result with **learning rate η** at 1 and then at 0.01. Then run the dish both ways. Set η to 1, press Reset, and watch live: read off the weight trace's time axis how long the salt weight takes to reach 3.00. Set η to 0.01, press Reset, skip ahead three minutes, and record the salt weight and the **Meals — total count**. Set η back to 0.3 when you are done.

| Learning rate η | By hand, with both rates at 40 | What the salt weight did |
|---|---|---|
| 1 | | reached 3.00 after about: |
| 0.01 | | after 3 minutes it was: , over this many meals: |

- **Q6.** Report your table. Do the two by-hand numbers match the reading's §5.2.1? In the dish, a meal lasts about a second, with the salt cell and the interneuron both at 1 while it lasts. So use the rule to work out what one meal should add to the salt weight at each learning rate, and check your answer for η = 0.01 against the run: divide the weight it reached by the meals it took. About how many meals at η = 0.01 move the weight as far as one meal does at η = 1? The reading says that being slow is what lets a low learning rate ignore coincidences, and being fast is what makes a high one treat an accident as a rule. Describe one situation in this animal's life where you would want the high setting, and one where you would want the low one. Which of §5.1.12's three problems is this slider?

**Step 4 — Three things coincidence cannot do.** Each of these is a run. Press Reset before each, and put each control back afterward.

*Indifferent to outcome.* On the World tab, switch on **A second cue, almond odor, at every site**, press Reset, and skip ahead three minutes. Look at the weight trace. There are two plastic weights now, salt and almond odor. **They lie exactly on top of each other, so you will see one line**; read the two values printed under the plot. Switch the second cue off again.

*Cannot bridge a delay.* Set **Interval between the touch and the food** to 10 s and press Reset. Watch one touch live: the salt is gone well before the food appears. Then skip ahead until the run time is about five minutes and record the salt weight. Set the interval back to 0.

*Can only add.* Go back to **Part 1a**. On the Circuit tab, drag b₁ to about −2, and skip ahead three minutes. Then press Reset, which now starts from your −2, and try b₁ = 0.1.

| Run | What you set | Weights after the run |
|---|---|---|
| Second cue, 3 minutes | almond odor at every site | salt: ; almond odor: |
| Delay, 5 minutes | interval 10 s | salt: |
| Part 1a, 3 minutes | b₁ = −2 | b₁: |
| Part 1a, 3 minutes | b₁ = 0.1 | b₁: |

- **Q7.** Report your table. For the second cue: the animal learned about almond odor exactly as much as about salt. Did it have any way of telling which one mattered? For the delay: the animal still ate, and salt still came before every meal. Use the rule to say why the weight barely moved, naming the term that was zero and when. These are the first two of §5.2.3's three limitations. Name them.
- **Q8.** With b₁ at −2 the animal avoided the toxin, which is what you want, and you put that weight there. Did the rule move it? With b₁ at 0.1, what happened? Use the rule, and the fact that y only fires once b₁x₁ passes the threshold, to explain both results. Then answer the question §5.2.1 ends on: a rule like this one can make a connection stronger. Can it, by learning, arrive at an inhibitory connection like the −2 you set by hand? Why not?

**Step 5 — The bounds.** Load **Part 1b** again, set η to 1, and skip ahead three minutes with both bounds off. On the Circuit tab, look at the weight trace. On the Learning tab, look at **The signal trace**, where the dashed blue line is the verdict over the last minute: roughly what fraction of that minute is it switched on? Then, on the Learning tab, switch on **Weakening**, press Reset, and skip ahead five minutes. Do the same with **Competition** on and Weakening off. For the last run, leave Competition on and also switch on the second cue on the World tab. Switch everything off again and set η back to 0.3 when you are done.

| Bounds | Salt weight at the end | Did the weight trace ever go down? | Roughly what fraction of the last minute was the verdict on? |
|---|---|---|---|
| Both off | | | |
| Weakening on | | | |
| Competition on | | | |
| Competition on, with the second cue | salt: ; almond odor: | | |

- **Q9.** Report your table. With both switches off, what has the animal become, and why is a cell that responds to everything useless? The reading's §5.3.5 says two things bound this, and the panel's notes say how each one works here. Describe what each switch did to the trace. For competition with two cues, say what happened to the amount each connection could hold, and find the reading's sentence about an input that "loses ground it already held". Finally: §5.2.1 named a limitation at the algorithmic level, and §5.3.2 answered it at the implementational level. Say what the limitation was and what the answer is.
- **Q10.** Here is a description of Step 2 that is tempting and wrong: *"The animal noticed that salt means food, so it learned to go to salt."* Rewrite it so that it says only what the wiring did. You may not say the animal noticed anything, worked anything out, or learned *that* anything means anything. The reading's §5.2.2 makes this demand and says why, and it points back to something you did in Lab 2. Say what the two cases have in common.

## Part 2: Where the Number Comes From (≈25 minutes)

### Goal

On a single cue, the Coincidence setting and the Prediction setting look alike: pair a cue with food and its weight goes up. The reading's §5.2.4 describes an experiment that tells them apart, and it is one the field actually ran. Run it under both rules. Then put all four kinds of learning on one problem, and ask of each one where its number came from.

### Instructions and What to Record

**Step 1 — Blocking, under Coincidence.** Load **Part 2a — Blocking**. The dish has three **phases**, and you decide when each one ends, with the *Go to phase* buttons on the World tab. In phase 1 salt alone marks the food. In phase 2 almond odor is added at every site, alongside the salt, and the food is unchanged. In phase 3 almond odor marks places on its own, and there is nothing there. Changing phase changes the dish and nothing about the animal: its weights carry over.

On the Learning tab, make sure the rule is **Coincidence**. Skip ahead three minutes at a time **until the salt weight has stopped climbing**, and record it. Press **Go to phase 2**, skip ahead four minutes, and record both weights. Press **Go to phase 3** and watch the animal for a minute: does it go looking for almond odor?

**Step 2 — Blocking, under Prediction.** On the Learning tab, choose **Prediction**. Press Reset, which puts the weights back and returns you to phase 1. Do exactly the same thing. Under this rule the salt weight takes longer to stop climbing, usually three to five minutes; do not move on until the trace is flat. While you wait, open **One algorithm, written down twice** on the Learning tab and watch it during a meal.

| Rule | Salt weight when it stopped climbing | After phase 2: salt | After phase 2: almond odor | Phase 3: does it seek out almond odor? |
|---|---|---|---|---|
| Coincidence | | | | |
| Prediction | | | | |

- **Q11.** Report your table. In phase 2, almond odor and food were perfectly paired: every almond site had food, under both rules. Under which rule did the almond weight grow, and under which did it barely move? What did each animal then do in phase 3?
- **Q12.** Explain the Prediction result with the numbers. Under that rule Φ = a − p, what arrived minus what was predicted. At the first meal of phase 1, what was p, and so how big was the error? At the first meal of phase 2, what was p, and how much error was left for almond odor to learn from? The reading's §5.2.5 does this arithmetic with 0.95 and 0.05. Then explain the Coincidence result: what was that rule multiplying in phase 2, and why did it have no way to know that the food was already accounted for?
- **Q13.** The reading's §5.2.4 says what a rat actually does when it is tested on the light alone. Which of your two animals behaves like the rat? So one of these two rules is wrong as an account of how that animal learns. Say which, and say what the experiment shows that learning tracks. Why did the instructions insist that you wait until the salt weight stopped climbing before adding the second cue? What would you expect if you had moved to phase 2 early?
- **Q14.** The panel **One algorithm, written down twice** shows Rescorla and Wagner's rule above Widrow and Hoff's, with one set of numbers flowing through both while a meal is arriving. Copy down what it showed at one meal. Which term in the upper equation is which term in the lower one? One of these was written by people explaining a rat, and the other by people building a circuit, twelve years apart. What does the reading say that shows, and which idea from Module 1 is it an example of?
- **Q15.** Under Prediction, the signal trace section prints **The held prediction p**, and says how long ago it was made. The reading's §5.2.6 says this is what earns prediction learning a name of its own, even though its arithmetic is the same as a teacher's. What has to be generated, when, and held until when? Does the Coincidence rule hold anything? Why does the reading say that calling b₁ "a prediction" under Hebb's rule is our description rather than the mechanism's?

**Step 3 — Four signals, one problem.** Load **Part 2b — Four signals, one problem**. Two sites are marked by salt and two by almond odor. One kind holds food, and the other holds nothing; *What the world does* says which. A switch on the World tab, **Almond odor marks the food**, flips which is which. Everything about this dish is held still while you change one thing: the rule.

For each of the four settings in turn: make sure *Almond odor marks the food* is **off**, choose the rule on the Learning tab, and press Reset. Press **Skip ahead 3 min** and record both weights. Then switch **Almond odor marks the food** on, which does not reset anything, skip ahead three more minutes, and record both weights again. This takes minutes of dish time because the animal touches a site only two or three times a minute, which is why you are skipping rather than watching. Under the Teacher setting, read what the signal trace section says about where the target comes from.

| Rule | After 3 min — salt | After 3 min — almond odor | 3 min after the flip — salt | 3 min after the flip — almond odor |
|---|---|---|---|---|
| Coincidence | | | | |
| Prediction | | | | |
| Teacher | | | | |
| Verdict | | | | |

- **Q16.** Report your table. For each of the four rules, say in a sentence what it learned in the first three minutes, and what it did about the flip. One of the four could not tell the cue that marks food from the cue that marks nothing, and could not let go of anything afterward. Which, and why? One of them stopped changing the weight well short of 1. Which, and what was it waiting for before it stopped?
- **Q17.** This is the reading's table `t-teaching-signals`, and you have just filled it in by running it. For each of the four settings, say what Φ was, and where that number came from: the connection itself, the world a moment later, something that already knew the answer, or one number about how things went.
- **Q18.** Now rank the four by how easily an animal in a dish could actually get hold of that number, from easiest to hardest, and defend your ranking. For the Teacher setting, the panel told you where the target came from in this simulation. Where would a real worm get one? If you met machine learning before this course, you probably met the teacher's kind of learning first, and thought of it as the basic case. What does the reading's §5.2.7 say about that, and why?

## Part 3: Credit Across Time (≈17 minutes)

### Goal

In Part 1, a ten-second delay defeated the Coincidence rule completely. The reading's §5.2.8 describes what it takes to bridge a delay and to hand credit to the thing that earned it: an estimate of how well things are going, a broadcast error, and a fading mark on whatever was recently active. Watch all three at work.

### Instructions and What to Record

**Step 1 — Read the panel first.** Load **Part 3 — The corridor**. The dish is now a lane. The animal starts at one end, and food waits at the other. On the way it crosses three stretches of colored floor, each sensed by a cell of its own: **the marker**, then **the turn**, then **the approach**. At some point in every trial a **passing vibration** washes through, pink, and leads nowhere. After every meal the animal is picked up and put back at the start. The rule is held at **Verdict**: Φ is δ, the broadcast signal, which is the dopamine of the Chemistry tab.

Before you watch anything, read the line in bold on the World tab. It is also at the top of the **Credit** section on the Learning tab.

- **Q19.** Copy that line out. The reading's §5.1.11 sorts learning into four tiers and places each on the animal tree. Which tier is this part of the lab about, and which animals does the reading say have it? Which tiers can a real nematode manage? So this part runs a rule in an animal that does not have it. The reading's §5.2.5 says something about Rescorla and Wagner's rat and Widrow and Hoff's circuit that explains why that can still be worth doing. Say what it is. Then say what you would be wrong to conclude about real worms from what you are about to see.

**Step 2 — Value seeping backward.** Open the Learning tab and find the **Credit** section. Its grid has one row for each finished trial and one column for each point in the chain. The green boxes are what the animal's value estimate holds each point to be worth. The pink box at the end is the **surprise at the food**: the size of the broadcast signal at the moment the meal lands. Watch the first four or five trials live, which takes about a minute, and watch the eligibility bars under the grid fade after the animal leaves each stretch of floor. Then skip ahead three minutes, and then one more. The grid keeps the oldest trial at the top and scrolls; the newest trial is at the bottom.

| | First trial on which its value passed 0.30 | On trial 1 | On about trial 30 |
|---|---|---|---|
| the approach | | — | — |
| the turn | | — | — |
| the marker | | value: | value: |
| Surprise at the food | — | | |

- **Q20.** Report your table. In what order did the three points gain value? Compare the grid with the reading's figure `f-td-chain`. The animal only ever eats at the far end of the lane. So how does the marker, which it crosses several seconds earlier, come to be worth anything? Use the words *estimate*, *next estimate*, and *bootstrapping*. The reading says that treating an unreliable estimate as a target sounds like a recipe for learning nothing, and then says why it works anyway. Why does it?
- **Q21.** What happened to the surprise at the food over the thirty trials? The food did not change. What did? Then connect this to the reading's §5.3.7: it describes what dopamine cells do when an outcome is better than predicted, worse than predicted, and exactly as predicted. Which of those is trial 1, and which is trial 30? One honest note sits under the dopamine plot on the Chemistry tab. Say what it says and why the reading bothers to say it.

**Step 3 — The trace window.** On the Learning tab, set **eligibility trace window** to 0, press Reset, and skip ahead three minutes. Look at the grid and at the weight trace. Then set the window to 10, press Reset, and skip ahead three minutes. Set it back to 3.

| Trace window | First trial on which the marker's value passed 0.30 | Surprise at the food at the end |
|---|---|---|
| 0 s | | |
| 3 s (from Step 2) | | |
| 10 s | | |

- **Q22.** Report your table. With the window at zero, what did the chain learn, and what happened to the surprise at the food? Explain it using what you watched the eligibility bars do: by the time the news arrives, what state is each connection in? What did the wider window change? The panel's note on this slider keeps two claims apart, one from §5.2.8 and one from §5.3.8. Say what each claim is, and why the second does not prove the first.
- **Q23.** Look at the weight of the **passing vibration** on the Circuit tab's weight trace, in any of your runs. The vibration was active before the food on every single trial, and the Coincidence rule of Part 1 would have strengthened it. What did this rule do with it? The reading's §5.2.8 explains this with a rat that grooms itself on the way to the food tray. Give its explanation in terms of the dish: what does the vibration do to the estimate of how well things are going, and what happens a moment later? This is the third of §5.2.3's limitations. Name it.

**Step 4 — How far ahead to care.** Set **discount γ** to 0.5, press Reset, skip ahead three minutes, and read the last row of the grid. Do the same at 0.99. Set it back to 0.9. The note under the slider tells you what an outcome ten seconds away is worth at each setting.

| Discount γ | An outcome 10 s away is worth | Last row of the grid: marker, turn, approach |
|---|---|---|
| 0.5 | | |
| 0.9 (from Step 2) | | |
| 0.99 | | |

- **Q24.** Report your table. At γ = 0.5, how far back along the chain did value get? At 0.99? Explain the difference using the note under the slider. The reading's §5.1.12 says some rate of discounting is unavoidable, and explains why an outcome in ten days cannot count as much as the same outcome in ten seconds. What goes wrong for an animal at each extreme?

## The Closer: Extinction Is Not Unlearning (≈10 minutes)

### Instructions and What to Record

Load **Closer — Extinction**. The rule is held at **Prediction**. Look at the Circuit tab's diagram: besides food odor and salt, this animal has four cells that report its situation rather than a smell. Two say which dish it is in, **dish one** or **dish two**, and two say which session this is, **session one** or, after a wait, **session two**. In this model, a connection from one of those four cells can only ever become *inhibitory*. That is a modeling choice, and what it stands for is this: what an animal learns about a place is that something does *not* hold there. The association itself is carried by the cue. The World tab's scorecard has a new number for this scenario, **Response to salt alone, here and now**, which is what the verdict would be to salt by itself, in the dish and the session the animal is currently in.

**Step 1 — Acquisition and extinction.** Phase 1 is acquisition: salt marks the food. Skip ahead four minutes, and record the salt weight and the response. Press **Go to phase 2**. Now salt marks nothing. Watch live for a minute: it takes only two or three touches for the response to fade. Skip ahead one more minute, and record every weight and the response. Then watch the animal for a moment.

| | Salt weight | dish one | session one | Response to salt alone |
|---|---|---|---|---|
| Before acquisition | 0.00 | 0.00 | 0.00 | |
| After acquisition | | | | |
| After extinction | | | | |

- **Q25.** Report your table. The response went back to roughly where it began. Did the salt weight? The reading's §5.2.11 calls one account of extinction "the tidy story". What is the tidy story, and what does your table say about it? Where did the learning that made the response fade actually go, and what is its sign? One more thing: after extinction the animal still heads for salt, even though its response has gone. Explain how both can be true. The approach steers on the salt weight alone, and the four situation cells never steer.

**Step 2 — The three returns.** **Pause the dish first**, with the pause button at the bottom of the screen. The first three buttons act instantly and work while the dish is paused, and pausing matters: salt still marks nothing, so an animal left running goes on touching empty salt sites, and the response you are trying to read fades again within a touch or two. Do these in order, from the one extinguished animal, reading the response after each. Check the weights printed under the weight trace before and after **Move** and **Wait**. For the last button, press play again: the delivered meal waits until the animal is clear of any salt, which can take up to half a minute, and the World tab says when it is waiting. Read the response as soon as the meal has landed.

| Button | What it does | Response to salt alone | Did any weight move? |
|---|---|---|---|
| (after extinction) | | | |
| **Move to the second dish** | the animal is in another dish | | |
| **Move back to the first dish** | | | |
| **Wait** | time passes, with no training of any kind | | |
| **Deliver one outcome** | one meal at its mouth, with no cue | | |

- **Q26.** Report your table. The reading's §5.2.11 names three findings. Match each of *renewal*, *spontaneous recovery* and *reinstatement* to the button that produced it. Two of the three moved no weight at all, and the response came back anyway. Use your Q25 table to explain exactly why it came back, and why it went away again when you moved the animal back. Could a weight that had simply decayed to its starting value have produced any of this?
- **Q27.** The reading says that something has to hold the original association and its later contradiction at the same time, and that something has to arbitrate between them. In this animal, what holds each, and what does the arbitrating? Then the practical question. The reading calls this the most consequential result in the chapter for anyone hoping to be rid of a learned response, whether the learner is a rat, a dog, or a person. Suppose a fear has been extinguished in a therapist's office. Say what your table predicts about the following week, in a different place.
- **Q28.** Every weight in this lab is, in the reading's word from §5.3.11, a *residue*. After all the salt and food this animal has been through, could you read off from its weights how many times it ate, or when, or which meal came first? What can its weights tell you? Use the reading's distinction between a *disposition* and a *record*, and say which one this lab's learning produces. Explain why words like *storage* and *retrieval* do not fit what you watched.
- **Q29.** In Lab 4 you asked what would have to be added to the animal for it to change its own weights, and this week you added it. Now ask the next question. What would have to be added to *this* animal for it to be able to tell us *when* it last ate, rather than only what tends to be worth approaching? The reading's §5.3.11 gives two experiments where a disposition stops being enough. Describe one, and say what the animal in it must have kept. That is Module 10, and you have just asked its question.

## Completing the Lab Assignment

- Make sure you answer all the questions in the document learning_lab_report.docx.
- Make sure you have added everyone's name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
