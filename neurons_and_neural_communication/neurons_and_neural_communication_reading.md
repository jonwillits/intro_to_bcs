# 3. Neurons and Neural Communication

This module is about the neuron. It is the cell that turns an event into a fast, precisely aimed signal. And it is the first piece of biological machinery this course examines at all three of Marr’s levels. While reading, look for the beginnings of answers to these questions:

- What problem were neurons the solution to? And why did only some kinds of living things ever need to solve it?
- What does a single neuron actually compute, and how much of a mind could be built out of something that simple?
- If every signal a neuron sends is identical to every other one, where is the information?
- What does it cost to have this machinery for thinking, and how does the bill get paid?
- The unit at the center of modern artificial intelligence is named after the neuron. How close is the resemblance, and where does it break down?

By the end, we should have a working answer to each question. We will also have the beginning of a habit, a demonstration of how we can investigate a capacity at all three of Marr’s levels.

---

Most of us learn at some point that a cell has parts. A nucleus holding its DNA. Mitochondria supplying its energy. A membrane holding the whole thing together. And small machines inside it that build proteins and other molecules. The list is familiar enough that it is easy to stop finding it strange. But it is *very* strange!

Somewhere in this planet’s first billion years or so, lifeless chemistry became organized into something that maintains itself, powers itself, repairs itself, and makes more of itself. Nothing about chemistry suggests it should do any of that. Two questions grow out of the strangeness. First, where did that complexity come from? Second, why was this complexity worth all the effort?

Of all the kinds of cells that complexity eventually produced, one is primarily responsible for minds. The neuron senses, it signals, and in a small way, it decides. In a human mind, something like eighty-six billion of them, wired to one another, are reading this sentence right now.

In our first three modules, we built the structure we use in the course. Module 0 asked what brain and cognitive science is. Module 1 asked how mind relates to brain, and adopted Marr’s three levels of explanation for answering questions about both. It also said that from here on, the course would take one capacity at a time and work it at all three levels. Module 2 asked what can be learned by setting two systems side by side, and laid down the evolutionary narrative the rest of the course follows. Now, we are ready to start the narrative.

Our first step is the cell that makes minds physically possible. Two things about that cell organize this chapter. First, neurons are the animal’s answer to a problem: ordinary chemical signaling was not fast enough for many problems animals faced. Second, neurons are the body’s first great metabolic outlier. They are extraordinarily expensive to run.

This chapter has three sections, one for each level [](#t-levels-neuron). §3.1 asks why neurons evolved. §3.2 asks what a neuron computes. §3.3 asks how a living cell physically manages it, and what it costs to run.

: Marr’s three levels, the question each asks, the discipline that asks it, and this module’s example. Every module from here on reprints this table with its own example in the last column. {#t-levels-neuron}

| Level | The question it asks | Discipline | This module’s example: the neuron |
|---|---|---|---|
| Computational | What problem is being solved, and why does solving it matter? | Evolution and ecology | Fast, long-distance, reliable signaling, for an animal that must sense, decide, and act before something else does |
| Algorithmic | What is represented, and by what procedure? | Cognitive psychology and AI | Receive, integrate, transmit; a threshold, and an all-or-nothing spike |
| Implementational | By what physical means, and at what cost? | Neuroscience | Ion gradients across a membrane, the sodium-potassium pump, and the action potential |

One thread runs through all three levels, and it is worth attending to. Neurons are expensive. Animals could afford them only after a revolution in the way living things capture energy, and the price of running them still shapes how brains are built today. The story that opens §3.1, about how life became rich enough to build neurons at all, is the same story that closes §3.3, about why the brain is the most expensive organ in the body.

A second thread starts here and runs to the end of the course: the comparison between natural and artificial minds. It begins at the smallest scale available, a single cell. This is because the unit at the heart of modern artificial intelligence is also called a neuron, and artificial neurons were built as stripped-down copies of biological neurons. We will set the two beside each other as we go, and look hardest at the place where they turn out to differ most. This is not what they compute, but what they are made of.

## §3.1 — Computational: Why Neurons Evolved

### §3.1.1 — The Computational Question

This chapter is the first place in the course where we take a single thing and ask all three of Marr’s questions about it, one section at a time. First, the computational question: what problem was being solved when neurons evolved?

Living things have no designer. So when we ask what a biological structure is for, the only answer available that does not appeal to magic is a historical one: the structure is here because the organisms that had it left more descendants than the organisms that did not. Asking what a neuron is for is therefore the same as asking what selective pressure favored building a neuron.

That gives us the question this section answers. What could a neuron do that earlier life could not do, and for whom did that difference matter enough to be selected? The disciplines that answer questions in this shape are evolutionary biology and ecology. Each of the three sections of this chapter names its level and its discipline as it opens, because the rhythm is new and worth feeling as it starts.

Recall the principles of natural selection we discussed in Module 2. Variation arises among individuals. Some of that variation is heritable. Some heritable variants leave more descendants than others. And so, over generations, the population changes.

Module 2 discussed that process with regard to the evolution of species, and of the traits those species have. Now, we discuss how that process changed something even more fundamental: the kinds of cells that an organism has. A neuron is an adaptation in exactly the sense Module 2 gave the word. And the same three-part logic that explains the coloring of a moth, also explains why some lineages came to build neurons, *and most never did*.

One misuse of natural selection that we discussed in Module 2 is important to us here. Module 2 was firm that evolution is not a climb toward anything, and that there is no ladder with human beings at the top of it. This section walks forward through time, from chemistry to cells to animals. This walk forward through time reads very easily as a walk upward. But it is not one. Neurons are not an achievement that some lineages managed and others failed at. They are an expensive solution to a problem, and this solution was the path taken by only some living things. Plants have no neurons. But they are not thereby behind. By every measure that matters to a plant, plants are doing just fine, thank you very much.

### §3.1.2 — The RNA-World Hypothesis and the Beginning of Life on Earth

A neuron is a cell, and an unusually elaborate one. Before we can ask how evolution produced such a thing, there first had to be cells. And a cell is not an obvious object. It is a bounded, organized system of chemistry that maintains and repairs itself, obtains energy and materials from its surroundings, and belongs to a lineage capable of making more cells. It is far from obvious how the chemistry of a lifeless planet crossed that threshold. So our story starts earlier than an introduction to the mind usually starts: on an Earth awash in chemistry, but without life.

One leading hypothesis about this transition is the RNA-world hypothesis. RNA, or ribonucleic acid, is a carbon-based polymer remarkable for its ability both to carry information in its sequence and, when folded into certain shapes, to accelerate chemical reactions. This does not mean that scientists know life began with RNA. RNA may have been preceded by simpler chemical systems, and precisely how it first arose remains unresolved.

The Earth formed approximately 4.5 billion years ago. During the hundreds of millions of years that followed, energy from sunlight, electrical discharges, impacts, geothermal heat, and chemical gradients drove innumerable reactions. Some produced increasingly complex organic molecules. Under certain conditions, RNA building blocks can form without life, and activated building blocks can join into short chains. Something like this may have happened on the early Earth, although no surviving evidence tells us exactly when or where.

Most early RNA molecules would presumably have broken down or lacked any useful activity. A few may have folded into shapes that accelerated particular reactions. Catalytic RNA molecules of this kind are called *ribozymes*. Eventually, according to the RNA-world hypothesis, RNA or a related molecule became involved in making copies of molecular sequences — perhaps through networks of molecules that helped replicate one another.

Once those copies resembled their templates, there was *inheritance*. Because copying was imperfect, there was *variation*. And if some variants survived or reproduced more effectively than others, there was *selection*. At that point, the basic ingredients of Darwinian evolution were present, even if nothing yet existed that everyone would agree to call an organism. Evolution may therefore have begun before cells — and perhaps before life had acquired a clear boundary.

### §3.1.3 — The Evolution of Cells

Replicating molecules are not yet cells. What they lack is a boundary. The next step may have begun when some of these replicating systems became enclosed. Simple fatty molecules existed in which one part interacts with water, while another avoids it. This caused them to assemble spontaneously into hollow, membrane-bound *vesicles*. Most vesicles would have contained little of consequence, but some may have trapped RNA and other useful molecules.

Their membranes could let small molecular building blocks pass in and out, while retaining the longer strands inside, keeping cooperating molecules together and shielding them from dilution. Vesicles could also acquire more fatty molecules, grow, and split under physical forces, passing some of their contents to each daughter. If a particular RNA system helped its vesicle grow, persist, or reproduce, selection could now act on the whole package, rather than on naked molecules alone. Such packages are called *protocells*. Over time, increasingly tight coordination among RNA replication, energy use, membrane growth, and division may have transformed protocells into the ancestors of true cells.

At some stage, protocells also changed how they stored information. In the standard RNA-world account, catalysts evolved that converted RNA building blocks into DNA building blocks and copied information from RNA into DNA. DNA was less vulnerable to spontaneous breakdown, and its complementary strands made damaged information easier to recover. Protocells using DNA could therefore preserve larger sets of instructions more reliably, although RNA and DNA may have coexisted from much earlier.

The instructions coded by DNA and RNA allowed cells to do more than replicate their genetic material. DNA stored them. RNA copied and used them to create proteins, while retaining some of its earlier catalytic roles. Proteins became the principal catalysts of cellular chemistry.

Together, DNA, RNA, and proteins formed a system that captured energy, built and repaired membranes, produced new molecular machinery, and coordinated the copying and division of the cell. Cells that constructed and maintained themselves more effectively left more descendants, allowing natural selection to improve increasingly elaborate cellular systems.

By the time of *LUCA* — the Last Universal Common Ancestor — this division of labor had probably become established. LUCA was not the first life, nor necessarily a single organism. But it was the ancestral population from which all cellular life alive today descends. It already possessed the genetic code, ribosomes, protein enzymes, and a complex metabolism. Considerable evolution had therefore occurred before LUCA. It marks not life’s beginning, but the deepest common ancestor that surviving organisms allow us to reconstruct.

One feature of this early cellular world matters more for our purposes than any particular piece of chemistry. Long before life had neurons, cells evolved ways of sensing their surroundings and acting on what they sensed. A swimming bacterium such as *E. coli* can compare the present concentration of a nutrient with the concentration it encountered a few seconds earlier. If conditions are improving, it continues in roughly the same direction. If they are worsening, it tumbles and sets off in another. This behavior, called *chemotaxis*, gradually carries the bacterium toward nutrients and away from harmful substances. The loop of receiving information from the world, transforming it internally, and changing behavior in response is therefore billions of years older than neurons. A single cell can already close that loop, using receptor proteins, molecular signaling pathways, and a protein motor.

The cell was also processing information in another sense. DNA was transcribed into RNA, and RNA sequences were translated into proteins, allowing stored information to direct the cell’s construction, maintenance, and reproduction. Genetic processing and sensory processing were different operations, but both were already present in cellular life. Neurons would not invent either information processing or the sensing-and-action loop. They would add a new layer: a specialized means for transmitting information rapidly between distant parts of a multicellular organism, allowing many cells to sense and act as a coordinated whole.

### §3.1.4 — The Energy Revolution

Everything a cell does costs something. Building a protein, moving a flagellum, repairing damage, and copying a genome, all cost a great deal. Cells pay all of these bills in the same currency: **ATP**, a small molecule that stores energy in a chemical bond and releases it where it is needed. A cell’s whole economy runs on making ATP and spending it.

ATP did not have to be invented for this job. Adenosine triphosphate is a nucleotide: adenine, a sugar, and three phosphate groups. It is one of the four building blocks that RNA is assembled from, and the phosphates are what “activated” those building blocks so they could join into chains. So the molecule was already there, already abundant, and already carrying energy in its phosphate bonds. Phosphate bonds are well suited to the role. They release a great deal of energy when broken, and they do not break on their own in water, so a cell can store energy in them and use it when it chooses. Why this nucleotide became the currency rather than one of the other three is still argued over. What is not in doubt is that once it was the currency, it was very difficult to replace, because by then everything else was built to use it.

Early cells made ATP in a way that is ingenious and meager at once. Energy from chemical reactions is used to pump protons across a membrane, so that protons pile up on one side. They then flow back through a protein that spins as they pass. Making ATP means pushing phosphate groups together, and they repel one another electrically. The spinning is the mechanical force that does the pushing.

Water behind a dam is the usual comparison, and it is a good one, because the arrangement stores energy as a difference across a barrier and collects it on the way down [](#f-proton-gradient). The scheme works, and it works in essentially every cell alive today. What it did not do, in early life, was produce very much. Early life could produce energy. But it was energy poor.

![Early life’s way of making ATP, and the arrangement §3.3.2 will meet again. Energy from chemical reactions drives protons to one side of a membrane, where they pile up. They return through a protein that spins as they pass, and the spinning is the mechanical force that pushes phosphate groups together. Storing energy as a difference held across a barrier is a trick life found early and never gave up.](reading_images/fig-proton-gradient.svg){#f-proton-gradient alt="A cross-section of a membrane drawn as a horizontal band of paired fatty molecules. Above the band, many small circles marked H plus are crowded together; below it there are only four. On the left, a protein spanning the membrane carries a long arrow pointing upward, labeled as energy from chemical reactions pushing protons up against the gradient. On the right, a second protein carries an arrow pointing downward, leading to a circle marked with a curved rotation arrow, which in turn feeds a circle labeled ATP."}

Then a revolution occurred: some of these cells evolved the ability to capture sunlight. *Photosynthesis* uses light to build sugar out of carbon dioxide and water. The sugar could then be broken down, and its energy released, to power the creation of ATP. This turned a renewable and enormous energy source (sunlight) into a storable chemical one. The consequences for life were large. The consequences for the planet were larger, because photosynthesis has a waste product, and the waste product is oxygen.

For most life on earth, the “pollution” created by photosynthesis (the massive amount of oxygen released) was at first a catastrophe. Oxygen is chemically aggressive. It wrecks the molecules of organisms not built to handle it. And its accumulation is associated with one of the earliest mass extinctions in Earth’s history, known as the *Great Oxygenation Event*.

The consequence is one the rest of this chapter depends on. The same chemical aggressiveness that made oxygen a poison, makes it an unusually good acceptor of electrons. And a lineage that could make use of that could extract far more energy from the same food. This process, in which oxygen serves as the final acceptor of the electrons stripped from food, is called *aerobic respiration*. And it yields something like fifteen times as much ATP from a molecule of sugar as the older, oxygen-free methods do. Oxygen was a poison. But it became a windfall for the cells that happened to be able to make use of it. And everything expensive that life built afterward was paid for out of that windfall.

### §3.1.5 — What the Surplus Allowed

A large and reliable energy surplus makes arrangements affordable that were not affordable before. The history of life after oxygen is largely a history of newly affordable adaptations.

The word *affordable* invites a misreading worth heading off. It can sound as though life had been waiting for the money to arrive, holding plans it could not yet pay for. There were no plans, and nothing was waiting. Before oxygen, mutations pushing toward greater complexity would have arisen as mutations always do: a larger cell, an extra internal compartment, more machinery to build and maintain. Those variants appeared, and they died out. What they cost in energy was more than what they returned, so the cells carrying them left fewer descendants and the variation did not spread. Then some lineages happened onto a way of using oxygen, and the arithmetic changed underneath them. The very same variation that had been too expensive to keep was now worth its price, and the cells carrying it left more descendants rather than fewer. Nothing about the mutation had changed. What changed was the energy available to pay for it. Selection never looked ahead. It only ever compared the variants that already existed, and the new energy surplus changed which of them was worth keeping.

One of the first major adaptations after the evolution of aerobic respiration was that some lineages evolved larger, more elaborate cells. A *eukaryote* is a cell with its DNA enclosed in a nucleus, and its chemistry divided among internal compartments. It is the kind of cell that plants, fungi, and animals are built from. Eukaryotes appear to have arisen through *endosymbiosis*. One cell engulfed another and, instead of digesting it, kept it. The engulfed oxygen-users became *mitochondria*, compartments dedicated to aerobic respiration. A cell with its own internal power plants can pay for a great deal more machinery than one without them.

Another major adaptation was *multicellularity*, the arrangement in which cells that could live independently instead stay together and function as a single organism. Multicellularity has arisen many separate times. What it allows is *division of labor*. If every cell must do every job, then every cell will probably be mediocre at all of them. But if cells can specialize, some can be built for movement, others for digestion, and others for sensing. Each can be far better at its one job than any generalist cell could be at any job. Bones, muscles, skin, and other organs are what specialization looks like once it has run for a while.

Specialization and multicellularity also creates a problem that did not exist before. A colony of identical cells has nothing much to coordinate. A body of specialized cells has to act as one thing. The cells that sense are not the cells that move, and the cells that move are not the cells that digest. So information gathered by one kind of cell has to reach a different kind entirely, and in time for it to be useful. The cells that must act on what a sensor detects cannot detect it themselves. Call this the **coordination problem**. Every complex multicellular organism has some version of it, and how urgently it needs solving turns out to depend entirely on how the organism makes its living.

### §3.1.6 — Three Ways to Be Complex

Complex multicellular life did not solve the coordination problem once. It solved it at least three times, differently, and setting the three side by side isolates exactly the variable we are looking for [](#t-three-strategies).

: Three strategies for complex multicellular life, and what each one demands of a body. Only one of the three makes fast, whole-body coordination worth paying for. {#t-three-strategies}

| | Plants | Fungi | Animals |
|---|---|---|---|
| How it gets energy | Makes its own food from sunlight | Grows into its food and absorbs it | Finds food, and eats other organisms |
| What the body does | Stays put; grows toward light and water | Stays put; grows through the material it feeds on | Moves through the world, and is moved through by others |
| What can go wrong in a second | Very little | Very little | Being eaten; losing prey; a bad step |
| Coordination it needs | Slow and chemical is enough | Slow and chemical is enough | Fast, aimed, whole-body |

Reading across the table is Module 2’s comparative method, applied not to two species but to three whole ways of making a living. Module 2’s more common move asks why two things are alike. The useful move here is the mirror of it: these three are all complex, all multicellular, all descended from the same eukaryotic beginning, and only one of them evolved neurons. What separates that one from the other two is the thing we are looking for.

The separating variable is speed, and the reason is that animals eat other organisms and are eaten by them. A plant threatened by drought has hours or days to respond, and it responds with growth and chemistry, which is enough. An animal being hunted has a fraction of a second. In a predator–prey arms race, the animal that senses, decides, and acts slightly faster than its opponent is the animal that eats or the animal that escapes, and both outcomes get written into the next generation. So the animal way of life puts a premium on speed that the other two strategies simply do not have.

That premium is worth naming, because it is the thing the rest of this chapter is about and the thing much of the rest of the course is about. Call it the **sense → decide → act loop**: take in information about the world, do something with it, and produce an action, fast enough for the action to still be the right one. It returns at the algorithmic level, where we ask what the neuron computes, and at the implementational level, where we ask what it costs to run. It is also not a problem unique to living things. Any system that has to operate on its own in a changing world faces some version of it, and a robot or a self-driving car in a later module needs its own answer to it. The neuron is evolution’s answer.

The animal solution shows up early in development, and in one piece. Very early in the development of an animal embryo, at gastrulation, the cell layers that will become gut, muscle, and nervous system are laid down together, which is what we should expect given that none of the three is much use without the other two.

### §3.1.7 — Why Chemistry Was Not Fast Enough

Cells had been signaling to one another for billions of years before animals existed. And animal bodies still use chemical signaling constantly. A hormone is released into the bloodstream by one tissue, travels through the body, and changes what other tissues do. Chemical signaling is cheap, it reaches everywhere, and it does not require any special apparatus beyond the ability to make the molecule and respond to it.

Its limitation is that it moves by diffusion, and diffusion is slow in a way that gets rapidly worse with distance. A small molecule crosses a micrometer, roughly the width of a bacterium, in about a millisecond. It crosses a millimeter in several minutes. It would cross a meter, the length of a large animal, in something on the order of a decade. The time does not grow in proportion to the distance; it grows with the square of the distance, so every doubling of distance quadruples the wait [](#f-diffusion-distance). Diffusion also spreads in every direction at once, which means a chemical signal cannot be aimed at one destination. And it lingers, which means it cannot easily be switched off. For a message like *grow* or *get hungry* or *begin reproducing*, that might be fine. For a message like *the left side of the body should contract, now*, these limitations could be fatal.

![The time a small molecule takes to diffuse a given distance, on logarithmic scales. Diffusion crosses a bacterium in well under a millisecond, a thick tissue in minutes, and the length of a large animal in about a decade — because the time grows with the square of the distance rather than in proportion to it. The shaded band is the fraction of a second an animal being hunted actually has.](reading_images/fig-diffusion-distance.svg){#f-diffusion-distance alt="A line graph with distance on the horizontal axis from one micrometer to one meter, and time on the vertical axis from a millisecond to years, both scales logarithmic. A single straight rising line crosses three marked points: about 0.3 milliseconds across a bacterium, about 6 minutes across a thick tissue, and about 11 years across the length of a large animal. A shaded band along the bottom of the plot, below a tenth of a second, is labeled as the time an animal being hunted has; the line leaves that band almost immediately."}

So it is worth being careful about what neurons actually contributed. They did not invent communication between cells, and they did not invent behavior. Both were in place long before them. What they did was make a trade. Chemical signaling is cheap and reaches everything; neural signaling gives up the cheap broadcast reach and buys speed, distance, and aim in return [](#t-chemical-vs-neural). The two coexist in every animal body, doing the jobs each is suited to. Animals still run on hormones for everything that can afford to be slow.

: The trade neurons made. Chemical signaling was not replaced; it was joined by something that gives up reach and buys speed, distance and aim. Both are still running in every animal body, doing the jobs each is suited to. {#t-chemical-vs-neural}

| | Chemical signaling | Neural signaling |
|---|---|---|
| How the message travels | by diffusion, or carried in the bloodstream | as a signal regenerated at full strength along a fiber |
| Crossing the length of a large animal | years, left to diffusion | a fraction of a second |
| Where it arrives | everywhere at once | at one specific destination |
| Switching it off | it lingers | it ends with the signal |
| What it costs | cheap, and needs no special apparatus beyond making the molecule | expensive, and the cost is the subject of §3.3 |
| The kind of message it suits | *grow*, *get hungry*, *begin reproducing* | *the left side of the body should contract, now* |

A **neuron**, then, is the cell specialized to make that trade. It takes an event, whether in the world or elsewhere in the body, and converts it into a signal that travels fast, travels far without weakening, and arrives at a specific destination rather than everywhere. That is the computational-level answer to what a neuron is for. And it is why neurons took hold in the animal lineage and not in plants or fungi. The lineages whose sense → decide → act loop ran faster, were the lineages that ate rather than were eaten.

Fast, aimed, long-distance signaling comes with a cost attached, and the cost is the other thread of this chapter. Speed of that kind is not free. And the surplus that made animals possible in the first place, is the same surplus that neurons spend in order to signal.

We have stated the problem that neurons turned out to answer for early multicellular life. The next question is not why but how. Granting that a neuron’s job is to take signals in, combine them, and pass one along, what exactly is it computing? That is the algorithmic level.

## §3.2 — Algorithmic: What a Neuron Computes

### §3.2.1 — The Algorithmic Question

The previous section asked what neurons are for, and answered with a problem: animals need to sense, decide, and act faster than diffusing chemicals allow. This section asks a different question about the same cell. If a neuron’s job is to take signals in and pass a signal along, how exactly is it doing that? That is Marr’s algorithmic level, and it is a question about procedure rather than purpose.

Answering it requires a process that is worth performing deliberately, because it will happen in every module from here on. For the time being, we are going to set the biology aside, and describe the neuron as though we did not know what it was built from. This is the abstraction Module 1 said makes comparison between brains and machines tractable. And this chapter is where the reader sees the price and the payoff: a functional description here, a physical one in §3.3.

At this level of abstract description, a neuron does three things. It *receives* signals from other cells. It *integrates* them, combining many inputs into a single verdict. It *transmits* one signal onward. Receive, integrate, transmit. Everything else in this section are details fleshing out those three verbs.

### §3.2.2 — Four Roles the Cell Has to Fill

Receiving, integrating, and transmitting require four things. At the algorithmic level, they are better thought of as jobs, rather than as objects or parts. The job that a neuron is performing needs an input surface, the place where signals from other cells arrive. It also needs an integrator, where arriving signals are pooled and a verdict is reached. It needs an output, that carries the verdict away to other neurons. And something has to be the junction where the output of one cell becomes the input of the next.

Each of these four jobs is a real piece of a real cell, with a name and a shape. The way biological neurons do this will be described in §3.3. But for now we stay at the more abstract level.

One feature of the arrangement matters more than any of the four roles. The flow within a single neuron is one-way. Signals arrive at the input surface, are pooled by the integrator, and leave down the output line. They cannot run backward. A cell with a distinct input end, and a distinct output end, can be wired to other cells in a definite direction. That is what makes it possible to build a circuit rather than a puddle.

The difference between the two is worth being concrete about. In a neural circuit, whether two neurons are connected has nothing to do with whether they are physically near each other. One neuron’s output line may run the length of the organism’s body to reach the cells it connects to, while a cell pressed right up against it receives nothing. Connection is a matter of wiring rather than proximity. And because it is, it is possible to ask what a given input leads to and get an answer.

Now suppose instead that signals could enter and leave a cell anywhere on its surface. Every cell would influence every neighbor it touched, in every direction at once, and activity would spread outward from wherever it began rather than travel anywhere in particular. That is the puddle, where being next to something is the same as being connected to it. And it is the same defect chemical signaling had: a message that goes everywhere carries no information about where it was meant to arrive. One-way flow is what turns a collection of cells into something that can be wired to perform complex computations [](#f-circuit-vs-puddle).

![The same seven cells in the same positions, joined two different ways. On the left, signals run in one direction to particular cells, one of them distant, while a cell in the middle of the group receives nothing at all. On the right, every cell influences every neighbor it touches and activity spreads outward in rings from wherever it began.](reading_images/fig-circuit-vs-puddle.svg){#f-circuit-vs-puddle alt="Two panels side by side, each showing the same seven circles in the same positions. In the left panel, arrows run between particular circles in one direction only, including one long arrow that skips across the panel; a circle near the center is ringed in red and has no arrows touching it. In the right panel, plain lines join every circle to each of its near neighbors, and a series of dashed concentric rings spreads outward from the leftmost circle across the whole panel."}

Module 4 is entirely about what happens once complex computations become possible.

### §3.2.3 — Integration and Threshold

The middle verb is the interesting one. A neuron does not pass along what it receives. It receives from many cells at once and produces one output. This means something has to happen in between. What happens is **integration**: the arriving signals are added up.

What the neuron does with the total is the crux. It does not report the total. It compares the total against a **threshold**, a level the summed input has to reach. Below threshold, the neuron does nothing at all. At or above it, the neuron acts. So a single neuron is not a wire or relay that just passes information along. It is a small evaluator, pooling evidence from many sources, and answering one question with it. Given everything arriving right now, do I act now, or not?

That is a real computation, performed by one cell. And notice how little the cell needs to know. Nothing in it requires a view of the animal’s situation, or any idea what the inputs mean. Sum the inputs, compare against a level. Almost everything in this book is built out of that operation, repeated in enormous numbers. The magic comes from how the neurons are wired together.

That is a claim about the description, though, and not about the cell. Sum-and-threshold is a choice about how closely to look, taken because it is simple enough to reason about and to build with. Whether it is also *sufficient* — whether a real neuron is doing something considerably richer that this description throws away — is an open question, and a live one. §3.2.9 returns to it once the description has been made precise enough to argue with.

### §3.2.4 — The All-or-Nothing Spike

When a neuron does act, what it produces is an **action potential**, commonly called a *spike*: a brief, stereotyped electrical event that travels the length of the cell. §3.3 shows how biological neurons physically make an action potential. What matters at the algorithmic level is its shape, which is to say that it does not *have* a variable shape.

An action potential is **all-or-nothing**. Cross the threshold, and the neuron produces a full spike. Fall short, and it produces nothing. There is no such thing as a small action potential, or a large one, or one that fades partway along. This is the single most counterintuitive fact about neurons. A stronger stimulus does not produce a bigger spike. Every spike a given neuron fires is essentially identical to every other one.

Ask Marr’s question about that design. Why would a signaling system throw away the obvious option of letting the signal’s size carry the message? The answer is exactly the demand §3.1 established. A graded signal, one whose size means something, degrades as it travels. It fades with distance, blurs in time, and picks up noise from everything around it. So by the time it has crossed a meter of animal there is no way to tell how much of what arrived was the message. An all-or-nothing signal has none of those problems, because it is regenerated at full strength the whole way. What arrives at the far end is exactly what left. The signal is fast, it is sharply timed, and it is as reliable at a meter as at a micrometer, which is the combination §3.1 said the animal way of life demanded, and chemical signaling alone could not supply.

It is worth noticing that human engineers made the same choice, independently and for the same reason. Digital signals are all-or-nothing for precisely this purpose. A value that is only ever fully on or fully off can be cleaned up and passed along without accumulating error. And a value that varies continuously cannot. Two very different kinds of systems (biological organisms and digital electronics), facing the same problem of getting a message somewhere intact, arrived at the same solution.

And life had arrived at the same solution long before the evolution of neurons or the invention of digital electronics. The information in DNA is carried by which of four base molecules occupies each position, not by how much of anything is present. And that is why a sequence can be copied for billions of years and still be read correctly. A discrete signal can be checked and restored, while a continuous one can only be approximated.

### §3.2.5 — Where the Message Is

The all-or-nothing spike raises a question that has to be answered before we can go further, because on its face it looks like it makes neurons useless. If every spike is identical, how can a neuron say anything except *yes*? A cell that can only produce one signal, can only carry one message.

That question has more than one answer, and the answers work together. The first answer concerns a single cell’s own output. The key is to realize that a neuron’s message is not in any one spike, any more than the meaning of a sentence is in any one word. It is in how many spikes, and when. A neuron presented with a faint stimulus fires occasionally. Presented with a strong one, it fires far more often, and the spikes come closer together. Nothing about any individual spike has changed. What changed is the number of them in a stretch of time. This is the neuron’s **firing rate**, and the sequence itself is called a *spike train*. So the whole correction runs this way. A stronger stimulus does not produce a bigger spike. It produces more spikes, faster.

An example makes the arrangement concrete. Press a finger against a table, gently at first and then hard. Receptors in the fingertip have to report not merely that contact has happened but how much of it, and they have to report it most of a meter away, to the spinal cord and the brain.

Consider what either the earlier, chemical-only method, or the purely digital all-or-none method, would do on its own. A chemical signal could carry the amount easily, since the quantity released can be made proportional to the pressure. But §3.1 already described that method’s shortcoming. Left to diffusion, the message would take years to cross the arm. Carried in the blood, it would arrive faster. But it would also arrive everywhere in the body, rather than at the one place that needs it. A purely all-or-nothing signal, one spike for contact and nothing otherwise, would arrive in milliseconds and arrive intact. But it could report only that something had been touched, not how firmly.

The firing rate gets both. Every spike is identical and every spike is regenerated at full strength, so the message survives the trip the way a digital signal or a DNA sequence does. And the number of spikes in a second is a quantity that can take any value in a range, so the amount survives too. Press harder and the receptors fire faster [](#f-rate-code). What travels up the arm is a stream of identical pulses. What arrives is a number.

![Three seconds of a touch receptor’s output, at three levels of pressure. Every mark is the same size in every row, because every action potential a cell fires is the same size as every other. What changes with pressure is how many marks there are, and how close together.](reading_images/fig-rate-code.svg){#f-rate-code alt="Three horizontal rows of short vertical marks on a common one-second timeline, labeled a light touch, a firmer press, and pressing hard. The marks are identical in height and width in all three rows. The top row has five marks spread widely apart, the middle row twelve, and the bottom row twenty-four packed closely together."}

And there is more in a spike train than its rate. The precise timing of spikes carries information too. In some systems, timing carries a great deal of information. The important point is the one already made: meaning rides on patterns embedded in the series of identical pulses, never on the size of any one of them.

There are other answers to how action potentials carry information that will depend on things we will explain later. But in short, a spike’s effect also depends on which chemical carries it across the junction to the next cell, and on how strong that particular connection is. Those two come in the next sections, and what happens once connections can change with experience is Module 5. It depends as well on which cell fired in the first place, since an identical spike arriving from the eye means something quite different from one arriving from the ear, and that is a question the course takes up when it reaches perception. Rate and timing are where we start, because they are what a single cell can vary from moment to moment on its own. The rest are properties of the wiring.

### §3.2.6 — Two Ways to Describe an Output

Describing a neuron’s output as a rate resolves an apparent contradiction that runs through the rest of this chapter. It is worth being explicit about that contradiction, because the two descriptions are about to be used side by side, and someone who takes them for competing claims will be lost. A neuron’s output is all-or-nothing, and a neuron’s output is a rate that can take many values. Both are true. They are descriptions at two different time scales, not two competing theories or explanation. Look at a single millisecond and there is either a spike or there is not, and if there is one it is the same size as all the others. Look at a hundred milliseconds and there is a count instead, and a count is a number that can land anywhere in a range. A rate is not an alternative to all-or-nothing signaling. A rate is what a lot of all-or-nothing events look like when they stop being looked at one at a time [](#f-two-time-scales).

![One spike train at two magnifications. Across a hundred milliseconds there is a count, and a count can take any value in a range. Within a single millisecond there is one event, the same size as every other. The two descriptions are not competing claims about the cell; they are answers to questions asked at different time scales.](reading_images/fig-two-time-scales.svg){#f-two-time-scales alt="Two panels. The left panel shows nine identical vertical marks along a hundred-millisecond line, with a note that nine spikes in a hundred milliseconds is ninety per second. A small rectangle around one of the marks opens out, along two dashed guide lines, into the right panel, which shows the smooth rising and falling voltage curve of a single action potential filling the frame."}

Which description is the right one depends entirely on the question being asked. This is Marr’s point, arriving in a new place. Ask what a cell contributes to an animal’s behavior over a stretch of time long enough for behavior to happen, and the rate is the quantity that matters. Ask how the cell physically produces one event, and the individual spike is the object of study. This section, working at the algorithmic level, will describe neurons in terms of rates. §3.3, working at the implementational level, will describe a single spike in terms of ions crossing a membrane. Both will be models of the same cell, and the fact that they look nothing alike is not a problem to be resolved. It is what having multiple levels of analysis is for.

### §3.2.7 — Excitation, Inhibition, and Modulation

So far, we have described the inputs arriving at a neuron as all pushing in the same direction: toward the threshold at which an action potential will occur. But this was a simplification that we will flesh out now.

Signals usually cross the junction between cells, neurons included, chemically. The arriving spike causes the sending cell to release a **neurotransmitter**, a chemical that drifts across the gap and binds to the receiving cell. What the receiving cell does about this depends on which chemical arrived. **Excitatory** neurotransmitters push the receiving neuron toward its threshold, making a spike more likely. **Inhibitory** neurotransmitters push the neuron away from its threshold, making a spike less likely. Which particular chemicals do each job is a fact about the machinery, which we will discuss in §3.3.

Because the integrator sums both kinds together, a neuron can do considerably more than register how much is arriving. It can fire only when one input is active and another is silent, which is the beginning of *this and not that*. It can stay quiet unless several inputs arrive close enough together in time, which is a coincidence detector. It can be shut down entirely by a single well-placed inhibitory connection, which is a veto. None of these is a matter of relaying anything. The balance between excitation and inhibition is what turns a chain of cells passing messages along into an assembly that computes something. This is an idea we will explore in much more detail in Module 4.

There is a third category of neurotransmitters, which we will merely mention for now. Some signals do not push a neuron toward its threshold or away from it. They change how strongly it responds to everything else, turning the whole cell’s sensitivity up or down. This is called **modulatory signaling**. It is how an animal’s internal state — hunger, alarm, whatever it was doing a moment ago — reaches into a circuit and changes what that circuit does with the same inputs. The same circuit for recognizing food may, for example, respond differently when the animal is hungry than when it is not. The specific chemicals that do this work, and the account of internal states and value that they make possible, are discussed in Module 4.

### §3.2.8 — Writing a Neuron Down

Everything said so far has been said in words, and words are where an account like this stops in many introductory courses. But it is worth going one step further, because a great deal of what brain and cognitive science actually does with a description of this kind is write it down as something that can be computed with. Module 2 called that the synthetic method: understanding by building. A description in words can be agreed with. A description precise enough to compute with makes predictions, including predictions about cases nobody has tested. And it can be wired to other descriptions like it, run, and tested.

Start from the rate description, since rate is the property this kind of description can put a number on. One neuron receives input from several others. And each of these input neurons has its own firing rate. Call those input rates x₁, x₂, x₃, and so on. Each connection also has a strength, and a sign: an excitatory connection pushes the receiving cell up, an inhibitory one pushes it down, and connections differ in how much of either they do. That strength-with-a-sign is a connection’s **weight**, written b₁, b₂, b₃. Finally, most neurons are not silent when left alone; they fire at some low background baseline firing rate. Call that baseline b₀. Then the neuron’s own output rate, y, is:

> y = b₀ + b₁x₁ + b₂x₂ + b₃x₃

That simple equation is a model of a neuron. It says: take each input’s rate, multiply it by how strongly and in which direction that input connects. Add up the results, and add the baseline firing rate. The total is what this neuron does.

Numbers make it concrete. Suppose a neuron sits at a baseline of 5 spikes per second and has two inputs. The first is excitatory, with a weight of 2. The second is inhibitory, with a weight of −3. If the first input fires at 10 spikes per second while the second is silent, the output is 5 + 2(10) + (−3)(0), which is 25 spikes per second. Now let the second input come on at 5 spikes per second, and leave the first exactly where it was. The output is 5 + 20 − 15, which is 10 spikes per second. The excitatory drive did not change at all, and the cell’s output fell by more than half. That is inhibition doing arithmetic, and it is the mechanism behind every claim in Module 4 about how circuits make decisions.

Push the same example a little further, and the simple linear model shows us its own limitation. Let the inhibitory input rise to 15 spikes per second: 5 + 20 − 45, which is −20. A neuron cannot fire a negative number of times per second. So the sum cannot be the final answer. It has to pass through one more step, a function that holds the output at zero whenever the total falls below zero. A real cell also imposes a ceiling, since no neuron can fire faster than a few hundred times a second. There are a number of simple ways we can modify the linear function to respect these constraints, which we will describe in Module 4.

### §3.2.9 — What the Model Is Worth

A model is a deliberate simplification, and the honest way to present one is to say what it leaves out. This model ignores timing entirely, treating a hundred spikes as a hundred spikes whenever they arrived. It assumes the inputs simply add and subtract, when a real cell does something considerably more complicated with signals arriving at different points on its input surface. It has no refractory period — the enforced pause after each spike that §3.3 explains — and no history, and no noise. Every one of those omissions is a way the model is wrong. But it is wrong in those ways on purpose. To repeat, a model is a deliberate simplification, and the way that it simplifies is a theoretical claim about what properties are important for certain kinds of explanations and which are not.

Whether a particular model is correct about these claims is an open, empirical question. Some researchers argue that what this model of a neuron leaves out is too important. On their account, the branching input surface performs enough computation of its own that a single cortical neuron is better understood as a small network than as a single unit. Reproducing what one such cell does can take an artificial network that is several layers deep.

But to many scientists, what those omissions buy in exchange is an account precise enough to predict what the cell will do for input combinations no one has tried, and simple enough that thousands of these units can be wired together and the behavior of the whole assembly can be worked out. That trade is why the model is worth having.

And it is worth pausing and reflecting on our model of a neuron [](#f-neuron-model). It takes numbers in, multiplies each by a weight, sums them, and passes the total through a function. That is the model of a biological neuron we arrived at by describing a cell. It is also, almost exactly, the unit at the heart of an artificial neural network, where positive and negative weights play the roles that excitation and inhibition play here. The resemblance is not a coincidence and not a discovery. The artificial “neuron” is called that because it was built as a stripped-down copy of real neurons. It is a caricature, deliberately. But it is the most concrete case we have yet met of Module 1’s **multiple realizability**. It is the same receive-integrate-threshold function, running in wet tissue in one case and in silicon in the other. What happens when many such units are wired together, and what happens when the weights are allowed to change with experience, are the subjects of Modules 5 and 7.

![A single unit, biological or artificial. Each input arrives with its own rate, each connection applies its own weight, the weighted inputs and the baseline are summed, and the total passes through a function that holds the output rate at or above zero.](reading_images/fig-neuron-model.svg){#f-neuron-model alt="Three arrows enter from the left, labeled x subscript one, x subscript two and x subscript three. Each passes through a small circle labeled with a weight, b subscript one, b subscript two and b subscript three. The three weighted paths converge on a summation symbol, which receives a fourth input labeled b subscript zero from below. A single arrow leaves the summation symbol and enters a box containing a curve that runs flat along zero on the left and rises steadily to the right. The arrow leaving the box is labeled y."}

### §3.2.10 — From One Neuron to a Behaving Animal

One cell that sums its inputs and answers a yes-or-no question is a long way from an animal doing anything. The gap is smaller than it looks. The cheapest way to see that is to look at the simplest animal anyone has fully mapped.

*Caenorhabditis elegans* is a soil worm about a millimeter long [](#f-c-elegans). Its adult hermaphrodite form has exactly 302 neurons. It was the first animal whose entire wiring diagram was worked out — every cell, and every connection between them. This is a map we now call a **connectome**. A worm with 302 neurons behaves. It steers toward the smell of food and away from substances that would damage it. It reverses when its nose meets an obstacle, and it changes what it does when it has not eaten.

![An adult *C. elegans* hermaphrodite under a light microscope, about a millimeter long. Three hundred and two neurons, a complete wiring diagram, and an animal that steers toward food and reverses at an obstacle, all in a body this size.](reading_images/fig-c-elegans.jpg){#f-c-elegans alt="A gray-scale light micrograph of a nematode worm lying in a shallow S-curve and filling the frame from left to right. The body is smooth-walled and nearly transparent, tapering to a blunt head at the left and to a fine pointed tail at the right. Internal structures show faintly along its length as pale outlines."}

What produces that behavior is nothing but the arrangement this section has been describing, repeated and connected. Sensory neurons at the animal’s front end respond to chemicals in the water around it. Their output lines run to interneurons, which receive input from several sensory cells at once, and do exactly what §3.2.3 described. They sum, compare against a threshold, and produce a verdict. Those interneurons connect to motor neurons, which drive the muscles that bend the body. Sense, integrate, act, in an animal, using three or four cells in a row. §3.1 argued that the animal way of life demanded a fast sense → decide → act loop. *C. elegans* demonstrates that loop, made out of neurons, in an animal too small to see without a microscope.

The worm can do considerably more than that sketch suggests. Most of what it can do depends on how its neurons are organized, rather than on what any one of them computes. It weighs a good smell against a bad one, and crosses a barrier only if the food is worth it. It behaves differently when hungry. Those are questions about circuits and about internal states that we discuss in Module 4.

We now have an account of what a neuron computes, and a model precise enough to calculate with. Both were built with the biology deliberately set aside, and both describe the cell in terms of rates. That leaves the question we postponed at the start of the section. How does a living cell, made of fat and salt water and protein, physically produce any of this? What is an action potential, made of? And what does it cost to run? That is the question asked at Marr’s implementational level.

## §3.3 — Implementational: The Biology of Neurons, and What It Costs

### §3.3.1 — The Implementational Question

In §3.2, we described a neuron with the biology deliberately set aside. But now it is time to bring it back. The implementational question is the third and last of Marr’s levels: what physical stuff actually does this, and by what means? The discipline is neuroscience, and the answer is a cell made of fat, salt water, and protein doing something quite specific with electricity.

There is a second thing to watch for here. In §3.2, we worked at the scale of firing rates, over stretches of time long enough for behavior. This section works at the scale of one event lasting about a thousandth of a second. Those are different questions about the same cell, and they will produce two descriptions that look quite different. That is not a failure of either description. It is what having three levels is for. And by the end of this section, we will have two models of one neuron, and a clear account of why we want both.

Start with the four roles of a neuron we described in §3.2. Each role is filled by a distinct part of the cell, and the parts have shapes as well as names [](#f-neuron-anatomy). The input surface is the **dendrites**, a branching collection of tendrils that reach out from the cell body, often thousands of them [](#f-real-neuron). Each dendrite carries signals from a different source. The integrator is the **soma**, the cell body itself. The output line is the **axon**, a single long fiber that may run a millimeter or, in a large animal, a meter or more. And the junction where one cell’s output becomes the next cell’s input is the **synapse**, the narrow gap between an axon’s ending and the next cell’s dendrites. Those specific biological implementations are not necessary for the description of how a neuron computes that we gave in §3.2. But every one of them matters to how the computation is physically carried out, which is what the rest of this section is about.

![The four roles of §3.2, and the four parts of a real cell that fill them. Signals arrive on the dendrites, are pooled in the soma, and travel out along the axon — drawn here in the segments of myelin that §3.3.5 explains — to cross at a synapse onto the next cell.](reading_images/fig-neuron-anatomy.png){#f-neuron-anatomy alt="A drawing of a single neuron. At the left is a rounded cell body containing a nucleus, from which many thin branches spread out in every direction, each dividing repeatedly into finer twigs; a label reads dendrites, the input. A second label on the cell body reads soma, the integrator. A long fiber leaves the cell body toward the right, drawn as a chain of pale elongated segments, and is labeled axon, the output line. At its far end the fiber divides into several short branches, each ending in a small round swelling against the surface of a second and much larger cell drawn in pink at the right edge; a label there reads synapse, the junction."}

![Neurons of the dentate gyrus, stained by the Golgi method, at forty times magnification. The diagram above is a deliberate simplification, and this is what it simplifies. The branching input surface that §3.2.9’s objection is about is visible here, and absent from the diagram.](reading_images/fig-real-neuron.jpg){#f-real-neuron alt="A black-and-white micrograph of brain tissue. Against a mottled gray background, a scattering of darkly stained cell bodies lies toward the right of the field, each sending one or more thin processes up and to the left. The processes branch repeatedly, taper as they go, and cross over one another so that no single cell can be followed cleanly from one end to the other. Their surfaces are visibly rough rather than smooth. Nothing in the image is labeled."}

### §3.3.2 — The Membrane, the Gradients, and the Pump

A neuron, like any cell, is wrapped in a membrane made of two layers of fatty molecules with their water-repelling ends facing each other. Charged particles cannot cross this oily sheet on their own, which is the fact everything else rests on. So whatever is inside stays inside, and whatever is outside stays outside, unless something lets it through.

What is dissolved on either side of a neuron’s cell membrane is not the same. Sodium ions are concentrated outside the cell, and potassium ions inside it. Both are positively charged. The inside of a neuron is nonetheless negative relative to the outside, partly because the cell holds large negatively charged molecules that cannot cross the membrane at all, and partly because potassium escapes more easily than sodium gets in. An imbalance of charge across a barrier is a voltage, and the voltage across a resting neuron’s membrane is its **resting membrane potential**, roughly seventy thousandths of a volt, with the inside negative. The number matters less than what it means. A neuron at rest is not a neuron that is switched off. It is a neuron held under tension, like a charged battery or a drawn bow, with everything already in place for something to happen fast. Puncture the membrane and the ions would rush to equalize, sodium flooding in and potassium streaming out, until the difference was gone.

Nothing about that arrangement is stable on its own, because the membrane is not perfectly sealed after all. Studded through it are protein pores called **ion channels**. A few kinds of ion channels stand permanently open. Through those, ions trickle steadily downhill: potassium drifting out, sodium drifting in, each moving in the direction that erases the imbalance. Left alone, the gradients would run down to nothing within minutes.

But they do not run down and equalize, because the cell continuously pushes ions back where they came from, using a protein called the **sodium-potassium pump**, or Na⁺/K⁺-ATPase. The pump drives sodium out and potassium in, against their concentration gradients, which is the direction they do not want to go, and it pays for each cycle by spending a molecule of ATP. A resting neuron is therefore not sitting still. It is holding a steady state, with the pump expending energy to keep everything in balance [](#f-membrane-gradients).

![A patch of a resting neuron’s membrane. Sodium is concentrated outside and potassium inside, along with large negatively charged molecules that cannot cross at all, and the inside sits about seventy thousandths of a volt below the outside. Through leak channels the ions trickle downhill for free; the sodium–potassium pump drives them back uphill, spending a molecule of ATP each cycle. Ion counts are suggestive rather than literal.](reading_images/fig-membrane-gradients.svg){#f-membrane-gradients alt="A cross-section of a cell membrane drawn as a band of paired fatty molecules across the middle of the picture. Above it, labeled outside the cell, most of the small circles are marked Na plus. Below it, labeled inside the cell, most are marked K plus, along with several larger circles marked A minus. A pore through the membrane on the left carries one arrow down and one arrow up. A second, heavier structure on the right carries an arrow driving sodium upward and out and an arrow driving potassium downward and in, with a circle marked ATP feeding into it. A label at the right reads minus seventy millivolts, inside negative."}

Register what that means before going on, because we are going to build on it in the next section. A neuron doing absolutely nothing — receiving no input, sending no signal, sitting quietly in the dark — is spending energy continuously. It is spending it in order to remain ready. The readiness is what is being purchased in order to be able to send a signal at the right time.

### §3.3.3 — How a Spike Happens

Most ion channels, unlike the permanently open ones, are gated. This means they let their ion through when they are open and not when they are closed. What opens them divides them into two kinds that matter for us here. A *ligand-gated* channel opens when a particular chemical binds to it. A *voltage-gated* channel opens in response to the voltage across the membrane itself.

The ligand-gated channels are the inputs we described in §3.2, made physical. A neurotransmitter released at a synapse binds to receptors on the receiving cell’s dendrite. This causes channels to open, ions to trickle through, and the membrane voltage to shift slightly. An excitatory input lets in positive charge and nudges the voltage upward, toward zero. An inhibitory input pushes it back down. The summation §3.2.3 described as adding up inputs is, physically, these small voltage shifts arriving at the cell body and combining, resulting in a net change of potential across the membrane.

The voltage-gated channels are what turn that sum into a spike, and they do it through a runaway [](#f-action-potential). If the combined inputs push the membrane voltage up past a critical level, around fifteen thousandths of a volt above rest, voltage-gated sodium channels begin to open. Sodium rushes in, which pushes the voltage further up, which opens more sodium channels, which lets in more sodium. Once that loop starts it cannot be stopped partway, and the voltage shoots from negative to positive in about a millisecond. That is **depolarization**, the rising phase. The same depolarization that opened the sodium channels also closes them, through a second and slower mechanism in the same protein. The channels open, and then a fraction of a millisecond later they shut themselves off. Slower potassium channels then open and let potassium flow out, carrying positive charge with it and driving the voltage back down toward its resting state. That is **repolarization**. For a short interval afterward, the sodium channels have not yet reset, and no amount of input can make the cell fire again. That interval is the **refractory period** [](#f-channel-states).

That mechanism is the answer to a question §3.2 raised but did not answer. Why is a spike all-or-nothing? Because the rising phase is a positive feedback loop, and a positive feedback loop has no intermediate settings. Either the threshold is crossed and the loop runs to completion, producing a full spike, or it is not crossed, and nothing happens. There is no way for the cell to produce half of an action potential. The refractory period settles two more of §3.2’s assertions. First, a spike travels in one direction down the axon because the stretch it just left is briefly unable to fire again due to being in its refractory period. And second, a neuron has a maximum firing rate — a few hundred spikes per second at most — because it must wait out the refractory period between events.

![The membrane voltage of a neuron during a single action potential. The cell sits near its resting potential until input pushes it past threshold; sodium entry then drives a rapid rise, potassium exit brings it back down and briefly past rest, and the cell recovers. The whole event lasts about a millisecond, and its shape is the same every time.](reading_images/fig-action-potential.svg){#f-action-potential alt="A line graph with time in milliseconds along the horizontal axis and membrane voltage in millivolts along the vertical axis. The line runs flat near negative seventy millivolts, rises gradually to a marked threshold near negative fifty-five, then climbs almost vertically to a peak above positive forty before falling just as steeply, dipping below the resting level, and returning slowly to it. The rising segment is labeled depolarization, the falling segment repolarization, and the shallow dip at the end is labeled the refractory period."}

![How open the two kinds of voltage-gated channel are during the action potential above, on the same time axis. Sodium opens fast and then shuts itself off; potassium opens late and closes slowly. The rising phase is a positive feedback loop, which is why the spike has no intermediate settings, and the cell cannot fire again until the sodium curve has come back down.](reading_images/fig-channel-states.svg){#f-channel-states alt="A graph on the same time axis as the action potential trace above it, showing two curves. A solid red curve labeled sodium rises almost vertically to a tall narrow peak and falls back to zero within about two milliseconds; the area beneath it is shaded. A dashed dark blue curve labeled potassium rises later, reaches a much lower and broader peak after the sodium curve has begun to fall, and declines slowly over the rest of the window."}

### §3.3.4 — Hodgkin and Huxley: A Second Model of a Neuron

Everything in §3.3.3 is a story about invisible particles crossing a barrier we cannot watch. Stories like that are easy to tell, and hard to believe. It is worth knowing how this one came to be believed, because the answer is one of the best demonstrations in science of a habit this course keeps returning to.

In the late 1940s and early 1950s, Alan Hodgkin and Andrew Huxley worked on the giant axon of the squid, a nerve fiber up to a millimeter thick. It was large enough to thread a wire down the inside of it, which no ordinary axon permits [](#f-squid-axon). Using that access, they held the membrane voltage at fixed values and measured the currents that flowed at each one. Then they did something more ambitious than measuring. They wrote down a set of equations describing how the membrane’s permeability to sodium and to potassium changes with voltage and over time, and fitted the constants in those equations to what they had measured.

![The squid giant axon, dissected into a dish, with a glass pipette inserted along its length. A nerve fiber this thick is what made Hodgkin and Huxley’s measurements possible, and no ordinary axon permits it.](reading_images/fig-squid-axon.jpg){#f-squid-axon alt="A black-and-white photograph of a shallow round dish of liquid, lit from below against a dark background. A hand at the upper right holds a fine glass pipette whose tip has been inserted into a pale, nearly transparent strand running across the dish from left to right. The strand is thick enough to be seen plainly without magnification."}

Then they used the equations to calculate what an action potential should look like. Out came a curve with the right shape, the right height, the right duration, and a conduction speed matching the real axon. None of these values had been built into their equations. They had built something that behaved like a neuron, and it did so in ways they had not put in by hand.

The part worth dwelling on is what they did not have. Nobody had seen an ion channel. There was no direct evidence that the membrane contained discrete protein pores at all. Individual channels would not be observed for another two decades. Hodgkin and Huxley’s equations described the *behavior* of whatever was letting ions through, inferred entirely from the outside. And when the physical channels were finally found, they were largely as the equations required them to be. This is Module 2’s synthetic method — understanding by building — working at the implementational level. And it is why the account in §3.3.3 is a description of a mechanism rather than a plausible tale. Hodgkin and Huxley shared a Nobel Prize for this work in 1963.

It is also the second model of a neuron this chapter has built. Setting the two beside each other is the clearest view of Marr’s levels the chapter can offer. In §3.2.8, we formalized a neuron as a weighted sum of input rates. Hodgkin and Huxley formalized it as a set of currents crossing a membrane over the course of a millisecond. Neither is a simplified version of the other, and neither is more true. They answer different questions, at different time scales, at different levels. Ask what a cell contributes to a circuit, and the first model is the one that is more helpful. Wire ten thousand Hodgkin-Huxley models together, and the result would teach us very little more than the simpler model, at enormous cost. But ask how a cell physically produces one event, and the simple linear model has nothing whatever to say. Both are wrong in the way that all models are wrong, deliberately and in stated respects [](#t-two-models). And both are indispensable.

: Two models of one cell, built in this chapter, at two of Marr’s levels. The rows are not a scorecard. Neither model is a simplified version of the other and neither is more true; they answer different questions, and the last row is why a chapter that has both keeps both. {#t-two-models}

| | The rate model of §3.2.8 | The Hodgkin-Huxley model of §3.3.4 |
|---|---|---|
| Marr’s level | algorithmic | implementational |
| What it represents | firing rates, and a weight on each connection | currents crossing a membrane, and a voltage |
| The time scale it works at | long enough for behavior to happen | about a thousandth of a second |
| The question it answers | what does this cell contribute to a circuit? | how does a cell physically produce one event? |
| What it is built from | one line of arithmetic | equations fitted to measured currents |
| What it cannot say | how a spike is made | what an assembly of ten thousand cells does |
| Wire ten thousand together | the behavior of the whole can be worked out | enormous cost, and very little more learned |

### §3.3.5 — Down the Axon and Across the Gap

A spike at one end of an axon is useless unless it arrives at the other. It arrives at the far end not really as a single event traveling, but as a chain of events regenerating. Each patch of membrane, as it depolarizes, pushes the patch ahead of it past threshold, which fires in turn. Nothing is transmitted in the way a wire transmits, and nothing weakens along the way. This is the physical basis of §3.2’s claim that what arrives at the end is exactly what we started with at the beginning.

Regenerating a spike at every point along a meter of axon is slow and expensive, and vertebrates largely avoid doing it. Many axons are wrapped in **myelin**, a fatty sheath laid down by supporting cells in segments with small bare gaps between them. Ion channels cluster at the gaps, so the spike is regenerated only there and the stretches in between are crossed passively. The signal effectively jumps from gap to gap, a mode of travel called *saltatory conduction*. This is both far faster and considerably cheaper, since far fewer ions cross the membrane and far fewer have to be pumped back.

At the axon’s end, the signal changes form. The arriving spike opens channels that let calcium into the neuron. Calcium entry causes *vesicles* — small membrane packets holding neurotransmitters — to fuse with the cell’s surface and spill their contents into the synaptic gap. The neurotransmitters cross the gap, bind to the ligand-gated receptors we described above, and the cycle begins again in the next cell [](#f-synapse).

![Neurons in tissue, with one axon ending opened out. In the main panel, arrows follow the direction impulses travel, from a cell body out along its axon to the next cell. The inset enlarges a single ending: packets of neurotransmitter are released into the gap, cross it, and bind receptors on the far side.](reading_images/fig-synapse.jpg){#f-synapse alt="A color illustration of several neurons in tissue, drawn in shades of tan and pink. Labels identify a neuron, its dendrites and its axon, and a curved arrow labeled electrical impulses follows an axon from one cell toward another. A small white square marks one axon ending, and a boxed inset at the lower right shows that ending greatly enlarged: inside it are round packets labeled neurotransmitter molecules, and beneath them small red shapes cross a narrow gap to meet blue crescent shapes on the surface of the next cell, labeled receptor, with the gap itself labeled synapse."}

Which transmitter crosses the gap settles whether the effect is excitatory or inhibitory. In the brain, the dominant excitatory transmitter is **glutamate**, and the dominant inhibitory one is **GABA**. The difference between them is not really a fact about the two molecules, though. It is a fact about the channels their receptors open [](#t-glutamate-gaba). Glutamate binds to receptors that open channels permeable to sodium. So glutamate leads to positive charge flowing into the receiving cell, and its voltage climbs toward threshold. GABA binds to receptors that open channels permeable to chloride, a negatively charged ion. So GABA leads to negative charge flowing in, and the voltage is pushed down, away from threshold. One consequence is that the same neurotransmitter can excite one cell and inhibit another, if the two cells carry different receptors, opening channels for different ions.

: Why the same word, *excitatory*, is a fact about a channel rather than about a molecule. Read each row left to right: the transmitter arrives, its receptor opens a channel for one particular ion, and the charge that ion carries decides which way the voltage moves. One consequence is that the same transmitter can excite one cell and inhibit another, if the two carry different receptors. {#t-glutamate-gaba}

| | Glutamate | GABA |
|---|---|---|
| Its receptors open channels permeable to | sodium | chloride |
| The charge that ion carries | positive | negative |
| Which way that charge moves | into the receiving cell | into the receiving cell |
| What the membrane voltage does | climbs toward threshold | is pushed down, away from threshold |
| The effect, named | excitatory | inhibitory |

After an action potential, neurotransmitters are cleared out of the gap. This is done largely by *reuptake*, in which the sending cell pulls them back in to be repackaged. Every stage of the sequence costs energy. The ions that crossed must be pumped back, neurotransmitters must be manufactured and loaded into vesicles, and the vesicle membrane must be recovered and reused.

### §3.3.6 — What Signaling Costs

As we have noted, neurons’ ability to send discrete and continuous information, reliably and over long distances, comes with a price. The study of how an organism gets, stores, and spends energy is **bio-energetics**, and neural communication is one of its most interesting subjects.

The reason neural signaling is expensive follows directly from how it works. Energy must be spent just to maintain a neuron’s resting state. And a spike happens by letting ions run down gradients that were built at a cost. The signal is the spending of energy. Every ion that crossed the membrane during an action potential has to be hauled back across it afterward, one ATP at a time, by sodium-potassium pumps and other related systems. The cost of computing with neurons is dominated not by the computing, but by the cleanup: restoring the gradients that signaling ran down.

Putting numbers on that is harder than it sounds, since one cannot easily meter a working brain. The standard figures come from a careful accounting by David Attwell and Simon Laughlin, who priced out each step of signaling in ATP and added it up. Their budget for the brain’s gray matter concluded two things worth keeping separate. About three-quarters of the energy goes to signaling rather than to housekeeping such as building proteins and maintaining the cell. And almost all of that signaling cost goes on the sodium-potassium pump. Within the signaling share, at an assumed average firing rate, action potentials account for roughly half, effects at the receiving side of synapses for about a third, and simply holding the resting potential for a further one-eighth. That last figure is the one to notice [](#f-energy-budget): a substantial slice of the brain’s budget is spent by neurons that are doing nothing at all except staying ready.

A single spike, on Peter Lennie’s estimate, costs on the order of two and a half billion molecules of ATP. That is the unit price of one bit of neural activity, and the rest of this section is what follows from it.

![The energy budget for the brain’s gray matter, opened out in two steps. About three-quarters goes to signaling rather than to housekeeping, and almost all of that goes to the sodium–potassium pump restoring what signaling ran down. Within the signaling share, an eighth is spent by cells doing nothing at all except holding their resting potential. These are modeled figures at an assumed mean firing rate, not a measurement.](reading_images/fig-energy-budget.svg){#f-energy-budget alt="Two stacked horizontal bars. The upper bar divides all gray-matter energy into a large segment labeled signaling, about three-quarters of its width, and a smaller one labeled housekeeping. Dashed lines carry the signaling segment down to the lower bar, which divides it into five parts: forty-seven per cent action potentials, thirty-four per cent effects at the receiving side of synapses, thirteen per cent holding the resting potential, and three per cent each for presynaptic calcium and transmitter recycling."}

### §3.3.7 — The Brain as a Metabolic Outlier

An adult human brain is about two percent of body weight, but consumes about twenty percent of the body’s oxygen at rest. Expressed as power rather than as a share, the same measurement comes to roughly the twenty watts we mentioned in Module 0. The two numbers are one fact stated two ways.

Twenty percent is a striking share of a *basal metabolic rate*, and it is not evenly distributed across a life. In the middle of the first decade of childhood, when the brain is still being built, its share of the body’s oxygen use reaches as much as half. A growing child is, metabolically speaking, mostly a brain with a body attached.

The share is also unusual across species. Humans devote something like twenty to twenty-five percent of their daily energy budget to the brain. Other primates devote eight to ten percent. Non-primate mammals devote three to five percent. So the human brain is genuinely an outlier, and it is worth being clear about what kind of outlier it is. The cost of running a single human neuron is not remarkable. It is about the same as a primate neuron. What is unusual is how many of them there are. The cost is large because the brain is large, on an ordinary primate body plan, rather than because human neurons are special [](#t-brain-energy-share).

That distinction is worth remembering, because this is the section of the chapter where Module 2’s warning is easiest to forget. A number like twenty percent invites reading as an achievement, evidence that we are the animal that invested most heavily in thinking. It is better read as a constraint. A brain that expensive has to be fed every day, which limits what else an animal can be and what it must eat. Every lineage that did not build a big brain was not failing to; it was solving its own problems at a price it could afford.

: The brain’s energy cost, measured against four different things. The last row is what decides how to read the third: the human brain is expensive because it holds a great many neurons, not because a human neuron is an expensive one. {#t-brain-energy-share}

| Measured against | The figure |
|---|---|
| the body, at rest | about 2% of body weight and about 20% of the oxygen used — one measurement stated two ways, and about twenty watts |
| a lifetime | as much as half of the body’s oxygen use in the middle of the first decade of childhood, while the brain is still being built |
| other mammals | non-primate mammals spend 3–5% of the daily energy budget on the brain, other primates 8–10%, humans 20–25% |
| one neuron | about the same in a human as in any other primate |

### §3.3.8 — Energy as a Design Constraint

If the energy cost were merely large, it would be a fact about brains. What makes it interesting is that it is also a design pressure, visible in how brains are built and used.

Consider what the budget permits. The same accounting that showed us the cost of a single spike can be run in reverse. Given what the brain costs to run, and what a spike costs, the sustainable average works out to a fraction of a spike per neuron per second. This means that only a small proportion of cortical neurons can be strongly active at any one moment — on the order of one in a few hundred. Activity that thin is called **sparse coding**, and the point is that it is not an accident or an inefficiency.

Something close to that fact circulates as a neuro-myth in a badly mangled form. The claim that we use only ten percent of our brains is false in every sense that matters. What the claim asserts is that most of the brain sits idle, a reserve of unused capacity waiting to be unlocked. Nothing supports that. Every region does something, damage almost anywhere produces some deficit, and imaging finds activity throughout. What is true is narrower and considerably stranger. At any given instant only a small share of neurons are firing hard, and which small share it is changes from moment to moment. Over any stretch of time the whole brain is in use [](#f-sparse-coding). It is simply never all in use at once.

![A field of cortical neurons at two moments a few milliseconds apart. At each instant only a handful are strongly active, which is what the energy budget affords. It is a different handful each time, so over any stretch of time the whole population is used — and never all at once.](reading_images/fig-sparse-coding.svg){#f-sparse-coding alt="Two panels, each a regular grid of two hundred and eighty-six small pale dots. In the left panel, labeled one moment, two dots are drawn larger and much darker than the rest. In the right panel, labeled a few milliseconds later, three different dots are drawn larger and darker, and the two that were dark in the left panel are pale again."}

A brain in which most neurons fired most of the time is not a better brain that evolution failed to build. As we will see in Module 4, it’s a brain that would not code for information as effectively, since there is information in which neurons are firing and which are not. But a brain with a much higher proportion of its neurons firing is also a brain that could not be fed. Myelin is the same logic in a different place. Insulating an axon cuts both the delay and the ion traffic, and so does the balance a brain strikes between the cells that compute and the fibers that connect them. Wiring costs energy too, and a brain has to buy both out of one budget. Energy, in short, is a *metabolic constraint* — one of the forces that determines what a nervous system can look like.

### §3.3.9 — The Same Function in Silicon

Return now to §3.2.8’s simple linear model of a neuron, and connect it to our current discussion. The equation written there described a biological neuron and an artificial one about equally well, which was the point of writing it. Set the two implementations (organic matter and silicon electronics) side by side and the resemblance vanishes completely. One is protein pores in an oily membrane, moving salt against concentration gradients in warm water, paying for every ion with a molecule of ATP. The other is voltage on a silicon transistor: charge pushed along a conductor, and a switch thrown by an electric field, with no chemistry involved anywhere. Module 1 called this multiple realizability, and argued for it with thought experiments. Here it is, in a single cell, with both realizations built and running. And it locates the divergence precisely. Natural and artificial systems behave extremely similarly at the algorithmic level, where the same short equation served both. They could hardly be more different at the implementational level. That is not an incidental detail about hardware. It is where the comparison between minds and machines actually strains, and this course will return to it later.

The difference shows up first as speed. An action potential takes about a millisecond. A transistor switches in a small fraction of a billionth of a second. That gap is not a matter of engineering care, and no amount of it would close the gap. The two are not doing the same kind of physical thing. A neuron signals by bodily moving ions from one side of a membrane to the other, which is chemistry and takes time. A transistor moves charge through a conductor, which does not. Module 1 noted that brains are built from slow components and drew the consequence. A system that has to answer in a few hundred milliseconds, using parts that take a millisecond each, cannot run a long sequence of steps one after another. It has to do very many things at once instead. What we add here in §3.3 is the reason the parts are slow.

So the implementational level is not simply where a function gets realized, with everything important settled above it. It sets terms the levels above have to respect. Neurons are slow and expensive, so brains are massively parallel and mostly quiet. Sparse coding is not a design preference, but a consequence of a design constraint. Transistors are fast and individually cheap, so machines can run long sequences of steps very quickly. But packing enough of them together produces heat that has to be carried away, and the power has to come from somewhere outside the machine. Two implementations of a similar function, two different sets of constraints, and two quite different architectures built on top of them [](#t-neuron-transistor). This is Module 1’s claim that the levels are separable but not independent.

: One function, two substrates. These are two sets of constraints rather than a scorecard — §3.3.9’s claim is that neither implementation is better, and that each forces a different architecture in the levels above it. Switching times are given as this chapter gives them; a figure for the energy of a single transistor switch is deliberately left out, because it varies by orders of magnitude with the manufacturing process and the operating point. {#t-neuron-transistor}

| | A neuron | A transistor |
|---|---|---|
| What physically moves | ions, bodily, from one side of a membrane to the other | charge, along a conductor |
| Is chemistry involved | yes, and chemistry takes time | no |
| Time for one event | about a millisecond | a small fraction of a billionth of a second |
| What one event costs | ATP, spent hauling back every ion that crossed | electrical energy, most of it leaving as heat |
| Where the power comes from | food, and it has to be found every day | a supply outside the machine |
| What has to be carried away | waste heat, at a rate the body can manage | waste heat, and packing enough parts together makes it the limit |
| What those constraints force above | very many things at once, and most cells quiet | long sequences of steps, run very fast |

The energy figures make the divergence concrete. Eighty-six billion neurons run an entire human mind on about twenty watts, which is less than a dim light bulb, while artificial systems trained to do far narrower things consume orders of magnitude more. The comparison should not be pushed too hard, since the two are not doing the same job, and the accounting is not really commensurable. But it is enough to reframe the brain’s metabolic budget one last time. Expensive and cheap are both right here, and they do not conflict, because they are measured against different things. The human brain is expensive when measured against the animal’s whole budget: one organ taking a fifth of everything the body spends, which really does limit what else that animal can be. But the brain is cheap when measured against the work done: twenty watts for an entire mind, set beside any other arrangement anyone has found for doing the same job. The brain is a large share of a small budget, and a small price for what it delivers.

### §3.3.10 — Closing the Energy Arc

We can now close by returning to the two questions we asked at the start. Where did the complexity of a cell come from, and why that complexity was worth the effort. In §3.1, we answered the first. Complexity was not assembled in one step. It accumulated. Molecules copied themselves imperfectly, membranes enclosed them, DNA and RNA and proteins each took on different work, and finally resulted in cells that could maintain and reproduce themselves. The second question took the rest of the chapter to answer, and the answer has two halves. Oxygen answered one of them. It provided a new energy source that made expensive cells affordable for the first time. This latter section answers the other part of the question, and the answer turns out to be an accounting.

Neurons cost more to run than anything else an animal builds. And animals that happened to acquire them have gone on building them ever since, because what the outlay buys is the ability to sense, decide, and act before something else does. The bill is enormous, and it has been worth paying every time it has come due. So it is one continuous story: neurons exist because life became rich enough to run them, they persist because what they do is worth what they cost, and they are built the way they are because even now, life cannot quite afford to run them carelessly.

We have now built a neuron three times over: once as a solution to a problem, once as a function, and once as a physical machine with a running cost.

## Close — From a Neuron to a Nervous System

We have taken one kind of cell, the neuron, and examined it three times. We asked why it evolved, and the answer was a problem: animals make a living by moving through a world that moves back. The animal that senses, decides, and acts a fraction of a second sooner is the one that eats rather than being eaten. We asked what it computes, and the answer was three verbs and a threshold — receive, integrate, transmit, then fire or stay silent. We asked how biology manages it, and the answer was a set of gradients held under tension by a pump that never stops, and a self-propagating chain reaction that runs the length of an axon in a millisecond. Three questions, one cell, three answers that do not resemble one another in the slightest, but which are not in competition because they are answers to three different questions. That is a full turn of the wheel we promised in Module 1, and it will now turn once per module for the rest of this course.

Energy constraints ran the whole length of our narrative. Neurons became affordable only after oxygen made life rich enough to pay for them, and the brain still spends a fifth of the body’s resting budget staying ready and cleaning up after itself. The artificial parallel ran the whole length of it too. Artificial neural networks are named after this cell, and modeled on it. But we noted one place where the comparison genuinely strains, which is not the algorithm but the substrate. As we move forward and continue to compare biological and artificial neural networks, we will find more points of similarity and divergence.

A neuron, on its own, does very little. It sums what arrives, and answers a single yes-or-no question. But the limit is not quite what it first appears to be, and it is worth stating carefully. Give a neuron an excitatory input from one smell, and an inhibitory input from another. Its firing rate will climb with the first, and fall with the second. Wire that output to something that steers, and the animal moves toward the one and away from the other. The arithmetic is well within a single cell.

What is not in the cell is any of the meaning. A rate is only a rate. It becomes approach because of what the cell happens to be wired to, and the very same cell wired to the opposite muscles would produce avoidance. That is the lesson of the vehicles in Module 1’s lab, where the behavior changed completely depending on how the wires crossed, while the parts stayed the same. So value, goals, and states that outlast their causes are not properties a neuron has. They are properties an arrangement has. None of them comes from building a better neuron. They come from wiring ordinary ones together.

These limitations of single neurons are where Module 4 begins. Once neurons existed, there was strong evolutionary pressure to begin to wire them together into the first nervous systems. This led to a very effective system for representing value — how an arrangement of cells comes to treat some things as good and others as bad, and to act differently depending on the state it is in. Further out, Module 5 will ask how a synapse changes with experience, Module 6 scales this plan up into a vertebrate brain, and Module 7 asks what a nervous system built this way is able to perceive.

## Further Reading

Five places to go next, chosen because each one takes up a thread this chapter could only pull on briefly. Two of them disagree with things said here, which is the point.

**Nick Lane, *The Vital Question: Energy, Evolution, and the Origins of Complex Life*, 2015.** The long version of §3.1’s argument, by the biochemist who has done most to make energy the center of the origin-of-life story.

**Frances Ashcroft, *The Spark of Life: Electricity in the Human Body*, 2012.** An ion-channel physiologist on what §3.3 compressed into a few pages: how a membrane holds a voltage, what happens when channels fail, and why so many poisons and drugs work by jamming them. Written for readers with no biology background.

**Suzana Herculano-Houzel, *The Human Advantage: A New Understanding of How Our Brain Became Remarkable*, 2016.** The source of the counting work behind §3.3.7, and an argument that the human brain is not metabolically special at all but an ordinary primate brain scaled up, with the eighty-six billion figure as its centerpiece. It is also a good account of how a measurement nobody had bothered to make properly changed a settled story.

**Peter Sterling and Simon Laughlin, *Principles of Neural Design*, 2015.** Takes §3.3.8’s claim much further than this chapter does, arguing that most of what looks like the architecture of a nervous system follows from the cost of running it. Laughlin is a co-author of the energy budget the chapter quotes.

**Panayiota Poirazi and Athanasia Papoutsi, “Illuminating Dendritic Function with Computational Models,” 2020.** The objection §3.2.9 raises, made by two of the people who raise it: a review of the evidence that a neuron’s branching input surface computes enough on its own that treating the cell as a single summing unit throws away much of what it does. The most direct argument against the model this chapter builds.

## Glossary

**action potential** — The brief, stereotyped electrical event a neuron produces when its inputs push it past threshold, and which travels the length of the cell without weakening. Commonly called a spike.

**all-or-nothing** — Produced at full size or not at all. A neuron either fires a complete action potential or fires nothing; there is no such thing as a small or partial one.

**ATP** — A small molecule that stores energy in a chemical bond and releases it where the cell needs it. Every cell runs its economy on making ATP and spending it.

**axon** — The output line of a neuron: a single long fiber carrying the cell’s verdict away from the cell body, sometimes for a meter or more.

**bio-energetics** — The study of how an organism gets, stores, and spends energy.

**connectome** — A complete wiring diagram of a nervous system: every cell, and every connection between them.

**coordination problem** — The problem created by specialization in a multicellular body: information has to reach the part of the body that needs it from the part that has it, in time for it to be useful.

**dendrites** — The input surface of a neuron: a branching collection of processes reaching out from the cell body, each carrying signals from a different source.

**depolarization** — The rising phase of an action potential, in which sodium rushes into the cell and the membrane voltage climbs from negative to positive.

**excitatory** — Pushing a receiving neuron toward its threshold, making a spike more likely.

**firing rate** — The number of spikes a neuron produces in a stretch of time. Because every spike is identical, the rate rather than the size of any one spike is what varies with the strength of a stimulus.

**GABA** — The dominant inhibitory neurotransmitter in the brain. It binds to receptors that open channels permeable to chloride, letting negative charge into the receiving cell.

**glutamate** — The dominant excitatory neurotransmitter in the brain. It binds to receptors that open channels permeable to sodium, letting positive charge into the receiving cell.

**inhibitory** — Pushing a receiving neuron away from its threshold, making a spike less likely.

**integration** — Combining many arriving signals into one total, which the neuron then compares against its threshold. The middle of the neuron’s three jobs.

**ion channels** — Protein pores through the cell membrane that let particular ions across. A few kinds stand permanently open; most are gated, opening in response to a chemical or to the membrane voltage.

**modulatory signaling** — Signals that change how strongly a neuron responds to everything else, turning its sensitivity up or down rather than pushing it toward or away from threshold.

**multiple realizability** — The idea that one and the same mental state can be realized in different physical systems and materials, just as one temperature can be realized by many different arrangements of molecules. It is the concept that ties the mind–brain question to the machine question.

**myelin** — A fatty sheath wrapped around an axon in segments with small bare gaps between them, which makes conduction both faster and cheaper.

**neuron** — The cell specialized to convert an event, whether in the world or elsewhere in the body, into a signal that travels fast, travels far without weakening, and arrives at a specific destination rather than everywhere.

**neurotransmitter** — A chemical released by a sending cell at a synapse, which crosses the gap and binds to the receiving cell. Which transmitter arrives settles whether the effect is excitatory or inhibitory.

**refractory period** — The brief interval after an action potential during which the sodium channels have not yet reset and no amount of input can make the cell fire again.

**repolarization** — The falling phase of an action potential, in which potassium flows out of the cell and the membrane voltage returns toward its resting value.

**resting membrane potential** — The voltage across the membrane of a neuron that is not signaling, with the inside negative relative to the outside. A neuron at rest is not switched off but held under tension.

**sense → decide → act loop** — Taking in information about the world, doing something with it, and producing an action, fast enough for the action to still be the right one. The problem the animal way of life makes urgent, and the one neurons answer.

**sodium-potassium pump** — Formally the Na⁺/K⁺-ATPase: a protein that continuously drives sodium out of the cell and potassium in, against their gradients, spending a molecule of ATP for each cycle.

**soma** — The cell body of a neuron, where arriving signals are pooled and a verdict is reached.

**sparse coding** — Activity in which only a small proportion of neurons are strongly active at any one moment. It is a consequence of the energy budget rather than an inefficiency.

**synapse** — The junction where the output of one cell becomes the input of the next: the narrow gap between an axon’s ending and the next cell’s dendrites.

**threshold** — The level the summed input to a neuron must reach for the cell to fire. Below it the neuron does nothing at all; at or above it, it produces a full action potential.

**weight** — The strength of a connection together with its sign: positive for an excitatory input, negative for an inhibitory one. In the model of a neuron, each input’s rate is multiplied by its weight before the total is summed.

## Image Credits

Most of this chapter’s figures were drawn for the course and carry no separate credit. Five come from elsewhere, and are reproduced here under the terms named.

**The neuron and its four parts** — Jon Willits. Base illustration generated with ChatGPT; labels added by the author.

**Golgi-stained neurons of the dentate gyrus** — MethoxyRoxy, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Gyrus_Dentatus_40x.jpg), under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/).

**The squid giant axon** — NIH History Office, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Giant_Axon_of_Squid_(14356033761).jpg). Public domain, as a work of the United States federal government.

**Neurons and a synapse** — Christy Krames, MA, CMI, for the National Institute on Aging, National Institutes of Health, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Chemical_synapse_schema_cropped.jpg). Public domain.

**An adult *C. elegans* hermaphrodite** — Zeynep F. Altun, editor of WormAtlas, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Adult_Caenorhabditis_elegans.jpg), under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/).
