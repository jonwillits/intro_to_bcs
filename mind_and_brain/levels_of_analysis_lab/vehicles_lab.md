# Lab 1
In this lab, you will explore a simulation of simple agents called Braitenberg vehicles.
In the simulation, you will imagine you are a scientist who has discovered a new kind of organism.
You have found six varieties, which have been named 2a, 2b, 2c, 3a, 3b, and 3c.
Each variety is a different color, and the key is shown in the panel on the left of the simulation.
One thing we know: these organisms can sense light and move in response to it.
In the simulation, light sources appear as glowing gold orbs.
The organisms live at the bottom of a pit with steep walls, which they cannot climb.
Your task is to observe, explore, and describe what each of the six varieties does,
and then to work out why they do it.

## Part 0: Opening the Simulation (≈2 minutes)
To do this lab, you'll need to do two things.
1. Open the simulation in your web browser:
[Braitenberg's Vehicles](https://jonwillits.github.io/bcogapp/#/m01-vehicles).
It runs in any modern browser on Mac, Windows, Linux, or a Chromebook.
There is nothing to install and nothing to set up — just open the link.
2. Download the lab report Microsoft Word document.
It is available here: [Lab 1 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/mind_and_brain/levels_of_analysis_lab/vehicles_lab_report.docx)
This document is what you will turn in to the course website.

A few things that will help before you start:
- The **Lab** button at the top of the simulation opens these instructions next to the simulation,
so you can read and experiment at the same time.
- The buttons along the bottom let you **play/pause**, **step** forward one moment at a time,
**reset** the simulation, and change the **speed**.
- You can **Left-click the ground** to add a light source, and **right-click** to remove the nearest one.
The **Clear lights** button removes all of them at once.
You can place lights on the floor of the pit, or up on the flat rim outside its walls.
- **Click and drag** to move the camera around the world, and scroll to zoom in and out.

## Part 1: First Impressions  (≈5 minutes)

### Goal of Part 1
The purpose of this stage is to notice patterns and give them names.
Later, we will step back and consider what might actually be happening under the hood.

### Instructions
1. Start the simulation and watch the vehicles for a few moments without doing anything. Notice how they move.
2. Keep track of which color is doing what. The key in the left panel tells you which color is which variety.
3. Reset and restart the simulation as often as you’d like. Try out different arrangements of the light sources.

### What to Record
Write down your first impressions.
For now, don’t worry about being technical or precise.
Just describe the behaviors in everyday language.
Don’t be afraid to use “mentalistic” language like curious, afraid, aggressive — that’s part of the exercise!
How would you describe what each of the six varieties seems to be doing?

## Part 2: Systematic Compare and Contrast (≈15 minutes)

### Goal
Now that you’ve had a chance to freely explore, your task is to compare the six varieties systematically.
Instead of describing them in everyday language, focus on how their behaviors differ when you change the environment.

### Instructions
1. Run the simulation again, this time paying attention to the differences between the six varieties.
2. Change the world and see what happens.
Press **Clear lights** to empty it, then left-click to place a single light source.
Watch what each variety does when there is only one thing to react to.
Then add more sources, placing them in different corners.
3. Try placing a source right in front of a vehicle, and try placing one far away.
Move sources gradually closer or farther by removing and re-adding them.
4. Use **pause** and **step** to slow down a moment that happens too quickly to see.
5. Try putting one or more lights up on the rim, outside the walls of the pit, and watch what the vehicles do.
6. Reset and restart as often as needed. Keep experimenting until you feel you’ve seen enough patterns.
If you want, feel free to draw a picture of what you are observing.

### What to Record
- What are the consistent differences you notice among the six varieties?
- How does the distance to the light source change each variety’s behavior?
- Do they respond the same way to a single source as they do to multiple sources?
- What happens when there are no light sources at all? Which vehicles still move, and how?
- Do all six varieties steer? Are there any that never seem to turn toward or away from anything, no matter where you put a light source?
- What happens when you put a light up on the rim, where no vehicle can reach it? Does it still affect them? Does a light up there seem to pull as strongly as one down on the floor?
- Which behaviors seem predictable and which seem surprising?

## Part 3: Reverse Engineering the Mind (≈15 minutes)

### Goal
Shift from describing behaviors to explaining them.
You will now be able to look inside each vehicle at the wiring that controls it.
Your task is to connect what you observed in the simulation with how the wiring actually works.

### Instructions
**Click on any vehicle** in the simulation.
A panel will open showing that vehicle's wiring diagram,
along with live readings from its sensors and actuators.

Each vehicle has two light sensors, one on the right and left sides of its head (marked **S**).
And each vehicle has two actuators, one on the right and left sides of its body (marked **A**).
Actuator is a word for a part of an entity that helps it move, like a foot, wheel, or flagellum.
The lines in the diagram show you which sensor is connected to which actuator.

The wiring of these organisms differs in two ways.

The first is *which* actuator a sensor is connected to.
There are three kinds.
One kind of wiring is called "Ipsilateral".
Ipsilateral is a Latin word you see in brain science meaning "same side" (ipsi = same, lateral = side).
This means that each of the vehicle's sensors is connected to the actuator on the same side of its body as the sensor.
Another kind is called "Contralateral".
Contralateral means "opposite side" (contra = opposite, lateral = side).
This means that each of the vehicle's sensors is connected to the actuator on the opposite side of its body.
The third kind is "fully connected".
This means that each sensor is connected to *both* actuators,
so every sensor can drive every actuator at once.
Notice that ipsilateral and contralateral are really just this same wiring with half of the connections missing.

The second is *what the connection does* when the sensor detects light.
Some connections are **excitatory**, and are drawn in green:
the more light that sensor receives, the faster it makes that actuator go.
Others are **inhibitory**, and are drawn in red:
the more light that sensor receives, the slower it makes that actuator go.

The six varieties cover every combination of these two choices:
three wiring patterns, each of which can be excitatory or inhibitory.

The panel also shows you the numbers behind the behavior.
Each sensor and actuator is labelled with its live value,
and the thickness of each line shows how strongly that sensor is driving its actuator right now.
Underneath, the panel writes out the arithmetic for each actuator, which looks something like this:

`A_L = 0.60 + (−2.40 × 0.31)`
`    = −0.14`

Read that as: the actuator starts from the vehicle's **actuator bias** (its resting drive, what it does with no light at all),
and then each connection adds its **connection strength** multiplied by what that sensor currently senses.
The plot shows how each sensor's activation changes over time.
Pause the simulation, or use step, if you want to study a single moment closely.

At the bottom of the panel are two sliders that change **only the vehicle you have selected**,
leaving the other five exactly as they were:
- **Connection strength** — how strongly each connection drives its actuator.
- **Actuator bias** — how fast the vehicle moves when it senses nothing at all.

Work with your group to inspect all six varieties.
For each one, note how it is wired, and then compare that wiring to the behavior you described in Part 2.

### What to Record

- For each variety (2a, 2b, 2c, 3a, 3b, 3c), record whether its wiring is ipsilateral, contralateral, or fully connected, and whether its connections are excitatory or inhibitory.
- How does the wiring explain the way each variety moves around the light sources?
- Some varieties never steer at all, no matter where you put a light source. Find them, and compare their two actuator values as they move. What is it about their wiring that makes turning impossible?
- Some of these varieties differ from each other in only one of the two wiring choices. Why do such small differences in wiring lead to such different “psychological-looking” behaviors?
- Put a light up on the rim, select a vehicle that is drawn toward it, and raise its **connection strength**. What changes, and what does the vehicle end up doing? Using the numbers in the panel, explain why a light up on the rim pulls more weakly than one on the floor, even from the same spot on the map.

## Part 4: Philosophical Reflection (≈20 minutes)

### Goal
Step back from the wiring details.
Reflect on what these vehicles tell us about the relationship between brains, behavior, and how we explain them.
You will connect your observations to Marr’s levels of analysis, which we discussed in class and in our reading.

### Instructions
1. Think back to your first impressions in Part 1.
What kinds of words did you use to describe the vehicles’ behavior?
Did you use everyday mentalistic terms like “fear,” “curiosity,” or “aggression”?  
2. Compare those initial descriptions with what you learned about the wiring in Part 3.
How do the two explanations differ?  
3. Recall Marr’s three levels of analysis from this week’s readings: 
4. As a group, discuss how each level could be applied to explain the vehicles’ behavior.  
5. Reflect on whether the levels provide complementary or conflicting explanations.

### What to Record
- Which mentalistic descriptions came up in your group’s first impressions?  
- How did your explanations change after seeing the wiring diagrams?  
- Define Marr's three levels of analysis.
- How would you describe these vehicles’ behavior at each of Marr's levels?  
- Do the different levels of analysis seem to give complementary or contradictory explanations?  
- Which level(s) do you think are most useful for understanding these vehicles, and why?  

## Completing the Lab Assignment
- Make sure you answer all the questions in the document vehicles_lab_report.docx.
- Make sure you have added everyone's name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website.
Remember, even though you worked in a group, each lab member must submit their own lab report.
