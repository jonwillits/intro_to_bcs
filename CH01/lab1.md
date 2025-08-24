# Lab 1

In this lab, you will explore a simulation of simple agents called Braitenberg vehicles. 
In this simulation, you will imagine you are a scientist who has discovered a new organism.
We are calling the organism "Vehicle 2".
You are interested in trying to understand Vehicle 2's behavior.
One thing we know: Vehicle 2 can sense heat and move in response to it. 
Some vehicles (2A) are colored blue, the other (2B) is colored red. 
Your task is to observe, explore, and describe what vehicle 2A and 2B do.

### Part 0: Installing the Python and Downloading the Simulation (≈15 minutes)

To run the simulation first you will need to install Python 3.13 on your computer, 
following the instructions here: [Installing Python](https://github.com/jonwillits/python_for_bcs/blob/master/ebook/CH00/0.0.%20Installing%20Python.md).
Once you have successfully installed Python, then download the program located here: [Braitenberg's Vehicles #2](https://github.com/jonwillits/intro_to_bcs/blob/master/CH1/vehicles.py).

### Part 1: First Impressions

**Instructions**
1. Start the simulation and watch the vehicles for a few moments without doing anything. Notice how they move.
2. Experiment by moving the heat sources to different positions in the space. Place them close to the vehicles, far away, or in clusters. Watch carefully how the red and blue vehicles respond.
3. Reset and restart the simulation as often as you’d like. Try out different arrangements of the heat sources.

**What to Record**

Write down your first impressions. For now, don’t worry about being technical or precise — just describe the behaviors in everyday language.
- How would you describe what the blue vehicles seem to be doing?
- How would you describe what the red vehicles seem to be doing?
- If you were telling a friend about this, what kinds of words would you use? 
Don’t be afraid to use “mentalistic” language like curious, afraid, aggressive — that’s part of the exercise!

**Goal of Part 1**

The purpose of this stage is to notice patterns and give them names. Later, we will step back and consider what might actually be happening under the hood.




1. Watch the simulation independently for a few minutes and then jot down your thoughts about what is happening. 
After observing the behavior and developing hypotheses about their behavior, answer the following questions:
   - Briefly describe what your group thought was happening. What were your first impressions about how the organism was behaving?


2. Recall from this week's readings, we talked about Marr's three levels of analysis. 
   - Define the three levels.
   - In your description of the organism's behavior above, what level of explanation did your description correspond to? Why?
   - For the two levels your description did not match, give an example of the kind of explanation you would need to give
   to explain the organism's behavior at that level.
 
6. Now imagine that you have done a dissection on one of these organisms and discovered the organization of their nervous system that controls their movement.
   It is surprisingly simple, and is shown in the figure below:

   ![Turtle Vehicle Simulation Motor Nervous System](../images/turtle_neuro.png)

   It turns out that the two kinds of turtles have slightly different nervous systems. The blue turtles' nervous system looks like the one on the left. At the front of the organism near the eyes are two neurons that are heat sensitive, one on the left, and one on the right. These neurons project all the way to the back of the organism and stimulate the feet (the boxes on the bottom left and bottom right). As you can see in the picture, the blue organism has what is called "ipsalateral" organization, the sensor on the left is connected to the foot on the left, and the sensor on the right is connected to the foot on the right. The red turtle, shown on the right, has was is called a "contralateral" organization. It is very similar to the blue turtle, except that the left heat sensor is connected to the right foot, and the right heat sensor is connected to the left foot. This means that if a heat source is located ahead and to the middle of the turtles, it will stimulate the heat sensors that are closer to the heat source a little more than the sensors that are further away, causing the connected legs to move faster.

   Discuss the implications of the organization of this nervous system. What does it explain about how and why the organisms behave the way that they do? 
 
8. One of the main themes of this week is that there are many different levels of analysis, and they sometimes provide different answers. You already attempted to describe this organism's behavior at multiple levels of analysis. Now, I want you to reflect on the value of the different levels, by answering the questions below.
   - Do you think the different levels of analysis provide complimentary or contradictory explanations? Your group members may disagree on this question, feel free to document different perspectives.
   - Are some levels of analysis better or more useful than others, at least in certain circumstances? Again, your group may have differing opinions, please share them. 
  
  
  
 
