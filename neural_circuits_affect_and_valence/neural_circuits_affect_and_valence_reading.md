# 4. Neural Circuits, Affect, and Valence

This module is about what happens when neurons are wired together. One neuron settles one small question. An arrangement of them steers an animal through a world, decides what in that world is worth approaching, and holds a state that outlasts the moment that caused it. While reading, look for the beginnings of answers to these questions:

- Neurons existed. What made it worth wiring them to one another, and what could an animal do once they were?
- Nothing in the world arrives labeled good or bad. So where does a verdict like that come from?
- Several signals arrive at once, and they disagree. How does an arrangement of cells turn them into one action?
- An animal behaves differently when it is hungry, with the same body and the same wiring. What is different?
- Mood is a word for a state that outlasts its cause. Is that a human thing, or does a millimeter-long worm have a version of it?

By the end, we should have a working answer to each one. We will also turn Marr’s wheel a second time, on an arrangement of cells rather than on a single cell.

---

In Module 3, our story stopped at a cell type. An energy revolution made elaborate cells affordable, bodies became multicellular, specialization created the problem of getting information from one part of a body to another quickly, and the neuron is the animal lineage’s answer to that problem. Then the story stopped. No animal was named after that, and no body was described. We also met a worm doing things that one cell cannot account for, without ever being told how animals got from the first neuron to that worm.

One claim from the end of Module 3 is this chapter’s premise, and it is worth restating exactly rather than loosely. A single neuron can weigh competing inputs. Give it an excitatory input from one smell and an inhibitory input from another, and its rate climbs with the first and falls with the second. That arithmetic fits inside one cell. What does not fit inside the cell is any of the meaning. A rate is only a rate. It becomes approach because of what the cell is wired to, and the identical cell wired to the opposite muscles would produce avoidance. So value, goals, and states that outlast their causes are not properties a neuron has. They are properties an arrangement has. This chapter is where that claim becomes mechanical.

The question, then, is what changes when many neurons are wired together. How does an arrangement of cells take a noisy world and produce one sensible action? And where, in the wiring, do value and even mood come from?

One idea runs the length of the answer, and it is worth watching for. A nervous system tags the world as good or bad, and then acts on the tag. Approach and avoidance, weighing a trade-off, hunger changing a verdict, a mood that outlasts the thing that caused it: all of it grows out of good and bad. Nothing in the world arrives with either label already on it.

This chapter has three sections, one for each level [](#t-levels-circuit). In §4.1, we ask why nervous systems came to be wired into circuits at all, and what steering demands of one. In §4.2, we build the arrangements of neurons that meet those demands. In §4.3, we find those arrangements in the tissue and chemistry of real animals.

One thing is left out on purpose. Every circuit in this chapter has weights that hold still, and how a weight comes to change within an animal’s lifetime is Module 5’s subject. Real animals learn, including the small ones in this chapter. But a circuit is far easier to follow while its numbers are not moving, so we hold them still for one chapter.

The comparison with artificial systems continues as well. In Module 3, an artificial neuron was a stripped-down copy of a real one. Here the comparison grows up. Machines navigate the way the first steering animals did, and artificial circuits compute the same logic that real ones do. Late in the chapter we find one thing biology does that has no counterpart in an artificial network at all.

The place to begin is where the story stopped. Neurons exist, and there is now pressure to wire them to one another. From there we climb, from a nervous system that can coordinate a whole body to one that can point that body somewhere in particular. The second step, aiming, is what demands everything else in this chapter.

<!-- pin: t-levels-circuit -->

: Marr’s three levels, the question each asks, the discipline that asks it, and this module’s example. {#t-levels-circuit}

| Level | The question it asks | Discipline | This module’s example: the steering circuit |
|---|---|---|---|
| Computational | What problem is being solved, and why does solving it matter? | Evolution and ecology | Steering: moving toward some things and away from others, which demands evaluating, combining, committing, and modulating |
| Algorithmic | What is represented, and by what procedure? | Cognitive psychology and AI | Weights, thresholds, and a handful of recurring wiring patterns; valence and arousal as two numbers |
| Implementational | By what physical means, and at what cost? | Neuroscience | Nerve nets condensing into ganglia, a worm whose wiring diagram is complete, and neuromodulators released into the tissue |

## §4.1 — Computational: From Coordination to Steering

### §4.1.1 — The Computational Question

In Module 3, we followed a single line of descent, from lifeless chemistry to the evolution of a single kind of cell. Then, energy became abundant enough to pay for elaborate cells. Some of those cells stayed together in multicellular organisms. And once they were together, they specialized.

Specialization created a coordination problem. The cells that sense are not the cells that move. This means information has to travel. In the animal lineage, the answer to that problem was the neuron, a cell that converts an event into a signal that is fast, aimed, and undiminished at the far end.

That is where we stopped our story. It stopped at a cell type rather than at an animal. We didn’t discuss the phylogenetic tree of animals that developed after animals evolved. In this chapter, we resume that story. Neurons existed. What was there to gain by wiring them to one another? The computational question asks what problem is being solved, and why solving it was worth what it cost.

One warning we gave in Module 2 applies here, with more force than it did in Module 3. Walking forward through the animal tree reads very easily as walking *up* it. But a jellyfish is not a rough draft of a worm, a worm is not a rough draft of a fish, and a fish is not a rough draft of us. Each is a lineage that has been solving its own problems for as long as any of the others.

### §4.1.2 — Bodies Before Neurons

It is tempting to picture the first nervous system arriving in a body that was waiting for one. That is not what happened, and the animals that show us why are still around.

Sponges are animals. They are multicellular, they develop from an embryo, and as adults they are anchored to a surface for life, drawing water in through their pores, and filtering food out of it. But they do not have a single neuron. No synapses, no nerves, no muscle of the ordinary kind. They have nothing that would count as a nervous system by any definition.

A sponge nonetheless behaves. Irritate one, and it will slowly close its pores and contract its whole body. This squeezes water and debris out through its opening, in a movement researchers have taken to calling a sneeze. The contraction is coordinated across the animal. It is also extraordinarily slow. The whole event takes minutes rather than milliseconds, because it is propagated by chemical and mechanical signals passed from each cell to its neighbors.

That is Module 3’s argument demonstrated in a live animal. Slow cell-to-cell chemical signaling is a real way to coordinate a body. And for an animal that is fixed to a rock, and that eats by filtering, minutes is fast enough. Sponges have been making a living this way for more than half a billion years. The oldest fossils widely accepted as sponges are around 580 million years old. Chemical traces in older rock may push the group back to something like 635 million years, though whether sponges left those traces is disputed.

But critically, sponges carry much of the molecular equipment a neuron is built from. They have genes for the proteins that make synapses, receptors, and the ion channels that do the physical work of an action potential. A great many of those parts are present in an animal with no neurons to put them in. *Placozoans*, another group with no neurons at all, coordinate their feeding using cells that release peptides onto their neighbors, and those cells look increasingly like something a neuron could be made out of.

So the question is not where the pieces came from. In Module 3, we established that a single cell can sense its world and act on what it senses. And we established that cells have been signaling chemically to one another for billions of years. The pieces were already lying around. What had not happened yet was the arrangement. There were not yet cells that were specialized for signaling and for nothing else, connected to particular partners rather than to whichever cell they happen to touch, and carrying signals one way. In Module 3, we called that difference a circuit rather than a puddle. The step to a nervous system is the arrangement, not the invention of a new kind of chemistry.

### §4.1.3 — A Mouth to Operate

What a sponge also lacks is a mouth. Water enters through pores spread over the whole body, and food is captured by individual cells, one particle at a time. Nothing has to be caught, and nothing has to be swallowed.

But once multicellular animals existed, some lineages evolved a mouth. In principle, a mouth is quite simple. It is just a single opening leading into a cavity where food is broken down. Cells near the mouth specialize for opening and closing. Cells deeper along the cavity specialize for digestion. Eventually that division of labor can lead to very specialized tissues and organs.

In some of the earliest animals with mouths, such as the first corals and sea anemones, this led to an opening around which sat a ring of tentacles that carried stinging cells. That arrangement changes what a body has to do. Prey has to be struck, held, carried to the opening, and admitted, and the opening has to close behind it. Filtering asks for no coordination beyond keeping the water moving. Catching does.

In Module 3, we argued that an animal needs to move information across its body faster than diffusing chemicals can carry it. The earliest arrangement that managed this was not a brain and did not look much like one. It was a **nerve net**: neurons distributed through the body wall, each connected to its neighbors, spread through the animal rather than gathered anywhere in particular.

Today, *cnidarians* such as jellyfish, sea anemones, corals, and the freshwater hydra still run on nerve nets. Every one of them is an interesting example of a nervous system in its own right. Notice that not all of these animals are even capable of moving from place to place. An anemone is fixed to rock. Corals and hydra are likewise fixed to one location for most or all of their lives.

The oldest fossils widely accepted as cnidarians are also around 580 million years old, though that number is less settled than it sounds. Several of the Ediacaran identifications are argued about, and the most securely identified early cnidarian is some twenty million years younger. Either way, the date lands close to the age of the oldest accepted sponges, close enough that the fossil record cannot settle which of the two came first [](#f-animal-timeline). Free-swimming jellyfish arrived later, in one branch of the group, rather than being the shape the first ones had. The earliest nerve nets we can reconstruct were therefore running in animals that stayed put.

![The stretch of time this chapter’s story runs through, drawn twice. The upper strip is all of Earth’s history; the shaded window at its right-hand end is expanded below. Sponges, cnidarians and bilaterians each begin at their oldest widely accepted fossils and continue as lines to the present, because all three groups are still here. Two of the marks are ranges rather than dates: the origin of animals, because it comes from molecular clocks rather than from fossils, and the first cnidarians, because the identifications are argued about.](reading_images/fig-animal-timeline.svg){#f-animal-timeline alt="Two horizontal time axes, one above the other. The upper axis runs from 4.54 billion years ago on the left to the present on the right, with a pale shaded block covering only its last short stretch and two faint dashed lines running from the ends of that block down to the ends of the lower axis. The lower axis runs from 900 million years ago to the present. Above it, a hatched bar spans 833 to 650 million years for the origin of animals. Below that, a small hollow circle at 635 million years is labeled as disputed chemical traces. Three horizontal lines follow, each ending in an arrowhead at the present. Sponges begin with a filled dot at 580 million years. Cnidarians begin with a short capped bar spanning 580 to 560 million years, joined to the sponge dot by a short dashed vertical line. Bilaterians begin with a filled dot at 555 million years. A legend distinguishes filled marks for first accepted fossils from a hatched bar for a molecular-clock estimate and a dashed mark for a disputed one."}

This suggests that the first nervous systems were probably not for getting anywhere. Animals anchored to a rock still have a great deal to coordinate. They have tentacles that have to fire together, and a body wall that has to contract as one when something threatening or enticing arrives. They have a mouth that has to open at the right moment, and close afterward. All of that is whole-body coordination in the service of eating, and none of it involves travel.

How confident should we be about this being how nervous systems first evolved? Reasonably, and not more. Researchers disagree about what the first neurons were selected for. On one account nervous systems arose to coordinate a contractile body surface, which is movement of a body rather than movement through a world. On another they arose to control the beating cilia of swimming larvae, which is closer to locomotion after all. There is also a live question about whether nerve nets evolved once or twice, since the comb jellies have one built differently enough that it may be an independent invention. What is not in dispute is the shape of the sequence. Bodies coordinated slowly without neurons, then bodies coordinated quickly with them. Mouths came along sometime during that transition.

### §4.1.4 — Then the Medusa

Free-swimming jellyfish put the nerve net to a more demanding use. Consider what a moon jelly does when it swims [](#f-moon-jelly). Its bell contracts, all of it at once, and the animal is pushed through the water. That single act is a real solution to Module 3’s coordination problem. The muscles around the whole rim of its bell have to shorten at the exact same time, because a contraction that traveled around the bell in sequence would waste most of its force. A wave of activity crossing the net reaches every part of the ring within a few thousandths of a second, and the bell squeezes as one thing.

Notice how little machinery the arrangement requires. There is no brain. There is no one place that a decision is made, or from which orders are sent. Cnidarian nerve nets are not perfectly uniform. What matters here is that a net can coordinate a whole body with nothing in it that resembles a center. The nervous system is the arrangement itself, spread through the tissue it moves. Having a nervous system is not the same as having a brain, and neither is the same as making a decision. A nerve net gets a body to act as one body, quickly. That is the first thing a nervous system was ever for.

![A moon jelly. The bell contracts as one piece, driven by a nerve net spread through the body wall with nothing at its center that could be called a brain.](reading_images/fig-moon-jelly.jpg){#f-moon-jelly alt="Two translucent bell-shaped jellyfish photographed against black water, one nearer and larger than the other. In each, four pale horseshoe-shaped structures show through the top of the bell, arranged symmetrically around its center. Short fine tentacles fringe the whole rim of each bell, and four longer frilled arms trail beneath it. Nothing in either animal looks like a head or a center."}

### §4.1.5 — Coordination Without Aim

Basic nerve nets let animals coordinate their bodies quickly, but they also have limitations. A moon jelly’s body has **radial symmetry**: it is built around a central axis and is much the same all the way around [](#f-body-plans). Turn the animal a few degrees and nothing about it has changed. That symmetry has a consequence that is easy to miss. An animal built that way has no front, or back, or left or right. No part of it always arrives anywhere first. This means there is no privileged place for sensors to gather, because there is no best place to put them.

Consider, then, what the jellyfish can and cannot do. It can contract its bell, and by contracting, it can rise. It can relax and sink. It can sense light, gravity, and the chemistry of the water around it. And it can pulse more often or less often in response. What it cannot do is answer the question, *which way*. It goes somewhere. It does not go somewhere in particular.

Jellyfish bodies have coordination in time, then, without direction in space. And that is not a failure and not a small way to live. Cnidarians have been doing exactly this for something on the order of six hundred million years, in every ocean and at every depth. Whole-body coordination without steering is a successful strategy.

The limitation of being unable to steer is nonetheless real. The question, then, is how does an animal move in a particular direction, on purpose?

### §4.1.6 — The Bilaterian Body Plan

In one group of animals, the radial plan gave way to a new plan: **bilateral symmetry**. This means having a left and a right side that mirror one another. And, far more consequentially, a front and a back [](#f-body-plans). Nearly every animal most people could name is built that way: worms, insects, snails, fish, birds, and human beings.

The front is the part that matters. An animal with a front has an end that arrives first. And the end that arrives first is the useful place to put sensors. It is also the useful place to put the neurons those sensors report to, since a verdict reached near the sensors is a verdict reached sooner. In §4.3, we will discuss the tissue that gathers there and what it is made of. But here, our focus is on what this arrangement makes possible.

What it makes possible is **steering**: moving forward, turning, and letting what the front end detects decide which way the turn goes. Steering is this module’s evolutionary addition, in the sense we gave that phrase in Module 2. It is a capacity that solved a problem, and that everything downstream is built on top of. An animal that steers does not merely move. It moves toward some things and away from others.

The navigating machines human beings build follow the same plan, and for the same reason. Cars, boats, aircraft, and submarines are bilaterally symmetric with a designated front, because forward-plus-turn is a simple and general arrangement for getting somewhere.

One animal makes the cost of steering unusually visible, by giving it up. A sea squirt begins life as a swimming larva with a nerve cord and a small brain at the front, and it steers, moving through the water in search of somewhere to settle. Once it finds a surface, it attaches head-first. It then rebuilds itself into a filter feeder that, like a coral, will never move again. Its tail, *and its brain*, are broken down into molecules useful for other purposes. What remains is a much reduced ganglion, enough to run the siphons and the gut. Sea squirts are chordates, not early animals. An animal that stops steering does not need to go on paying for the machinery that steers.

![Two body plans, drawn from above. The radial body is built around a central axis and is much the same in every direction, so no part of it arrives anywhere first and sensors have no privileged place to gather. The bilateral body has a left and a right that mirror each other and, consequentially, a front and a back, with the sensors and the neurons they report to gathered at the end that arrives first.](reading_images/fig-body-plans.svg){#f-body-plans alt="Two diagrams side by side, each an animal seen from above. On the left, a circular body with a fine mesh of lines spread evenly across the whole disc and short sensory marks distributed uniformly around its entire rim; dashed lines drawn through the center in several orientations indicate that the animal looks the same whichever way it is turned. On the right, an elongated body with a single mirror line running from one end to the other; small sensory marks and a dense knot of the mesh are gathered at one end, and an arrow ahead of that end shows the direction of travel."}

### §4.1.7 — What Steering Demands

Steering is not free. The rest of this chapter is a description of what it costs in information processing. A jellyfish drifting on a current doesn’t need to pay these costs. An animal that aims itself does.

Steering demands four abilities [](#t-steering-demands). An animal that steers has to *evaluate* what it senses. It has to *combine* signals that disagree with one another. It has to *sharpen and commit*, turning a near-tie into a clear difference and then collapsing the result into a single action. And it has to let its own condition *modulate* every one of those judgments. We state the four demands here, showing what has to be computed. In §4.2, we build the arrangements of neurons that compute them. In §4.3, we find those arrangements in the tissue and chemistry of real animals.

: The four demands steering makes of a nervous system. In §4.1, we state the demand; in §4.2, we supply an arrangement of neurons that meets it; in §4.3, we find that arrangement running in an animal. {#t-steering-demands}

| The demand | What steering requires | Where we answer it |
|---|---|---|
| Evaluate | Sort what is sensed into good, bad, and neither, since no direction can be preferred without a reason to prefer it | valence (§4.1.8) · the labeled line (§4.2) · the worm’s sensory neurons (§4.3) |
| Combine | Weigh several cues at once, both by how strong each one is and by which combination of them is present | trade-offs and logic (§4.1.9) · weights, thresholds and logic units (§4.2) · the worm’s steering circuit (§4.3) |
| Sharpen and commit | Turn a near-tie into a clear difference, and collapse many competing votes into exactly one action | sharpening and committing (§4.1.10) · lateral and mutual inhibition (§4.2) |
| Modulate | Let the animal’s own state change the verdict, and let a state outlast the event that caused it | internal state and affect (§4.1.11) · feedback loops (§4.2) · the neuromodulators (§4.3) |

### §4.1.8 — Evaluate: The Birth of Good and Bad

Before an animal can move toward anything, something has to make one direction preferable to another. That is less obvious than it sounds, because nothing in the world arrives labeled.

Consider a chemical drifting past a worm’s head. It is a molecule. Nothing about its shape, its concentration, or the receptor it happens to fit makes it inherently, objectively good or bad. Whether it is worth approaching depends on what the animal is, on what it eats, and on what eats it. A compound that means food to one species could mean danger to another.

So good and bad are not inherent in the world. They are assigned. The assignment is **valence**: the tag a nervous system attaches to what it senses, marking a thing as worth moving toward or away from. Valence is the first thing steering requires.

What valence provides is *approach and avoidance*. These are the two directions a steering animal can take with respect to anything it detects. A worm climbing a gradient of food odor is approaching. The same worm turning away from a substance that would damage it is avoiding. In both cases the animal is acting on a verdict it assigned rather than on a property it found.

It is worth being clear about how strong that claim is, because we make it mechanical in §4.2, and find it in tissue in §4.3. There is no goodness in the molecule, and there is none in the sensory cell that detects the molecule either. Value comes into existence somewhere in the arrangement of cells between the sensor and the organism’s actuators.

### §4.1.9 — Combine: Trade-offs and Logic

In a laboratory, a stimulus can be presented on its own. Out in the world, several arrive at once. Each one is a *cue*: something an animal can sense that carries information about what is out there. And they often imply different things. So another demand of steering is that many signals need to be combined into one direction of travel. Combination has two aspects that are worth keeping separate.

The first aspect is quantitative. Different cues pull with different strengths, and the strengths have to be weighed against one another. A well-studied case uses *Caenorhabditis elegans*, the millimeter-long soil worm we introduced in Module 3. *C. elegans* avoids copper, because copper is toxic to the worm. But what happens if there is food on the far side of a strip of copper? The animal meets a genuine trade-off. Whether it crosses depends on how strong the food odor is, set against how forbidding the barrier is. Make the attractant stronger, and more worms will cross. Make the copper more concentrated, and fewer do. Nothing here is a yes-or-no rule. Two graded quantities are set against each other, and the behavior results from which one wins.

The second aspect is relational. Sometimes what matters is not how strong the cues are, but which combination of them is present. An animal might need to feed only when there is food odor *AND* when the water is not too warm. It might need to flee when it detects a shadow *OR* a sudden vibration. Either one is sufficient on its own. It might need to advance when there is food odor *AND NOT* the scent of something that eats it. Those three relations, *AND*, *OR*, *NOT*, are primitive operators in symbolic logic, and the basis of digital electronics and computers. But long before that, they arrived as demands on behavior.

A demand that depends on which combinations of cues are present together can be written down compactly and exactly. We can list every combination of the conditions, and beside each combination, write what the outcome should be, or what the animal should do. The result is a **truth table** [](#t-truth-tables). A truth table listing the outcome for all combinations of inputs is more precise than a sentence describing the relationship. This is because it says what should happen in *every* case, including the cases nobody thought to mention. A piece of a nervous system that computes one of these three relations is called a **logic gate**.

Written out, a truth table states what a piece of a nervous system does. It says nothing whatever about how. That mapping from conditions to action is the circuit’s **target function**. Naming the target before knowing the mechanism is ordinary business at the computational level, and we did the same thing in Module 3, when we said what neurons had to accomplish several pages before any account of how they accomplish it.

: Three target functions over the same two cues. Each row is one combination an animal might meet, and each of the last three columns is a different demand steering could make of that combination. A target function says what a piece of a nervous system must do, and says nothing about how it does it. In §4.2, we build arrangements of neurons that satisfy all three. {#t-truth-tables}

| Cue A | Cue B | *A AND B* | *A OR B* | *A AND NOT B* |
|---|---|---|---|---|
| absent | absent | do not act | do not act | do not act |
| absent | present | do not act | act | do not act |
| present | absent | do not act | act | act |
| present | present | act | act | do not act |

### §4.1.10 — Sharpen and Commit

The next set of demands, sharpening and committing, concerns the quality of a decision.

Sharpening comes first. Suppose two cues arrive that are nearly equal. A food odor is very slightly stronger on the left than on the right. The difference is real and it is tiny. A nervous system that reported it faithfully would hand the muscles a near-tie. But when a decision must be made, it would be more useful to exaggerate the difference. Take a shallow gap in the input, and produce a steep one in the output. The result is that the marginally better direction becomes plainly the better one. Exaggerating a difference is something a nervous system might do. An animal that does it can act more decisively, and sooner, than one that does not.

Committing is the harder demand, and it follows from a fact about bodies rather than a fact about information. A worm has one body, and the body can go in one direction. So however many cues were weighed and combined, the result has to be a single action. Not a blend of two actions, and not half a turn to the left with half a turn to the right, which would carry the animal somewhere that neither cue recommended. Exactly one.

That constraint is not a small one. A system that averages its options is a system that walks between two doors into the wall. Several of the arrangements we will see in §4.2 look strange on first meeting. There are neurons whose main job is to quiet other neurons. But machinery of that kind is exactly what a body needs when it must make a choice and suppress the alternatives.

### §4.1.11 — Modulate: Internal State and Affect

The demands so far — evaluate, combine, sharpen and commit — treat an animal’s verdicts as fixed, as though a smell that is good is simply good. But few verdicts *are* fixed.

Food is not always worth having. A worm that has just eaten gains little by crossing a strip of copper. An odor that was worth a burn an hour ago is not worth one now. So valence depends on something besides the world. It depends on the animal’s own condition: hunger, injury, fatigue, whatever it was doing a moment ago. We can call that condition an **internal state**. The fourth demand is that internal state be able to reach into the evaluation and change the verdict.

The *C. elegans* worm supplies us with a clear example. Carbon dioxide is a cue *C. elegans* normally avoids. But a worm that has gone some hours without food avoids it far less. And under some conditions, the worm is drawn toward carbon dioxide, since in a worm’s world carbon dioxide can mark decaying material that other worthwhile things gather around. We have the same animal, the same molecule, but opposite behavior depending on the worm’s internal state.

The demand to modulate hides a second and subtler requirement. Sensory evidence is fleeting. A predator’s scent arrives and then disperses. Food is found in one spot, and then the spot is empty. An animal whose behavior tracked only what its sensors report at this instant would stop fleeing the moment the smell thinned, and stop searching the moment the last morsel was gone. It is better to keep going, to enter a state that outlasts the event which caused it, and that keeps shaping behavior after the evidence is gone.

Persistent states of that kind are where **affect** begins. Affect is an internal state that outlasts its cause and biases what an animal does over a stretch of time, rather than at a single instant. Two quantities describe a surprising amount of it. The first is valence, which we already discussed. Are things currently good, or bad? The second is **arousal**, meaning how activated the animal is. How vigorously and how readily will it react to anything at all?

These two quantities, valence and arousal, define a two-dimensional space. An affective state is then a position in that space [](#f-valence-arousal). Panic and gloom share a negative valence, and differ in arousal. Contentment and boredom sit at much the same arousal, and differ in valence. Panic and excitement sit at much the same arousal too, and differ in nothing but whether things are going well.

![The two dimensions of affect, with five states placed on them. Valence runs left to right, from bad to good. Arousal runs bottom to top, from quiet to activated. Panic and gloom share a valence and differ in arousal; panic and excitement share an arousal and differ in valence; gloom, boredom and contentment sit at much the same arousal and differ in valence.](reading_images/fig-valence-arousal.svg){#f-valence-arousal alt="A square plot. The horizontal axis is labeled valence and runs from bad on the left to good on the right; the vertical axis is labeled arousal and runs from quiet at the bottom to activated at the top. Five labeled points are marked. Panic sits high on the left, and Excitement sits high on the right at the same height, joined to it by a faint horizontal guide line. Directly below it, near the bottom of the left side, sits gloom. To the right of gloom and at the same height sits boredom, a little way toward the middle. Further right and still at the same height sits contentment, on the positive side of the valence axis. A faint vertical guide line joins panic and gloom, and a faint horizontal guide line joins gloom, boredom and contentment."}

One connection to Module 3’s discussion of energy costs is worth flagging. A persistent state is partly an accounting decision. Reacting hard is metabolically expensive, so an animal that stays keyed up is spending energy, and an animal that stops responding is conserving energy. We will return to that in §4.3, when we discuss it in terms of its chemical implementation.

### §4.1.12 — A Machine That Steers

In Module 3, we set a single artificial neuron beside a single real one, and found the resemblance close at the algorithmic level and nonexistent at the implementational one. The comparison can be taken up a level: not a single neuron, but a whole agent with a job to do.

A robot vacuum makes a fair example, precisely because it is not trying to be an animal. It is a disc that has to cover a floor and find its way back to its dock. The problems it has to solve to do its job are the same four we have discussed.

It steers. The body is round, but the machine has a front: a bumper, a direction of travel, and its sensors clustered at that end. It goes forward and it turns. And what the leading end detects, settles which way the turn goes. That is the bilaterian arrangement, showing up in a machine.

A robotic vacuum also assigns valence and combines what it senses. A wall is bad, and the dock is good. Neither fact is in the wall or in the dock. Both are in how the machine is wired to respond to them. Dirt detected underneath is a reason to stay the course. A drop-off detected is a reason to turn away. The two have to be settled against each other, rather than obeyed one after the other.

The robot’s own state affects the verdict, and some of its states outlast their causes. The dock is good only when the battery is low. And a machine that has detected a dirty patch keeps working that patch for a while after the sensor has stopped reporting dirt.

None of this makes a robot vacuum exactly like a worm. What it shows is that the four demands belong to the problem, rather than to biology. Anything that has to get somewhere useful in a world it only partly senses will meet them. It is worth being careful about what kind of resemblance this is. In Module 2, we called it convergence when one problem produces much the same solution in lineages that did not share it. This is not quite that. The robotics tradition the vacuum comes from turned to animals deliberately, after years of building machines that planned a route from a stored map and found the world changed faster than they could plan. So the resemblance is partly borrowed. But the borrowing is itself the evidence: the demands were legible enough in real animals that engineers could read them off and build with them.

The computational level has now done its work. Steering demands that an animal evaluate what it senses, combine cues that disagree, sharpen faint differences and commit to one action, and let its own state modulate all of it. Every one of those is a statement about what has to be computed. But none of them says what has to be represented, or by what procedure. In §4.2, we take the four demands in the order they were raised and build, for each, the arrangement that meets it.

## §4.2 — Algorithmic: Circuits That Compute Value

### §4.2.1 — The Algorithmic Question: From a Unit to a Wiring Diagram

We have defined the four demands of a steering organism. In this section, we define some mechanisms. The algorithmic question asks what information a system represents, and what procedure it runs on those representations. The answers come in the order the demands were raised. What they add up to is that a small number of wiring patterns do nearly all of the work.

In Module 3, we established what makes a set of neurons a circuit rather than a puddle. Flow within a cell runs one way, and connection is a matter of wiring neurons together, rather than merely being near each other. Two neurons whose cell bodies are pressed against each other may have nothing to do with each other. Another neuron’s axon may reach across a whole animal to form a connection with the other neurons it talks to.

That fact is what makes the rest of this section possible. Because connection is wiring, a nervous system can be drawn as a diagram. And the diagram can be reasoned about without knowing anything about the cells. A **neural circuit** is a set of neurons connected in a specific pattern, doing something together that no one of them does alone.

Many neural circuits follow patterns. They are small, and they recur [](#f-motifs). A **circuit motif** is a wiring pattern that turns up again and again, in different animals and in different parts of the same brain, because it computes something generally useful. Motifs stand to circuits roughly as letters stand to words. There are not many of them, and almost everything in this section is built from five.

![The five circuit motifs used in this section, drawn in one panel. Convergence and divergence are the two simplest. Lateral inhibition sharpens a difference, mutual inhibition forces a choice, and a feedback loop keeps activity running after its input has stopped. Each is returned to, one at a time, in the subsections that follow.](reading_images/fig-motifs.svg){#f-motifs alt="Five small wiring diagrams arranged in a row, each labeled. In the first, four circles at the left all send arrows into a single circle at the right. In the second, one circle at the left sends arrows out to four circles at the right. In the third, a row of five circles each send arrows to their immediate neighbors, the arrows ending in flat bars rather than points. In the fourth, two circles face each other and each sends a flat-barred arrow to the other. In the fifth, a circle sends an arrow to a second circle, which sends an arrow back to the first, forming a closed loop."}

### §4.2.2 — Convergence and Divergence

We begin with the two simplest circuit motifs.

**Convergence** is when many cells project onto one cell. It is what makes our second demand, combination, possible. A cell can only weigh and combine information that actually arrives at that cell. In Module 3, we described a neuron summing whatever reached it. Convergence is the question of what should be arranged to reach it.

**Divergence** is one cell onto many. It is how a single verdict can reach muscle all over the body at once. It is what makes coordination possible, and what makes an action capable of being a whole-body commitment rather than a local twitch. A worm that reverses does not reverse in one segment. It coordinates its whole body to do so at the same time.

### §4.2.3 — The Floor and the Ceiling

In Module 3, we wrote a neuron down as an equation, and worked it with numbers. We also showed how a simple linear model of a neuron has limitations. Make the inhibitory input into a neuron strong enough, and the weighted sum goes negative. But no cell can fire a negative number of times per second. Similarly, a linear equation has no maximum value, but any real physical neuron will have some maximum firing rate.

Now we can address these issues. A real cell has a floor and a ceiling that a bare sum does not. It cannot fire less often than never, and it cannot fire faster than its refractory period allows. So the sum cannot be the final answer. It has to pass through one more step, a function that takes the total and squashes it into the range the cell can actually produce. Such a function is called an **activation function** [](#f-activation-function).

Two common activation functions are worth naming. A **threshold function** has a hard boundary, an abrupt transition from no firing to maximum firing. Below the threshold the unit is silent, at or above it the unit fires, and there is nothing in between. A **sigmoid function** has a softer, S-shaped curve that behaves like a threshold at the extremes, and grades smoothly in the middle. The name means nothing more than S-shaped.

Both functions have a floor and a ceiling, which solve the problems the linear equation introduced. A smooth curve is closer to what a real neuron does than a hard step is. But the hard step is the easier one to compute logic with. The difference between them is another instance of a point we made in Module 3: a model’s simplifications are claims about what matters or what is useful.

Nothing else about the unit needs to change to deal with the problems introduced by using a linear equation. The inputs still arrive as rates, the connections still carry weights with signs, and the weighted sum still happens. We just have to add the activation function step at the end of it.

![Module 3’s weighted sum, before and after an activation function is added. On the left the bare sum runs off the bottom of the plot into firing rates no cell can produce. On the right the same sum is squashed into the range between silence and the cell’s maximum rate, by a hard threshold and by a smooth S-shaped curve.](reading_images/fig-activation-function.svg){#f-activation-function alt="Two plots side by side. Each has the weighted sum on the horizontal axis and the output firing rate on the vertical axis. In the left plot a straight diagonal line passes through the origin and continues below zero into a shaded region marked as impossible. In the right plot two curves are drawn over the same axes: a step that sits flat at zero, jumps vertically at a marked threshold, and then runs flat at a marked maximum; and a smooth S-shaped curve that leaves zero gradually, rises steeply near the threshold, and flattens toward the same maximum."}

### §4.2.4 — Thresholds and Logical Computation

A bounded activation function does more than keep a neuron’s output inside the range a real cell can produce. It also turns the neuron into a logic gate. A unit that fires only when its weighted inputs pass a threshold is a unit that answers a yes-or-no question about a combination of conditions. That is exactly the shape of the truth tables we introduced in §4.1.

In Module 1, we said that the three levels are separable but not independent, and this is what that looks like from close up. In §4.1, a truth table was proposed as a computation that would help a steering organism solve problems it encounters. Now at the algorithmic level, a truth table can be the outcome that neural circuitry algorithms produce.

Give a unit y two excitatory inputs (x₁ and x₂), each with a weight of 1, and set its threshold at 2. Either input on its own contributes 1, which does not reach the threshold, and so y stays silent. But x₁ and x₂ together contribute 2. If both are active, the threshold is reached, and the unit fires. The unit y computes *AND*. Unit y will fire if units x₁ and x₂ are both firing.

Now change one number. Leave the weights for both x₁ and x₂ at 1, but set the threshold to 1 instead of 2. Either input on its own now reaches the threshold, and so do both together. The unit y now computes *OR*. Unit y will fire if either x₁ OR x₂ is firing. Nothing about the wiring changed. Only the threshold level of y changed.

To compute the logical operation *NOT*, the negation of an input, the unit y only needs an inhibitory input. In Module 3, we described this as a connection carrying a negative weight. Give y a standing excitation strong enough to fire it on its own, and one inhibitory input x₁ whose negative weight is large enough to cancel that excitation. With this, y fires whenever x₁ is silent, and falls quiet whenever x₁ is firing. Wire that inhibition *alongside* an excitatory input, and y computes *this and not that*, one of the problems we described in §4.1 that steering organisms face [](#t-truth-tables).

So the truth table we wrote down in §4.1, is satisfied by a simple wiring diagram and two numbers [](#f-logic-units).

One thing to be clear about, because it is the lesson we drew from the lab in Module 1. The unit y is not choosing anything, and it does not know what *AND* means. The logic is in the weights and the threshold, and nowhere else. Set them one way and the unit computes one function. Set them another way and the same unit computes a different one.

![Two units with identical wiring and different numbers. Each receives the same two excitatory inputs, each of weight one. The unit on the left has a threshold of two and fires only when both inputs arrive. The unit on the right has a threshold of one and fires when either does. The truth table beneath each shows what it produces for all four combinations.](reading_images/fig-logic-units.svg){#f-logic-units alt="Two diagrams side by side. In each, two circles on the left labeled x one and x two send arrows into a single circle on the right; each arrow is labeled with a weight of one, and the receiving circle carries a threshold value. The left circle is labeled threshold equals two and titled AND; the right is labeled threshold equals one and titled OR. Below each diagram is a four-row table listing the two input values and the unit's output for every combination; the AND table has a single one in its output column and the OR table has three."}

### §4.2.5 — Drawing Decision Boundaries

The neural circuit similarity between an AND gate and an OR gate can be shown in a drawing as well, which illustrates a useful way to think about neural circuits and logical computation. Consider a neural circuit with an output y and with two inputs, x₁ and x₂. We can put the two inputs on a pair of axes. Every possible combination of values of those inputs is then a point on a plane.

Draw what this looks like when we visualize a truth table for a logical function like AND or OR. We can plot all possible inputs: (0,0), (0,1), (1,0), and (1,1), representing all combinations of whether x₁ and x₂ are firing or not. We can then color-code those points according to whether or not, for that logical function, the output neuron y is supposed to be firing or not firing. Blue for yes, orange for no. For the logical function AND, we should only color the (1,1) point blue, the rest should be orange. For the logical function OR, we should only color the (0,0) point orange, the rest should be blue.

More generally, we can visualize what a neural circuit does, whether it says “yes” or “no” to any particular input, by color-coding the background color of the graph. A neural circuit that has one output unit with a threshold or sigmoid activation function will necessarily divide the space up using a single line. On one side of the line, the neural circuit will output a “yes”, and on the other side it will output a “no”. That line is the unit’s **decision boundary** [](#f-decision-boundary). The location of a circuit’s decision boundary is decided by its weights, in this case, b₀, b₁, and b₂.

Next, draw a boundary for the circuit calculating *AND*, and for the circuit calculating *OR*. The difference between the circuits doesn’t (need to) involve changing the slope of the decision boundary line. It just needs to shift in space, so that the points (0,1) and (1,0) change what side of the line they are on. Both OR and AND agree about how to respond to (0,0) and (1,1). The circuit should be off, and on, respectively. But they differ on how they respond to (0,1) and (1,0). The OR circuit should be on for those inputs, the AND circuit should be off. Shifting the decision boundary accomplishes this. And a shift in a line, with no accompanying rotation or change in slope, is another way of saying we are changing the intercept, or in this case, b₀, the base firing rate of the y neuron. Raising the threshold does the same work as lowering the baseline, which is why we could produce AND and OR earlier by moving the threshold alone. The baseline and the threshold are two knobs that slide the same line.

This shows us that we can use simple straight line decision boundaries to show how neural circuits can compute basic logical functions like AND, OR, and NOT on their inputs. A single straight line is a limited thing, though. There are computations organisms need to perform that no single line can produce, however the weights and the threshold are set. We will show how neural systems can deal with these problems in Module 7.

![The same four inputs, plotted twice. Each point is one combination of x₁ and x₂: blue where the circuit should fire, orange where it should not. The shaded background shows what a circuit with that decision boundary actually does, so a correct circuit is one whose shading matches its points. For AND only (1,1) is blue; for OR only (0,0) is orange. The two boundaries are parallel, because going from one to the other shifts the line without rotating it.](reading_images/fig-decision-boundary.svg){#f-decision-boundary alt="Two square plots side by side, labeled AND and OR. In each, the horizontal axis is x sub 1 and the vertical axis is x sub 2, both running from zero to one, and four dots mark the corners. Dots the circuit should fire for are blue and filled; dots it should stay silent for are orange and hollow. In the AND plot only the top right dot, at one and one, is blue and filled. In the OR plot only the bottom left dot, at zero and zero, is orange and hollow. A straight diagonal line crosses each square from upper left to lower right, with the region beyond it shaded pale blue and the region before it shaded pale orange. The line in the AND plot lies close to the top right corner, cutting off that one dot. The line in the OR plot lies close to the origin, cutting off that one dot. The two lines are parallel."}

### §4.2.6 — Lateral Inhibition

In §4.1, we noted that a nervous system sometimes needs to exaggerate a small difference. Here is a wiring pattern that does it.

Take a row of units, each receiving its own input, and have each one inhibit its neighbors in proportion to how active it is. A unit receiving a slightly stronger input inhibits the units beside it slightly harder than they inhibit it back. Its lead grows. A shallow step in the input comes out as a steep one in the output [](#f-lateral-inhibition). This arrangement is called **lateral inhibition**.

The consequence is easiest to see in perception. An edge between a light region and a darker one looks crisper to most living creatures with eyes than the light arriving from it warrants. This is because the units on the bright side are inhibited less than their neighbors while the units on the dark side are inhibited more. The nervous system is not reporting the light. It is reporting the difference, amplified. This is one of the main ways visual systems are biased to detect object boundary edges, since they are often accompanied by differences in the amount of light, which then gets exaggerated by the visual system.

![What lateral inhibition does to a gentle edge. The input rises gradually from a dark region to a light one. The output, drawn over it, has the same overall levels but a much steeper transition, with a dip on the dark side of the edge and a bump on the light side.](reading_images/fig-lateral-inhibition.svg){#f-lateral-inhibition alt="A single plot with two curves drawn on the same horizontal axis. A faint dashed curve, labeled input, rises gradually from a low level on the left to a high level on the right. A heavier solid curve, labeled output, follows the same overall path but changes far more abruptly in the middle, dropping below the dashed curve just before the rise, in a marked dip, and overshooting above it just after, in a marked bump, before settling to the same high level."}

### §4.2.7 — Mutual Inhibition, and Choosing Exactly One

The hardest demand we discussed in §4.1 was committing: one body has to go in the one direction of its top choice, not in the average direction of its set of choices.

The circuit motif that solves this problem is two units that each inhibit the other. Suppose both receive nearly equal input. Whichever is momentarily ahead inhibits its rival a little harder. So the rival’s activity falls, and then the rival inhibits back a little less, so the leader climbs further still. The lead runs away. Within a short time one unit is firing and the other is silent. The arrangement is **mutual inhibition**, and the outcome it forces is called **winner-take-all** [](#f-winner-take-all).

What matters is what the circuit does with a near tie. It does not average the two options, and it does not report that the contest was close. It chooses. An animal that needed exactly one action gets exactly one action, and the fact that the evidence was nearly balanced is discarded along the way.

The shape of that argument is familiar. In Module 3, we explained the all-or-nothing action potential as a positive feedback runaway: sodium entering the cell opens channels that admit more sodium. Once the loop starts, there is no intermediate setting available. Mutual inhibition is the same runaway, one level up, built out of cells rather than channels, and producing a decision rather than a spike.

It also answers a question we left open in Module 3. We asked why activity that is so sparse — only a small fraction of cells strongly active at any moment — should carry information well. Now we can state the answer. A circuit that suppresses everything except the winner produces a sparse pattern, because the pattern is the instantiation of that decision. The silence of the losing units is not an absence of information. It is the result.

![Two mutually inhibiting units, started from nearly equal input. Their activity traces separate within a few tens of milliseconds: the unit that was momentarily ahead climbs to its ceiling while the other is driven to silence. A circuit of this kind does not average a near tie. It resolves one.](reading_images/fig-winner-take-all.svg){#f-winner-take-all alt="Above, a small wiring diagram of two circles side by side, each sending a flat-barred inhibitory arrow to the other, with an input arrow entering each from above. Below, a plot with time on the horizontal axis and activity on the vertical, showing two curves that begin almost on top of each other at a middling level. Within a short interval one curve rises and flattens near the top of the plot while the other falls and flattens at zero."}

### §4.2.8 — Loops That Keep Running

The fourth demand was for states that outlast whatever caused them.

Every arrangement so far has run in one direction, from input to unit to output. Connections of that kind are **feedforward**. But nothing stops a unit’s output from running back toward its own input, either directly or around a longer path through other units. A connection that does that is a **feedback** connection, also called a **recurrent connection**, because activity can run around the loop again and again.

Feedback connections and recurrent connections are not a retreat from the one-way rule. Each connection *within* a loop still runs in one direction. A neuron’s output still leaves by its axon, and arrives on another cell’s dendrites. And the loop is built out of those one-way links. A recurrent circuit has one-way connections that loop back around.

What a loop provides is persistence. A unit that excites something that excites it back can keep itself going after the input that started it has stopped. The stimulus lasts a moment. The activity lasts as long as the loop keeps running.

This has big implications. It means an internal state does not have to be *stored* anywhere. There need be no record, no trace, and nothing written down. A state can simply be a circuit that is still running, minutes after the thing that set it off has gone. We return in Module 10 to the difference between a state held in activity and a state held in a changed connection, which is a different thing entirely.

### §4.2.9 — Where Valence Lives

In §4.1, we claimed that good and bad are assigned rather than inherent in the world. But we left unexplained where those assignments come from. The circuit answer is simpler than most readers expect, and can be a little unsettling to some.

A sensory neuron does not carry a “good” signal. It carries a rate: so many spikes per second, more of them when the thing it responds to is stronger. Nothing about the rate says whether that thing is worth approaching. Two sensory cells, one responding to a food molecule and one to a toxin, can produce output identical in every respect a downstream cell could measure.

What makes one neuron a “good-detector” is what it is wired to. Route its output through to the machinery that drives the animal forward, and the cell is a positive-valence cell. Whatever the cell responds to, the animal approaches. Route the identical cell to the machinery that drives a withdrawal response instead, and it becomes a negative-valence cell. An arrangement of that kind is called a *labeled line* [](#f-labeled-line). But the label is not on the line. It is at the far end of it, the thing the line connects to.

![One sensory cell, drawn twice, with everything about the cell held the same. On the left its output is routed to the muscles that drive the animal forward, and whatever it responds to becomes something the animal approaches. On the right the identical cell, firing at the identical rate, is routed to the muscles that drive a withdrawal, and the same thing becomes something the animal avoids.](reading_images/fig-labeled-line.svg){#f-labeled-line alt="Two square panels side by side, labeled “Wired one way” and “Wired the other.” Each contains a single circle at the left, labeled as one sensory cell firing at rate r, and two rectangles at the right labeled forward muscles and reverse muscles. In the left panel an arrow runs from the circle up to the forward muscles box, which is drawn in full strength while the reverse muscles box is faint; beneath it the words the animal moves toward it. In the right panel the arrow runs from the identical circle down to the reverse muscles box, which is now the strong one; beneath it the words the animal moves away from it."}

So valence is a fact about the wiring diagram. In Module 3’s Close, we said that value is a property of an arrangement rather than of a cell, and this is the arrangement. We made the same point in Module 1’s lab, with two wires and a pair of motors, where crossing the wires reversed the behavior with every part unchanged.

At the level of neural circuitry, there is no good signal, no bad signal, no pleasure molecule, no pain molecule. There is just a cell, and where its output goes.

### §4.2.10 — Affect as Two Numbers

In §4.1, we put affect on a plane, and placed four states on it. Algorithmically, that plane is a claim about representation. An animal’s affective state is two numbers: one for how good or bad things are, and one for how activated the animal is. What the animal does next is a function of its position in that representational space [](#f-valence-arousal).

Why two numbers, rather than a list of named states? A list has to be written in advance, and it can only hold what someone thought to name. A space does not. Every position in it is a possible state, including the positions between the labeled points and the ones no language has a word for. Two numbers also describe a worm and a person in the same terms, which a list of human emotion words could not.

The claim is about representation and nothing more. How many dimensions we need to adequately describe human emotional life is argued about. The point we are trying to make here is more general and abstract. We can understand a lot about the behavior of neural circuits and whole organisms by thinking of neural circuits as defining spaces for decisions and preferences. The neural circuits and their activity levels define internal states, and behavior can be understood in terms of these circuits and their states.

### §4.2.11 — The Same Motifs in Silicon

In Module 3, we set one artificial neuron beside one real one. The comparison can now be made at the scale of the circuit, and it continues to hold surprisingly well.

An artificial neural network is also built from units that take weighted inputs, sum them, and pass the total through an activation function. Those units are wired into patterns, similar to the patterns we have been describing. Convergence and divergence are what every layer of such a network is made of. Mutual inhibition turns up wherever a network has to settle on one output among several. Recurrent connections are how a network holds a state across time. One diagram serves for both biological and artificial systems, another example of Module 1’s multiple realizability, this time at the scale of the circuit rather than the cell.

### §4.2.12 — What a Fixed Circuit Cannot Do

We now have arrangements that evaluate, combine, sharpen, commit, and persist. Every demand we raised in §4.1 has a wiring pattern instantiating it.

But also notice that in every one of those arrangements we described, the circuits have fixed weights. The numbers were set in advance, and nothing that happens to the circuit changes them. That is a real limit. A circuit with fixed weights can only ever do what its weights were set to do. It cannot come to treat a new smell as food. It cannot get better at telling two similar things apart by doing it a thousand times. An animal built entirely out of arrangements like these would meet the world with a fixed repertoire, and would meet it the same way on the thousandth encounter as on the first.

Where the weights come from, and how they can change within a single lifetime, is the subject of Module 5. The fixed weights are ours rather than the animals’. Holding them still is a simplification we are making on purpose, and Module 5 is where they start to move. Two other doors we opened will be followed up on as well: what a single decision boundary cannot separate, and the difference between a state held in running activity, and one held in a changed connection.

All of it has been arrows and numbers on a page. What remains is what any of it is made of in a real animal. Which cells implement these algorithms? In what physical arrangement? And what allows them to hold a state for an hour rather than a second.

## §4.3 — Implementational: The Biology That Runs It

### §4.3.1 — The Implementational Question, and the Tissue That Runs It

In §4.1 we told the story of the first nervous systems as a story about capability. In §4.2, we drew circuits in arrows and numbers. The implementational question asks what physically does any of it, and what the doing costs. Here is the tissue. A nerve net is neurons spread through the body wall, each connected to its neighbors, with nothing at the center. It is why a jellyfish cut in half leaves two halves that both keep pulsing.

But a nerve net is not perfectly even. In many cnidarians, and in the worm, the net thickens in places. In some places a band of it runs around the body. We call this a **nerve ring**. Where a cluster of cell bodies concentrates in one spot, we call it a **ganglion**. A ganglion is a center without being a brain. It is somewhere that a great many connections happen to be, and so somewhere a great deal of processing happens to get done.

In bilaterians, the largest ganglia end up at the front, with the sensors. An animal that moves in one direction has an end that arrives first, and both the sensing and the deciding are more efficiently done at that end. The concentration of neurons at the front of an animal is called **cephalization** [](#f-cephalization). It is the physical answer to why a brain is in a head.

![The same nervous system at four degrees of concentration: a net spread evenly through the body wall, a net thickened into a ring, a ring with distinct clusters of cell bodies, and a bilateral body with its largest clusters gathered at the leading end. Nothing is added along the row. Neurons are only gathered into fewer places.](reading_images/fig-cephalization.svg){#f-cephalization alt="Four simplified animal outlines in a row, each drawn from above. In the first, a rounded body is covered by an even mesh of fine lines with no denser region anywhere. In the second, the mesh remains but one band of it, running around the body, is drawn heavier than the rest. In the third, that heavier band carries several small filled clusters spaced around it. In the fourth, the body is elongated with a leading end at the left, the mesh is sparse through the trunk, and two large filled clusters sit at the leading end beside several short sensory marks."}

### §4.3.2 — The Worm’s Wiring Diagram

In Module 3, we introduced *C. elegans*. We noted that its adult hermaphrodite form has 302 neurons in its entire body, mapped in what we called its **connectome**. We also left three of the worm’s behaviors unexplained: it weighs a good smell against a bad one, it crosses a barrier only if the food is worth it, and it behaves differently when hungry. Here they get their mechanism.

One thing that makes the worm worth our attention is that its wiring diagram is complete. Every neuron, every connection between them, has been reconstructed by hand from thousands of electron micrographs of serial slices through the animal. All three hundred and two neurons, and all several thousand connections between them. It was the first nervous system of any animal to be mapped in full, and for a long time the only one.

The enterprise has a name now. *Connectomics* is the attempt to produce complete wiring diagrams of nervous systems. It has since been done for a fly, and is under way, in pieces, for a mouse and for human tissue. Those maps are enormously larger, and the human work covers small volumes rather than whole brains.

These connectomes are enormously difficult to produce. The worm’s map took over a decade for 302 cells. A wiring diagram is not a thing that can simply be read off an animal. It is a thing that has to be built, slice by slice.

### §4.3.3 — Tracing One Behavior

The worm connectome shows us an actual circuit that steers [](#f-worm-circuit). A worm climbing toward food runs on sensory neurons in the head, which respond to chemicals in the water it swims in. Interneurons receive input from several of these sensory neurons at once. Motor neurons receive input from these interneurons, and drive the body-wall muscles. Sense, combine, act, in three or four cells. The interneurons are doing exactly what we described in §4.2: receiving from several sources, weighing what arrives, and producing a verdict.

The strategy is not what some intuitively expect. The worm does not point itself directly at the food. It cannot. Its head sweeps side to side as it moves, and what it has to work with is not the difference between one side and the other, but the difference between what it senses now and what it sensed a moment ago. If the concentration is rising, nothing triggers a turn, and the worm keeps going mostly straight. If the concentration is falling, it turns more often, more or less at random, until it happens to be heading somewhere better. Going straight is not a behavior the worm produces. It is what happens when the rule for turning is not met.

That is a complete instance of steering, in an animal with fewer neurons than this paragraph has letters. And it makes a point that is easy to miss. Steering does not require knowing where the target is, or trying to go *somewhere*. It requires only a comparison across time, and a rule about when to turn.

The Braitenberg vehicles from previous labs steer as well, but they steer on a different principle. These vehicles carry two light sensors, one on each side, each wired to a motor. Whichever sensor receives more light drives its motor harder, and the body swings. Whether it swings toward the light or away from it depends on nothing more than whether each sensor feeds the motor on its own side or the motor across from it.

That is similar, but not identical, to what the worm does. In both, which route a signal feeds is what makes that signal good news or bad news. But the comparison a vehicle makes is between two places at one instant, and the body’s own geometry delivers the answer. A vehicle is, in that sense, told which way the light is.

A worm is not told the direction of the entity driving the sensors in the same way. It is a millimeter long, and the difference in concentration between one side of its head and the other is very small. Differences between the sensors on the two sides would not provide a lot of information. Perhaps unsurprisingly then, its chemosensory neurons are not wired to compare left side input against right side input. Instead of comparing two sides, each side compares two moments: now versus a moment ago. What a vehicle gets from having a body wide enough to straddle a gradient, a worm gets from holding onto what things were like a second ago. When the signal is improving, a wave of bending runs head to tail, and the animal goes on. When it worsens, the wave runs backwards instead, the worm reverses, making a deep bend that swings its head somewhere new, and sets off along the new heading.

Those same three layers, sensory to interneuron to motor, also settle a harder case: what the worm does when a good thing and a bad thing arrive together. Copper is detected by sensory neurons that drive the avoidance behavior. The food odor is detected by sensory neurons that drive the approach behavior. Both converge on interneurons that produce a single verdict. The worm crosses the toxic barrier when the attractant inputs win. The trade-off is, in tissue, a small number of cells receiving from both routes at once.

![The worm’s chemotaxis circuit, traced from surface to muscle. Sensory neurons in the head respond to the attractant, interneurons combine what several of them report and compare it against a moment ago, and motor neurons drive the body-wall muscles. The approach route and the avoidance route are drawn separately, because which route a sensory cell feeds is what makes its signal good news or bad.](reading_images/fig-worm-circuit.svg){#f-worm-circuit alt="A layered wiring diagram over an outline of a worm's head. On the left, four small circles labeled sensory neurons sit at the animal's tip. Arrows run from them to a middle column of three larger circles labeled interneurons, with several arrows converging on each. From the interneurons, arrows run to a right-hand column labeled motor neurons, which connect to a band representing body-wall muscle. Two routes are distinguished by line style: a solid route ending at muscle labeled forward, and a dashed route ending at muscle labeled reverse."}

### §4.3.4 — The Two Ends of the Circuit

Sense, combine, act. In Module 3, and again in §4.2, we worked through the middle of that sequence carefully and left both ends of it alone. A transmitter binds, a channel opens, ions cross, the voltage moves. That account covers one neuron talking to the next. It does not cover how a smell in the water gets into the system at all, and it does not cover how a verdict inside the system becomes a body that bends. We will cover the complex sensory-motor systems that evolved in vertebrates in more detail in Module 8. But it is worth a brief sketch now, to see how the *sense* and *act* parts of the sequence differ from the rest of neural communication.

At the sensory end, the stimulus itself is the key, and different kinds of senses (touch and the chemical precursors of smell and taste) have different biological mechanisms. A touch presses on the membrane of a sensory neuron, and pulls a channel open mechanically. An odor molecule binds to a receptor protein on the surface, and a short chain of steps inside the cell opens a channel a moment later. But what follows after that is the same for both touch and smell. Ions cross into the cell, the voltage moves, and from there the cell behaves like any other neuron. Converting an event in the world into a change in membrane voltage is called **transduction**, and it is the one thing a sensory neuron does that no other neuron does.

One detail about the worm is worth stopping on, because it revises something we said in Module 3. There, we said that a neuron’s output is all-or-nothing: a full action potential, or none. We extolled the virtues of this digital-like information processing. In *C. elegans*, and in a number of other small invertebrates, this is mostly not true. The worm’s genome contains no voltage-gated sodium channels at all. Jellyfish *do* have those channels, and fire ordinary sodium spikes. So the nerve net of §4.3.1 is not what the worm is showing us. Nematodes appear to be a lineage that let all-or-none spikes go. Most of the worm’s neurons signal with graded changes in voltage, rather than with spikes. A larger input produces a larger swing, continuously. A calcium-based all-or-none spike has been found in one of the worm’s smell sensation neurons, so the picture is not uniform. But the animal whose circuit we have just traced largely does not fire in the way we described in Module 3.

But the broader point is true despite this correction. A threshold is a claim about a function: below some level of input nothing happens, and above it something does. An all-or-none spike is one way to build a threshold. A graded signal that stays too small to release any transmitter until the input is large enough is another way to build the same thing. Our claims about the disadvantages of graded neural firing are still true, such as how the signal fades and picks up noise with distance. But this is less of an issue in very small organisms like *C. elegans*. It may be that there was not evolutionary pressure to pay the added cost of perfectly discrete, all-or-none signals in such small creatures.

At the other end of the sense-combine-act system, the target is not a neuron. A motor neuron ends on a muscle cell, and the junction between the two is a **neuromuscular junction**. The neurotransmitter that crosses it is *acetylcholine*. It opens channels in the muscle membrane, and the muscle depolarizes much as a neuron would. What happens next is what makes a muscle a muscle. Calcium floods into the cell, filaments inside it slide past one another, and the fiber shortens, pulling on adjacent, attached cells. The verdict stops being a voltage, and becomes a force.

The worm’s body wall runs on an arrangement we have already built. Its muscles lie in strips along the length of the animal. Its motor neurons do two things at once. Excitatory motor neurons release *acetylcholine* onto the muscle on one side. Inhibitory motor neurons release *GABA* onto the muscle on the opposite side. If the animal contracts one side while releasing the other, the body bends. Then the two swap. That is §4.2’s mutual inhibition, implemented in musculature [](#f-motor-alternation).

Another interesting fact about *C. elegans* is that the two sides in question are the animal’s back and its belly, not its left and its right. A worm lies on its side, so a bend that looks from above like a sweep to the left and the right is, in the animal’s own frame, a bend upward and downward. A wave of that alternation, starting at the head and traveling toward the tail, is forward movement.

![The worm in cross-section, with the muscle on one side contracting while the muscle on the other is released, and the two motor neurons that hold that arrangement. The excitatory neuron releases acetylcholine onto the contracting side; the inhibitory neuron releases GABA onto the released side. The sides are the animal’s back and belly, not its left and right.](reading_images/fig-motor-alternation.svg){#f-motor-alternation alt="On the left, a circle representing a cross-section through the worm. Its upper half is filled solid and labeled contracting; its lower half is outlined with a heavy dashed arc and labeled released. The top of the circle is labeled back, in parentheses dorsal, and the bottom is labeled belly, in parentheses ventral. On the right, two small circles one above the other: the upper is labeled ACh and an arrow with an arrowhead runs from it to the words back muscle; the lower is labeled GABA and a line ending in a crossbar rather than an arrowhead runs from it to the words belly muscle."}

Turning is the same circuit motif one layer up. One small group of interneurons drives the forward wave. Another drives the backward one. The two suppress each other, so only one of them is in charge at any moment. When the comparison across time comes out badly, the backward group wins, the wave reverses, the animal backs up, and a deep bend swings its head somewhere new. The rule about when to turn is not written down anywhere in the worm. It is which of two mutually inhibiting groups of cells currently has the upper hand.

### §4.3.5 — Neuromodulation, and What a Connectome Does Not Tell Us

There is a limit to what we can learn from connectomes. And that limit is the reason the chapter is not finished at the end of a wiring diagram.

The worm’s wiring has been completely known for decades, and its behavior still cannot be predicted from the diagram. Give the same animal the same input twice, and it may do different things. A worm that has just eaten, and a worm that has gone hungry for hours, will respond to the same molecule in opposite ways, with the same 302 neurons wired the same way.

So the diagram is not the whole machine. Something else is varying, and in this case it is not the connections. In Module 3, we described a tradeoff in neural versus chemical information processing. A neuron gives up the cheap, everywhere-at-once reach of chemical signaling, in exchange for speed, distance, and aim. Signaling by diffusion was the old way, and it was slow and unaimed and could not be switched off.

Neuromodulation shows us that the old way did not go away with the evolution of neurons. The body still uses chemical signaling, and that chemical signaling can affect the firing of neurons as well. A **neuromodulator** is a chemical that is released into the surrounding tissue rather than into a single synapse. It reaches many cells at once. It acts over seconds to minutes rather than milliseconds. And it does not carry a message. What it does is change what the cells that receive it do with the messages they are already getting. Neuromodulators turn a neuron’s sensitivity up or down, temporarily making one pathway easier and another harder.

The effect of neuromodulators is that one wiring diagram can behave as several different circuits, depending on what chemicals are currently nearby. The worm’s connections do not change when it gets hungry. What changes is the chemistry running through them.

### §4.3.6 — Four Molecules, and the Space They Move an Animal Through

Four neuromodulatory molecules are worth naming, and it is worth showing that they are not four unrelated chemicals [](#t-neuromodulators). They are four ways of moving an animal around the two-dimensional affective space we drew in §4.2 [](#f-modulator-space).

*Dopamine* drives pursuit. It is the chemistry of wanting a thing and going after it. Treating dopamine as the chemistry of enjoying the thing once it arrives is a common misperception, and the distinction matters enough that we return to it in §4.3.10.

*Serotonin* tracks satiety and the overall tone of the system. In the worm, it is tied to food quite directly. A hungry worm that finds bacteria to eat slows almost to a stop, and that slowing depends on serotonin.

*Norepinephrine* sets arousal and vigilance in vertebrates. It is the dial for how strongly they react to anything at all.

*Endorphins*, and the other opioids the body makes itself, carry relief and satisfaction. They are the chemistry of liking, rather than wanting, which is why the two can come apart.

: The four neuromodulators, what each one does, and where each moves an animal on the valence–arousal space of §4.2. Read the third column as a direction of travel rather than a location: a modulator shifts an animal’s state, and where it ends up depends on where it started. The last column is why a chapter about a millimeter-long worm has anything to say about a human mood. {#t-neuromodulators}

| Molecule | What it does | Where it moves the animal | In human life |
|---|---|---|---|
| Dopamine | Drives pursuit of a thing: wanting, and the effort spent getting it | Raises arousal; raises expected valence rather than current valence | Motivation, and what is captured in addiction |
| Serotonin | Signals satiety and sets the overall tone of the system | Lowers arousal; raises valence toward contentment | Mood and patience; a common target of medication |
| Norepinephrine | Sets vigilance: how strongly to react to anything | Raises arousal, at either valence | Alertness and startle; arousal set too high in anxiety |
| Endorphins and other opioids | Carry relief and satisfaction: liking rather than wanting | Raises valence; lowers arousal | Pleasure and pain relief; the target of opioid drugs |

![The valence–arousal space of §4.2, with the four neuromodulators drawn on it as arrows rather than points. Each arrow shows the direction a modulator pushes an animal’s state, not a place the animal sits. The four are not four unrelated chemicals. They are four ways of moving through one space.](reading_images/fig-modulator-space.svg){#f-modulator-space alt="The same square plot as the earlier affect figure, with valence on the horizontal axis from bad to good and arousal on the vertical from quiet to activated, and the four labeled states faint in the background. Four heavy arrows are drawn from a common point near the middle. The arrow labeled norepinephrine points straight up. The arrow labeled serotonin points down and to the right. The arrow labeled endorphins points right and slightly down. The arrow labeled dopamine points up and to the right."}

### §4.3.7 — Where Biology and Artificial Networks Genuinely Diverge

In Module 3, we located one divergence between natural and artificial systems: the same algorithm (weighted input summed into an output) is implemented in radically different materials. Here we have a second big difference, and it sits higher up.

An artificial network has weights and activations, and that is all it has. Nothing in it corresponds to a chemical released into the space between units. Nor are there typically any artificial mechanisms for reaching all of the units at once the way neuromodulators do, changing how every one of them responds for a stretch of time, and then wearing off. Engineers do sometimes set a global parameter that changes a whole network’s behavior at once, but it is set from outside, rather than released by the network into itself.

This is a real asymmetry, but its implications are unclear. It is not obvious that the artificial systems are missing something they need. It is not obvious that they are not.

### §4.3.8 — What a State Costs

A state that outlasts its cause is what lets an animal keep fleeing after the scent has thinned, and keep searching after some of the food is gone. That is what made persistence worth having in the first place. Neuromodulators are an important part of how a small animal maintains a persistent state. A chemical released into the tissue keeps a circuit tuned one way for minutes, long after the event that set it off.

Holding a state that way has a consequence the wiring diagram does not show. Reacting strongly is metabolically expensive. An animal that stays keyed up is spending and spending continuously. An animal that stops responding under conditions it cannot escape is conserving. That is the non-pathologizing way to understand many behaviors, including in humans. Giving up is a thing bodies do to save energy, not simply a thing that goes wrong.

### §4.3.9 — Conservation, and Why This Is About Human Beings

The reason a chapter about a millimeter-long worm bears on human motivation is that some human chemistry is very old. But the conservation is partial, and the complexity and differences are interesting.

Dopamine and serotonin are notable cases. Both are present in the worm and in human beings. And both act through receptor families that are recognizably related across that evolutionary distance. A worm slowing on a bacterial lawn and a person losing interest in a meal are not the same event, but the machinery is not unrelated either.

Norepinephrine is less similar. The worm does not appear to make norepinephrine at all. It uses two other amines, octopamine and tyramine, in roles that overlap with the vertebrate arousal system, in ways that are still being worked out. So the four molecules in the table are not four ancient constants. Two run deep, and the others are more recent or more variable.

That is exactly what we should expect, given the comparative method of Module 2. Shared machinery is evidence of shared ancestry. Different machinery doing a similar job is evidence of something else, often shared constraints. Telling the two apart is the whole business of comparative work.

The human end is where this matters most. Motivation, mood and alertness in ordinary life run on these systems. When they go wrong, the shapes are recognizable in the terms we have built. Addiction is understandable as the wanting system being captured and driven by something that does not feed it. The loss of the ability to enjoy things, which clinicians call *anhedonia*, is understandable as the valence axis being stuck in a low state, so nothing registers as worth pursuing. Anxiety is understandable as arousal set high and staying there. None of this is a complete account of any of those conditions, in humans or worms. And none of these is a simple chemical shortage. The phrase *chemical imbalance* suggests a level that has dropped and could be topped up. But that is not what anyone finds when they look. These are systems with feedback, states, and histories. They go wrong in ways that match their structure.

### §4.3.10 — A System That Can Be Hijacked

One last consequence follows from everything above. A system that assigns value is a system that can be fooled about value. Anything that acts directly on the “wanting” chemistry (dopamine and its receptors) produces the pull toward a thing, without the thing. That is what addictive substances do, and it is why wanting and liking can come apart. And it is why, when they do come apart, this is not a curiosity but the center of the problem. The pursuit can grow, while the satisfaction shrinks.

It is not only substances. Any arrangement that reliably triggers pursuit can sit on the same circuit. Things designed to hold attention are designed against exactly this machinery, whether or not anyone intended it.

Steering has now been answered at all three levels. Why it was worth having, what arrangements compute it, and what tissue and chemistry run it.

## Close — What Wiring Made Possible, and What It Still Cannot Do

We have taken an arrangement of neurons, called a neural circuit, and examined it three times.

We asked why neurons came to be wired into circuits at all. An important answer, perhaps *the* answer, is for steering. An animal that moves in a direction has to settle which direction. And settling it demands evaluating what information arrives, combining signals that disagree, committing to one action, and letting the animal’s own condition change the verdict.

We asked what such an arrangement computes. The answer was a short list of wiring patterns: convergence, divergence, weights against a threshold, lateral inhibition, mutual inhibition, and recurrent feedback loops that feed themselves. Each of these helps meet the demands we listed at the computational level.

We asked what physically implements these computations. The answer was a net of neurons condensing into rings and ganglia and then into a front end. We discussed a worm whose entire wiring diagram we possess. We also discussed a handful of chemicals released into the tissue that retune the whole arrangement for minutes at a time.

All of this has been an elaboration of one idea. In the earliest animals, “good” and “bad” are verdicts an arrangement assigns, rather than properties the world provides. The value of an input derives from what a cell is wired to. And it also derives from the neuromodulatory chemistry currently running through the circuit, which is what decides how much any of it matters at this moment.

The comparison with artificial networks ran the length of the chapter, and it came out differently at each level. The demands are the same. The wiring patterns are very nearly the same, which is why one set of diagrams served for both. The chemistry and a lot of the implementational details are not. Whether that absence is a deficiency is not something anyone can currently say.

One thing has been missing from every arrangement in this chapter. Neuromodulation looks at first like the missing thing. The same wiring produces different behavior from one hour to the next, and the animal’s own condition is what decides which. But none of that is learned. A hungry worm and a fed worm run the same circuit with different chemistry, and once the chemistry wears off, the modulation has left nothing behind. The weights do not move. Nothing about that episode is kept.

So the circuits we have built in this chapter meet the world with a repertoire that was set before the encounter began. They meet it the same way on the thousandth encounter as on the first. Real animals do not, and that includes the animals in this chapter. Leaving learning out was a choice, and we made it because a circuit is much easier to understand while its numbers hold still. How a weight changes within a single lifetime is the subject of Module 5. In Module 6, we scale this arrangement up into a vertebrate brain. In Module 7, we ask what a single decision boundary cannot separate, and what has to be added to separate it. We also look at the amazing pattern-recognition abilities that follow. And in Modules 11 and 12, when decisions stop being reflexive, we come back to value with much more to say about it.

## Further Reading

Places to go next, chosen because each one takes up a thread we could only pull on briefly.

**Peter Godfrey-Smith, *Metazoa: Animal Life and the Birth of the Mind*, 2020.** A philosopher of biology walking the same stretch of the animal tree we walk in §4.1 — sponges, corals, and the first nervous systems. Unusually explicit about how the inferences are made and where they are shaky. The best single place to follow up our question in §4.1.3 about how any of this is known.

**Valentino Braitenberg, *Vehicles: Experiments in Synthetic Psychology*, 1984.** The book behind the vehicles from the labs, and short enough to read in an evening. Braitenberg builds fourteen machines out of sensors wired to motors, and watches how quickly an observer starts describing them with words like fear and aggression. The claim in §4.2 that value lives in the wiring is his claim, made forty years ago and without explicit reference to neurons.

**Cornelia Bargmann, “Beyond the Connectome: How Neuromodulators Shape Neural Circuits,” 2012.** The argument from §4.3.5, by the neuroscientist who did most to establish it. A review article rather than a book, and heavier going than the rest of this list, but it is the clearest statement anywhere of why a complete wiring diagram is not a complete machine. Bargmann works on *C. elegans*, so the examples are the ones we use.

**Amanda Gefter, “The Man Who Tried to Redeem the World with Logic,” 2015.** The story behind neural logical computation we described in §4.2. In 1943, Warren McCulloch and Walter Pitts showed that a network of threshold units can compute logic. Gefter tells how the paper came to be written, by a neurophysiologist and a runaway who had taught himself logic in a public library. Free to read, and a better first encounter with the idea than the original paper, which is written almost entirely in formal notation.

**Lisa Feldman Barrett, *How Emotions Are Made: The Secret Life of the Brain*, 2017.** Barrett takes valence and arousal as seriously as we do in §4.1, and then argues that most of what ordinary talk builds on top of them is wrong. She argues that anger and fear are not states a brain has, but categories a brain constructs.

**Antonio Damasio, *The Strange Order of Things: Life, Feeling, and the Making of Cultures*, 2018.** Damasio argues that valence is even older than nervous systems. A bacterium keeping itself alive is already doing what we credit to circuits, and that feeling rather than wiring is the thread worth following.

## Glossary

**activation function** — The rule that turns the total input a unit receives into the output it produces. It sets the shape of the relationship, including whether the change from quiet to firing is abrupt or gradual.

**affect** — An internal state that outlasts its cause, and biases what an animal does over a stretch of time, rather than at a single instant.

**arousal** — How activated an animal is: how vigorously and how readily it will react to anything at all. One of the two dimensions of affect, alongside valence.

**bilateral symmetry** — A body plan with a left and a right that mirror each other, and with a front and a back. The front is the end that arrives first, which is where the sensors gather.

**cephalization** — The concentration of neurons at the front of an animal, with the sensors. It is the physical answer to why a brain ends up in a head.

**circuit motif** — A wiring pattern that turns up again and again, in different animals and in different parts of the same brain, because it computes something generally useful.

**connectome** — A complete wiring diagram of a nervous system: every cell, and every connection between them.

**convergence** — Many cells projecting onto one cell, so that one unit receives from several at once. The motif that makes weighing possible.

**decision boundary** — The line through the space of possible inputs that separates the combinations a unit fires to, from the combinations it does not.

**divergence** — One cell projecting onto many, so that a single verdict reaches several destinations at once.

**feedback** — A connection running from a later stage of a circuit back to an earlier one, so that activity can run around the loop again and again. Also called a recurrent connection.

**feedforward** — A connection running from an earlier stage of a circuit to a later one, with no path back.

**ganglion** — A cluster of neuron cell bodies concentrated in one spot, where a great many connections happen to be, and so a great deal of processing happens to get done. A center without being a brain.

**internal state** — The animal’s own condition — hunger, injury, fatigue, what it was doing a moment ago — which can reach into an evaluation and change the verdict.

**lateral inhibition** — An arrangement in which active cells suppress their neighbors, so that a small difference between inputs is turned into a large difference between outputs.

**logic gate** — A piece of a nervous system that computes a logical relation among its inputs, such as *AND*, *OR*, or *NOT*.

**mutual inhibition** — An arrangement in which two units each suppress the other, so that only one of them can be active at a time.

**nerve net** — Neurons distributed through the body wall, each connected to its neighbors, spread through the animal rather than gathered anywhere in particular.

**nerve ring** — A band of nerve net running around the body, thicker than the net around it.

**neural circuit** — A set of neurons connected in a specific pattern, doing something together that no one of them does alone.

**neuromodulator** — A chemical released into the surrounding tissue rather than into a single synapse. It reaches many cells at once, acts over seconds to minutes, and changes what those cells do with the messages they are already getting rather than carrying a message itself.

**neuromuscular junction** — The junction where a motor neuron ends on a muscle cell, and where a signal in the nervous system becomes a contraction.

**radial symmetry** — A body plan built around a central axis, much the same all the way around, with no front and no back.

**recurrent connection** — Another name for a feedback connection: one that lets activity run around a loop again and again, so that a circuit can hold a state after the input that started it has stopped.

**sigmoid function** — An activation function with a soft, S-shaped curve, behaving like a threshold at the extremes and grading smoothly in the middle.

**steering** — Moving forward, turning, and letting what the front end detects decide which way the turn goes. Not merely moving, but moving toward some things and away from others.

**target function** — A mapping from conditions in the world to the action a piece of a nervous system should produce. It says what has to be computed, and says nothing about how.

**threshold function** — An activation function with a hard boundary: an abrupt transition from no firing to maximum firing.

**transduction** — Converting an event in the world into a change in membrane voltage. It is the one thing a sensory neuron does that no other neuron does.

**truth table** — A list of every combination of inputs a circuit might meet, paired with the output the circuit should produce for each one.

**valence** — The tag a nervous system attaches to what it senses, marking a thing as worth moving toward or away from. Value is assigned rather than found.

**winner-take-all** — The outcome mutual inhibition forces: one option ends up active and the others end up silent, however close the competition started.

## Image Credits

Most of this chapter’s figures were drawn for the course and carry no separate credit. One comes from elsewhere, and is reproduced here under the terms named.

**A moon jelly** — Luc Viatour, [www.lucnix.be](https://www.lucnix.be), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Aurelia_aurita_(Cnidaria)_Luc_Viatour.jpg), under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
