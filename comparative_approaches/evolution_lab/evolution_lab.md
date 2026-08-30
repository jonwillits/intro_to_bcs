# Lab 2

In Lab 1 you were a scientist who had found six varieties of a new organism, and your job was to work out how each one was built. This time the organisms are still there, but nobody has built them. They have a **population**: they reproduce, their offspring resemble them, and the offspring are not identical. Left alone in a world with food in it, a population like that changes.

Your job in this lab is to watch that happen, take the process apart to see what it needs in order to work, and then face the problem this week's reading is really about. You will be handed four populations that somebody else evolved, and asked why two of them are alike.

## Part 0: Opening the Simulation (≈3 minutes)

1. Open the simulation in your web browser: [Evolving Vehicles](https://jonwillits.github.io/bcogapp/#/m02-evolution). As before, it runs in any modern browser, and there is nothing to install.
2. Download the lab report Microsoft Word document. It is available here: [Lab 2 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/comparative_approaches/evolution_lab/evolution_lab_report.docx) This document is what you will turn in to the course website.

Most of the controls are the ones you already know. You can still left-click the ground to add a light and right-click to remove one, still drag to move the camera, and still click a vehicle to open its wiring panel. Four things are new:

- **A light is now food.** A vehicle gains energy while it sits in the light, and loses it otherwise.
- **The population breeds.** The simulation runs in **generations**. At the end of each one, the vehicles that gathered the most energy leave offspring and the rest do not. Offspring inherit their parent's wiring, with small random changes.
- **You cannot set the wiring by hand any more.** The sliders from Lab 1 are gone. Wiring is now something a vehicle inherits.
- **There is a panel showing the whole population at once**, not just one vehicle: where every individual's wiring sits, how much energy the population is gathering, and what colors the vehicles are.

## Part 1: Watch a Population Adapt (≈6 minutes)

### Goal
Before taking anything apart, see what the process does.

### Instructions
1. Press **Reset**, leave every control at its default, and place three or four lights around the floor of the pit.
2. Turn the speed up and let it run for **50 generations**. It should take a minute or two.
3. Watch the world, and watch the population panel beside it.

### What to Record
- **Q1.** Describe what happened over those 50 generations, in everyday language. Don't try to be technical. Write it the way you would tell a friend what you just watched.
- **Q2.** Write down the **generation number** you stopped at, the **average energy** the population was gathering at generation 1 and at generation 50, and the **body color** of most of the population at the end.

> Keep your answer to Q1 exactly as you first wrote it. You will be asked to come back to it in Part 4.

## Part 2: What the Process Actually Needs (≈18 minutes)

### Goal
The reading says evolution by natural selection needs three things to be true of a population: **variation**, **inheritance**, and **differential reproduction**. That is a claim you can test, because this simulation lets you switch each one off.

### Instructions
Run each of the following as a separate experiment. Each time, press **Reset (same seed)** first, so that you start from the identical founding population and the only thing that differs is the switch you threw. Run each one for about 30 generations.

1. **Take away variation.** Set the **mutation rate** to **0** and run.
2. **Take away inheritance.** Restore mutation, set **inheritance** to **off** (offspring now get random wiring), and run.
3. **Take away selection.** Restore inheritance, set **selection** to **off** (parents are now chosen at random), and run. Then run it a **second time from the same starting population** and compare the two outcomes.
4. **Shrink the population.** Turn selection back on and set **population size** to its smallest value. Run a few times.
5. **Change the world.** Restore all the defaults and evolve a well-adapted population for 30 generations. Then, without resetting, switch the **light regime** from **food** to **poison** and keep running.

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

Open the **Lineages** tab. It holds four populations — **W**, **X**, **Y**, and **Z** — that were evolved before you got here. You can run them, put lights wherever you want, and watch them. What you cannot see yet is their wiring or their ancestry. Both are hidden, and you will unhide them in stages. **Do not unhide anything until the step that tells you to.**

### Instructions and What to Record

**Step 1 — Sort them by behavior.** Put a single light in the middle of the floor and watch all four.
- **Q9.** Describe what each of W, X, Y and Z does. Then group them: which ones behave alike?

**Step 2 — Commit to an answer.** For every pair you grouped together in Q9, you now have to say why they are alike, using this week's vocabulary, *before* you are allowed to look.
- **Q10.** For each similar pair, say whether you think the resemblance is a **homology**, an **analogy**, or a **coincidence**, and give your reason. Guessing is fine. Committing to a guess is the point.

**Step 3 — Look inside.** Now press **Reveal wiring** and click into each population's vehicles, using the same panel you used in Lab 1.
- **Q11.** For each of W, X, Y and Z, record whether the wiring is ipsilateral, contralateral or fully connected, and whether the connections are excitatory or inhibitory.
- **Q12.** At least two populations that behave the same way are wired differently. Which ones, and what does that tell you? Answer using the reading's terms **behavioral equivalence** and **mechanistic equivalence**.

**Step 4 — Look at the history.** Now press **Reveal tree**, and then open **True history** to see all four on one tree with their founders.
- **Q13.** Which resemblance turned out to be homology, which turned out to be analogy, and which turned out to be neither? For each, say how the tree tells you so. Then go back to your Q10 answers. Which did you get right, and what misled you on the ones you got wrong?

**Step 5 — Break them.** The reading gives a rule for finding out whether two systems really do the same thing: find out whether they **break the same way**. Two of these populations behave almost identically in the world you have been using. Your job is to design a world in which they do not. Things you can change: where the lights are, how many there are, whether a light sits on the floor or up on the rim, whether a light disappears part-way through, and how much **sensor noise** there is.
- **Q14.** Describe the test you designed, say what you predicted before running it, and report what happened. Did the two populations come apart? If your first test failed to separate them, describe that one too, and what you tried next.

## Part 4: What the Comparison Licenses (≈16 minutes)

### Goal
Step back from the simulation and ask what this hour actually established, and what it did not.

### Instructions and What to Record

**Q15 — The color.** Look again at the body color you recorded in Q2. Nearly the whole population ended up that color. Write the best explanation you can for why that color was favored in that world. Make it a good one — give the argument you would give if you had to defend it.

*(Do not read ahead until you have written Q15.)*

**Q16.** Body color in this simulation does nothing at all. It is not sensed by anything, it does not affect energy, and it changes nothing about how a vehicle moves. It became common because it happened to belong to the individual whose *wiring* was winning, and it was carried along for the ride.
- Given that, what was wrong with the explanation you just wrote — not with your reasoning, but with the question?
- The reading calls this kind of explanation a **just-so story**, and describes Gould and Lewontin's argument that not every trait is an adaptation. Explain their point using your own Q15 as the example.
- Here you were told the answer. In real biology, nobody tells you. What follows from that?

**Q17 — Your own words.** Copy the three sentences from your Q1 answer that come closest to describing the population as though it wanted something, tried something, learned something, or was heading somewhere. Then rewrite each one so that it says the same true thing without any of that. If you find you wrote no such sentences, say so, and write the three sentences you were most tempted to write.

**Q18 — Which population is better?** Population **Z** was evolved in a world where light is poison, and it flees light. Population **W** was evolved in a world where light is food, and it approaches light. Put Z into W's world, and W into Z's world, and watch. Then answer: which of the two populations is *better adapted*? Which one is *better*? Explain why those are not the same question, using what the reading says about the ladder of intelligence.

**Q19 — Turn it on the simulation.** You have spent an hour calling this evolution. It is a computer program with a few dozen dots in it. The reading gives three senses in which an artificial system can match a natural one: **behavioral equivalence**, **mechanistic equivalence**, and **engineering convenience**. Which one is this simulation, and how do you know? What did using it let you learn that you could not have learned by reading about evolution, and what would you be wrong to conclude from it?

**Q20 — One more run.** Here are two runs of the simulation. They reached different outcomes. The person who ran them changed one thing on purpose: the mutation rate. Here is the full log of both runs. *(See the report document.)*
- Name something else that differed between the two runs.
- What is the word the reading uses for that?
- What would you have to do differently to be able to say the mutation rate caused the difference?

## Completing the Lab Assignment
- Make sure you answer all the questions in the document evolution_lab_report.docx.
- Make sure you have added everyone's name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
