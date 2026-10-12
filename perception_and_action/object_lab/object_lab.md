# Lab 8

In Lab 7, a fish told an eel from a sucker by its smell, and the hardest thing we asked of its network was **invariance**: treating one thing as one thing across inputs that barely overlap. In §7.1.7 of the reading we said that a face seen from the front shares little of its image with the same face turned to one side. This lab is about that problem in vision, where it is at its hardest, and about what a trained network does with it.

Every part of this lab runs the same test twice. First you take it. Then a trained network takes it, on the very same images. The network’s answers stay hidden until you have committed your own, so that nothing it does can lean on what you did, and nothing you do can lean on it. The reason is the method we set out in §8.2.4: the strongest tests of a model change one thing at a time and check whether the model fails where people fail.

One word runs through every part. What people and networks achieve is not invariance but **tolerance**, in the sense we defined in Module 7: recognition survives a great deal of change in the image, but not all of it. Part 1 looks inside a network at how tolerance to one kind of change is built in, layer by layer. Part 2 removes contour in two ways and moves a part. Part 3 teaches a shoe from two views. Part 4 adds two kinds of noise. The closer shows the photograph networks a drawing.

A word about the networks. A **network**, here as in the reading, is an artificial neural network: a model of units and weighted connections, run on a computer. The four in this lab were trained before the lab existed, on the instructor’s computer, and nothing you do changes them. They are our networks, not the ones in the reading, so their numbers differ from the reading’s. The one thing that learns while you watch is a single unit in Part 3.

Plan on about 70 minutes.

## Part 0: Opening the Simulation (≈3 minutes)

1. Open the simulation in your web browser: [Objects](https://jonwillits.github.io/bcogapp/#/m08-objects). It runs in any modern browser, and there is nothing to install. Your drawings stay in the browser; nothing is sent anywhere.
2. Download the lab report Microsoft Word document. It is available here: [Lab 8 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/perception_and_action/object_lab/object_lab_report.docx) This document is what you will turn in to the course website.

### The five tabs

- **Draw** is Part 1: a drawing pad, a strip showing every layer of a network, and two plots.
- **Parts** is Part 2: twelve drawings with half their ink removed, then your own drawing, then one part moved.
- **Views** is Part 3: one shoe learned from two views and tested from many.
- **Noise** is Part 4: photographs clean and under two kinds of noise.
- **Closer** shows the photograph networks your drawing.

Two lines sit under the tabs on every part. One says that a network here is a model, not a brain. The other says that these networks were trained before this lab, and that nothing done here changes them, apart from the readout unit in Part 3. The **Run seed** under them fixes every trial order, the noise, and the readout’s starting weights; **New seed** draws another. Your seed differs from your neighbor’s, so your trials and your numbers will be close to theirs and not identical.

Three of the parts test you before they test a network. Each opens on a short description of what will happen and a **Begin** button, and ends in a **Commit my answers** button that stays disabled until every trial has an answer. Nothing from a network appears on the screen before you press it.

## Part 1: Inside the Stack (≈12 minutes)

### Goal

In §7.2.9 we said that a network can meet part of the demand for invariance through its architecture. **Convolution** applies the same small feature detector at every position, so a shifted input gives a shifted map of detections. **Pooling** keeps the strongest response in each small neighborhood and gives up exactly where it was, so a small shift no longer changes the pooled output. Stack several rounds, and each layer tolerates a little more. We also said what this gives and what it does not: tolerance to a shift in position, and nothing for a turn, a change of size, or a change of viewpoint. Here you watch both claims inside a real network, the **drawing network**, which was trained on 144,000 line drawings of 24 kinds of thing from a public collection of drawings made by players of a game.

### Instructions and What to Record

**Step 1 — Draw.** The pad says **Draw this:** and names a category. Draw it with a mouse or a finger. After each stroke, the five most likely labels appear with their probabilities, on five lines that keep their places. **Undo** removes the last stroke and **Clear** all of them. Draw the thing you were asked for, then draw two or three other things from the list of 24 on the output of the strip (bicycle, clock, mushroom, umbrella, and cat are easy ones), and watch the labels after each stroke.

- **Q1.** Report the category you were asked to draw, the network’s top label and its probability when you had finished, and how many strokes it took before that label first came out on top. Then describe one drawing the network got wrong, and what label it gave instead. Does it fail on things you would call bad drawings, or on things you would call good ones?

**Step 2 — Look inside.** Under *Look inside*, the **layer strip** runs from left to right: the input, then for each of four blocks the maps produced by its convolution and the maps left after its pooling, then the output as 24 bars. Each column prints its size. Click any map to enlarge it under the strip. Read the sizes across the strip, and compare a convolution map with the pooled map that follows it.

- **Q2.** Report the size of the input, of block 1’s convolution maps and pooled maps, and of block 4’s pooled maps. Each pooling halves each side; what has happened to the number of positions by the last pooled layer? In §7.2.9 we said what pooling gives and what it takes away, and a line under *Look inside* says it in one sentence. Copy that line out and say in your own words what the network no longer has at its last pooled layer.

**Step 3 — Tolerance to a shift, layer by layer.** Switch off **Center and scale the drawing first**. Two plots appear under *Tolerance, layer by layer*. Each line of the **Shift test** is one shift of your drawing to the right, by 2, 4, 6, or 8 pixels of the 64, and each point is how closely a layer’s activity for the shifted drawing matches its activity for the original: a correlation, 1 for identical. The layers run from the input to the last pooled layer. Fill in the table for the 2-pixel and the 8-pixel shifts.

| Shift | input | pooled 1 | pooled 2 | pooled 3 | pooled 4 |
|---|---|---|---|---|---|
| 2 pixels | | | | | |
| 8 pixels | | | | | |

- **Q3.** Report your table. Does the match rise from the input to the last pooled layer? Explain why a shift of two pixels makes the input match so poorly, and why the deepest layer matches so much better, using what convolution and pooling each do to a shifted map. Measured over 200 drawings, the match for an 8-pixel shift rises from about 0.17 at the input to about 0.55 at the last pooled layer. Is yours in that neighborhood?

**Step 4 — Tolerance to a turn.** The **Turn test** beside it turns your drawing by 45°, 90°, and 180°, and under it three lines give the label the network puts on each turned version.

- **Q4.** Report the match at the last pooled layer for the 180° turn, and the three labels. Set the 180° match beside the 4-pixel shift’s match at the same layer. Which is larger, and by how much? In §7.2.9 we said which kinds of change convolution and pooling build in tolerance to, and which they build in nothing for. Which kind is a turn, and do these two plots agree with the claim?

**Step 5 — Where the size tolerance came from.** With **Center and scale the drawing first** still off, press **Clear** and draw the same object small, in one corner of the pad. Watch the labels. Then switch centering back on. The line under the switch says what the step is.

- **Q5.** What happened to the labels when the drawing was small and in a corner, and what happened when you switched centering back on? Copy out the line under the switch. This step is not part of the network and was not learned; in Lab 7 you saw the same idea as a built-in receptor, a bet placed before learning starts. If the plots in Step 3 had been drawn with centering on, what would a shift have looked like to the network, and what would the plot have wrongly suggested?

**Step 6 — Version B.** Switch on **Version B: trained on shifted, turned and resized copies**. It is the same network trained on copies of each drawing that were shifted, turned, and resized at random, which is the training we described in §7.2.9 as the way most networks come to tolerate size and angle. Draw something clearly, press **Turn it upside down**, and read the labels under Version A and under Version B. Then press **Restore the drawing** and try **Squash it flat**, **Squeeze it thin**, and **Mirror it** under both.

- **Q6.** Report the label for your upside-down drawing under each version. Over 200 drawings, Version A names about 39% of upside-down drawings and Version B about 83%. Then report which of the other three changes Version B handled and which it failed. In §7.2.9 we said that whether training on altered copies is enough to explain how animals recognize things across such changes is a live dispute. What does Version B’s pattern of successes and failures say for and against that explanation?

## Part 2: Parts (≈15 minutes)

### Goal

In §8.2.4 we described two accounts of how recognition survives a change of view. On the first, an object is recognized as an arrangement of a few simple volumes, Biederman’s **geons**, and the features that identify a geon survive most changes of viewpoint. The test that made the account famous removed the same amount of contour from line drawings in two ways: in the middles of the edges, leaving each part recoverable, or at the places where parts join. People named the first and failed almost completely on the second. We also described a second finding: people rarely confused a simple object with a version in which one part had moved, and networks confused those versions easily. Part 2 puts both tests to you, and then to the drawing network.

### Instructions and What to Record

**Step 1 — Contour deletion, you first.** Open the Parts tab and read the screen, then press **Begin**. Twelve drawings come one at a time, each with half its ink removed by one of two erasers: **Mid-line**, which centers its gaps on the middles of the runs between joints, or **At the joints**, which centers them on corners, on stroke ends that lie near another stroke, and on crossings. You are not told which eraser was used. Name each drawing from the grid of 24, using **Previous** and **Next** to move, then press **Commit my answers**.

After the commit, four lines on the left give your percent right with each eraser and the network’s, and the twelve are revealed with the truth, your answer, and the network’s label.

- **Q7.** Report the four percentages. Which eraser was harder for you? Which drawings did you miss, and for each, was it the mid-line or the joints version? Look at two of the revealed drawings, one of each kind, and describe where the gaps fell.

**Step 2 — The larger test.** On the right, *The larger test* gives the network’s percent right over 200 held-out drawings per eraser, at three deletion levels, and the gap between the erasers.

| Ink removed | Mid-line | At the joints | Gap |
|---|---|---|---|
| 35% | | | |
| 50% | | | |
| 65% | | | |

- **Q8.** Report the table. In §8.2.4 we said that people failed almost completely on the nonrecoverable drawings and named the recoverable ones. Does this network show a gap in that direction? Does it show one in the other direction? Then read the line on the left that begins with Biederman’s name and say what these erasers do and do not reproduce of his method, and why that matters for what the network’s result can and cannot show.

**Step 3 — The erasers on your own drawing.** Press **Go on to Step 2: your drawing**. Your drawing from Part 1 is on the pad; keep it if it has parts, or clear it and draw something that does, such as a mushroom, a cup with a handle, or a snowman. The line beside the erased copy says how many joints were found. Compare **Mid-line** with **At the joints** at 50%. Then raise **share of ink removed** under each eraser until the network’s top label for the erased drawing changes.

- **Q9.** Report how many joints were found and where the joint eraser put its gaps. Report the share at which the label changed under each eraser. Which version is harder for you to recognize? Is the network’s order the same as yours?

**Step 4 — Move one part.** Press **Go on to Step 3: move one part**. The chip names a mushroom, an ice cream, or a coffee cup. Draw it on the first pad. On the second pad, draw the same object with one part moved as the prompt says: the cap under the stem, the scoop under the cone, or the handle on top. Answer whether the moved version is still that object (*yes*, *no*, or *only just*) and press **Commit my answer**. Four lines then give the network’s label and probability for each version, how closely the network’s last layer matches between the two, and, for comparison, how closely it matches between two ordinary drawings of the same category.

- **Q10.** Report your answer, the two labels with their probabilities, and the two matches. If the moved version matched the original about as closely as two ordinary drawings of the same thing match each other, the move made little difference to the network. Did it? Then say what in §8.2.4 would predict for a network here, and whether this one behaved that way.

**Step 5 — Ten built pairs.** Press **Go on to Step 4: the built pairs**. Ten drawings from the display set are shown beside versions with one group of strokes moved. Answer *yes*, *no*, or *only just* for each pair, then press **Commit my answers for the ten pairs**. Each pair then shows the network’s two labels and the two matches.

- **Q11.** On how many of the ten pairs did the network keep its label when the part moved? On how many did you say the moved version was still the same object? Name two pairs where your answer and the network’s label went different ways, and say which way. In the reading we said people rarely confused a moved version with the original, while networks confused them easily. Which of those two does this network behave like, and which do you?

## Part 3: Views (≈20 minutes)

### Goal

On the second account in §8.2.4, an object is stored as a set of views, and a new view is recognized by how close it is to a stored one. People who learned a novel object from a few views recognized new views between the learned ones well, views beyond them less well, and views at right angles to them worst. We also said that the two accounts are ends of a continuum of tasks: telling which of several similar objects is in view depends heavily on viewpoint, while telling a mug from a bucket depends on it much less. Part 3 runs that experiment on you with a shoe, among other shoes and among other things, and then on a **readout**: one unit that reads a frozen photograph network and learns by the rule from Lab 5.

### Instructions and What to Record

**Step 1 — Study, then test.** Open the Views tab and read *What will happen*; the study and the test take about five minutes without a break, so do not press **Begin** until you are ready. One shoe, the target, wobbles for ten seconds around one view and ten seconds around another, 75° apart. Then 48 pictures come one at a time. Half are the target from new views: between the two you studied, beyond them, or tipped at right angles to them. The rest are other objects at the same views: in half the pictures other shoes, in the other half other things, such as a bowl or a mouse. You are not told which. Answer **same shoe** or **not the same shoe** for each, then press **Commit my answers**.

**Step 2 — Your scorecards.** Six scorecards appear, one for each condition in each set, laid out as in Lab 7: **hits**, **misses**, **false alarms**, and **correct rejections**, then the hit rate, the false-alarm rate, and **d′** from the two rates. With four trials of each kind a rate of 0 or 1 is common, and a line under the card says it was counted as half a response short of the end, as in the By hand box from Lab 7, so d′ runs from about −2.3 to 2.3.

| Set | Between, d′ | Beyond, d′ | At right angles, d′ |
|---|---|---|---|
| One shoe among shoes | | | |
| One shoe among other things | | | |

- **Q12.** Report your table. In §8.2.4 we gave an order for people: between best, beyond next, at right angles worst. Does your row for the shoes follow it? Each condition has the same distances from the nearest learned view, 15° and 30°, as the line on the right says; explain why the experiment was built that way, and what a difference between conditions would have meant without it.
- **Q13.** Compare your two rows. In §8.2.4 we said which kind of task depends heavily on viewpoint and which much less. Is the other-things row higher and flatter than the shoes row? Explain, using what the parts of a shoe and a bowl have in common and what two running shoes have in common.

**Step 3 — The readout.** On the left, *Features ready* counts up while you take the test: the frozen **Standard** photograph network turns every picture the part uses into the activity of its last layer before the labels, 1,024 numbers. Two readout units each read those numbers. One learns the target against the other shoes, the other learns the target against the other things, both from the same two views you studied. The rule is Lab 5’s, written out on the panel: each weight changes by the learning rate times its input times a prediction error, Φ = a − p, where p is the prediction the unit made before the picture’s outcome arrived and a is whether it was the target. Switch **Learning on** and press **Skip ahead 50 steps** until both units read *(at the target)* beside their percent right on their training images.

- **Q14.** How many presses did each unit need to reach 95% on its training images? When both reached 100%, a line appeared under the numbers; copy it out and explain, from the rule’s arithmetic, why the weights then barely move. Read the line that begins *Only this one unit learns*. The layers underneath it are the Standard network’s, trained on photographs that are nothing like these renders. What has the readout learned, and what has it not had to learn?

**Step 4 — The readouts take your test.** Under your scorecards, six more appear for the readouts on the same 48 trials, and under them two pairs of curves: each readout’s evidence for the target at every 15° around the vertical axis and around the horizontal one, with the learned views marked and the criterion dashed.

| Set | Between, d′ | Beyond, d′ | At right angles, d′ |
|---|---|---|---|
| One shoe among shoes, the readout | | | |
| One shoe among other things, the readout | | | |

- **Q15.** Report the readouts’ table beside yours. Measured over eight target shoes and five seeds, the shoes readout’s d′ is lowest at right angles, and between is not reliably better than beyond; the other-things readout is higher and flatter. Where does your run agree with that, and where does it differ from the order we gave for people? Press **Skip ahead 50 steps** several more times and say whether the scorecards change.
- **Q16.** Describe the curve around the vertical axis for the shoes readout: where it peaks, how wide the peaks are, and whether there is a second rise on the far side of the shoe. In §8.2.4 we described a proposal that tolerance is built by combining many units, each tuned to one view, into one unit that responds to all of them, and in §8.3.4 we reported 773 cells recorded in trained monkeys, of which 71 responded to particular views and 8 across views. Which of those two kinds of cell does this readout resemble, and why could its two learned views not make it the other kind?

## Part 4: Noise (≈12 minutes)

### Goal

In §8.2.4 we described a test of whether training on altered copies of images is enough to explain tolerance. A network trained on photographs sprinkled with one kind of noise beat people on that noise, 80% against 46%, and then scored about 10% on a second kind of noise that looks similar to a person, close to chance. Training gave tolerance to the alteration that was trained and very little beyond it, while people handled a distortion they had never seen. Part 4 runs that test on you and on three **photo networks** that are identical except for what they were trained on: **Standard** on clean photographs, **Trained on noise A** on photographs with noise A at many strengths, and **Trained on blurred and sharp** on photographs each sharp or blurred at random, which is the mixture we described in the same section as making a network rely more on shape.

### Instructions and What to Record

**Step 1 — Your test.** Open the Noise tab, read *What will happen*, and press **Begin** when you are ready for about five minutes. Thirty-six grayscale photographs come one at a time, for about a fifth of a second each, then a mask, then the grid of sixteen names. Twelve are clean, twelve carry noise A, and twelve carry noise B, mixed and not announced. **Noise A** replaces a share of the pixels with black or white; **noise B** nudges every pixel by a random amount. The strength of each adapts to you: after a right answer the next picture with that noise is a little noisier, after a wrong one a little cleaner, so you end near the strength at which you are half right. The two current levels are printed on the left. Press **Commit my answers** when all thirty-six have a name.

**Step 2 — The three networks on your pictures.** After the commit the three networks name the same thirty-six pictures, at the strengths you were shown, and a table sets their percent right beside yours and beside chance, which is one in sixteen. Under it, *Where your noise settled* gives your level for each noise over the last six of its trials, and a second table reads off each network’s percent right at your settled level from the larger test.

| | clean | noise A | noise B |
|---|---|---|---|
| Standard | | | |
| Trained on noise A | | | |
| Trained on blurred and sharp | | | |
| you | | | |
| your settled level | — | | |

- **Q17.** Report the table and your two settled levels. Noise A started at 0.20 of the pixels and noise B at ±0.35. Did you settle above or below the start on each? Which network beat you on noise A, and by how much? Which beat you on noise B?
- **Q18.** The larger test on the right scores each network over 800 held-out photographs at the starting strengths and across a range of strengths. Report Standard’s and Trained on noise A’s percent right at noise A 0.20 and at noise B 0.35. The first half of the pattern from §8.2.4 is that the noise-trained network beats the clean-trained one on the trained noise. The second half is that it collapses on the other kind. Does our network show the first half? Does it show the second? State the comparison in numbers, and say what it means that a network trained on one pixel noise handled a different pixel noise it was never trained on.
- **Q19.** Beside the three networks’ description is a line about the eye. Copy it out. Trained on blurred and sharp did about as well as Standard on clean photographs; read its row across the noise strengths and say whether blurred training gave it any tolerance to noise that Standard lacks. In §8.2.4 we said what networks trained on a mixture of sharp and blurry images came to do. Which of those claims does this row test, and which does it leave untested?

## The Closer: A Drawing Is Not a Photograph (≈5 minutes)

### Instructions and What to Record

Open the Closer tab. Your drawing from Part 1 is on the pad; keep it if it is one of the sixteen categories the photo networks know, or clear it and draw the one **Draw this:** names. Press **Label my drawing**. The drawing is rendered as black strokes on white at the photograph networks’ size, and four lines give the three photo networks’ labels with probabilities and the drawing network’s label.

- **Q20.** Report the four labels. The three photo networks have never been shown a drawing. In §7.2.11 we said that networks trained on photographs lean on surface texture over shape, and a drawing has no texture. Did any of the three name your drawing? Draw two more things from the sixteen and report the label each network gave.
- **Q21.** The larger test on the right gives each network’s percent right over 800 held-out drawings of the sixteen categories, with the drawing network’s and chance. Report the five numbers. In §8.2.4 we predicted that a network trained on blurred and sharp images relies on shape more often and so should do better on drawings than one trained on sharp images alone. By how many points does it beat Standard here, and is that a difference you would trust from 800 drawings? Which network did best on drawings, and was it the one the prediction named?
- **Q22.** Under *The clock*, copy out the line about a network that gives people’s answers. Across this lab you have seen the networks fail where you did not (a turned drawing, a drawing instead of a photograph) and succeed where you did not (noise A, and perhaps noise B). Pick one place where a network and you agreed and one where you did not, and say what each does and does not show about whether the network works the way you do. In §8.2.4 we gave a reason, in one sentence about two kinds of clock, that agreement alone shows nothing; put that reason in your own words.

## Completing the Lab Assignment

- Make sure you answer all the questions in the document object_lab_report.docx.
- Make sure you have added everyone’s name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
