# 5. Learning and Plasticity

This module is about learning. Every neural connection (or weight) discussed in Module 4 was set in advance, across generations, by differential survival. An animal built that way can only ever do what it was built to do. Here, the neural connections move within a single lifetime. This raises a question. What does it take to move a weight? While reading, look for the beginnings of answers to these questions:

- The nematode avoids copper, and nothing in the worm’s own life taught it to. So what does an animal that can learn have, that the worm does not?
- Can an animal with no brain learn? And what would settle a question like that, one way or the other?
- There are four ways to change a connection, and each one needs something different to be present before the connection will move. A teacher that already holds the right answer sounds like the easiest of the four to learn from. Why is it the hardest for an animal to arrange?
- A synapse can register only the two cells it sits between. So how does a synapse come to change because something, somewhere else, went better than expected?
- A synapse changes, and stays changed. Is that a memory? If it is not, what is missing?

By the end, we should have a working answer to each one. We will also turn Marr’s wheel a third time, and find three places where it strains — which is worth knowing about any tool used as often as this one.

---

At the end of Module 4, we had an animal that could steer. Its nervous system evaluated what arrived at its surface. It combined signals that disagreed. It sharpened a difference into a decision, and committed to one action rather than half of two. And it held a state that outlasted the thing that caused it. Every one of those arrangements worked because of its weights, the strength of the connections between neurons. These weights affected which input counted for how much, and with what sign. And the way we discussed them in Module 4, every one of those weights was set in advance.

And as we discussed, having hard-wired neural connection weights means the animal has limited ability to adapt to new circumstances. One kind of flexibility was available to that animal, and it is worth being exact about why it is not enough. An animal with hard-wired weights can still be modulated. A neuromodulator washing through the tissue changes what the same circuit does with the same input. This allows a hungry worm to treat a faint food signal as worth pursuing, while a fed one ignores it. But when the chemistry clears and reverts to the previous state, the animal is exactly what it was before. The weights do not move. Nothing that happened is kept or changed. Nothing we could call learning occurs.

The limit is easiest to feel by changing the world on such an animal. Move the food to the other side of the dish. Make the smell that has always meant a meal mean poison or predator risk instead. If weights are fixed, the animal can only ever produce the responses its weights were set to produce. From the outside, we could see how the weights should change to work better in a new situation. But the animal cannot do this on its own, and that’s a serious limitation.

Getting from that animal, to one that can learn, asks for a distinction we have been using without explicitly stating it. Marr’s three levels are one way a question about a capacity can change [](#t-levels-learning). Moving *down* Marr’s levels changes the *kind* of question, with the capacity held fixed. We can take steering, and ask what problem is being solved, by what procedure, and by what physical means. One capacity, three questions.

There is a second distinction we can make about a capacity. Here, we hold the kind of question fixed, and take a narrower *case* of it. For example, a nerve net solves the problem of coordinating a whole body in time. A bilaterian solves the problem of coordinating a body *and aiming it somewhere*. Both of those are computational questions. But aiming is coordination with a constraint added, one notch more specific. An account of coordinating a body is not an account of aiming one. The move from broad to narrow is not limited to the computational level. A procedure has narrower cases too, and so does a physical mechanism. We will watch all levels get more specific later in this module.

What tells apart movement between levels, and movement from broad to narrow, is the vocabulary a description is stated in. Moving between the levels changes that vocabulary: the computational description of steering is stated in terms of the animal’s world, the algorithmic one in terms of what is inside the animal, and the implementational one in terms of physical parts. Taking a narrower case tends to use the same vocabulary, or at least many of the same words. Coordinating a body and aiming one are both stated in terms of the animal’s world. Aiming simply covers fewer situations. And a narrower case earns a name of its own when it changes what a solution must have, not when it is merely harder.

From here, some of our models will make this kind of move. Rather than stepping forward in evolutionary time and introducing a new animal in the human lineage, we will stay within an animal and describe an additional capacity not covered in previous modules.

In this module, that capacity is learning, and it comes in more than one variety. Two questions divide the varieties, and they cross rather than stack. The first is *what there is to learn*. How complicated is a relationship that an animal has to pick up? The second is *what there is to learn from*. What kind of information does an animal have to go on, at the moment a connection changes?

<!-- pin: t-levels-learning -->

: Marr’s three levels, the question each asks, the discipline that asks it, and this module’s example. {#t-levels-learning}

| Level | The question it asks | Discipline | This module’s example: a weight that can change |
|---|---|---|---|
| Computational | What problem is being solved, and why does solving it matter? | Evolution and ecology | Detecting contingencies that selection could not have fixed a response to: ones that change within a lifetime, ones that differ from place to place, and ones that are new to the species |
| Algorithmic | What is represented, and by what procedure? | Cognitive psychology and AI | Rules that move a weight — on local activity alone, on a target supplied by the world or by a teacher, or on one broadcast number reporting how things went |
| Implementational | By what physical means, and at what cost? | Neuroscience | A synapse that detects coincidence, a signal from elsewhere that gates what the coincidence does, and a fading mark that decides which synapses are still candidates |

## §5.1 — Computational: The Advantage of Changing Within a Lifetime

### §5.1.1 — The Problem, Inherited

In Module 3 we asked the computational question of a cell, and in Module 4 of an arrangement of cells. Here we ask it of a *change*. What problem does a change inside an animal solve, and why did an animal that could make one leave more descendants than an animal that could not?

In Module 4 we discussed weights of neural circuits as though they were all hard-wired and fixed. Real animals learn, including the small ones in that chapter. For the purposes of the chapter, we discussed the circuits as fixed, because a circuit is far easier to explain while its numbers are not moving. An animal built that way cannot come to treat a smell it has never encountered as a sign of food. It cannot come to treat a smell that has always meant food as a sign of danger. Put such an animal into a world whose regularities have shifted, and it goes on producing what it was built to produce. If it fails, it will continue failing identically every time.

The fix is simple. The weights need to change. But naming a fix is not the same as knowing what it requires, and the rest of §5.1 is about that difference.

### §5.1.2 — Detecting a Contingency Is Not New

Animals don’t need learning for detecting contingencies in the world. The worm avoids poisonous copper. In the places that worm’s ancestors lived, dissolved copper was a dependable sign of harm — a **contingency**, a reliable relationship between one thing and another. And the worm’s nervous system reflects that contingency: copper ahead, and the animal avoids it.

Nothing that happened in the worm’s own lifetime established the relationship, though. It was detected across generations, by differential survival among animals whose wiring differed. And the outcome resulted in a population whose wiring reflected that contingency. In Module 2, we met two senses of the word *adapt*. One ran across generations, and one ran within a lifetime. The worm’s copper avoidance is the first kind of adaptation: a lineage comes to fit its world because the variants that fit left more descendants. Nothing was trying to do the fitting. Nothing had to *know* that copper was dangerous, for the animals that avoided it to become the common kind.

So the new capacity in this module is not contingency detection. Animals were tracking contingencies for a very long time before any of them could learn. What is new is a *second route* to the same result, running on a different timescale, and inside *one* animal, during *one* lifetime.

### §5.1.3 — The Timescale Mismatch

Selection is a slow filter, and a coarse one. A neural response becomes common in a lineage only if the contingency it reflects was true for a long time, and experienced by a large number of individuals. Under those conditions, a difference in survival can accumulate across generations.

There are three kinds of contingencies that can slip through a filter of that shape. Some contingencies hold for a season and then reverse, so that the response that fit last month no longer fits this month. Some are true in one patch of territory, and false in the next, so that no single wiring fits the whole species. And some have never occurred in the lineage at all, because the flavor or the predator or the chemical is new.

Taste aversion is a simple case, and it carries two of the three at once. A rat eats something with an unfamiliar flavor, and is sick several hours later. It will not touch that flavor again. The flavor may be one no rat in that lineage ever encountered, and a plant that poisons a rat in one patch of territory may not grow in the next. The delay between eating and sickness rules out any moment-by-moment reflex. And the learning holds after a single experience — because the cost of a second experience is death.

That gives us the module’s problem, stated precisely [](#f-two-timescales). It is not *detect contingencies*, which Module 4’s animals already do. It is detecting *contingencies that selection could not have fixed a response to*, because they change within a lifetime, differ from place to place, or are new to the species.

![One contingency, two routes to a response. Along the upper route, a flavor that predicts sickness comes to produce avoidance across many generations, by differential survival among animals whose wiring differed; the individual animal is unchanged by anything that happens to it. Along the lower route, the same contingency produces avoidance inside a single animal, after a single experience, and that animal is different afterward.](reading_images/fig-two-timescales.svg){#f-two-timescales alt="Two horizontal routes drawn one above the other, both leading from the same box on the left, labeled a flavor is followed by sickness, to the same box on the right, labeled the flavor is avoided. The upper route is long and divided into many small segments, each labeled as one generation, with small animal figures above it whose numbers change from segment to segment; it is labeled selection across generations. The lower route is a single short arrow spanning one segment labeled one lifetime, with a single animal figure above it drawn once before and once after; it is labeled learning within a lifetime. A bracket at the right indicates that both routes end in the same behavior."}

### §5.1.4 — What an Acquired Response Requires

Copper avoidance is not something a worm needs to learn. A worm reared without ever meeting copper avoids it on first contact. Whatever the wiring reflects about copper, it reflects because of what happened to the worm’s ancestors, and not because of anything that happened to the worm.

An animal that can *acquire* a new avoidance during its own life needs something a fixed-weight nervous system does not have. It needs a part of itself that changes due to experiences the animal has, and that thereby comes to reflect something about the world. That is what the fixed-weight picture leaves out, and it is what we add this week. **Learning** is a lasting change in what an animal does, produced by experience and resting on an internal state that experience can modify. **Plasticity** is the property of nervous tissue that makes such a state possible. It is the capacity of a connection, or a cell, to undergo a lasting change as a consequence of activity.

It is tempting to say that the earlier state was *wrong*, that the animal’s initial weights were a mismatch to what the weights *should be*. But that’s actually not a correct way to think about it. The world can change while a connection does not, and nothing anywhere in the animal marks the difference. An animal in that condition is still learning, by any reasonable use of the word. Whether a mismatch can drive its own correction is a further question, and we take it up in §5.2.

In the next four sections we take up the first of the two questions, what there is to learn. We work through four relationships an animal might pick up, each asking more of it than the one before.

### §5.1.5 — Tier One: Changing the Response to Something That Keeps Happening

The simplest thing an animal can do with experience is change how strongly it responds to something it has experienced before. **Habituation** is a decline in a response to a stimulus that has been repeated without consequence. A sea anemone, touched repeatedly by a drifting frond, will stop withdrawing. Habituation is *not* fatigue. Present a novel stimulus, and the full response returns immediately. Nothing is used up. Something has been adjusted. **Sensitization** is habituation’s partner, a rise in responsiveness to stimuli generally after something significant has happened. A sea anemone that has just been attacked, withdraws from almost anything.

Both of those count as learning, by the definition we gave in §5.1.4: a lasting change in what an animal does, produced by experience. What tier one requires is very basic. There is no link between two events here, no outcome to compare against, nothing that could be called a target response. There is only a running count of how often something has occurred, and whether anything ever followed it. What habituation and sensitization do for the animal is nevertheless real. Attention and energy are both finite. An animal that keeps responding to a stimulus that is never followed by anything, is spending energy and attention on a non-event.

One further benefit of tier one can be shown in an animal already familiar to us. A cnidarian’s stinging cells fire once and are spent. A brush against the body wall might be prey or might be debris. Sensitization gates their firing, so that several independent kinds of evidence for prey must arrive together before one cell is committed. Ken Cheng, who has reviewed this literature systematically, notes that this behaves just like an AND gate. A touch alone does not fire the cell. A chemical trace of prey alone does not fire it either. Only both together do.

### §5.1.6 — Tier Two: Linking Two Things That Occur Together

Tier two adds an important requirement to tier one: a link between two states, rather than a change in one state. An animal that can form such a link can do two things it could not do before. It can act before an event, rather than needing to wait for it. And it can treat a novel combination of cues as a single thing, when no cue on its own would identify it. In both space and time, something other than the important event can become as meaningful to the animal as the event itself.

The combination is the simpler of the two, because nothing has to be carried forward in time. A patch of ground may be safe only when a particular smell and a particular texture underfoot occur together. Neither cue settling anything on its own, and this particular combination wasn’t present in the organism’s evolutionary history. What such a link needs is that the combination be distinguishable from its parts, so that the animal’s response to both together is not simply the sum of its responses to each alone. Module 4’s threshold units did that, and so does the cnidarian’s stinging cell — but in both, the combination was fixed in advance. Tier two is the capacity to acquire a new association.

A link that runs across time is harder to form. When the cue arrives, the thing it predicts has not happened yet. When the outcome arrives, the predictive cue is over. So something in the animal has to carry the first event forward until the second one arrives, and the two have to meet somewhere.

Order matters as well, though not in the way it might first seem. A rustle in the grass that comes before a predator supports acting in advance. A carcass that comes after a predator supports something different — avoiding an area where a predator likes to feed. Both links are useful, and neither does the other’s job. But associations in time require recording which event came first, so it can be used to distinguish something that is coming, from something that has been.

The nematodes we have been studying can form these kinds of associations. When they are exposed to a particular food odor, together with a chemical that makes them ill, they will afterward steer away from that odor. This is an association between two things, neither of which nematodes’ wiring came hard-wired to relate. But with association-based abilities, a worm can learn to relate that a particular odor goes with illness, without necessarily needing to associate either of those with the act of eating itself. Its own actions are not critical to the association, just reliable dependencies in its world. Learning of this kind, where one thing comes to be treated as a sign of another, is what psychologists call **classical conditioning**, or *Pavlovian conditioning*.

The classical conditioning tradition has a vocabulary of four terms, and it is easiest to see in a reflex. A puff of air to the eye makes it blink, in an animal that has never been trained. The puff is an **unconditioned stimulus**, and the blink an **unconditioned response**. Sound a tone just before the puff, over and over, and the tone alone will come to make the eye blink. The tone is now a **conditioned stimulus**, and the blink it produces a **conditioned response**. What has changed is which event sets the reflex off, and nothing about what the animal chooses to do. Our worm example has the same shape: a toxic chemical is the unconditioned stimulus and the malaise it causes the unconditioned response, while the odor is the conditioned stimulus and steering away from it the conditioned response. Steering is a movement rather than a reflex, which is worth noticing but does not change the structure. What gets learned in either case is a link between two events. The response is how we can tell the link is there, and not one of the two things being linked.

### §5.1.7 — Tier Three: Linking What Happened to the Animal’s Own Actions

Tier three adds two more requirements.

First, the animal must distinguish *this happened*, a tier two ability, from *this happened after I acted*. That distinction has no meaning for a purely sensory learner. A tier two animal registers only that two events are associated, without distinguishing that its own actions were involved. Telling those two apart requires that the animal can incorporate what it just did as a fact of its own.

The difference is clearest where the same thing can happen either way. A branch overhead dips, and fruit comes down. If it dipped because the wind moved it, the animal has learned something about wind. If it dipped because the animal shook the trunk, the animal has learned something it can do again. Nothing in the falling fruit distinguishes the two cases. The distinction is available only to an animal that has its own shaking alongside the fruit, and not just the fruit.

Second, in order for this information about its own actions to be useful, the animal must keep information about its own different actions distinct. Something inside it must be able to change for one action, without changing for others. If it cannot do this, then nothing it learns about one action could guide its future choice between actions.

An animal usually has more than one thing it could try. Faced with a log across its path, it could climb over, dig under, or go around. Each of the three is followed by a consequence. A learner that pooled those outcomes together would come away knowing that logs are an obstruction, but would be no wiser about the best way to get around one. Learning of this kind, where what the animal did becomes one of the linked terms, is what psychologists call **operant conditioning**, or *instrumental conditioning*.

The operant conditioning tradition has a vocabulary too. The situation the animal is in is the *discriminative stimulus*. What the animal does is the *response*. What follows is the *consequence*. A consequence that makes the response more likely in that situation afterward is a **reinforcer**, and one that makes it less likely is a **punisher**. Edward Thorndike stated the principle in 1911 as the *law of effect*, and B. F. Skinner later coined *operant* for behavior that operates on the environment, rather than being drawn out of the animal by a stimulus. Skinner’s word is apt for what tier three adds, since what the animal did is now inside the link.

### §5.1.8 — Tier Four: Bridging a Delay

Tier four is the hardest problem to solve, and it is the one that changes the most about what an animal can do. Cooking a meal, studying across a semester, practicing an instrument: the outcome arrives long after the actions that produced it, and a great many irrelevant actions happened in between.

The new requirement in tier four is a record of what was done, persisting until the outcome arrives. Without one, there is nothing left to modify by the time the news comes in. The second half of the problem is just as hard. Even given the record, the credit has to be assigned appropriately to all the actions that were involved. For a tasty meal, stirring mattered, but scratching an itch halfway through did not. Both are actions that preceded the rewarding event. That is **credit assignment**, and it is the problem that bedeviled the first machines built to learn, as we will see in §5.2.

### §5.1.9 — What There Is to Learn From

There is one thing the four tiers do not settle. They say what information has to be in the link, and how far apart in time its terms can lie. They say nothing about what information the animal’s situation makes available, when something has to change. Sometimes that information is nothing but what co-occurred.  Sometimes it is the next thing that happened. Sometimes that information might be the way the animal *should have* responded, from some source that knew the answer. And sometimes that information is a verdict on whether the outcome was good or bad.

So there are two separate questions here, and they cross rather than stack. The first is about the relationship an animal has to pick up: one thing that keeps happening, two things that go together, an action and what followed it, or terms separated by a long delay. The four tiers answer that question. The second is about what the animal has to go on while it does: nothing but co-occurrence, the next thing that happens, an answer from a source that already holds it, or a verdict on how things went. What there is to learn, and what there is to learn from. The tiers are ordered, one on top of another. The four things the animal can learn from are not ordered. An animal with a teacher does not thereby have a verdict on good or bad, and an animal with a verdict on good or bad does not thereby have a teacher.

Good and bad, in particular, are not what any of the four tiers add. Module 4’s animals already tag the affect of what reaches them. An animal can learn that turning left in this burrow is followed by a draft of cold air, with none of that being good or bad. Learning instead that turning left went well, or went better than expected, is a different thing altogether. For now, we keep the two apart. In §5.2 we divide the kinds of learning by what there is to learn from, rather than by the tiers.

### §5.1.10 — Do Animals Without Brains Learn? And How Do We Know?

There is a clean adaptive argument that says tier one — habituation and sensitization — is all the learning that non-bilaterians need to do. A sessile filter-feeder has little use for associations. It does not choose between patches. It does not pursue. And the things that happen to it are largely things it cannot act on in advance. So a jellyfish or an anemone should have habituation and sensitization, and nothing more, despite having had hundreds of millions of years in which to acquire more. The argument is a good one, and has been stated confidently in some recent literature.

The argument that non-bilaterians only need tier one learning also makes a prediction, a prediction that appears to be failing in more recent research. Habituation is amply documented in hydras, jellyfish and sea anemones. And sensitization has been studied in detail in anemones. Their ability to do tier one learning is not in dispute at all. But with regard to tier two and tier three — classical and operant conditioning — the picture has changed quickly and recently.

Classical conditioning in a sea anemone rested for decades on one well-controlled study from 1975 and two weaker ones. In 2023 it rested on two, because a group working on *Nematostella vectensis* — an animal we met in Module 4 — paired a light with a shock across twenty training rounds. They found considerably more retraction to the light alone in animals that had experienced the shock-light pairing than in animals that had not, including animals given the light alone and animals given the shock alone. That same year, a study of the box jellyfish *Tripedalia cystophora* reported operant conditioning. The animals learned to stop bumping into obstacles, and the effect disappeared when the obstacles were made easy to see, and again when the visual cue was removed. A cluster of about a thousand neurons, cut away from the rest of the animal, was conditioned on its own in a dish.

Three lessons follow, and all three use tools Module 2 already gave us. First, this is what a well-formed adaptive argument looks like when it is tested rather than admired. The adaptive argument predicted an absence. The absence is not holding up, and Module 2’s warning about adaptationist stories told after the fact is exactly the warning being vindicated. Second, Morgan’s Canon can be applied asymmetrically, and here it has been. Were the same suite of controls run in an insect or a tardigrade, nobody would hesitate. What resists the conclusion in a cnidarian is a prior assumption about what a brainless animal ought to be able to do, doing work *the data* is supposed to do. And third, if cnidarians do learn, a further interesting question opens. Cnidaria is the sister group to Bilateria, so the capacity is either ancestral to all nervous systems, or it arrived twice — homology or convergent evolution.

One point of fairness. The confident adaptive argument appeared in 2023, likely written prior to when the author could have known about the contradicting results. This is a field moving faster than publication can keep up with. The current verdict is that on the question of existence of tier 2 and 3 learning in non-bilaterians, the evidence is positive and the burden now sits with the skeptics. But the question is still open [](#t-cnidarian-evidence).

<!-- pin: t-cnidarian-evidence -->

: What has and has not been shown, by kind of learning and group of animals, following Cheng’s systematic review and the two 2023 results that postdate it. The last column names what would settle the cell, which is the more useful thing to know about an open question. {#t-cnidarian-evidence}

| Kind of learning | Hydras | Jellyfish | Sea anemones | What would settle the open cells |
|---|---|---|---|---|
| Habituation (tier one) | Amply shown | Amply shown | Amply shown | Nothing outstanding |
| Sensitization (tier one) | A hint only | No studies | Shown, with a neurobiological literature | Straightforward replication in the other two groups |
| Classical conditioning (tier two) | Not studied | Not studied | Two well-controlled demonstrations, one from 1975 and one from 2023 | Independent replication in a second laboratory; a retention test beyond ten minutes |
| Operant conditioning (tier three) | Not studied | One demonstration, 2023, with an isolated ganglion conditioned separately | Suggestive only, on weak controls | Replication in a second species; an acquisition curve and an extinction test |

### §5.1.11 — Most of Learning Is Older Than the Vertebrate

Putting the tiers against the animal tree gives a result that is not the expected one [](#f-tier-timeline). Tiers one and two are old and widespread. They are present in animals with a few hundred neurons, they are present throughout the bilaterians, and on current evidence tier one extends below the bilaterians entirely.

Tier three is documented across the bilaterians. Below them the evidence thins to a single 2023 result in one box jellyfish. Tier four is the one that arrives late, and it arrives with vertebrates.

So the headline is not that learning is a vertebrate invention. Most of learning is considerably older than the vertebrate, and what the vertebrate adds is the ability to bridge a delay. That is a claim about when particular capacities appear, and not a ranking of animals by intelligence; Module 2’s warning about reading the tree as a ladder applies here as much as anywhere.

![The four tiers of learning placed against the animal tree in deep time. Tier one appears earliest and is found in every group shown. Tier two is present throughout the bilaterians. Tier three and tier four are marked with bands rather than points, because the evidence for when each appears is contested; the band for tier three is the widest, and the tier-two mark for non-bilaterians is drawn as an open mark because it rests on a small number of studies. Every surviving lineage is drawn as a line reaching the present.](reading_images/fig-tier-timeline.svg){#f-tier-timeline alt="A horizontal time axis running from about 700 million years ago on the left to the present on the right. Four labeled lineage lines run from their first accepted appearance to arrowheads at the right-hand edge: sponges, cnidarians, invertebrate bilaterians, and vertebrates. Above the lines, four rows of marks indicate the tiers of learning. The tier one row carries filled marks on cnidarians and both bilaterian lines. The tier two row carries filled marks on both bilaterian lines and an open mark on cnidarians. The tier three row carries filled marks on vertebrates and invertebrate bilaterians, and an open mark on cnidarians. The tier four row carries a filled mark on vertebrates only, with a narrower hatched band before it. A legend distinguishes filled marks for well-supported evidence, open marks for limited evidence, and hatched bands for contested timing."}

### §5.1.12 — Problems That Come with Learning

Three problems come with the capacity to learn. Two belong to an animal learning which of its actions lead to good outcomes. The third belongs to every learner, whatever it is learning.

The first is **exploration versus exploitation**. Should the animal take the option already known to be decent, or sample one that might be better and might be worse? Every attempt at the uncertain option is an attempt not made at the reliable one. An animal that never tries the uncertain one is stuck with the first adequate option it found. There is no setting of this that is right in general, there is always a trade-off at work.

The second is how far ahead to care. An outcome arriving in ten seconds and an identical outcome arriving in ten days cannot count equally, or nothing would ever favor acting now over acting later. Some rate at which distant outcomes count for less is unavoidable, and in §5.2 we give it a name and a number.

The third comes with learning of any kind. Change a connection with every experience, and nothing from yesterday survives into this afternoon. But if a connection never changes, nothing is ever learned. Every learner needs a setting somewhere between the two extremes. Learners probably need a schedule that moves the setting over a lifetime. It is useful to be plastic or malleable early, when little of the world has been encountered. And it is useful to be more fixed later, when most of the world has been encountered already. That is **stability versus plasticity**, and it is a genuine trade-off in the Module 4 sense: two properties that cannot both be had at once. We take it up in §5.3.

What is left, then, is the mechanical question. What rule could move a weight so as to meet any of this? The candidates differ mainly in what they make the change depend on.

## §5.2 — Algorithmic: Rules That Change a Weight

### §5.2.1 — Hebb’s Rule

A weight has to change, and something inside the animal has to do the changing. Whatever does it can use only the information available where the connection is, at that moment. That constraint does most of the work in what we describe below. A rule that needs nothing but the two cells a connection joins is one kind of answer. A rule that needs a report from somewhere else in the animal is another kind, and a great deal harder to arrange.

One of the oldest proposals for how this could work is also one of the simplest. Donald Hebb stated it in 1949: when one cell repeatedly takes part in triggering the firing of another, some growth process takes place such that the first becomes more effective at triggering the firing of the second. Or as it is sometimes shorthanded, Hebb’s rule is “neurons that fire together, wire together”. This rule intuitively captures the idea that if two neurons both tend to fire at the same time, learning should come to *make* one fire if the other is firing. Two correlated cues should come to elicit each other’s neural patterns of firing.

Writing down Hebb’s rule formally means writing down a change in one of the weights, the b-values, that we used in Module 3 to model a neuron. Take the connection running from one input cell into the receiving cell. That connection’s weight is *b₁*, the input cell’s firing rate is *x₁*, and the receiving cell’s own rate is *y*. **Hebb’s rule** makes the change in *b₁* proportional to how active the two cells were at the same time:

> *Δb₁ = ηx₁y*

The Δ is the usual way of writing *the change in*. The remaining term, *η*, is the **learning rate**: a small number that sets how much of the maximum possible change is made on any one occasion (the effect of different values of the learning rate will be explained shortly). So the rule says to multiply the sending cell’s rate by the receiving cell’s rate, scale that product down by the learning rate, and add the result to the weight.

Let us flesh it out with some examples and details. Start with the learning rate set to a value of 1. This means that the change in the connection strength between two neurons will be exactly the product of their firing rates.

Consider some possible values we might see for the firing rates of *x₁* and *y*. If both firing rates are large (both firing rapidly), the change in weights will be positive and large. This reflects that since *x₁* and *y* were firing rapidly at the same time, *y*’s firing rate should come to reflect *x₁*’s firing rate, which is done by making *b₁* much more positive. For example, if *η*=1, *x₁*=40 and *y*=40, then Δ*b₁* will equal 1600, (1 * 40 * 40). If one or especially both of the neurons are firing at a lower rate, the change will be much smaller. For example, if *η*=1, *x₁*=40 and *y*=2, then Δ*b₁* will equal 80, (1 * 40 * 2). And if *η*=1, *x₁*=2 and *y*=2, Δ*b₁* will equal 4. The change is still a positive number, reflecting *x₁* becoming more excitatory for *y*, but by a smaller amount. The two neurons are still correlated, but less so, and so the change shouldn’t be as big.

Now change the learning rate and leave everything else alone. With *η*=0.01, *x₁*=40 and *y*=40, the product of the two firing rates is still 1600, but Δ*b₁* is 16 (1600 * 0.01). The same occasion moves the weight by a hundredth of what it moved before. Nothing about the two neurons is different. What is different is how much a single occasion is allowed to matter, and that is the whole job of the learning rate. At *η*=1, two cells that happen to fire together once, for reasons that will never recur, move the weight as far as a hundred ordinary occasions would at *η*=0.01. At the lower rate a single occasion barely registers, and *b₁* only becomes large if *x₁* and *y* fire rapidly together again and again. Being slow is what allows a low learning rate to ignore coincidences. Being fast is what makes a high one liable to treat an accident as a rule. The trade-off between stability and plasticity from §5.1.12 turns out, for a rule like this one, to be a single number.

Working through those numbers may raise a question the rule cannot answer. Firing rates are never negative, and neither is the learning rate, so Δ*b₁* is never negative either. Every occasion makes the weight grow, by either a small or larger amount. A connection running Hebb’s rule can grow without limit and can never shrink, and nothing in it could ever arrive at an inhibitory connection of −3 like we saw in Module 3. Negative weights are not the difficulty, since Module 3 already had one. Arriving at a negative weight *by learning* is the difficulty, and the basic form of Hebb’s rule has no way to do it. The first rule in this chapter that can subtract arrives in §5.2.5, and the physical account of what weakens a connection is in §5.3.

Setting that issue aside for now, every quantity in that rule is present locally at that exact connection between the two neurons. The sending cell’s activity is arriving there. The receiving cell’s activity is right there as well. Nothing else is consulted. No signal reports whether anything good happened, and no signal states what the receiving cell should have done instead. A connection running Hebb’s rule strengthens because two cells were active together, and for no other reason.

### §5.2.2 — Coincidence Without a Goal

Put a rule like Hebb’s rule into a nervous system whose cells respond to different things, and the wiring comes to reflect which things in the world go together. A rat hears a tone a moment before food arrives at a tray. The cells responding to the tone and the cells responding to food are active at nearly the same moment, over and over. The connection between them strengthens, and after enough repetitions the tone alone drives the food-related cells hard enough to send the rat to the tray. There is nothing that supervised that. Nothing was labeled in advance by any kind of teacher. The tone and the food kept occurring together, and a rule that responds to things occurring together did the rest.

It is hard to describe that outcome without ascribing something to it that is not there. The wiring ends up fitted to the world. So the temptation is to say that the rat worked out what the tone means, or that the neurons learned the relationship. But nothing in Hebb’s rule represents a goal. Nothing in it registers being wrong, or being right. There is no comparison anywhere in the rule, because there is nothing to compare against.

That fact is one we have encountered before. In Module 2, we discussed how adaptation makes organisms look designed, without anyone designing them. This is because adaptive fit is what is left over after differential survival, rather than something any organism was aiming at. Hebbian learning has the same structure, one level down and on a far shorter timescale. The regularity in the wiring is what is left over after repeated co-activity, rather than something the organism or the wiring was trying to accomplish. Both senses of *adapt* work the same way. There is a process with no foresight, that leaves behind a result that *looks like* foresight.

An important fact about Hebb’s rule is that it has no term for good or bad. An animal that *does* have a notion of good or bad can still make use of a rule that does not. When a cue and a good outcome occur together, a Hebbian link between them forms, and that link will afterward make the animal more likely to do what it did the last time the cue was present. The rule strengthens the connection. Something else can bias which links are considered good, bad, and by how much. Those are two separable jobs, and the rules that follow differ mainly in how they handle the second.

### §5.2.3 — Three Things Coincidence Cannot Do

Hebb’s rule has three limitations, and each one blocks something we said a learner needs to do in §5.1 [](#f-hebb-fails).

The first is that Hebb’s rule is indifferent to outcomes. Whatever was active together is wired together, whether the pairing mattered or merely happened. A rat hears a tone a moment before food, and the link forms. That same rat hears the ventilation fan a moment before food several hundred times as well, and that link forms too. Neither the rule nor anything else in the rat marks one of those as the useful one. There is no term anywhere in *Δb₁ = ηx₁y* referring to how things turned out.

The second is that Hebb’s rule cannot bridge a delay. Move the food to ten seconds after the tone, and the two populations of cells are no longer active at the same moment. The product of their activities is near zero at every instant, so there is nothing for the rule to multiply, and nothing to strengthen. Hebb’s rule works on simultaneity, and a great deal of what an animal needs to learn is not simultaneous.

The third is that Hebb’s rule cannot apportion credit across a sequence. Picture a rat in a chamber, with a lever on one wall, and a small opening on another wall where food is delivered. Pressing the lever is what causes a food pellet to drop into that opening, a moment later. The rat then has to cross the chamber and put its nose into the opening to eat. Pressing the lever is the action that mattered. Putting its nose into the opening is the action that happened last. If learning only strengthens what was active when the food arrived, the lever press will be missed entirely, because the lever press was over by then. If learning strengthens everything active in the preceding minute, then incidental grooming and sniffing along the way will be strengthened just as much as the lever press. That is the credit assignment problem we described in §5.1.8, creating a problem for Hebb’s learning rule.

![Three cases in which a coincidence rule fails, drawn as three timelines sharing one time axis. In the first, two events coincide but one of them is harmless and irrelevant, and the rule strengthens both links equally. In the second, the two events are separated by ten seconds, so no moment contains both. In the third, a sequence of several actions precedes a single outcome, and the rule has no way to distinguish the action that mattered from the ones that merely happened along the way.](reading_images/fig-hebb-fails.svg){#f-hebb-fails alt="Three stacked timelines, each running left to right with a shared time axis beneath. The first timeline is labeled indifferent to outcome and shows two pairs of overlapping event marks, one pair labeled tone and food and the other labeled fan and food, with an identical strengthening arrow drawn under each pair. The second is labeled cannot bridge a delay and shows a tone mark and a food mark separated by a gap labeled ten seconds, with a dashed arrow between them crossed out. The third is labeled cannot apportion credit and shows four action marks labeled lever press, grooming, sniffing and tray approach followed by a single food mark, with arrows of equal weight drawn from every action to the food."}

### §5.2.4 — Blocking: Pairing Is Not the Point

One experiment demonstrates the first of those three limitations, that Hebb’s rule is indifferent to outcomes. Imagine a rat that is trained that a tone reliably predicts food. Then a light is added, so that tone and light arrive together, and the food still follows. That continues for many trials. Light and food are now perfectly paired. Every light is followed by a food delivery, and no food arrives without one. But if we test the rat’s response to the light on its own afterward, without the tone, the rat will do almost nothing. It never learned that the light signaled food.

A coincidence rule like Hebb’s rule does not predict and cannot explain this result. Light and food were active together as reliably as any two things in the experiment, so a rule strengthening what co-occurs would have strengthened that connection. What kept the connection from forming was that the food was already predicted by the time the light arrived. Nothing about the light was news. The name for this result is **blocking**: learning tracks what was not already predicted, rather than what merely co-occurred. Blocking is well documented in mammals. An apparent demonstration in honeybees did not survive a later replication attempt, so whether any invertebrate shows it is unsettled.

### §5.2.5 — Error-Driven Learning, Discovered Twice

Explaining why blocking occurred was a major challenge for psychologists. Robert Rescorla and Allan Wagner proposed the fix in 1972. Let an association have a strength, *V*, standing for how strongly the cue currently predicts the outcome. Let *λ* stand for the strength the association should eventually reach with this outcome, so that a large food delivery eventually supports a large value, and no food supports none. Then, the change in association strength on a trial is proportional to the gap between the two:

> *ΔV = αβ(λ − V)*

The two remaining terms, *α* and *β*, are rate terms belonging to the cue and to the outcome. Between them, they do the work *η* (the learning rate) did in Hebb’s rule. The gap itself, *λ* − *V*, is the **prediction error**. Calling that gap a prediction error is worth unpacking, because *λ* is the term that needs it. Think of *λ* as the strength the association would eventually reach if the animal were trained with this outcome over and over without end. A large food delivery would settle at a strong association, a small delivery at a weak one, and no food at all at nothing. So *λ* is a statement about the outcome that actually arrived, written on the same scale as *V*, which is a statement about what the animal expected. Two numbers on the same scale can be subtracted, and what arrived minus what was expected is what a prediction error is. When the two match, the animal got what it expected, and nothing changes.

Blocking falls out immediately, and numbers show it better than words do. Set *λ* to 1, so that the food delivery can support an association at full strength. On the very first tone trial *V* is 0, the gap is the whole of *λ*, and the change is as large as the rate terms allow. After many trials the tone has driven *V* to something like 0.95, and the gap is 0.05. Whatever the rate terms are, only a twentieth as much change is available on that trial as was available on the first — and that holds for every cue present, including the light that has just been added. The light is not ignored because the rat decided to ignore it. There is almost nothing left to learn while the outcome is already predicted.

Twelve years earlier, and in a different world, Bernard Widrow and Marcian Hoff were building an adaptive electronic circuit. Their problem was to make an output match a desired output. They called the desired output *t*, for target, and the output the circuit actually produced *o*. Their rule was to change each weight in proportion to the difference between those two, scaled by the input that weight carries:

> *Δb₁ = η(t − o)x₁*

They called this the **delta rule**, delta for the difference. Compared to Hebb’s rule, the delta rule differs in exactly one place. Hebb multiplies the input rate by the receiving cell’s own activity. The delta rule multiplies it by how wrong the receiving cell was.

Now set Rescorla and Wagner’s rule beside the delta rule, and the correspondence is exact [](#f-two-equations). The outcome the world delivered, *λ*, is the target *t*. The strength already present, *V*, is the output *o*, which is what the animal currently produces by way of expectation. The rate terms *α* and *β* do the work of the learning rate *η*. And the input term *x₁* is either one or zero on a conditioning trial, depending on whether the cue was present, which is why it does not appear in the animal version at all. One group was explaining a rat, and the other was building a circuit. Neither knew of the other, and the same algorithm was written down twice. Module 1’s point about multiple realizability arrives here in a form we can check term by term. The procedure is the same object whether it is carried out in a rat or in a circuit, and the description that matters at the algorithmic level mentions neither.

In §5.1.4 we left a question open. Can a mismatch between what an animal’s weights currently hold, and what the world delivers, drive its own correction? The difference between Hebb’s rule and the delta rule can help us answer this question. In §5.2.2 we emphasized that Hebbian wiring is *not* aiming at any outcome, because nothing in Hebb’s rule holds an expectation, and nothing in it registers a miss. But in the delta rule, there *is* an expectation, *V*, and a delivered outcome, *λ*. The computed difference between them is the thing driving the change. So *the system was wrong and corrected itself* is not a story laid over the mechanism. It is a description of the mechanism. That is the lesson worth carrying forward. Language about goals and errors earns its place exactly where something in the mechanism actually explicitly involves goals and errors.

There is a general method behind the delta rule. Measure how wrong the output is. Work out which direction each weight would have to move to make the output less wrong. Move the weights a small step in that direction. That is **gradient descent**. The word *gradient* means slope. 

Picture a graph with the value of one weight along the horizontal axis, and how wrong the output is on the vertical axis. Changing that weight traces out a curve, and the lowest point on the curve is where the output is least wrong. The gradient at any point on that curve is how steeply the curve is rising or falling there. This tells us both which direction is downhill, and how large a step is worth taking. Going downhill on that curve is the *descent*. And for a single unit, gradient descent is precisely the delta rule. What happens when there is more than one layer of weights between input and output is a much harder problem, which we will address in Module 7.

A picture of this kind can be drawn over any process that ends up extremizing something. In fact, biologists draw one for natural selection — the *adaptive landscape*, with fitness plotted upward, so that populations are depicted climbing toward greater fitness, where the delta rule’s weights descend. Drawing the picture is not what makes the delta rule different. What makes it different is that the delta rule computes the slope and then moves along it, while nothing in a population computes anything at all. The landscape is in the biologist’s description, and the climb is what differential survival leaves behind.

![Rescorla and Wagner’s rule and the delta rule written one above the other, with the terms that correspond joined. The outcome the world delivers corresponds to the target; the association strength already present corresponds to the circuit’s current output; the two rate terms together correspond to the learning rate. The input term is written explicitly in the delta rule and is implicit in the animal version, where a cue is either present or absent.](reading_images/fig-two-equations.svg){#f-two-equations alt="Two equations written on separate lines, one above the other, each with its terms labeled beneath. The upper line reads delta V equals alpha beta times the quantity lambda minus V, labeled Rescorla and Wagner, 1972, with lambda annotated as the strength the outcome supports and V annotated as the strength already present. The lower line reads delta b sub 1 equals eta times the quantity t minus o, times x sub 1, labeled Widrow and Hoff, 1960, with t annotated as target, o as actual output and x sub 1 as input. Curved lines connect lambda to t, V to o, and alpha beta to eta. A brace at the right of both lines marks the parenthesized difference in each as the prediction error."}

### §5.2.6 — Where the Target Comes From

The delta rule needs a target. Something has to state what the output should have been, on this occasion, for this input. That is a nontrivial piece of information to have lying around. The obvious source for it is a teacher, meaning something that already holds the right answer, and is in a position to hand it over. Nervous systems are not well supplied with teachers. Very little of what an animal needs to get right arrives with an answer attached.

But there is a second source, and it requires nothing that is not already happening. Let the target be the next thing that actually occurs. A system that can produce a prediction about its upcoming input, and hold that prediction until the input arrives, and then compare the two, has manufactured its own target out of the world. No teacher had to label anything, and nothing had to know the answer in advance. The rule is the same rule, and only the supplier of the target has changed.

Learning of that kind is **prediction learning**. It is an answer to the second of the two questions from §5.1.9, what there is to learn from. It differs from a teacher in one respect only: where the target comes from. But that difference in source earns it a name of its own, by the standard we set at the start of this module, because it changes what a solution must have. The prediction has to be generated before the input arrives, and held until it does. None of the other rules require anything to be held.

Hebb’s rule is not a case of this. It is true that *b₁* can be described as a prediction. But nothing in Hebb’s rule is generated before the input arrives, nothing is held, and no difference between a predicted and observed value is computed. The change is a product of two quantities, the presynaptic and postsynaptic firing rates, present at the same moment. Describing *b₁* as a prediction is *our* description, in just the way the adaptive landscape is the biologist’s.

In contrast to Hebb’s rule, Rescorla and Wagner’s rule has been an instance of prediction learning all along. The association predicts food, a moment passes, and the world supplies the answer: food is either present or absent. The same shape turns up well away from conditioning. A moving edge crossing the visual field is somewhere slightly different a moment later. And where the edge actually turns up is a target for where it was predicted to turn up, requiring no explicit teacher and no labeling. This is also how large language models like ChatGPT and Claude are trained, which we take up in Module 13. The next word is a target that text supplies about itself, which is why such a model can be trained on text nobody annotated.

### §5.2.7 — Four Kinds of Learning, and the Order They Come In

The rules now in hand differ in exactly one respect, and it is the one named in §5.1.9: what information has to be present for a weight to move [](#t-teaching-signals).

Hebbian learning needs the two cells a connection joins, and nothing else. Supervised learning needs a statement of what the output should have been, from a source that already holds it. Prediction learning needs the next input, which the world delivers unasked. Reinforcement learning needs one number reporting how things went, attached to no particular output and carrying no indication of what would have worked instead. Those are four different situations an animal can be in, and nothing makes them a sequence. An animal with a teacher does not thereby have a verdict on good and bad, and an animal with a verdict does not thereby have a teacher.

There are terms from computer science and machine learning that are used here. Hebbian learning is *unsupervised learning*, where there is no teacher because there is no target at all, just the learning of correlated structure in the input. Prediction learning is *self-supervised*, the target having been manufactured out of the input stream itself. Supervised learning is the teacher case. Reinforcement learning is the verdict case. The last three are often grouped together as learning from a teaching signal, which is fair enough as long as it stays clear how different those three signals are from one another.

Now rank the four by how hard the required information is to arrange inside an animal, and the order comes out backward from the one most readers expect. Hebbian learning requires nothing that is not already at the connection. Prediction learning requires nothing the world is not already delivering. Reinforcement learning requires one number, and a body can generate such numbers easily: a full stomach, a rise in blood sugar, or a pain signal. A teacher is the hardest of the four to arrange, by a wide margin, because something inside the animal would have to already hold the correct output and be in a position to deliver it to the particular connections that produced the wrong one. Anyone who has learned about machine learning was likely introduced to supervised learning first, and most often, and will expect it to be the simple case. In a nervous system it is the exotic one.

<!-- pin: t-teaching-signals -->

: The four kinds of learning, sorted by what has to be available for a weight to move. The fourth column is the one that inverts the expected ranking. {#t-teaching-signals}

| Kind of learning | What the weight change depends on | Where that information comes from | How readily a nervous system could supply it | What it can learn | What it cannot |
|---|---|---|---|---|---|
| Hebbian (*unsupervised*) | The activity of the two cells a connection joins | Nowhere else; both quantities are already at the connection | Trivially — nothing has to be arranged | Which things in the world go together | Anything about whether the result was any good |
| Prediction (*self-supervised*) | The difference between what was predicted and what then arrived | The world, which delivers the answer a moment later | Easily, provided a prediction can be held until the input arrives | Structure in how one moment follows another | Anything the world does not eventually reveal |
| Supervised | The difference between the output produced and the output specified | A teacher that already holds the correct answer | With difficulty; the answer has to exist somewhere inside the animal already | Any mapping the teacher can specify, quickly and precisely | Anything for which no answer is available |
| Reinforcement | One number reporting how things went | A verdict generated by the body or by the outcome itself | Readily — one broadcast quantity is enough | Which actions lead to good outcomes | What should have been done instead, directly |

### §5.2.8 — Bridging the Delay, and Assigning the Credit

Error-driven learning repairs the first of Hebb’s three limitations, its indifference to outcomes. The other two — bridging a delay, and apportioning credit across a sequence of actions — are both problems about time. An error term on its own does not have a way to reach across time. Blocking showed that a summed error can divide credit among cues that are present together. But nothing in it divides credit among things that happened at different moments. Computing an error requires something to compare against, and at the moment an animal acts there is nothing yet to compare against. By the time the outcome arrives, the action is usually long over. Tier four requires a record of what was done that persists until the news comes in, and a way of apportioning that news across everything the record contains.

Start with the simpler half, which is how much a delayed outcome should count for at all. In §5.1.12, we said that an outcome arriving in ten days cannot count as much as the same outcome arriving in ten seconds. The usual way of writing that down is **discounting**: a factor *γ*, a little below one, applied once for every step of delay between now and the outcome. At *γ* = 0.9, an outcome ten steps away counts for about a third of the same outcome delivered immediately. One that is a hundred steps away counts for almost nothing at all. Raise *γ*, and distant outcomes weigh more heavily. Lower it, and behavior is governed by what is close at hand.

The harder half, apportioning credit across a sequence of actions, has a solution that looks at first like cheating. Instead of waiting for the true outcome and comparing against that, compare each outcome estimate against the next outcome estimate the system itself produces. For example, suppose the animal holds an estimate of how well things are going, and revises it moment by moment. When an estimate at one moment is followed by a better estimate at the next moment, the difference between the two can itself be treated as an error. That error can move a weight right then, with nothing left to wait for. That is **bootstrapping**, and the family of rules built on it is **temporal-difference learning**. Over repeated trials, the effect is that value seeps backward along the chain. The moment just before the food carries it first, then the moment before that, and eventually the lever press at the start [](#f-td-chain).

Treating an unreliable estimate as a target sounds like a recipe for learning nothing. But it works, because the chain is anchored. Something real happens at the end of it, and every estimate in the chain is connected, through however many links, to that.

This settles something we left open in §5.2.3. A simple coincidence rule strengthens everything active before the food, grooming and sniffing included. A rule built on estimates of changes to future outcomes does not. What moves a weight is whether an action changed the estimate of how well things are going, and not whether food eventually arrived. Pressing the lever changes the estimate, because a pellet is on its way that was not on its way before. Grooming does not change it, because the animal is no better placed afterward than it was before. No change in the estimate, no error, and nothing to strengthen.

The animal does not have to know in advance that grooming is irrelevant. Early on its estimates are poor, and grooming may well pick up some credit. What removes it is experience, as the estimate before grooming and the estimate after it converge on the same estimated future value. With discounting in force, grooming does slightly worse than nothing, since it leaves the same outcome one step further away.

Animals do bootstrap. An animal can be trained that a tone predicts a shock, until the tone alone produces fear. Then, if a light is paired with the tone, the light becomes frightening, even if it was never paired with the shock. The only thing available to teach the light was the tone, and the tone was itself nothing more than a learned predictor. A learned prediction has become a teacher in its own right, which is exactly the assumption temporal-difference learning runs on.

Two jobs have been running together in everything described above. Choosing what to do is one. Judging how things are going is the other. They can be separated, and a system can be good at one while it is still poor at the other. In machine learning terminology, the part that judges is the *critic*: it learns to predict how well things will go from here, and its prediction errors are the temporal-difference errors just described. The part that chooses is the *actor*: it holds a **policy**, meaning a mapping from situations to what to do in them, and it adjusts that mapping using the critic’s errors. When things go better than the critic expected, whatever the actor just did becomes more likely in that situation afterward. What the critic learns is **value**, and what the actor learns is behavior, and the arrangement is called an **actor–critic** architecture. Separating the two is a computational insight before it is an algorithm: an animal that cannot yet act well can still be improving at telling good situations from bad ones, and that improvement is not wasted.

Propagating value backward through time still leaves the other half of credit assignment unexplained. Something has to mark which connections were involved, so that a signal arriving later finds the right ones. The algorithmic proposal is a fading mark left on whatever was recently active — an **eligibility trace**. This makes it so that a connection remains a candidate for a while, after it has done its work, and stops being one once enough time has passed. A trace is a proposal about a procedure rather than a claim about tissue. Whether anything in a nervous system behaves like one is a separate question, and a striking answer to it is in §5.3.

![Value propagating backward along a sequence over successive trials. On the first trial only the moment immediately before the reward carries any value. On each later trial the value appears one step earlier in the sequence, until the first action in the chain carries most of it and the reward itself is no longer surprising.](reading_images/fig-td-chain.svg){#f-td-chain alt="A grid of five rows, each row a horizontal sequence of six boxes labeled lever press, approach, tray, nose in, food, and after. Rows are labeled trial one through trial five from top to bottom. Shading indicates the value assigned to each box. In the top row only the box just before food is shaded. In each successive row the shading extends one box further to the left, so that by the bottom row the lever press box is the most heavily shaded and the food box is unshaded. A small arrow beneath each row points leftward, labeled the error moves earlier."}

### §5.2.9 — The Same Rules, Built in Machines

Every one of those rules makes for a plausible explanation of biological behavior. But they also have parallels in the machine world, many of which go back quite a bit further than people expect [](#f-ai-timeline).

Widrow and Hoff’s delta rule was not a theory about animals. It was the learning rule of ADALINE, a physical adaptive circuit built at Stanford in 1960, whose weights were physical resistances the machine itself adjusted. An even earlier attempt is instructive. In 1951 Marvin Minsky and Dean Edmonds built SNARC, forty units of vacuum tubes and clutches meant to model a rat finding its way through a maze. Its rule was to strengthen whatever connections had been recently active whenever the machine did well. That is the right instinct, but it is not enough. With everything recently active strengthened alike, the connections that mattered, and the connections that merely happened to be on, were treated identically. SNARC improved a little and then stopped. The credit assignment problem had reared its head in a machine, sixty years before it had a satisfying answer.

Arthur Samuel’s checkers program, written through the 1950s, learned by comparing each position’s evaluation against the evaluation it arrived at a few moves later, and adjusting the earlier evaluation toward the later. That is temporal-difference learning, running two decades before it had the name. The program came to play checkers better than Samuel did. The same idea reappeared in 1992 in TD-Gammon, which taught itself backgammon to within reach of the best human players, and arrived at opening moves the human literature had dismissed.

AlphaZero, Google DeepMind’s AI for playing the game Go and a number of other games, is those same two pieces made very large. It is given the rules of a game and nothing else. No record of human play, and no opening book. And then it plays against itself. One part of the network estimates how good a position is, which is the critic. Another part proposes moves, which is the actor. The estimates are trained on the outcomes of its own games, and the moves are trained on the estimates. The resemblance to an animal is at the level of the procedure, and that is the only level at which we claim it. Nothing about AlphaZero’s weights, its training schedule or its hardware resembles a nervous system, and in §5.3 we will make that distance wider rather than narrower. What is genuinely shared is the shape of the rule. And it is notable that the shape was arrived at twice — once by people asking what a rat is doing, and once by people trying to make a machine improve.

![Two parallel timelines from 1949 to the present. The upper line marks the machines: SNARC in 1951, ADALINE in 1960, Samuel’s checkers program through the 1950s, TD-Gammon in 1992, and AlphaZero. The lower line marks the animal work that arrived at the same rules: Hebb’s proposal in 1949, the delta rule in 1960, Rescorla and Wagner in 1972, and second-order conditioning. Vertical connections join the pairs that are the same algorithm.](reading_images/fig-ai-timeline.svg){#f-ai-timeline alt="Two horizontal timelines drawn one above the other against a shared year axis running from 1949 to the present. The upper timeline is labeled machines and carries marks at 1951 for SNARC, 1960 for ADALINE, the mid 1950s for Samuel’s checkers program, 1992 for TD-Gammon, and the late 2010s for AlphaZero. The lower timeline is labeled animals and carries marks at 1949 for Hebb’s proposal, 1960 for the delta rule, and 1972 for Rescorla and Wagner. Dashed vertical lines connect ADALINE to the delta rule, Samuel’s checkers program to temporal-difference learning, and AlphaZero to actor and critic. A note beneath the SNARC mark reads credit assignment, unsolved."}

### §5.2.10 — Habits and Goals

Two ways of choosing an action are available to a learner with the machinery described so far. One is to repeat whatever has worked in this situation before, which is what a policy adjusted by reinforcement amounts to. The other is to consult a model of what leads to what, run the model forward, and choose on the basis of where it ends up. The first way is **model-free**. The second is **model-based**.

An experiment tells the two apart. A rat is trained to press a lever for a particular food. Then, away from the lever, that food is made sickening, paired with an illness until the rat will not touch it. Put the rat back at the lever. A rat choosing on a model of what the lever leads to should stop pressing immediately, because on that model the lever leads to something it now wants nothing to do with. A rat repeating what has worked should keep pressing, because nothing about the lever itself has changed. *Reinforcer devaluation* is the name of the manipulation, and which result appears depends on how much training came first. Modest training leaves the pressing sensitive to devaluation, and the behavior is **goal-directed**. Extended training makes the pressing insensitive, and the behavior has become a **habit**.

### §5.2.11 — Extinction Is Not Unlearning

Stop delivering food after a lever is pressed, and an animal’s lever pressing fades. Stop pairing the tone with the shock, and the fear fades. That is **extinction**, and the tidy story about it is that the weight has gone back down to roughly where it started. The tidy story is wrong, and three findings show us why [](#f-extinction-return). The first finding goes by the name **spontaneous recovery**. Wait a period of time after a behavior has been extinguished, with no further training of any kind, and the response returns on its own. The second is called the **renewal effect**. Extinguish a response in one room and test it in another, and the response returns. The third is called **reinstatement**. Deliver the outcome once on its own, unannounced and unpaired, and the extinguished response returns as well.

A weight that just decayed back to its starting value could produce none of that. There would be nothing left to come back. What extinction adds is new learning, rather than the removal of old learning. The new learning is about the context nearly as much as about the cue. Once an animal has learned an association, and the association is violated, it does not unlearn the association. They learn a new fact: the old association doesn’t seem to be true in this new context. The original association survives underneath, as a part of that new fact.

How are we to understand which fact should govern the animal’s behavior, the original association, or the newer, more context-dependent knowledge about the lack of an association? It depends on where the animal is, and how long it has been. Stating the consequence for a rule plainly: an update procedure cannot simply put the weight back. Something has to be able to hold the original association and its later contradiction at the same time. And then, something has to arbitrate between them. That is a real complication. It is also the most practically consequential result in this chapter for anyone hoping to be rid of a learned response, whether the learner is a rat, a dog, or a person.

![Acquisition, extinction, and the three ways a response comes back, drawn as response strength over successive sessions. The response rises during acquisition and falls during extinction. Three separate continuations follow: after a delay with no training the response partly returns; tested in a different context it returns; and after a single unpaired delivery of the outcome it returns.](reading_images/fig-extinction-return.svg){#f-extinction-return alt="A line graph with sessions on the horizontal axis and response strength on the vertical axis. A single curve rises across a shaded region labeled acquisition, then falls across a second shaded region labeled extinction, approaching but not reaching zero. From the end of the extinction region, three separate dashed continuations branch upward to partial heights, labeled spontaneous recovery after a delay, renewal in a different context, and reinstatement after one unpaired outcome. A dotted horizontal line at the original acquisition height is labeled the level reached before extinction."}

### §5.2.12 — What Cannot Be Learned, and Why That Is Not a Flaw

One more limit, and it is not a limit of the rules. Pigeons trained to peck a key for food will, given enough training, come to peck the key the way they peck at grain, even where a different movement would work better. Raccoons trained to drop coins into a slot for food start rubbing the coins together instead, the way they handle food before eating it. The reinforcement is arranged correctly in both cases. The animal drifts back toward something that is more natural for its lineage.

The same point shows up as a difference in what can be linked at all. A rat associates a novel flavor with illness across several hours, after a single pairing. The same rat associates a flavor with an electric shock hardly at all, however carefully the pairing is arranged. And it associates a noise with a shock readily, while a noise with illness is nearly hopeless. The rules have no preferences. The animal does, and the preferences line up with the pairings its ancestors had reason to pick up. A pre-established tendency to have an easier time learning one thing over another, due to biological dispositions or other learned knowledge, is called an **inductive bias**.

The consequence is that none of these rules are blank slates operating on arbitrary inputs. What they run on has already been sorted by what a lineage needed. Module 2’s warning against treating any one animal as the general case applies here in a specific form. A rule that looks fully general written on a page is, in a real animal, applied to some pairings and not to others. What determines which pairings is partly a question about representations, and we take that question up in Module 7.

Four kinds of rule have now been described, and each of them works, in the sense that a system running one improves at something. Whether anything in a nervous system actually does any of this is a different question. Answering it means finding something that can deliver *better than expected* to the right connections at the right moment.

## §5.3 — Implementational: What Physically Changes, and What Gates It

### §5.3.1 — What Physically Changes, and Where the Account Stops

In §5.2 a weight is a number in a rule. In an animal it is a physical arrangement, and something physical has to move when it changes. In Module 3, we said that the strength of a connection was one of the answers to how identical spikes can carry different amounts of information. Now we will describe how that strength actually changes in real biological cells.

One boundary is worth stating first. What follows stops at the synapse and at the cell. Vertebrate brains also have whole structures given over to particular kinds of learning, and we take up where those are, and why an animal ends up with separate ones, in Module 6. But before there were brain systems specialized for particular kinds of learning, there was learning at the level of individual synapses.

Underneath everything in §5.3 there is a single principle: a lasting change that is a function of activity. What varies is where the change is made, and what regulates it. A change can be made to the strength of a synapse, to how readily a cell fires at all, or to whether a connection is there in the first place. Any of those can be regulated. They can be regulated by a signal broadcast from somewhere else, by a fading mark that settles which synapses are still in the running, and by mechanisms that keep the whole arrangement from running away.

### §5.3.2 — Strengthening a Synapse, and Weakening One

Two connected cells fire together, repeatedly, and the synapse between them becomes stronger, and stays stronger for hours or longer. **Long-term potentiation** is the name for that lasting increase. If the sending cell fires repeatedly while the receiving cell stays quiet, the same synapse will weaken instead. This is **long-term depression**. Both are changes in how much an arriving spike accomplishes. More transmitter is released on the sending side, and there are more receptors on the receiving side to catch it — or less of each, in the other direction.

The pair matters more than either member of it. A synapse that could only strengthen would be a one-way ratchet, which is exactly the limitation we raised at the end of §5.2.1 regarding Hebb’s rule. Long-term depression is what makes a coincidence rule something that can move a weight in both directions, rather than something that can only add.

### §5.3.3 — The NMDA Receptor Is an AND Gate

How does a synapse detect that both of its cells were active? One answer is built into a receptor. The **NMDA receptor** sits on the receiving side and opens only when two conditions hold at once. Transmitter released by the sending cell has to be bound to it. And the receiving cell has to be depolarized already, enough to expel a magnesium ion that otherwise sits in the channel and plugs it. Transmitter alone does nothing, because the plug is still in place. Depolarization alone does nothing, because there is nothing bound. Both together and the channel opens, calcium enters the receiving cell, and the lasting change is set in motion.

That is a truth table built out of chemistry [](#f-nmda-and). In Module 4 we treated AND, OR and NOT as operations a threshold unit computes, with the threshold deciding which one. Here is an AND gate made of a protein, a magnesium ion and a voltage. **Coincidence detection** is the name for what the receptor does, and in this one case the name is not a description of the mechanism from a distance. It is the mechanism.

![The two conditions an NMDA receptor requires, set beside the truth table for AND. Transmitter bound and the receiving cell already depolarized are the two inputs; calcium entry is the output. Either condition on its own produces nothing, and only both together open the channel.](reading_images/fig-nmda-and.svg){#f-nmda-and alt="A two-part figure. On the left, a schematic synapse: a sending terminal above releasing transmitter molecules onto a receptor embedded in the membrane of a receiving cell below. The receptor channel is drawn twice, once with a magnesium ion lodged in its pore and labeled blocked, and once with the ion displaced and calcium ions passing through, labeled open. A label beside the first reads transmitter bound, cell not depolarized. A label beside the second reads transmitter bound and cell depolarized. On the right, a four-row truth table with columns headed transmitter bound, cell depolarized, and calcium enters. The first three rows read no, and only the row in which both inputs are yes gives yes in the output column. A caption bar joins the two halves and reads AND."}

### §5.3.4 — Timing, and Which One Came First

Overlap is not quite the whole story. What settles the direction of the change is order. If the sending cell fires shortly before the receiving cell fires, the synapse strengthens. If it fires shortly after, the same synapse weakens. The window in which order matters at all is a few tens of milliseconds wide, and outside that window very little happens in either direction [](#f-stdp-window). **Spike-timing-dependent plasticity** is the name for the whole pattern.

That answers an objection which has been sitting underneath §5.2 since Hebb’s rule was written down. A rule that responds to things happening together cannot tell a cause from a coincidence, because a cause and a coincidence both show up as co-occurrence. Except that at the synapse the two do not look alike. A cell that helped fire another cell fired first. A cell that merely happened to be active at the same moment is as likely to have fired just after as just before. So some of the difference between causing something and accompanying it is carried in a few milliseconds of order, and a synapse is sensitive to precisely that. It is also the second half of a promise from §5.1.6, which said that an association across time has to record which event came first.

![How much a synapse changes, plotted against the interval between the sending cell’s spike and the receiving cell’s spike. Intervals in which the sending cell fired first produce strengthening, intervals in which it fired second produce weakening, and intervals longer than a few tens of milliseconds in either direction produce almost nothing.](reading_images/fig-stdp-window.svg){#f-stdp-window alt="A line graph. The horizontal axis is the interval between the sending cell’s spike and the receiving cell’s spike, running from about minus eighty milliseconds on the left to about plus eighty on the right, with zero marked at the center. The vertical axis is the change in synaptic strength, with zero marked by a horizontal line across the middle. To the right of center, where the sending cell fired first, the curve rises steeply just past zero and then decays back toward the zero line by about forty milliseconds; this lobe is shaded and labeled strengthening. To the left of center, where the sending cell fired second, the curve drops steeply below the line and then returns toward it; this lobe is shaded differently and labeled weakening. Both lobes are flat at zero beyond roughly fifty milliseconds."}

### §5.3.5 — A Coincidence Rule Runs Away, and Biology Bounds It

A rule that strengthens what is already strong is a positive feedback loop, and Module 3 said what positive feedback loops do. They run to completion. Left to itself a Hebbian synapse would strengthen, which would make the receiving cell fire more readily, which would make the pairing more reliable, which would strengthen the synapse further. Every useful connection would end up saturated and every cell would end up responding to everything.

Two things bound it, and one of them answers the question we left open in §5.2.1. The first is long-term depression, which weakens a synapse directly. The second is **synaptic competition**. What a synapse needs in order to grow is limited and shared among the synapses onto the same cell, so strengthening some of them weakens others. Competition is not a bookkeeping detail. It is the reason an input that stops carrying useful signals does not merely fail to gain ground, but loses ground it already held.

Both are worth stating plainly, because the opposite is said often: the claim that Hebbian learning has no way to weaken a connection is false. One mechanism weakens a synapse directly, and another weakens it as a consequence of strengthening its neighbors.

### §5.3.6 — *Aplysia*, and a Third Cell

*Aplysia* is a sea slug with roughly twenty thousand neurons, many of them large enough to see without a microscope and to record from one at a time. Touch its siphon and it withdraws its gill. That one reflex, in that one animal, carries three kinds of learning: habituation when the touch is repeated without consequence, sensitization after a shock, and classical conditioning when a touch is paired with a shock. In each case the change has been traced to particular synapses between identified cells.

Sensitization is the one to look at closely. A shock to the tail makes the animal withdraw more vigorously in response to almost anything afterward. What produces that is not a change inside either of the two cells in the reflex pathway. It is a third cell, which releases serotonin onto the connection between them, and thereby changes how much transmitter the sending cell releases.

Notice what has just happened. A signal arriving from outside the pair has changed what the pair does. That is the subject of the next section, and it was found first in an invertebrate.

### §5.3.7 — The Three-Factor Rule

Presynaptic activity. Postsynaptic activity. And a third signal, broadcast from elsewhere. Those are the **three-factor rule**, and the division of labor among them is the point. The local pair settles which synapses are eligible to change. The third factor settles whether they change at all, and in which direction.

That last part deserves care, because the obvious guess about it is wrong. The third factor is not a volume knob on a change the first two have already decided. In a number of preparations the same pairing of presynaptic and postsynaptic activity produces strengthening or weakening depending on which modulatory receptor is engaged. A modulator can reverse the sign of the change, and not merely scale its size.

That is the bridge we have needed since §5.2.3. A coincidence detector on its own is Hebbian, and a Hebbian rule has no term for how things went. Add a signal that arrives when things went better than expected, and the same coincidence detector becomes a reward learner, with nothing about the coincidence detection itself altered [](#f-three-factor).

Now the third factor can be named. Dopamine is one of the signals that does this job. In Module 4 we gave dopamine wanting and pursuit and held the rest back. Here is the rest. Dopaminergic cells fire above their baseline when an outcome is better than predicted, fall below it when an outcome is worse, and do not change when an outcome arrives exactly as predicted. That is the **reward prediction error** — the one broadcast number of §5.2.7, made physical, and released across a wide stretch of tissue rather than addressed to particular cells.

One honest note about the evidence. The recordings that established the dopamine result were made in vertebrates, and largely in primates. So the evidence comes from an animal that arrived long after the mechanism did, and how far down the tree the arrangement extends is a separate question from whether it works this way in a monkey.

![The three factors that decide whether a synapse changes. The sending cell’s activity and the receiving cell’s activity together make the synapse eligible; a modulatory fiber arriving from elsewhere decides whether the eligible synapse changes, and in which direction.](reading_images/fig-three-factor.svg){#f-three-factor alt="A diagram with two cells drawn left and right, joined by a synapse at the center, and a third fiber descending onto that synapse from above. The sending cell on the left is labeled presynaptic activity and the receiving cell on the right is labeled postsynaptic activity, with arrows from each converging on the synapse and a bracket beneath them labeled together, these make the synapse eligible. The descending fiber is labeled modulatory signal from elsewhere, and a separate arrow from it to the synapse is labeled decides whether the change happens, and in which direction. To the right of the diagram, three small panels show the same synapse after three cases: eligible with a positive modulatory signal, marked strengthened; eligible with a different modulatory signal, marked weakened; and eligible with no signal, marked unchanged."}

### §5.3.8 — The Trace Made Physical, and the Other Signal from Elsewhere

In §5.2.8 we needed a fading mark, so that a signal arriving after the fact could find the synapses that had been involved. Something of that kind exists. A synapse that has just been active is left in an altered state which decays over seconds. A neuromodulatory signal arriving inside that window converts the altered state into a lasting change. A signal arriving after the window has closed does not.

So an algorithmic proposal, invented to solve a timing problem, turns out to have a physical counterpart. It is worth being careful about what that does and does not show. It does not show that the algorithm is correct. It shows that the thing the algorithm needed is the sort of thing a synapse can be.

A single broadcast number is also not the only signal a nervous system can send from elsewhere. Some learning runs on a signal that specifies a different output, item by item, which is the teacher of §5.2.7. Vertebrates have a structure arranged around exactly that. In the cerebellum, each output cell receives, alongside its ordinary inputs, a single climbing fiber from one source, and that fiber’s firing is an error signal for that cell in particular. One fiber, one target cell, one instruction. Where the different kinds of learning end up in a vertebrate brain, and what an animal gains by keeping them apart, we take up in Module 6.

### §5.3.9 — Learning Has a Schedule

In §5.1.12 we said that a learner needs a setting somewhere between changing with every experience and changing with none, and probably a schedule that moves the setting across a lifetime. Nervous systems have such a schedule, and it is built out of the mechanisms already described.

Connections are made early in great profusion, far more of them than will survive. **Synaptogenesis** is the name for that proliferation. What follows is **pruning**, a cutting back in which activity decides which connections last, and the rule doing the deciding is the competitive one of §5.3.5, running while an animal is still being built. Early on, then, a nervous system is not merely adjusting weights. It is settling which connections will exist to have weights at all.

A **critical period** is a window during which experience has an outsized and lasting effect on how some piece of nervous system ends up wired. Two cases are worth having. The inputs carrying signals from the two eyes compete for territory in visual cortex, and closing one eye early in life leaves that eye holding less territory than it had before, and it does not recover the difference when the eye is reopened [](#f-competition). Do the same to an adult and very little happens. And human infants can hear distinctions that their language does not use, then lose much of that ability across the first year, as the contrasts that actually occur in what they hear come to organize how speech sounds are heard at all. In both cases the closing of the window is an active process rather than a gradual running-down, which is why it has a schedule rather than merely a rate.

The human version of these findings gets overstated often enough that it is worth separating what the evidence supports from what it does not. Supported: early experience has effects on some capacities that are large, specific, and difficult to reverse afterward, and the two cases above are the clearest of them. Not supported: that development is a series of windows that slam shut, that missing one means a capacity is gone for good, or that extra stimulation during a window produces a better capacity later. Adults learn second languages. Recovery from early deprivation is usually partial, which is neither nothing nor everything. A window that closes changes what later learning has to work with. It does not end learning.

![Inputs from the two eyes competing for territory in visual cortex, before and after one eye is deprived of input early in life. Before deprivation the territory is divided about evenly. After deprivation the open eye holds most of it, and the closed eye holds a narrow remainder, having lost ground it previously occupied.](reading_images/fig-competition.svg){#f-competition alt="Two horizontal bands drawn one above the other, each representing a stretch of visual cortex divided into alternating regions. The upper band is labeled before deprivation and its regions alternate in roughly equal widths between two shades, one labeled left eye and the other labeled right eye. The lower band is labeled after one eye is closed early in life. In it the regions belonging to the open eye are much wider and those belonging to the closed eye are narrow strips. A bracket beneath the lower band marks the difference between the two and is labeled territory lost, not merely territory not gained."}

### §5.3.10 — Several Loci, Several Regulators

A synapse is not the only thing a nervous system can change lastingly, and a reader who has been told nine times that a weight is what moves should be told what else does. The answer tidies §5.3 rather than complicating it.

There are three places a lasting change can be made. The *strength of a synapse* is the one described at length above. **Intrinsic excitability** is the second: a cell can change how readily it fires at all, so that the same arriving input carries it further, or less far, than it did before. And whether a connection exists at all is the third, which §5.3.9 has just shown being settled by competition during development.

There are three things that regulate any of them. A neuromodulatory signal gates the change and can set its direction, as in §5.3.7. An eligibility trace settles which synapses are still candidates by the time that signal arrives, as in §5.3.8. And **homeostatic plasticity** together with competition bounds the result, keeping total activity and total synaptic strength within a range rather than letting either run off, as in §5.3.5.

One principle, at several loci, with several regulators. Every mechanism in §5.3 has been an instance of it.

That frame also dissolves a question a good student asks. It is sometimes said that Hebbian plasticity is the only kind of learning there is, and that everything else is a modulation of it. On the account just given, that is a disagreement about which word to use rather than about what happens. Nobody disputes that a coincidence-sensitive change in synaptic strength exists, that neuromodulators gate it, that traces settle what it lands on, or that changes in excitability and in connectivity accompany it. Whether to call those last three learning, or the regulation of learning, is a naming question, and naming questions are not findings.

One clause of hedging is owed. What is described above is where the evidence currently sits, and not a demonstration that nothing else could hold a lasting change. A minority argument that some of what is stored is held inside cells, in molecules rather than in connections, is live, and a pointer to it is in the Further Reading.

### §5.3.11 — Learning and Memory

A synapse has now been shown changing, and staying changed. So is that a memory?

In one ordinary sense, it is. A persisting change caused by experience is close to what many people mean by the word, and on that reading every result in §5.3 is a memory result.

But that sense does no work. On it, a piece of metal that has been bent is remembering the force that bent it, and a path worn across a lawn is remembering the people who walked it. A word that covers everything distinguishes nothing.

The distinction that does work is about when the use of a stored thing is settled. A **disposition** is committed at the moment it is laid down. The weight changes, and what the change will do is fixed by the change itself: this animal is now more likely to do this in that situation. A **record** is uncommitted. Something is kept without its use being settled, and what it is for is decided later, at the moment it is retrieved. Learning as we have described it produces dispositions [](#t-disposition-record).

Two consequences follow, and both are worth having. The first is about vocabulary. *Encoding, storage and retrieval* is not a deeper way of describing what we have described above. It is a decomposition that only becomes necessary once what is kept is uncommitted, which is why the vocabulary sounds strange applied to habituation — nothing is retrieved when an anemone stops withdrawing. The second is about what a weight can report. A weight is a residue. It can say what tends to happen, and it can never say what happened. An animal whose learning is entirely dispositional cannot revisit a particular occasion, because no particular occasion was ever kept.

The distinction predicts its own hard cases, and the hard cases are the famous ones. In *sensory preconditioning*, two neutral things are paired with each other first — a bell and a light, with nothing following either one — and only afterward is one of them paired with something that matters. The animal then responds to the other one as well, though it has never been paired with anything. At the moment the bell and the light were linked, nothing had determined what that link would be used for. *Latent learning* is the same shape at a larger scale. Rats allowed to wander a maze containing no food appear to learn nothing, until food is introduced, at which point they reach it about as efficiently as rats that had been rewarded from the start. What they picked up while wandering was not committed to any use at the time they picked it up.

Latent learning is where a disposition stops being enough. Something was kept that was not a disposition to act, and it had to be put to work by a process that came later. Records, retrieval, and the animals that keep them we take up in Module 10, along with the distinction between episodic and semantic memory that will be needed there.

<!-- pin: t-disposition-record -->

: Two kinds of lasting change, told apart by whether the use of what is stored was settled when it was laid down. {#t-disposition-record}

| | A disposition | A record |
|---|---|---|
| Committed at encoding | Yes — what the change will do is fixed by the change | No — what it is for is settled later |
| A separate retrieval step | Not needed; the change acts whenever the situation recurs | Required, and it is where the use gets decided |
| What it can report | What tends to happen | What happened, on a particular occasion |
| Where it is taken up | Module 5 | Module 10 |

### §5.3.12 — One Mechanism, Several Jobs

Nothing described in §5.3.10 is a learning-specific device. The same coincidence detection, the same gating by a signal from elsewhere, and the same competition for something limited also wire a nervous system during development, tune a sensory map to the statistics of what reaches it, and support the memory system just handed on to Module 10. One set of parts, several architectures, several problems.

Module 1 taught multiple realizability: one function, running on many possible implementations. Here is the converse. One implementation, serving many functions. And the converse is what makes an inference from a part to a job unsafe, which is the move we named **reverse inference** in Module 2. Finding that a mechanism is present, or that a structure is active, does not establish which job is being done, when the same mechanism does several.

That is also what the frame of §5.3.10 was for. A principle stated generally enough to have several loci and several regulators, with nothing in it committed to any particular task, is exactly the kind of thing that gets reused everywhere. So the overlap is not an embarrassment for the account. It is what two earlier modules would have predicted.

## Close — General-Purpose Machinery, and What Comes After It

Four kinds of learning have been described, and what separates them is not what they change. All four change a weight. What separates them is how much of the world has to reach that weight before it will move, and, where an answer is needed, who supplies it. Nothing but the two cells a connection joins. The next input, which the world delivers without being asked. An answer from a source that already holds it. Or one number reporting how things went. Ranked by how hard the required signal is to arrange inside an animal, the order runs backward from the one most people expect, and a teacher is the hardest of the four rather than the easiest. One synapse, given the right third factor, implements all of it.

One lesson travels further than the rest, so it is worth stating on its own. Vocabulary about goals and errors earns its place exactly where something in the mechanism plays the part the word names. Hebb’s rule holds no goal and registers no miss, so reading design into it is the same mistake we refused to make about the peppered moth in Module 2. Error-driven learning holds an expectation and computes a difference against it, so the same words describe rather than decorate. That is a test, and it applies well outside this chapter.

Three places the levels strained are worth naming, now that we have earned them.

The first is that Marr’s three levels have no slot for evidence. Blocking, devaluation, renewal and instinctive drift are not computational, algorithmic or implementational claims. They are findings, and findings are what decide between proposals at every level. A scheme that classifies explanations is silent about the things that adjudicate them, and naming that gap is more useful than pretending the four categories were three.

The second is that the levels were not independently specifiable here. The scheme says it should be possible to settle what is computed without settling how it is done. But temporal-difference learning became the accepted account of animal learning in large part because of a finding from below it — recordings of a neuromodulatory signal behaving exactly as the algorithm’s error term said it should. The evidence for the algorithm came from the implementation.

The third is §5.3.12’s point. What turned up at the implementational level was not a mechanism for learning. It was a principle, sited in several places and regulated in several ways, none of it dedicated to learning in particular. A description that general does not pick out the function above it, which means the mapping between levels is loose downward as well as upward.

None of that means the levels fail. They did the work of this chapter, separating *why change at all* from *by what rule* from *in what material*, and that separation is what made it possible to compare the families at all. But a framework is a tool with a shape, and knowing where a tool strains is part of knowing how to use it.

What is missing is the handoff. Everything in this chapter is general-purpose and undifferentiated. The same rule runs in the same tissue wherever there are synapses, with no part of the animal given over to one kind of learning rather than another. The frame of §5.3.10 is what makes the limitation sharp: a principle general enough to be reused everywhere is, for that very reason, specialized for nothing. That is efficient, and it is limited. A system that does everything in one place cannot be very good at any of it, and it cannot do two incompatible things at once. So what happens when an animal is large enough to build specialists? That is Module 6, and it is the same question we asked about circuits in Module 4, one level up.

Three shorter threads are left hanging on purpose. What a single unit cannot learn however it is trained, we take up in Module 7. Traces that are kept rather than committed, in Module 10. And choosing what to do by consulting a model of the world, in Module 12.

## Further Reading

Five places to go next, chosen because each one takes up a thread this chapter could only pull on briefly.

**Ken Cheng, “Learning in Cnidaria: a summary”, 2023.** The scientist behind the count in §5.1.10, writing after his own verdict moved. Cheng went through every study anyone had run on learning in cnidarians and reported no firm case for operant conditioning anywhere, and no box jellyfish literature at all. Then the 2023 results arrived. This short piece is what he wrote once his tally had changed. The full systematic review, *Learning in Cnidaria: A systematic review*, is in *Learning & Behavior* 49(2), and its summary table is the clearest statement in print of what is established, what is contested, and what nobody has tried.

**Jacqueline Rose and Catharine Rankin, “Analyses of Habituation in *Caenorhabditis elegans*”, 2001.** Tier one gets three paragraphs in §5.1.5 and is worth more than that. Rose and Rankin take the simplest thing a nervous system can learn, and show how much turns out to be inside it. They demonstrate this in the worm of §5.1.6, under its full name.

**Richard Sutton and Andrew Barto, *Reinforcement Learning: An Introduction*, second edition, 2018.** The whole of §5.2 at full length, by two of the people who built it. Every rule named in this chapter is there with the mathematics left out here, and so is a great deal we never reached. Chapter 1 closes with a history that is the best short account anywhere of how animal learning and engineering arrived at the same equation without contact.

**Yuko Munakata and Jason Pfaffly, “Hebbian learning and development”, 2004.** One of the sources this chapter was built from, going further than §5.3.9 does. Munakata and Pfaffly take a Hebbian rule running under competition for something limited and ask what a developing brain gets out of the arrangement. The answer is that structure nobody specified in advance can come out of activity and a shortage. This chapter names that and moves on; they show it working, and they are careful about what the demonstrations do and do not establish.

**Wickliffe Abraham, Owen Jones and David Glanzman, “Is plasticity of synapses the mechanism of long-term memory storage?”, 2019.** The hedge at the end of §5.3.10, in full. Everything in §5.3 rests on the assumption that a lasting change at a synapse is where the learning is kept, and that assumption is better supported than any rival, but still not proved. Abraham, Jones and Glanzman set out why synaptic plasticity looks so much like the right answer, and then take seriously the mechanisms that are not synaptic at all, including the argument that some of what is stored is held inside cells, in molecules rather than in connections. Open access. Glanzman works on *Aplysia*, so the animal from §5.3.6 returns, on the other side of the question.

## Glossary

**actor–critic** — An arrangement that separates two jobs: a critic that learns to predict how well things will go from here, and an actor that holds a policy and adjusts it using the critic’s errors.

**blocking** — The finding that a cue perfectly paired with an outcome is not learned about, when some other cue already predicts that outcome. What gets learned tracks what was not already predicted.

**bootstrapping** — Using one of a system’s own estimates as the target for another, rather than waiting for the true outcome to arrive.

**classical conditioning** — Learning in which one event comes to be treated as a sign of another, so that a cue which previously did nothing comes to produce a response. Also called Pavlovian conditioning.

**coincidence detection** — Responding only when two things occur together, and to neither of them alone.

**conditioned response** — The response that a conditioned stimulus comes to produce. It is how the link can be seen from outside, rather than being one of the two things linked.

**conditioned stimulus** — An event that produces a response only because it has been paired with something that already produced one.

**contingency** — A reliable relationship between one thing and another, such that the first is a dependable sign of the second.

**credit assignment** — The problem of working out which of several actions, or which of several connections, was responsible for an outcome that arrived later.

**critical period** — A window during which experience has an outsized and lasting effect on how part of a nervous system ends up wired, and whose closing is an active process rather than a gradual running-down.

**delta rule** — A learning rule that changes a weight in proportion to the difference between a target output and the output actually produced, scaled by the input that weight carries.

**discounting** — Counting an outcome for less the further in the future it lies, by applying a factor slightly below one for every step of delay.

**disposition** — A lasting change whose use is settled at the moment it is laid down, so that the change itself fixes what the animal will now be more likely to do.

**eligibility trace** — A fading mark left on whatever was recently active, so that a signal arriving later can find the connections that were involved.

**exploration versus exploitation** — The trade-off between taking an option already known to be decent and sampling one that might be better and might be worse.

**extinction** — The fading of a learned response when the outcome stops arriving. It is new learning that competes with the original association, rather than the removal of it.

**goal-directed** — Choosing an action by consulting a model of what it leads to, so that changing the value of the outcome changes the choice immediately.

**gradient descent** — A general method for reducing error: measure how wrong an output is, work out which direction each weight would have to move to make it less wrong, and take a small step in that direction.

**habit** — A behavior chosen by repeating what has worked before, which continues even after the outcome it once produced has been made undesirable.

**habituation** — A decline in a response to a stimulus that has been repeated without consequence. It is not fatigue: a novel stimulus restores the full response at once.

**Hebb’s rule** — A learning rule that changes the weight between two neurons in proportion to how active both were at the same time, and that needs nothing beyond the two cells the connection joins.

**homeostatic plasticity** — Mechanisms that hold total activity and total synaptic strength within a range, bounding what other kinds of plasticity would otherwise drive to an extreme.

**inductive bias** — A tendency to find one thing easier to learn than another, established before the learning begins, whether by the animal’s lineage or by what it has already learned.

**intrinsic excitability** — How readily a cell fires at all, which can itself be lastingly changed, so that the same arriving input carries the cell further than it did before.

**learning** — A lasting change in what an animal does, produced by experience, and resting on an internal state that experience can modify.

**learning rate** — A small number setting how much of the available change a rule takes on any one occasion. A high rate follows the most recent occasion; a low rate averages over many.

**long-term depression** — A lasting weakening of a synapse, produced when the sending cell is repeatedly active while the receiving cell is not.

**long-term potentiation** — A lasting strengthening of a synapse, produced when the two cells it joins are repeatedly active together.

**model-based** — Choosing an action by running a model of what leads to what, and selecting on the basis of where the model ends up.

**model-free** — Choosing an action by repeating what has worked in that situation before, with no model of what the action leads to.

**NMDA receptor** — A receptor that opens only when transmitter is bound to it and the receiving cell is already depolarized, so that it responds to two conditions at once and to neither alone.

**operant conditioning** — Learning in which what the animal did is one of the linked terms, so that a consequence makes that action more or less likely in that situation afterward. Also called instrumental conditioning.

**plasticity** — The property of nervous tissue that allows a connection, or a cell, to undergo a lasting change as a consequence of activity.

**policy** — A mapping from situations to what to do in them.

**prediction error** — The gap between what was expected and what occurred. In Rescorla and Wagner’s rule it is the difference between the strength the association will eventually reach with an outcome and the strength already present.

**prediction learning** — Error-driven learning in which the target is the next input, supplied by the world unasked, which requires that a prediction be generated before that input arrives and held until it does.

**pruning** — The cutting back of an early overabundance of connections, with activity deciding which ones survive.

**punisher** — A consequence that makes the response it followed less likely in that situation afterward.

**record** — Something kept without its use being settled, so that what it is for is decided later, at the moment it is retrieved.

**reinforcer** — A consequence that makes the response it followed more likely in that situation afterward.

**reinstatement** — The return of an extinguished response after the outcome has been delivered once on its own, unpaired.

**renewal effect** — The return of an extinguished response when the animal is tested somewhere other than where extinction took place.

**reverse inference** — The move from “this brain region was active during the task” to “therefore the task involved the process that region does.” Tempting and often wrong, because brain regions are not dedicated to single processes, so how much an activation licenses depends on how selectively that particular region responds.

**reward prediction error** — A signal reporting that an outcome was better or worse than predicted, broadcast widely rather than addressed to particular cells. Dopaminergic cells carry one.

**sensitization** — A rise in responsiveness to stimuli generally, following something significant.

**spike-timing-dependent plasticity** — The dependence of synaptic change on the order of two cells’ spikes: the sending cell firing first strengthens the synapse, the reverse weakens it, within a window tens of milliseconds wide.

**spontaneous recovery** — The return of an extinguished response after a delay, with no further training of any kind.

**stability versus plasticity** — The trade-off between changing enough to learn something new and changing little enough to keep what was learned before.

**synaptic competition** — Competition among the synapses onto one cell for a limited shared resource, so that strengthening some of them weakens others.

**synaptogenesis** — The formation of new synapses, which early in life produces far more connections than will survive.

**temporal-difference learning** — A family of rules that compare each estimate against the next estimate the system itself produces, so that value propagates backward along a sequence.

**three-factor rule** — A rule in which presynaptic and postsynaptic activity together make a synapse eligible to change, and a third signal from elsewhere settles whether it changes, and in which direction.

**unconditioned response** — The response an unconditioned stimulus produces without any training.

**unconditioned stimulus** — An event that produces a response without any training.

**value** — An estimate of how well things will go from a given situation onward.
