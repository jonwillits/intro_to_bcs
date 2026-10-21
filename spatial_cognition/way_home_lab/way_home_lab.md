# Lab 9

In §9.1.1 of the reading, we described a small warm animal on a forest floor at night. It has to eat, it has to eat often, and every trip out ends with the same problem: getting back to the nest. In this lab you take that animal's position three ways. In Part 1 you are the forager, and the subject of an experiment on how people find the way home. In Part 2 you are the experimenter, running a healthy rat and five hidden rats through the tests of §9.1.6. In Part 3 you are the rat, and simulated head-direction cells, place cells, grid cells, and border cells fire beside the view as you move. A short closer asks when to leave a patch of beetles that is running down.

Two things run through every part. The first is the rule of the lab, which you met in Labs 6, 7, and 8: nothing a test would tell you is shown until you commit. In Part 1 you do not learn where the nest truly was, or how far off you ended, until you have committed a block of trials. In Part 2 you do not learn what a hidden rat relies on until you have committed a diagnosis for every one. In Part 3 each change is made only after you have committed a prediction about it. The second is a distinction we have kept since Lab 7. The healthy rat and you are animals, and may learn, choose, and search. Everything else that moves in this lab is a program: the four **navigators** of Part 1 are programs given your exact trips, the hidden rats of Part 2 each follow one programmed strategy, and the cells of Part 3 are a model computed by the program, not recordings from a rat. Each panel has a line to that effect.

Rats stand in for the early mammals of the reading. Most of what is known about the cells in Part 3 comes from rats, and the three apparatus of Part 2 are the ones that were built for them.

Plan on about 85 minutes.

## Part 0: Opening the Simulation (≈3 minutes)

1. Open the simulation in your web browser: [The Way Home](https://jonwillits.github.io/bcogapp/#/m09-rat). It runs in any modern browser, and there is nothing to install. Nothing you do is sent anywhere; your trials stay in the browser.
2. Download the lab report Microsoft Word document. It is available here: [Lab 9 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/spatial_cognition/way_home_lab/way_home_lab_report.docx) This document is what you will turn in to the course website.

### The five tabs

- **World** is Part 0: the forest floor by moonlight, a few steps from the nest, with nothing scored.
- **Home** is Part 1: five steps of finding the way home.
- **Rats** is Part 2: the laboratory, with its three apparatus and six rats.
- **Cells** is Part 3: a recording box, and the cells that fire as you drive.
- **Patches** is the closer: a night of foraging between patches of beetles.

Under the tabs on every part sit the line about rats standing in for the early mammals, the **Run seed** with **New seed**, the choice between **Eye view** and **Follow view**, and two boxes, **Narrower view** and **Low detail**. The seed fixes every beetle, every trial order, every hidden rat's label, every noise draw, and every spike. Your seed differs from your neighbor's, so your numbers will be close to theirs and not identical.

### How the lab is laid out

Every part, and every step within Parts 1 and 3, opens with a description in a panel over the view: what will happen, what to do, and about how long it takes. Read it, then press **“Begin”** on the side panel. The buttons that run a step are always on the left; the results are always on the right.

On a step's opening screen you will also find **“Go back to Step n−1”** and **“Go to Step n+1”**, and after a step **“Redo Step n”**. These are there so that you can go back to a reveal or repeat a step you were interrupted in. Do not use them to jump ahead. Each step of Part 1 and Part 3 builds on the one before, and a prediction committed out of order is a prediction about something you have not yet seen.

### The keys and the two views

On the World, Home, and Cells tabs you drive the animal: the up arrow or W walks forward at a steady pace, the left and right arrows or A and D turn, and the down arrow or S steps back slowly. The four buttons under the view do the same on a touch screen. The keys are ignored while a control has focus; click on the view to drive again. On the Home tab the **“Enter”** key presses “Here is my nest”.

**Eye view** shows the world through the animal's own eyes, low to the ground. **Follow view** shows the animal from behind and a little above. The two show the same world: the same fog, the same darkness, and nothing in the simulation changes when you switch, so switch whenever you like. There is no head bob and the pace is constant, but some people feel unwell in a first-person view. If you do, switch to the follow view or tick **Narrower view**. **Low detail** halves the draw distance and the ground clutter for a slower machine, and changes nothing else.

Spend two minutes on the World tab. Walk to the fallen log and the rocks and back to the nest, once in each view, and decide which view you prefer. Read the panel's line about the rule of the lab before you go on.

## Part 1: The Way Home (≈27 minutes)

### Goal

In §9.1.4 we set out the cues an animal can use to find its way, and how each one fails on its own. The animal's own movement gives how far and which way it has gone, but every step and turn carries some error, the errors add up, and nothing in the signals shows how far the estimate has drifted. A nearby landmark pins down position closely, but only nearby. A distant one gives a direction and little else. In §9.2.2 we named the procedure that uses the first of these cues: **path integration**, a running sum of turns and distances that points back to the start from anywhere, the **home vector**. In §9.2.3 we described three ways a drifting sum can be corrected, averaging it with a landmark, resetting it from a landmark, or following one source when the two disagree by a lot, and the principle under all three: a landmark is worth using only if it stays where it is.

Part 1 puts those procedures to you. Five steps take you out from the nest and back under five conditions: with everything in view, across bare ground with nothing but your own movement to go by, by moonlight with the landmarks back, from a picture of home after being carried, and after the landmarks have been quietly moved. After each block, four programs take your exact trips and their endpoints are revealed beside yours. **Running sum only** keeps a running sum with noise in its turns and steps and uses no landmark. **Landmarks only** heads for where the landmarks put the nest and has nothing to go on when none is in view. **Averaging** weights its running sum and the landmarks by how reliable each is. **Following one** averages when the two disagree by a little and follows the landmarks alone when they disagree by a lot. They are programs given the same trips, not models of you, and a line under each reveal reads the same.

One line on Part 1's first panel matters for everything you do here. A screen gives no sense of balance and no feeling of the body moving. Here, how far and which way you have gone comes only from the ground moving past and the keys you pressed. Keep that in mind when you compare your errors with the programs'.

### Instructions and What to Record

**Step 1 — Practice.** Open the Home tab, read the panel, and press **“Begin”**. The nest is the dark hole under the arched root, and a beetle is a small green glint among the leaves. Walk out to the beetle, which is eaten when you reach it, then walk back and press **“Here is my nest”** or the Enter key. Two trials; do one in each view. Nothing is scored. If something interrupts a trial, **“Restart trial”** starts it again on a fresh trip, and the reveal counts the restart.

- **Q1.** Which view did you use for most of Part 1, and why? In the first panel's words, what does a screen give you about your own movement, and what does it leave out? Name one cue from §9.1.4 that a real forager would have on this trip and you did not.

**Step 2 — Home across bare ground.** For this step the range is bare: no log, no rocks, no stump, no tree, and the nest is a plain spot on the ground that you will not see again once you leave it. Beetles appear one at a time, each a few meters from the last. After the last one, walk back to where you started and press **“Here is my nest”**. Eight trials in moonlight: three with two beetles, three with three, and two with four, in an order your seed sets. With nothing on the ground to steer by, the only way back is path integration. Keep track of your own turns and distances as you go. Each return ends where you press the button, or after two minutes.

After **“Commit my trials”**, the reveal shows each trial from above: your path out in amber with a numbered dot at each beetle, your return dashed in blue, the nest a green dot, where you pressed the button a blue ring, and where each program ended a red square. Under each overhead are the rows for the outward path, your error, and your time in each view, then one row for each of the four programs. A program's row carries two numbers. The first, under *error*, is how far the program ended from the true nest. The second, under *from you*, is how far the program's endpoint was from yours, which can be large even when the program's error is small. When a question asks for a program's error, report the first number; when a question asks which program ended nearest you, look for the smallest second number. Under the eight trials is a plot of your error against the length of the outward path, with the dots colored by beetle count. Fill in the table from the rows, taking the running-sum program's *error*, not its distance from you.

| Trial | Beetles | Outward path, m | Your error, m | Running sum only, its error, m |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |

- **Q2.** Report your table. In §9.2.2 we said that a running sum grows less accurate the farther the animal wanders. Looking at your plot, did your error grow with the length of the outward path? Over twenty seeds, the running-sum program's mean error grows only from about 0.7 m after two beetles to about 1.1 m after four, which is too small a change to see in eight trials, so do not expect a clean line; say what you do see, and say whether a trend in eight trials of one person would settle the question either way.
- **Q3.** On the same trips, the running-sum program ended about 0.3 to 3.6 m from the nest. How far off were you, on average? The program keeps its sum from a turn signal and a step signal, each with a little noise, which is what we said in §9.1.4 an animal's own movement provides. Using the line about the screen, say what the program had that you did not, and why that makes its errors so much smaller than yours. Then say where **Landmarks only** ended on every trial, and why it ended there.

**Step 3 — Home by moonlight.** The range is as it was: the fallen log, the two rocks, and the stump near the nest, and the tall tree in view from anywhere. Four trials of three beetles, in moonlight throughout, with the nest out of view from the start. Now you have two things to go by, your running sum and the landmarks. Use whatever helps. Do at least one trial in the view you did not use in Step 2.

| Trial | Your error, m | Nearest program to you (smallest *from you*) | That program's error, m |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

- **Q4.** Report your table, and compare your four errors with your eight from Step 2. In §9.2.3 we said that adults walking back to a start with both landmarks and their own movement combine the two close to the ideal, giving landmarks more weight when they are plentiful and stable. Did the landmarks help you? Which program ended nearest you most often? Read the line under the programs about ending in the same place, and say why your nearest program is not evidence that you used its procedure.
- **Q5.** Over twenty seeds, **Landmarks only** ends at the nest on most moonlight trials and stops at the last beetle on a few. Look at where it ended on your four trials, and at the overhead of any trial where it stopped short. The near landmarks can be seen within about 10 m. Using the table in §9.1.4, explain why a nearby landmark is the one that gives this program a position, and why the tall tree, which is always in view, is not enough on its own.

**Step 4 — A picture of home.** Before each trial you see a still picture in the lower right of the view: the scene from the nest, facing north, in moonlight. Then the screen fades and you are set down somewhere else, as if carried, with no trip out. The picture stays in its corner. Find the nest by matching what you see to the picture, and press **“Here is my nest”**. Four trials: two set down near the nest, about 3 m away, and two set down far from it, about 20 m. You cannot restart a trial in this step, since there is no trip to restart.

- **Q6.** Report your error on each of the four trials, near and far. A stored view of a place is what we called a **snapshot** in §9.2.1, and we said it can be matched only near the goal, where the surroundings still look much as they did. Did the picture get you home from 3 m? From 20 m? Then read the programs' rows: the running-sum program stays where it was set down, every time. Using §9.1.4, say why being carried leaves a running sum with nothing to say.

**Step 5 — When the landmarks move.** Moonlight on the way out, with the tall tree hidden by cloud, so the near landmarks are the only landmarks. Two or three beetles a trial. At the last beetle something startles you: the screen goes dark for two seconds, and the status box reads *Startled*. The return is in moonlight. Walk home and press **“Here is my nest”**. Four trials; on some of them, the range after the startle is not quite as it was.

After the commit, each trial where the landmarks were moved shows a line from 0 to 1. Zero is the true nest, where your running sum points. One is where the moved landmarks point, where the nest would be if they had not been moved. Your endpoint is a blue dot on the line and the programs' are gray dots, and the rows say how far the landmarks were moved, 15° or 60° about the last beetle.

| Trial | Landmarks moved | Your score on the line | Running sum only | Landmarks only | Averaging | Following one |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

- **Q7.** Report your table. Did you notice, on the way back, that anything had moved, on the small move or on the large? Where did you end on the line on each kind of move: near 0, near 1, or between? In §9.2.3 we said that on small conflicts people average, and on large ones they stop averaging and follow one source. Which of those did you do, if either, and which source did you follow?
- **Q8.** Over twenty seeds, the programs' medians on the line are about 0.08 for the running sum, about 0.96 and 0.86 for the landmarks, about 0.65 and 0.61 for averaging, and for following one about 0.69 on the small move and about 0.97 on the large. Explain each program's position from its procedure. Then say what following one does that averaging does not, and which of the two the reading's description of people matches. Finally, say which program the principle under all three procedures, that a landmark is worth using only if it stays where it is, would have told to ignore the moved landmarks, and why none of the four could tell that they had moved.

## Part 2: Places or Responses? (≈20 minutes)

### Goal

In §9.1.6 we asked what a rat that has learned the way to food has actually learned: a sequence of turns, or where the food is. On the familiar path the two cannot be told apart, so the tests that separate them all change something. In the plus maze, a rat trained from one arm is started from the opposite arm, and either repeats its turn or goes to the place. In the water maze, a rat swims for a platform it cannot see, from starts around the rim. On the radiating paths, a rat trained along a roundabout route finds it blocked and chooses among a fan of paths. We also said that much of the result depends on the room: a rack of cages or a window outside the maze marks the place, and a plain enclosure leaves only the turn. And in §9.3.2 we said that the two kinds of learning depend on different structures, the hippocampus for places and the striatum for turns.

Part 2 makes you the experimenter. The laboratory holds a healthy rat, **H**, and five hidden rats. H does what a rat does, using a map of the room, a route of turns, and a beacon it can head for, each when it serves. Each hidden rat follows one programmed strategy, a beacon, a route, a snapshot, or a map, or has one of two kinds of damage, and your job is to find out which is which by running experiments. The labels R1 to R5 are dealt to the five hidden rats by your seed, so the order of the buttons says nothing, and your neighbor's R2 is not your R2. The diagnosis menu offers six entries for five rats, so one entry is a distractor.

One caution before you start. These rats follow their programs every time, so their choices come out clean, twenty seeds of twenty. The real experiments were nothing like that. In §9.1.6 we reported that 19 of 53 rats took the shortcut on the radiating paths, and that a review of 47 later experiments found the preference in 17% of them. The programs show what each strategy predicts. They do not show what a rat does, and a line on the panel reads that real rats use several at once.

### Instructions and What to Record

**Step 1 — The laboratory.** Open the Rats tab, read the panel, and press **“Begin”**. The view is the shared orbit camera: drag to orbit, scroll to zoom, W, A, S, and D to pan, the arrow keys to rotate and tilt. **“Controls info”** at the bottom right of the view reopens a panel that lists every control. Choose a rat, an apparatus, a room, and any changes on the left, then press **“Run the test”** to watch the trials play out on the apparatus, or **“Skip ahead to the result”** to fill the result lines at once. The current trial's path draws in blue and the earlier ones in faint amber. Changing any setting clears the last result. *Tests run* counts your tests.

**Step 2 — The healthy rat on the plus maze.** With H and the plus maze, run three tests: the rich room with 4 training trials, the rich room with 64, and the plain enclosure with 4. The result lines give the probe trials from the north arm, how many ended at the east arm, the place, and how many at the west arm, the same turn.

| Test | Ended at the east arm (the place) | Ended at the west arm (the same turn) |
|---|---|---|
| rich room, 4 training trials | | |
| rich room, 64 training trials | | |
| plain enclosure, 4 training trials | | |

- **Q9.** Report your table. In §9.1.6 we said three things: that rats readily learn a place when something outside the maze marks it, that in a plain enclosure they repeat the turn, and that with long training they shift from the place to the turn. Which of the three does each row show? Switch **Room** to the plain enclosure and look at the view: what is missing that the rich room had, and why does that matter to a rat that learned the place?

**Step 3 — The hidden rats on the plus maze.** Run each hidden rat in the rich room with 4 training trials, and then in the plain enclosure. Note which arm each went to. Two of the hidden rats go to the west arm in the rich room; three go east. In the plain enclosure, the two that went west still go west, and the three that went east have no consistent arm.

- **Q10.** Which of your five labels went west, and which went east? From §9.1.6 and §9.2.1, which strategies would send a rat to the same turn whatever the room, and which would send it to the place only while the room marks it? What does the plain enclosure take away from a rat that uses a snapshot, a beacon, or a map, and why does it take nothing from a rat that uses a route? Write down your first guess at each label's strategy; you will revise it.

**Step 4 — The water maze.** Switch to the water maze with the platform hidden, and run H and every hidden rat. The result rows give the test trials, how many found the platform within 60 s, the mean time, and the probe's share of time in the platform's quarter, with one row per test trial under them. Then tick **Remove the cues just before the choice** and run them again. Then untick it and run H once more with **Platform** set to *visible*.

| Rat | Hidden platform: learns it? | Cues removed just before the choice: finds it? |
|---|---|---|
| H | | |
| (label) | | |
| (label) | | |
| (label) | | |
| (label) | | |
| (label) | | |

- **Q11.** Report your table. In §9.3.2 we said that rats with damage to the hippocampus still swim to a platform they can see but cannot find a hidden one whose position is defined only by the room. Which of your labels learned the hidden platform, and which did not? Removing the cues just before the choice separates two rats that both learned it: one still finds the platform most times, and one fails. Using §9.2.1 and §9.2.7, say which strategy needs the room in view at the moment of the choice and which can work from where it already is, and name the two labels. Then say why the visible platform is found by every rat, and what that tells you about what a beacon is.

**Step 5 — The radiating paths.** Switch to the radiating paths. The rat is trained along the roundabout route once, then the route is blocked and a fan of twelve paths is offered; path 6 is the one nearest the old food box, and paths 4 and 5 lie beside the blocked route. The lamp stands on its post behind the food box. Run every rat with **The lamp** *in place*, then *switched off*, then *moved across the room*. The bar chart on the right counts the paths taken, with path 6 in amber.

| Rat | Lamp in place | Lamp switched off | Lamp moved across the room |
|---|---|---|---|
| H | | | |
| (label) | | | |
| (label) | | | |
| (label) | | | |
| (label) | | | |
| (label) | | | |

- **Q12.** Report your table. With the lamp in place, two hidden rats that differ in every other test take the same path, path 6; with the lamp moved, one of them follows it to path 1 and the other stays on path 6. In §9.1.6 we said why the lamp in Tolman's room was a problem for his interpretation. Say, in the programs' terms, what that problem is: which two strategies the lamp in place cannot tell apart, and which change does tell them apart. Then say what the rat that keeps path 6 when the lamp moves must be using, and why we call a route never taken, in §9.1.6, the test of a map.

**Step 6 — Diagnose.** Choose a diagnosis for every hidden rat from the menu on the left, then press **“Commit my diagnoses”**. It is disabled until every rat has one. After the commit, **“Reveal”** beside each rat on the right prints its strategy, its line, and what you said.

- **Q13.** Report your five diagnoses and the five reveals. For each rat you got wrong, name the test that would have separated the two strategies you confused, and say what it would have shown. For the rat with damage to the hippocampus, say what it still had, and which of H's results it matched.
- **Q14.** H went to the place after 4 training trials, to the turn after 64, and to the turn in the plain enclosure. No hidden rat does all three. In §9.1.6 we quoted a reviewer: there is nothing in the nature of a rat which makes it a place or a response learner. Using that quotation and what we said in §9.3.2 about the hippocampus and the striatum, explain why the healthy rat looks like a different hidden rat in different tests, and why an experiment that finds place learning in one room and response learning in another is not a contradiction.

## Part 3: Inside the Map (≈25 minutes)

### Goal

In §9.3 we described cells whose firing follows where the animal is and which way it faces. A **head-direction cell** fires when the head points one way, whatever the animal is doing (§9.3.1). A **place cell** fires when the animal is in one part of its surroundings, its **place field**, whichever way it faces (§9.3.2). A **grid cell** fires at many places laid out at the corners of equilateral triangles, and a **border cell** fires along a wall (§9.3.3). And when a rat is moved to a new room, its place cells reorganize all at once, which is **remapping** (§9.3.5).

Part 3 puts you in a recording box with simulated cells of all four kinds firing beside the view. Three things about the model matter, and three lines on the panel say them. First, these cells are a model computed by this program, not recordings from a rat. Second, they respond to where the rat's own estimate puts it, not to where it is. The estimate is the running sum of §9.2.2, corrected by the walls and the card as we described in §9.2.3, and because the cells read the estimate, everything we said in §9.3.1 and §9.3.2 about drift, correction, and the card shows up in the cells. Third, the head-direction signal is kept by two rings. The **ring attractor** of §9.2.4 is the lower ring: a circle of units, each standing for one direction, that settles into one bump of activity, which a turn signal slides around the ring. The upper ring follows it one for one and holds the cells you see. A landmark's input learns onto the upper ring, by the Coincidence rule from Lab 5, and reaches the lower ring only as a small nudge that can correct a bump but cannot make one. We built it that way because of the vestibular lesion in §9.3.1: without the turn signal, there was no heading for a landmark to correct.

Each step from Step 2 on asks you for a prediction before anything changes, and then makes the change when you commit. Before each prediction, reread the passage named in the step. The predictions are not graded on being right; they are graded on being argued from the reading, and on what you make of the difference when the model disagrees with you.

### Instructions and What to Record

**Step 1 — Fill the maps.** Open the Cells tab, read the panel, and press **“Begin”**. The box is 1 m square, with gray walls, a dark floor, and a white card on the north wall. The eye view sits 4.5 cm above the floor; the follow view sits behind and above the rat, inside the walls. Drive for a minute, in both views, and watch the right panel, **The recording**, fill in.

Read the panel from the top. The rows give the room and the light, the simulated time, the gap between the estimate and the true position in centimeters, the bump's offset from the true heading in degrees, whether the white card holds the heading and when it took control, the directional tuning of the shown cells, and whether the turn pathway is intact. **The rings** are two circles of bars: the lower ring's bump turns as you turn, and the upper ring's bump sits on it; the decoded heading is printed under each. Under them, eight **head-direction cells** as polar plots, each with a lobe at the direction it prefers. Then six **place cells** as firing maps, heat squares of spikes divided by time spent, which fill in only where the rat has been. Then six **grid cells**, two from each of three groups whose spacings are about 30, 42, and 59 cm; in a 1 m box the largest group shows only two or three bumps. Then four **border cells**, one per wall. At the foot, an overhead of the box with the true path in amber and the estimate dashed in blue.

A **firing map** needs the floor covered many times, so after your minute press **“Let it explore by itself”** and **“Skip ahead 10 minutes”**. The exploring rat covers about 95% of the floor in ten minutes.

- **Q15.** Report the simulated time at which the line changed from *The white card does not hold the heading yet* to *The white card holds the heading*, and the gap between the estimate and the true position once the maps had filled. In §9.3.1 we said that a card takes control of the cells after about 8 minutes in a new room, not after 1. Over six seeds the model's card takes control after about 7.5 to 7.9 minutes. The card's input onto the upper ring starts at zero and learns by the Coincidence rule, growing when a view unit and a ring unit are active together. Explain, from the rule, why control takes minutes rather than seconds, and why the card could not take control in the first minute however much the rat looked at it.
- **Q16.** Describe one place field, one grid lattice, and one border band from your maps, in words: where each cell fires and where it does not. Read the two lines beside the grid cells. In §9.3.3 we said that grids as the running sum is the leading hypothesis, not a finding, and we listed the evidence against a simple version of it. Then read the line beside the place cells. In this model the place cells are computed from the estimate directly, not built from the grid cells. Using §9.3.8's developmental evidence, which the line beside the grid cells points at, say why the model was built that way rather than the other.

**Step 2 — Lights out.** Press **“Go on to Step 2”** and read the panel, but before you choose a prediction, reread the paragraph of §9.3.1 that begins *In the dark*, and the paragraph of §9.3.2 that begins *Place cells do not simply respond*. The question is what happens to the place fields when the lights go out. Choose, and press **“Commit my prediction”**. The maps from the light are pinned below the recording, the lights go out, and a fresh set of maps records in the dark. In the dark the fog closes to a few centimeters in both views, and only the floor's texture under the rat is drawn. The rat now has only its own turns and steps to go by, as you had on the bare ground in Part 1.

Drive along a wall for a while, then across the middle, watching the overhead and the gap row. A new row, *Drift of the bump since lights out*, appears under the bump row. Then press **“Lights on”**, and watch the next minute or two.

- **Q17.** Report your prediction, the gap between the estimate and the true position after about two dark minutes, and the drift of the bump after as long as you stayed dark. Over six seeds the gap averages about 5 to 31 cm in the dark against about 6 to 15 cm in the light, and after five dark minutes the bump stands about 3 to 105° from where it stood. Describe what the dark maps looked like against the pinned ones. Was your prediction right? If not, say what in the reading you would have had to weigh differently.
- **Q18.** In the overhead, when you drove along a wall, the dashed estimate snapped back onto that wall while the gap across the room stayed. In §9.2.3 we called this resetting, and in §9.3.3 we said that touching a wall corrects drift in grid cells. Explain why a wall can correct the estimate in only one direction, and what a corner would do. Then explain, from §9.1.4, why the estimate drifted at all once the card was gone, and why nothing in the rat's own movement could tell it how far. When the lights came on, what pulled the bump and the estimate back, and about how long did it take?

**Step 3 — Turn the card.** Press **“Go on to Step 3”**. Before the prediction, reread the paragraph of §9.3.1 that begins *In the dark, the head-direction signal keeps going*, down to its last sentence about a card that loses control. The question is what the head-direction cells do when the card is turned 90° while the rat is out of the box. Choose and commit. The screen fades, the rat is taken out, the card is moved a quarter turn around the walls, and the rat is set down again. Give it two minutes with **“Skip ahead 2 minutes”**, then read the rows under **What the step shows**: the eight cells' turns since the card was turned, their mean, and whether the card holds the heading.

- **Q19.** Report your prediction and the eight turns with their mean. Over four seeds the mean is about 88 to 92°, all eight together. Using §9.2.4, explain why the cells turn together rather than each by its own amount: what a landmark's input does to a single bump on a ring, and why there is only one bump to move. Then look at the pinned place maps against the new ones. Did the place fields turn with the card? Using what we said in §9.3.5 about grid cells and head-direction cells shifting together, say why they should.

Now the second half. Face the card in the view and press **“Move the card”**. It moves a quarter turn whichever way keeps it in view, and the row *Card moves seen by the rat in this room* counts up; if the rat cannot see the card the line reads *Turn to face the card first*. After each move, watch the lower ring for a minute, or skip two. Repeat until the line changes to *The white card no longer holds the heading*.

- **Q20.** Report how many seen moves it took, and what the rings did after each move before that. Over four seeds the card loses control after 3 to 5 seen moves. In §9.3.1 we reported only the outcome, that a card loses control if the animal has seen it move. The model has a rule for it: a jump in the card's bearing that the turn signal does not account for is a sign that the card moved, and each such jump halves the weight the system gives it. Say how that rule is the principle of §9.2.3, that a landmark is worth using only if it stays where it is, written as a procedure. Then say why the card turned out of sight in the first half of this step carried every cell with it, while the same card moved in sight is dropped: what does the rat have in one case that it lacks in the other?

**Step 4 — A new room.** Press **“Go on to Step 4”**. Before the prediction, reread §9.3.5 from its first paragraph to the paragraph about the square box changed step by step toward a circle. The question is what the place cells do in a new room. Choose and commit. The rat is carried to a round box, 1.1 m across, with blue walls, a pale floor, and a black card on the east side, and the first box's maps are pinned. Drive, let it explore, and skip until the new maps fill. The rows under **What the step shows** give which of the stored maps is in use, how many place cells are silent in this room, and whether the black card has taken control. Then press **“Back to the first room”**, and compare the maps that return with the pinned ones.

- **Q21.** Report your prediction, how many of the thirty place cells fell silent in the round box, and when the black card took control. Over six seeds, 8 to 16 of 30 fall silent and the rest fire in new places, and the black card takes control after about 8.2 to 8.7 minutes. Describe what the grid lattices and the head-direction lobes did between the two rooms. When you went back, did the first room's fields come back where they were? Read the line about how the program chooses a room's map. In §9.2.8 we described the choice of which map an animal is on, and in §9.3.5 we called the choice between maps, carried out by cells, pattern separation and pattern completion. Say which of the two the return to the first room shows, and why the rule is, as the line reads, not a model of the hippocampus's own circuits.

**Step 5 — Without the turn signal.** Press **“Go on to Step 5”**. Before the prediction, reread the paragraph of §9.3.1 that begins *The input that keeps the signal going comes from turning*, and the model's own line beside the step, which states the one assumption the reading does not. The question is what the head-direction cells do over a day with the turn signal gone and the card in view. Choose and commit. The turn pathway is removed and the row reads *Turn pathway: removed*. Press **“Skip ahead 1 day (90 simulated minutes)”** and watch the rings, the polar plots, and the directional tuning row before and after.

- **Q22.** Report your prediction, the directional tuning before the skip and after it, and what the two rings and the eight polar plots looked like afterward. Over four seeds the tuning falls from about 0.74 to about 0.05, and stays there with the card in view for a further hour. Are the cells silent? Read the row for the lower ring's bump strength. In §9.3.1 we reported that after the vestibular lesion the cells kept firing but not for any one heading, and that the signal never came back with a familiar card in view. Explain, from the two-ring arrangement in the Goal above, why a landmark can correct a heading but cannot supply one, and why a model with one ring and a learned card input would have given the opposite result. Then copy out the assumption line beside the step and say what we reported in §9.3.1 and what the model has to assume.
- **Q23.** The reveal rows in Part 1 printed your time in each view; here, say which view you used in the box and which you would tell another student to use. In the eye view a 20 cm rat in a 1 m box is close to the walls; in the follow view the card and the walls are in view at once. Does either view change anything the cells do? Read the line about the estimate once more and say why not.

## The Closer: Stay or Go (≈8 minutes)

### Goal

In §9.1.8 we described a second exploring problem: a patch that is running down. In §9.2.9 we gave the rule from the study of foraging: leave when the rate of finding food in the patch has fallen to the average rate for the habitat as a whole, counting the time it takes to travel between patches. A richer habitat means leaving sooner. The rule concerns when leaving is best, not how an animal arrives at it, and a line on the panel reads the same.

### Instructions and What to Record

Open the Patches tab, read the panel, and press **“Begin”**. The forager follows one rule, set by the slider: leave a patch when beetles turn up there more slowly than one every so many seconds. In the rich habitat a fresh patch gives about one beetle every 2 s and the next patch is 12 m away; in the poor habitat, one every 5 s and 30 m away. The question on the left is where the best setting is shorter, the rich habitat or the poor one. Choose and press **“Commit my prediction”**. Then press **“Run a night”** and watch the forager work the rim of a leaf pile, each beetle glinting at its nose as it is found, until the rule says leave and it crosses to the next pile; the rows under **This night** on the right count the hours, the beetles, the patches, and the beetles per minute. **“Skip ahead to the end of the night”** finishes the four hours. Then press **“Try every setting”**, which runs one night at each of the ten settings and plots beetles per minute against the setting, with the habitat's average rate as a dashed mark. Do this in both habitats.

| Habitat | Average rate, one every … s | Best setting, s | Beetles per minute at the best setting |
|---|---|---|---|
| rich | | | |
| poor | | | |

- **Q24.** Report your prediction and your table. Over twenty seeds the best setting is about 6 s in the rich habitat and about 12 s in the poor one. Was your prediction right? Using the rule in §9.2.9, explain why the forager should give up on a patch sooner where the habitat is richer, even though a rich patch is still giving beetles when it leaves. Then say what travel time has to do with it.
- **Q25.** The dashed mark sits at one beetle every 4.4 s in the rich habitat and every 15.7 s in the poor one, and the best setting lies one step after the mark in the rich habitat and one step before it in the poor. The rule the forager follows reads the patch's rate off the gap since the last beetle, which is a noisy estimate of a rate. Say why a long gap arrives by chance sooner in a rich patch than the rate has truly fallen, and what that does to the best threshold. Then copy out the line about what the rule says and does not say, and say what the chickadees of §9.2.9 did that this forager does by construction.

## Completing the Lab Assignment

- Make sure you answer all the questions in the document way_home_lab_report.docx.
- Make sure you have added everyone’s name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
