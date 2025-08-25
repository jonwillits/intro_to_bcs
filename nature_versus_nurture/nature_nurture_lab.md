# Lab 14: Nature vs. Nurture
 
In this lab we are going to simulate effects of evolution by natural selection.
Go to https://rednuht.org/genetic_cars_2/. 
It is recommended you use the Firefox browser if you have it. 
You will see that it is a simulation of “cars'' driving along a bumpy landscape. 
The further the cars get the bumpier the landscape gets. Each car drives until it gets stuck. 
The winning cars are the ones that get the farthest in the landscape.

Each car has a set of “genes” that specify physical traits that affect its performance. They are:
- Shape (8 genes, 1 per vertex)
- Wheel size (2 genes, 1 per wheel)
- Wheel position (2 genes, 1 per wheel)
- Wheel density (2 genes, 1 per wheel) darker wheels mean denser wheels
- Chassis density (1 gene) darker body means denser chassis

In the simulation, the cars that do a better job driving further get copied into the next generation, and the losing cars do not get to make copies of themselves. 
The number of winners copied is altered by the “Elite clones” option. 
If set to 1, the 1 winner of each race will be copied to the next generation, and the other 19 are generated randomly. 
Alternatively if you set it to 10, the top 10 performers are copied and the remaining 10 are generated randomly.

You can control various properties of the simulation using the options on the top right: 
- Mutation rate: chance that a reproduced copy of a car changes one of its genes
- Mutation size: if a mutation occurs, how big of a difference is it from the parent
- Floor: whether the floor is the same every time, or changes
- Gravity: how much gravity there is
- “Create new world with seed”: this allows you to type a number to generate a specific random world. It is a way to guarantee that you can replicate a specific world if you want to.

After setting the program parameters how you want, clicking the “Go” button will restart the simulation using the parameters you have chosen. 
In the plot right below the visual display, you can see the performance (in terms of distance achieved) of the best car (red), top 10 cars (green) and all 20 cars (blue) over time. 
Below that, you see a depiction of the 20 cars in each generation. You can speed up the simulation using the “surprise” and “fast forward” buttons. 
Surprise disables the visual display at the top (but you still see the cars race in the figure below. The “fast forward” button jumps to the end of that generation (having simulated the winner quickly offscreen) and goes ahead to the next generation. 
So if you press the fast-forward button repeatedly, you can quickly jump through the generations. But be careful about clicking it too fast, that sometimes crashes the simulation.
So wait a second between each click and make sure you see the next generation begin before clicking it again.

You can pause the simulation by clicking the “Go” button. This will open a window asking if you want to reset the simulation. If you hit cancel, the simulation will resume.

## 1. First Simulation (15 PTS TOTAL)

Change “Create new world with random seed” to 1, and make sure that you set the following values:
- ground: “fixed”
- gravity: “earth”
- Elite_clones: 1
- mutation rate and size: 0%

Then click the go button and run the simulation for at least 50 generations (remember you can speed through them by using the Surprise button, you don’t have to watch them all).
When it is done, answer the following questions:
- What kind of car tends to do the best over time, and how far is it getting? (1 PTS)
- Is its performance continuing to improve with each generation, or has it seemed to have hit a peak in its performance?  (2 PTS)
- Why do you think this is happening? (4 PTS)
- Is the car that did the best doing in your simulation similar to the one that is doing best in the simulation for the other people in your group? Explain why you think this might be happening? (4 PTS)
- Describe what’s happening in terms of the algorithm of natural selection. Make sure to reference all three components of the algorithm. (4 PTS)

## 2. High Mutation Rate (15 PTS TOTAL)
Now change the mutation rate and size to 100%, click the Go button (restarting the simulation) and run for at least 50 generations. 
Then answer these questions:
- How did the results compare?  (5 PTS)
- Your results were probably worse. Why? Explain how the performance differed in terms of the evolutionary algorithm. (5 PTS)
- If you change the number of elite clones to 10, will this change its performance on average? Don’t try it. Think it through from first principles. If you got the answer to 2b right, you wont need to simulate it to know what will happen.  (5 PTS)

## 3. Effect of Mutation Rate (22 PTS TOTAL)
You can think of the mutation rate (and size) and the number of copies as factors changing how natural selection can “search” through the space of possible cars, trying to find the one that is the best fit for the environment.
Then answer these questions:
- How does the mutation rate and size affect this search process?  (2 PTS)
- What is a good mutation rate? Again, don’t use the simulation, try to make a guess by thinking through the process. (5 PTS)
- How does the number of elite clones affect this search process? What is the optimal number if you are trying to find the best car quickly? (5 PTS)
- How does the search differ if the number of elite clones is 1 vs 10 vs 20 (the simulation doesn’t let you do 20, but you can imagine). (5 PTS)
- In your group, come up with a set of hypotheses about the best set of mutation and elite clone parameters, and test them by having each member of your group use different settings to evolve a population for 50 generations. Which one did best and how well did it do? (5 PTS)

## 4. Effects of Environmental Variation (30 PTS TOTAL)
Now we want to think about the role that environmental variation plays. 

### 4.1. Random Environments (10 PTS TOTAL)
Without restarting your simulation, think about what happens if you change the floor variable from fixed to “random” (meaning that each generation the floor changes). 
- Do you think the population that you have trained so far on floor 1 do better or worse, on average?  Why? (5 PTS)
- Alternatively, consider that you changed the gravity setting to a different planet. Do you think the population that you have trained so far on floor 1 do better or worse, on average?  Why? (5 PTS)

Now change your settings to the following:
- Mutation rate: 5%
- Mutation Size: 50%
- Elite clones: 5
- Gravity Earth

### 4.2. Divide Into 2 Groups (10 PTS TOTAL)
Next your TA will now divide the class into two groups, A and B. 
Group A will be training cars with the floor set to fixed, and each group member will use a different random seed. 
Person A1 will do random seed 1, A2 will do random seed 2, and so on. 
Members of group B will set their floor to mutable, meaning that the floor will be randomized each time. 

- Before we start, which group do you think will perform best, on average. Why?  (5 PTS)

Now run the simulation for 50 generations. 
Then pause the simulation and have everyone report their results. 
- Which group did better, on average?  (5 PTS)

### 4.3. Switch Conditions (10 PTS TOTAL)
Next, switch groups. Do not reset your simulation. 

If you were in group A (with fixed floor), change the floor to mutable.
If you were in group B (with mutable floor), change it to fixed (meaning it will repeat over and over whatever floor it had done last). 
- Which group do you think will do better? Why? (5 PTS)

Now run the simulation for 50 generations and report the results. 
- Did the result match your hypothesis? (5 PTS)

## 5. Comparing Evolution by Natural Selection and Learning (18 PTS TOTAL)
- Evolution by Natural Selection can be considered an algorithm. What are the steps of the algorithm? Try to put it into words. (6 PTS)
- Is evolution by natural selection more like supervised learning or unsupervised learning? Why (4 PTS)
- What are at least two similarity and differences (each) between evolution by natural selection and by supervised and unsupervised learning (8 PTS)


