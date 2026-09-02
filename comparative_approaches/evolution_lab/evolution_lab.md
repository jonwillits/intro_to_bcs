# Lab 2

In Lab 1 you were a scientist who had found six varieties of a new organism, and your job was to work out how each one was built. This time the organisms are still there, but nobody has built them. They have a **population**: they reproduce, their offspring resemble them, and the offspring are not identical. Left alone in a world with food in it, a population like that changes.

Your job in this lab is to watch that happen, take the process apart to see what it needs in order to work, and then face the problem this week's reading is really about. You will be handed four populations that somebody else evolved, and asked why two of them are alike.

## Part 0: Opening the Simulation (≈3 minutes)

1. Open the simulation in your web browser: [Evolving Vehicles](https://jonwillits.github.io/bcogapp/#/m02-evolution). As before, it runs in any modern browser, and there is nothing to install.
2. Download the lab report Microsoft Word document. It is available here: [Lab 2 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/comparative_approaches/evolution_lab/evolution_lab_report.docx) This document is what you will turn in to the course website.

Most of the controls are the ones you already know. You can still left-click the ground to add a light and right-click to remove one, still drag to move the camera, and still click a vehicle to open its wiring panel. Five things are new:

- **Food is four patches that drift.** Each one gives out a steady trickle of energy and never runs out, but it wanders slowly across the floor, so a vehicle has to keep up with it. A patch's energy is **shared among everyone feeding on it**, and the closer you are the bigger your share — so crowding onto one patch costs you.
- **Moving costs energy.** The faster a vehicle's actuators are driven, the more it spends. A vehicle that races around the arena without finding anything will run itself down, and one that sits still spends almost nothing — but food drifts away from whoever is not following it.
- **There are no generations.** Nothing happens in rounds and nothing is reset. Each vehicle is born, lives about a minute, and dies of old age. The arena holds a fixed number at a time, so a new vehicle is born only when one dies — and the slot goes to whichever adult has stored the most energy. Offspring inherit their parent's wiring, with small random changes.
- **Colour now tells you the wiring.** In Lab 1 color was a label for the variety. Here a vehicle's body color is computed from its connection strengths, so two vehicles of the same color really are wired alike. The trait that is *inherited but has nothing to do with behavior* is the **mark** — the small bead each vehicle carries. Keep the two apart; you will need the difference later.
- **You cannot set the wiring by hand any more.** The sliders from Lab 1 are gone. Wiring is now something a vehicle inherits.
- **There is a panel showing the whole population at once**, not just one vehicle: where every individual's wiring sits, how much energy the population is gathering, and what colors the vehicles are.

## Part 1: Watch a Population Adapt (≈6 minutes)

### Goal
Before taking anything apart, see what the process does.

### Instructions
1. Press **Reset simulation** and leave every control at its default. The world already starts with food in it, so do not add any of your own for this part — how much food there is turns out to matter, and you want the default amount.
2. Turn the speed up and let it run until about **150 vehicles have been born**. The panel counts them for you under **Born since the start**. It should take a minute or two.
3. Watch the world, and watch the population panel beside it — especially the cloud showing where every individual's wiring sits, and the **mark** distribution underneath it.

### What to Record
- **Q1.** Describe what happened over that run, in everyday language. Don't try to be technical. Write it the way you would tell a friend what you just watched.
- **Q2.** From the population panel, write down **how many were born** by the time you stopped, **births per minute early on** and **now**, and — from the mark distribution — **which mark most of the population ends up wearing**, and what percentage wear it.

> Keep your answer to Q1 exactly as you first wrote it. You will be asked to come back to it in Part 4.

## Part 2: What the Process Actually Needs (≈18 minutes)

### Goal
The reading says evolution by natural selection needs three things to be true of a population: **variation**, **inheritance**, and **differential reproduction**. That is a claim you can test, because this simulation lets you switch each one off.

### Instructions
Run each of the following as a separate experiment. Each time, press **Reset simulation** first — it redraws the *identical* founding population, so the only thing that differs is the switch you threw. (The button beside it, **New seed**, draws a different founding population; do not use it here, and remember that it exists — Q20 comes back to this.) Run each one until about 100 vehicles have been born.

1. **Take away variation.** Set the **mutation rate** to **0** and run.
2. **Take away inheritance.** Restore mutation, set **inheritance** to **off** (offspring now get random wiring), and run.
3. **Take away selection.** Restore inheritance, set **selection** to **off** (parents are now chosen at random), and run. Then run it a **second time from the same starting population** and compare the two outcomes.
4. **Shrink the population.** Turn selection back on and set **How many the arena holds** to its smallest value. Run it a few times. A population this small can die out altogether — if your arena empties, that is a result, not a crash, and it is worth recording how often it happened.
5. **Change the world.** Restore all the defaults and let a population evolve until about 100 have been born. Then, without resetting, switch the **Light regime** from **Food** to **Poison** and keep running.

### What to Record
- **Q3.** With mutation set to zero, what happened? Did the population improve at all, and did it keep improving? Explain what this tells you about where the wiring the population ends up with *came from*.
- **Q4.** With inheritance off, what happened, and why?
- **Q5.** With selection off, the population still changed. Describe how it changed, and describe how your two runs from the same starting point differed from each other. Change without selection is called **drift**. The reading gives three reasons two things can end up alike: shared origin, shared problem, and coincidence. Which of the three is drift a source of?
- **Q6.** With a very small population, did the best variety always win? Describe what you saw.
- **Q7.** When you switched the lights to poison, what happened to a population that had been doing well? The reading says an adaptation is "a fit between a creature and a particular set of circumstances." Use what you just watched to explain what that sentence means, and what it rules out.
- **Q8.** Someone watching Part 1 says: *"the lights taught the vehicles to steer toward them."* Using your Q3 and Q4 results, explain exactly what is wrong with that sentence.

## Part 3: Four Populations (≈25 minutes)

### Goal
This is the part the week's reading is about. Two things are alike. Why?

Open the **Lineages** tab. It holds four populations — **W**, **X**, **Y**, and **Z** — that were evolved before you got here. Nothing evolves in this tab: these populations are finished, they do not breed, and the food does not run out, so a light you place stays where you put it for as long as you want to watch. You can run them, put lights wherever you want, and watch them. What you cannot see yet is their wiring or their ancestry. Both are hidden, and you will unhide them in stages. **Do not unhide anything until the step that tells you to.**

### Instructions and What to Record

**Step 1 — What is each one doing?** Put a single light in the middle of the floor and watch all four.
- **Q9.** Describe what each of W, X, Y and Z does. Then group them by **job**: which of them are getting to the light and staying there, and which is not?
- **Q9b.** One of the populations that gets to the light does it in a way the others plainly do not. Which one is it, and describe how it moves. Does it still count as doing the same job as the others? Say why or why not.

**Step 2 — Commit to an answer.** For every pair you grouped together in Q9, you now have to say why they are alike, using this week's vocabulary, *before* you are allowed to look.
- **Q10.** For each similar pair, say whether you think the resemblance is a **homology**, an **analogy**, or a **coincidence**, and give your reason. Guessing is fine. Committing to a guess is the point.
- **Q10b.** Is there anything *other* than how they behave that makes any two of these four look like they belong together? Write down what you notice, and say whether you think it means anything.

**Step 3 — Look inside.** Now press **Reveal wiring** and click into each population's vehicles, using the same panel you used in Lab 1.
- **Q11.** For each of W, X, Y and Z, record whether the wiring is ipsilateral, contralateral or fully connected, and whether the connections are excitatory or inhibitory.
- **Q12.** At least two populations that **do the same job** are wired differently. Which ones, and what does that tell you? Answer using the reading's terms **behavioral equivalence** and **mechanistic equivalence**. Then look back at your answer to Q9b: does the wiring explain the way that population moves?

**Step 4 — Look at the history.** Now press **Reveal tree**, and then open **True history** to see all four on one tree with their founders.
- **Q13.** Which resemblance turned out to be homology, which turned out to be analogy, and which turned out to be neither? For each, say how the tree tells you so. Then go back to your Q10 answers. Which did you get right, and what misled you on the ones you got wrong?

**Step 5 — Break them.** The reading gives a rule for finding out whether two systems really do the same thing: find out whether they **break the same way**. You now know that one of these populations is wired differently from the other two. In the world you have been using, that difference shows up as exactly one thing — the way it travels. Your job is to find a world where it shows up as something more. Things you can change: where the lights are and how many, whether a light sits on the floor or out on the raised ground beyond the arena wall, whether you remove a light part-way through while they are heading for it, and how much **sensor noise** there is. **Left-click the ground to add a light, right-click to remove one.** Unlike the food in the other tab, lights here stay where you put them and never run out, which is what makes a test you design repeatable.
- **Q14.** Describe the test you designed, say what you predicted before running it, and report what happened. Did the odd population do something the other two did not, beyond travelling the way it does? If your first test failed to separate them, describe that one too, and what you tried next.

## Part 4: What the Comparison Licenses (≈16 minutes)

### Goal
Step back from the simulation and ask what this hour actually established, and what it did not.

### Instructions and What to Record

**Q15 — The mark.** Look again at the mark you recorded in Q2. Nearly the whole population ended up wearing it. Write the best explanation you can for why that mark was favored in that world. Make it a good one — give the argument you would give if you had to defend it.

*(Do not read ahead until you have written Q15.)*

**Q16.** The mark does nothing at all. It is not sensed by anything, it does not affect energy, and it changes nothing about how a vehicle moves. (Body **color** is a different matter — that is computed from the wiring, so it means a great deal. The mark is the one that means nothing.) It became common because it happened to belong to the individual whose *wiring* was winning, and it was carried along for the ride.
- Given that, what was wrong with the explanation you just wrote — not with your reasoning, but with the question?
- The reading calls this kind of explanation a **just-so story**, and describes Gould and Lewontin's argument that not every trait is an adaptation. Explain their point using your own Q15 as the example.
- Here you were told the answer. In real biology, nobody tells you. What follows from that?

**Q17 — Your own words.** Copy the three sentences from your Q1 answer that come closest to describing the population as though it wanted something, tried something, learned something, or was heading somewhere. Then rewrite each one so that it says the same true thing without any of that. If you find you wrote no such sentences, say so, and write the three sentences you were most tempted to write.

**Q18 — Which population is better?** Population **Z** was evolved in a world where the lights were dangerous and food was spread everywhere, and it flees light. Population **W** was evolved in a world where the lights *were* the food, and it approaches light. You cannot move these two populations between worlds — the Lineages tab has no light regime — so answer it from what you have already seen: you watched a light-approaching population meet a poison world in Part 2, experiment 5. Which of the two populations is *better adapted*? Which one is *better*? Explain why those are not the same question, using what the reading says about the ladder of intelligence.

**Q19 — Turn it on the simulation.** You have spent an hour calling this evolution. It is a computer program with a few dozen dots in it. The reading gives three senses in which an artificial system can match a natural one: **behavioral equivalence**, **mechanistic equivalence**, and **engineering convenience**. Which one is this simulation, and how do you know? What did using it let you learn that you could not have learned by reading about evolution, and what would you be wrong to conclude from it?

**Q20 — One more run.** Here are two runs of the simulation. They reached different outcomes. The person who ran them changed one thing on purpose: the mutation rate. Here is the full log of both runs. *(See the report document.)*
- Name something else that differed between the two runs.
- What is the word the reading uses for that?
- What would you have to do differently to be able to say the mutation rate caused the difference?

## Completing the Lab Assignment
- Make sure you answer all the questions in the document evolution_lab_report.docx.
- Make sure you have added everyone's name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
