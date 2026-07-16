# Lab 1
In this lab, you will explore a simulation of simple agents called Braitenberg vehicles.
In the simulation, you will imagine you are a scientist who has discovered a new kind of organism.
You have found four varieties, which have been named 2a, 2b, 3a, and 3b.
Each variety is a different color, and the key is shown in the panel on the left of the simulation.
One thing we know: these organisms can sense heat and move in response to it.
In the simulation, heat sources appear as glowing gold orbs.
Your task is to observe, explore, and describe what each of the four varieties does,
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
**reset**, and change the **speed**.
- **Left-click the ground** to add a heat source, and **right-click** to remove the nearest one.
The **Clear lights** button removes all of them at once.
- **Click and drag** to move the camera around the world, and scroll to zoom in and out.

## Part 1: First Impressions  (≈5 minutes)

### Goal of Part 1
The purpose of this stage is to notice patterns and give them names.
Later, we will step back and consider what might actually be happening under the hood.

### Instructions
1. Start the simulation and watch the vehicles for a few moments without doing anything. Notice how they move.
2. Keep track of which color is doing what. The key in the left panel tells you which color is which variety.
3. Reset and restart the simulation as often as you’d like. Try out different arrangements of the heat sources.

### What to Record
Write down your first impressions.
For now, don’t worry about being technical or precise.
Just describe the behaviors in everyday language.
Don’t be afraid to use “mentalistic” language like curious, afraid, aggressive — that’s part of the exercise!
How would you describe what each of the four varieties seems to be doing?

## Part 2: Systematic Compare and Contrast (≈15 minutes)

### Goal
Now that you’ve had a chance to freely explore, your task is to compare the four varieties systematically.
Instead of describing them in everyday language, focus on how their behaviors differ when you change the environment.

### Instructions
1. Run the simulation again, this time paying attention to the differences between the four varieties.
2. Change the world and see what happens.
Press **Clear lights** to empty it, then left-click to place a single heat source.
Watch what each variety does when there is only one thing to react to.
Then add more sources, placing them in different corners.
3. Try placing a source right in front of a vehicle, and try placing one far away.
Move sources gradually closer or farther by removing and re-adding them.
4. Use **pause** and **step** to slow down a moment that happens too quickly to see.
5. Try the **Sensor gain** and **Base drive** sliders and notice what each one changes.
6. Reset and restart as often as needed. Keep experimenting until you feel you’ve seen enough patterns.
If you want, feel free to draw a picture of what you are observing.

### What to Record
- What are the consistent differences you notice among the four varieties?
- How does the distance to the heat source change each variety’s behavior?
- Do they respond the same way to a single source as they do to multiple sources?
- What happens when there are no heat sources at all? Which vehicles still move, and how?
- Which behaviors seem predictable and which seem surprising?

## Part 3: Reverse Engineering the Mind (≈15 minutes)

### Goal
Shift from describing behaviors to explaining them.
You will now be able to look inside each vehicle at the wiring that controls it.
Your task is to connect what you observed in the simulation with how the wiring actually works.

### Instructions
**Click on any vehicle** in the simulation.
A panel will open showing that vehicle's wiring diagram,
along with live readings from its sensors and motors.

Each vehicle has two heat sensors, one on the right and left sides of its head (marked **S**).
And each vehicle has two motors, one on the right and left sides of its body (marked **M**).
Motor is a word for a part of an entity that helps it move, like a foot or a wheel.
The lines in the diagram show you which sensor is connected to which motor.

The wiring of these organisms differs in two ways.

The first is *which* motor a sensor is connected to.
One kind of wiring is called "Ipsilateral".
Ipsilateral is a Latin word you see in brain science meaning "same side" (ipsi = same, lateral = side).
This means that each of the vehicle's sensors is connected to the motor on the same side of its body as the sensor.
The other kind is called "Contralateral".
Contralateral means "opposite side" (contra = opposite, lateral = side).
This means that each of the vehicle's sensors is connected to the motor on the opposite side of its body.

The second is *what the connection does* when the sensor detects heat.
Some connections are **excitatory**, and are drawn in green:
the more heat that sensor receives, the faster it makes that motor go.
Others are **inhibitory**, and are drawn in red:
the more heat that sensor receives, the slower it makes that motor go.

The four varieties cover every combination of these two choices.

In the panel, the thickness of each line shows how strongly that sensor is driving its motor right now.
The plot shows how each sensor's activation changes over time,
and the numbers underneath show the live sensor and motor values.
Pause the simulation, or use step, if you want to study a single moment closely.

Work with your group to inspect all four varieties.
For each one, note how it is wired, and then compare that wiring to the behavior you described in Part 2.

### What to Record

- For each variety (2a, 2b, 3a, 3b), record whether its wiring is ipsilateral or contralateral, and whether its connections are excitatory or inhibitory.
- How does the wiring explain the way each variety moves around the heat sources?
- Some of these varieties differ from each other in only one of the two wiring choices. Why do such small differences in wiring lead to such different “psychological-looking” behaviors?

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
