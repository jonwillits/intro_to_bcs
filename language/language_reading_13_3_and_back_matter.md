<!-- DRAFT FOR MERGING (Claude, 2026-11-15). Written while language_reading.md was open in Jon's editor, so nothing here has been put into that file. Three blocks, each marked with a MERGE comment: (1) the chapter-opening block replaces the PLACEHOLDER comment on line 1, above the t-levels-language pin; (2) §13.3 goes after the end of §13.2.14; (3) the Close, Further Reading and Glossary go after §13.3, at the end of the file. Audited as one merged copy against snapshot 0056: 0 errors; body 16,050 words; 14 warnings, 12 of them single-use glossary terms, 1 for length, and 1 in the levels table. Delete this comment and the MERGE comments when merging. -->

<!-- MERGE 1 of 3: replaces the PLACEHOLDER comment on line 1 -->

# 13. Language

This module is about language: what it lets one mind do for another, how people and machines come to use it, and what in the brain makes it possible. While reading, look for the beginnings of answers to these questions:

- What is language for, and how do the signals of other animals, and of apes taught by people, compare with it?
- When did *Homo sapiens* come to use language, and what does a child need in order to learn one?
- How do listeners find words in a stream of speech, and how do learners work out what the words refer to?
- Do children learn rules or statistics, and how much of language must be built in from birth?
- How are language models built, what do they learn about form and meaning, and where do they fall short?
- What in the brain makes language possible, and how separate is it from the rest of thought?

By the end, we should be able to say what using a language requires, which procedures could produce it, and what the evidence from brains and from machines does and does not show.

<!-- MERGE 2 of 3: goes after the end of §13.2.14 -->

## §13.3 — Implementational: Language in the Brain

### §13.3.1 — Controlling the Voice

In §13.1.6, we described how a living macaque’s vocal tract can make far more vowels than textbooks had claimed, so the body does not explain why other primates do not speak. What, then, does a speaker’s brain do that a monkey’s brain does not?

Speaking requires timing movements of the larynx against movements of the tongue and lips to within tens of milliseconds. Consider the words *tot* and *dot*. For the *t*, the vocal folds in the larynx open once, in a slow gesture lasting about 100 to 150 milliseconds. The opening starts as the tongue closes against the ridge behind the upper teeth, and the tongue releases about halfway through it [](#f-larynx-timing). Because the folds are still apart, the voice resumes more than about 30 milliseconds after the release. For the *d*, the folds stay together, and the voice resumes less than about 20 milliseconds after the release. So a speaker must time two parts of the body against each other, many times a second, and whatever stops other primates from speaking lies in the control of these movements, not in the shape of the vocal tract.

![The larynx and the tongue for the words *tot* and *dot*. For the *t*, the vocal folds open once, in a slow gesture timed to the tongue’s closure, and the tongue releases about halfway through it, so the voice resumes late. For the *d*, the folds stay together, and the voice resumes almost at once. Durations are illustrative values within the ranges the source gives (after Weismer, 2006, Fig. 2).](reading_images/fig-larynx-timing.svg){#f-larynx-timing alt="Two diagrams, one for tot and one for dot, each with a line for the vocal folds above a bar for the tongue, against time running to the right. In both, the tongue is closed for a stretch and then releases at a dashed vertical line. For tot, the vocal-fold line rises in one slow hump, labeled folds open once, for 100 to 150 milliseconds, that starts when the tongue closes and ends well after the release; a zigzag for voicing begins only after the hump ends, and an arrow marks the voice-onset time as more than about 30 milliseconds. For dot, the vocal-fold line stays flat, and the voicing zigzag begins just after the release, with a voice-onset time of under about 20 milliseconds."}

One group of researchers argues that animals that learn their sounds share two features of the brain. One is a pathway in the forebrain for learning and producing sounds, which in songbirds includes a loop through the basal ganglia that young birds need in order to imitate song. The other is a direct connection from motor cortex to the neurons in the brainstem that move the larynx, or the syrinx, the organ birds sing with [](#f-vocal-pathways). In vocal learners, motor cortex sends up to hundreds of axons to each of these brainstem neurons. In mice, it sends one to three. Monkeys produce their calls through circuits in the midbrain and brainstem. If the proposal is right, the human difference from other primates is a connection that lets the forebrain control the voice directly. The proposal rests largely on one laboratory’s work, and its human half is a proposed match to the songbird circuit.

![Vocal pathways in a songbird, and the human pathways one group of researchers proposes as their match. In each, a production pathway runs to motor regions with a direct connection to the brainstem neurons that move the syrinx or the larynx, and a learning loop runs through the basal ganglia and thalamus (after Jarvis, 2019, Fig. 3).](reading_images/fig-vocal-pathways.svg){#f-vocal-pathways alt="Two box diagrams side by side, labeled songbird and human, proposed. In the songbird panel, a box labeled HVC has an arrow to a box labeled RA. Below them, a dashed learning loop runs from HVC through boxes labeled Area X, thalamus, and LMAN, and back up to RA. A thick arrow labeled direct connection runs from RA down to a box labeled brainstem vocal neurons, which leads to the syrinx. The human panel has the same layout, with premotor cortex and Broca’s area in place of HVC, laryngeal motor cortex in place of RA, and anterior striatum, thalamus, and frontal cortex in the loop; the brainstem vocal neurons lead to the larynx. A note below says that motor cortex sends up to hundreds of axons to each brainstem vocal neuron in songbirds and people, and one to three in mice."}

The same group found that dozens of genes, out of thousands examined, showed the same specialized activity in the song regions of birds and the speech regions of human beings, but not in species that do not learn their sounds. So the convergent evolution of vocal learning that we described in §13.1.3 may extend to brain pathways and the genes active in them.

### §13.3.2 — FOXP2

If the control of speech differs between people and other primates, genes are part of the explanation. Can the effect of a single gene on speech be found?

In one large family, about half the members across three generations have a severe disorder of speech and language. In 2001, researchers traced it to a mutation in one copy of a gene called *FOXP2*. Every affected member carried the mutation, and no unaffected member did. An unrelated child with a similar disorder had a break in the same gene. The core difficulty, called *childhood apraxia of speech*, is in sequencing the movements of the mouth. Affected members did worse than unaffected ones on many tests, including tests of grammar. But only on repeating words and nonwords, and on imitating movements of the mouth, did the two groups not overlap at all [](#f-ke-family). Whether their difficulties with grammar follow from the difficulty with movement is unresolved.

![How affected members of the family were identified. On most tests, the affected and unaffected members differed on average but overlapped. On repeating words and nonwords, and on imitating movements of the mouth, they did not overlap at all. The distributions are schematic, since the source reports no values for them (after Vargha-Khadem et al., 2005, Fig. 1).](reading_images/fig-ke-family.svg){#f-ke-family alt="Two panels, each with two bell-shaped curves along a score axis, one for affected members and one, dashed, for unaffected members. In the left panel, labeled most tests, including grammar and nonverbal intelligence, the two curves are shifted apart but overlap in the middle. In the right panel, labeled repeating words and nonwords, and imitating movements of the mouth, the curves are far apart and do not overlap. A note says no values are plotted."}

*FOXP2* is not a gene for language. It regulates the activity of many other genes, in many tissues and in many species. In songbirds, its activity rises in the learning loop while young birds learn their song. In the affected family members, imaging found differences in the basal ganglia and in frontal cortex. So a gene with a large effect on speech in one family need not be a gene for language. And as we described for genes and intelligence in Module 12, a single gene with a large effect in one family explains almost none of the variation among people in general.

The human version of the FOXP2 protein differs from the chimpanzee version at two places, which Neanderthals share. In 2002, one study proposed that the human version had swept through our species by natural selection within the last 200,000 years. But a 2018 reanalysis found the signal of a sweep only when samples from Africa and elsewhere were pooled, mixing populations with different histories, and not within either group. So a signal in the genome can come from how samples are combined, and this gene has not dated the origin of language.

### §13.3.3 — Broca, Wernicke, and Aphasia

Where in the brain is language? The first answers came from people who lost language after damage to the brain. A loss or impairment of language caused by brain damage is called **aphasia**.

In 1861, the French physician Paul Broca examined a patient, Leborgne, who could say only one syllable, *tan*. After Leborgne died, Broca found damage on the surface of the left frontal lobe. In 1874, the German neurologist Carl Wernicke described patients who spoke fluently but understood poorly, with damage further back, in the temporal lobe. These cases became the classic model of language in the brain. On that model, a region of the left frontal lobe, Broca’s area, is for speaking, and a region further back, Wernicke’s area, is for understanding.

The patient on whom the classic model was founded had damage that the model’s region does not describe. Broca kept Leborgne’s brain whole, so he saw mostly its surface, though he noted that the damage went deeper. In 2007, Nina Dronkers and her colleagues scanned the preserved brain with MRI. The damage extended far below the surface, through the insula, parts of the basal ganglia, and a long bundle of fibers. On the surface, it was worst in front of the region now called Broca’s area [](#f-leborgne).

![Leborgne’s brain. Left, the outer surface of the left hemisphere, which is most of what Broca could see, with the damage worst just in front of the region now called Broca’s area, outlined with dashes. Right, a schematic slice through both hemispheres, of the kind MRI showed in 2007, with the damage extending deep into the insula, the basal ganglia, and a long bundle of fibers (after Dronkers et al., 2007).](reading_images/fig-leborgne.svg){#f-leborgne alt="Two drawings. On the left, a side view of a left hemisphere, front at the left. A dark patch near the lower front of the frontal lobe is labeled damage on the surface, and a dashed oval just behind it is labeled Broca’s area today. Lighter patches mark smaller damage in the temporal and parietal lobes. On the right, a front-to-back slice shows two hemispheres as ovals, left and right. In the left hemisphere, dark shapes labeled insula, putamen, caudate, and long fiber bundle mark damage deep below the surface; the same structures in the right hemisphere are pale and undamaged."}

Later evidence has led most researchers to treat the classic model as history. Damage confined to the region Broca described usually causes speech problems that pass within weeks, and lasting aphasia of Broca’s kind comes from larger lesions that reach deeper tissue. People with that kind of aphasia also misunderstand sentences whose meaning depends on their structure, and people with other aphasias make similar errors. The places where damage matters also vary from person to person. In a 2016 survey of 159 researchers who chose to respond, half chose one definition of Broca’s area and about a quarter chose another, and 90% judged the classic model outdated. So the regions that Broca and Wernicke described have no agreed boundaries, although a 2018 textbook still teaches the model.

Language in the hands points the same way. Deaf signers become aphasic after damage to the left hemisphere, while damage to the right leaves their signing intact and impairs their spatial skills. One deaf signer with a large lesion in the left frontal lobe signed haltingly and ungrammatically, but understood signing normally. Sign and speech use largely the same regions of the left hemisphere, with some differences. So these regions serve language, not hearing or the voice, as the sign languages we described in §13.1.4 led us to expect.

### §13.3.4 — The Language Network Against the Multiple-Demand Network

If the classic regions have no agreed boundaries, how can the regions that serve language be found, and how can we ask what else they do? In Module 12, we described the **multiple-demand network**: a set of regions in the frontal and parietal lobes of both hemispheres that become more active as many different kinds of task become harder. We said there that nearby regions that respond to language responded weakly or not at all to those tasks.

The regions that serve language can be found in each person. Evelina Fedorenko and her colleagues compared brain responses to sentences with responses to strings of nonwords, read or heard, in a scan of a few minutes. The regions that respond more to sentences make up the **language network**, usually in the left frontal and temporal lobes. These regions lie in slightly different places in different people. In one study, the location where most people’s regions overlapped was active in only 18 of 25 people, and a map averaged over the group captured only about a third of each person’s activity [](#f-individual-localizer). So finding the regions person by person is what makes it possible to ask whether they do anything besides language.

![The language regions of four people, found by comparing responses to sentences with responses to strings of nonwords, and a map averaged over a group. The individual maps are schematic, drawn to show that the regions lie in slightly different places in different people (after Fedorenko et al., 2010, Fig. 5, and 2024, Fig. 2).](reading_images/fig-individual-localizer.svg){#f-individual-localizer alt="Five small side views of a left hemisphere in a row, front at the left. The first four, labeled person 1 to person 4, each show five dark patches in the frontal and temporal lobes, in similar but slightly shifted positions from one person to the next. The fifth, labeled group map, shows the same five places as small dark centers inside larger pale halos. Text below says that each person’s regions lie in slightly different places, that the best-overlapping location was active in only 18 of 25 people, and that the group map captured about a third of each person’s activity."}

In the same people, the language regions were then tested on hard tasks of other kinds: arithmetic, holding several items in mind, and resisting a habitual response. These tasks strongly engaged the neighboring multiple-demand regions, but left the language regions nearly quiet [](#f-two-networks). There were exceptions, since one frontal language region responded when people held words in mind, and music produced weak responses. Each task was tested in only 11 to 15 people. Even so, brain activity separates language from the regions used for hard tasks of many kinds, in the same people and the same scans.

![The language network and the multiple-demand network on one hemisphere, at average positions. The language regions lie in the frontal and temporal lobes, usually on the left. The multiple-demand regions lie nearby, in the frontal and parietal lobes of both hemispheres. Both vary in position from person to person (after Fedorenko et al., 2024, Fig. 2, and Duncan, 2010).](reading_images/fig-two-networks.svg){#f-two-networks alt="A side view of a left hemisphere, front at the left. Five solid dark patches mark the language network: two in the lower frontal lobe, labeled inferior frontal, one higher in the frontal lobe, and two along the temporal lobe, labeled anterior temporal and posterior temporal. Five hatched patches mark the multiple-demand network: along a groove in the frontal lobe, labeled inferior frontal sulcus, at the front tip, in front of the strip that controls movement, near the junction of the frontal and temporal lobes, and in the parietal lobe, labeled intraparietal. The solid and hatched patches sit close together but do not coincide."}

Patients point the same way. People with severe aphasia can still do arithmetic, reason about causes, follow what other people believe, appreciate music, and find their way. In the 80 patients we described in Module 12, damage weighted toward the multiple-demand network predicted a loss in reasoning with new problems, and damage weighted toward the language network did not. The reverse held for verbal fluency, the ability to produce many words of one kind quickly. These correlations were modest. So in adults, several kinds of thinking survive the loss of most language.

These dissociations are evidence that adult reasoning does not depend on the language regions. They are not evidence that language plays no part in thought. They do not show whether language was needed to build these abilities in childhood, or whether some form of thought that these tests did not target depends on language. And defenders of the thought view in §13.1.1 reply that tests of patients measure how they use language, not what they know of it. So the brain evidence narrows the question of what language is for, without settling it.

The language regions also track structure that the sound does not mark. In one study, people listened to syllables spoken at a perfectly regular rate of four per second. Their brain activity also rose and fell twice a second, with the phrases, and once a second, with the sentences, but only if they knew the language. So listeners build structures like those we described in §13.2.8, and their brains track those structures.

### §13.3.5 — Two Streams for Speech

How does a heard word lead both to its meaning and to the ability to say it back? On one influential model, speech is processed along two streams that leave auditory cortex [](#f-speech-streams). A ventral stream runs forward and down through the temporal lobe, largely in both hemispheres, and maps sounds onto meanings. A dorsal stream runs back to the end of the deep groove above the temporal lobe and then forward to the frontal lobe, mainly in the left hemisphere, and maps sounds onto the movements of speaking. If the streams are separate, damage can impair understanding speech while sparing repeating it, or the reverse.

![Two streams for speech on one influential model. From auditory cortex, a ventral stream runs forward through the temporal lobe and maps sounds onto meanings, largely in both hemispheres. A dorsal stream runs back to the end of the groove above the temporal lobe and then forward to the frontal lobe, and maps sounds onto the movements of speaking, mainly in the left hemisphere. Locations are approximate (after Hickok and Poeppel, 2007, Fig. 1b).](reading_images/fig-speech-streams.svg){#f-speech-streams alt="A side view of a left hemisphere, front at the left, with a shaded patch on the upper surface of the temporal lobe labeled auditory cortex. A solid arrow runs from it forward and down along the temporal lobe, labeled ventral stream: sound to meaning, in both hemispheres. A dashed arrow runs from it back and up, then curves forward above the groove to the frontal lobe, labeled dorsal stream: sound to the movements of speaking, mainly left."}

The two streams for speech follow the same organizing idea as the two visual streams. In Modules 7 and 8, we described a ventral visual stream for recognizing objects and a dorsal visual stream for guiding action. The speech streams also separate recognizing from acting, in different pathways. The match is partial, since the dorsal stream for speech matches only the action half of the visual dorsal stream. Other researchers place the decoding of speech sounds further forward, and give the dorsal stream a role in locating sounds as well. So the brain may reuse one arrangement across senses, with details that are still argued.

### §13.3.6 — Two Hemispheres

Does language depend on one side of the brain? In Module 6, we described **lateralization**, a difference between what the left and right sides of a brain do, in animals as different as chicks and schooling fish. In most people, language is lateralized too. It depends more on the left hemisphere than on the right, but not on the left alone.

The clearest evidence about the two hemispheres comes from people whose **corpus callosum**, the great bundle of fibers connecting the hemispheres, was cut to treat severe epilepsy. Michael Gazzaniga and his colleagues tested such patients from the early 1960s. A word or picture flashed for less than about 200 milliseconds to one side of the point a person is looking at reaches only the opposite hemisphere. The patients named a word flashed to the right side, which reached the left hemisphere, but said they had seen nothing on the left side. Yet with the left hand, which the right hemisphere controls, they could pick out the object named on the left [](#f-split-brain-test). Speech almost always came from the left hemisphere. Clear language in the right hemisphere appeared in only a few of dozens of patients, and those right hemispheres understood some words but not word order. A few patients began to speak single words from the right hemisphere years after surgery, one after about 13 years. So a hemisphere that cannot speak can still understand some language.

![A split-brain test. While the person looks at a central dot, one word is flashed to each side. The word on the right reaches the left hemisphere, which speaks, so the person names it and reports seeing nothing else. The word on the left reaches only the right hemisphere, which guides the left hand to pick out the matching object under the screen (after Gazzaniga, Ivry, and Mangun, 2014, Fig. 4.13).](reading_images/fig-split-brain-test.svg){#f-split-brain-test alt="A screen at the top shows the word KEY to the left of a central dot and RING to the right. Below, a head seen from above contains two hemispheres, labeled left and right, separated by a dashed line labeled corpus callosum cut. A line runs from KEY to the right hemisphere and from RING to the left hemisphere, crossing on the way. A box beside the left hemisphere says the person says ring, and saw nothing else, with a note that speech comes from the left hemisphere. A box beside the right hemisphere says the right hemisphere guides the left hand to pick out the key among objects under the screen."}

The speaking hemisphere also readily explains actions whose cause it did not see. One patient’s left hemisphere was shown a chicken claw, and his right hemisphere a snow scene. His right hand chose a picture of a chicken, and his left hand a picture of a shovel. Asked why, he answered, “Oh, that’s simple. The chicken claw goes with the chicken, and you need a shovel to clean out the chicken shed”. Gazzaniga and a colleague called this capacity the **interpreter**. The evidence comes from a few patients, who do not report feeling divided. So a fluent explanation of one’s own behavior can be produced without access to its cause.

Handedness shifts the chance that language is on the right, but does not settle it. About one person in ten is left-handed. In one study, about 4% of the most strongly right-handed people had language mainly in the right hemisphere, and about 27% of the most strongly left-handed [](#f-handedness-language). The share rose gradually with the strength of left-handedness. So most left-handers also have language mainly on the left, and the old rule that left-handers have language on the right is false.

![The percentage of people with language mainly in the right hemisphere, in seven groups from the most strongly left-handed to the most strongly right-handed, with the number of people in each group. Most people in every group, including the most strongly left-handed, have language mainly on the left (data from Knecht et al., 2000, Fig. 3).](reading_images/fig-handedness-language.svg){#f-handedness-language alt="A dot plot with seven handedness groups along the horizontal axis, from most strongly left-handed at the left to most strongly right-handed at the right, and the percentage with language mainly on the right on the vertical axis, from 0 to 40 percent. The values, from left to right, are 27, 27, 22, 11, 10, 6, and 4 percent, for groups of 37, 26, 50, 18, 40, 48, and 107 people. Each dot has a vertical bar showing one standard error."}

Lateralization is a property of particular functions, not a type of person. In resting brain scans of 1,011 people aged 7 to 29, a person strongly lateralized in one network was not more lateralized in the others, so there are no left-brained and right-brained types. Lateralization for language also develops. In one sentence task, right frontal activity appeared in about 90% of children aged 4 to 6 and about 14% of adults, although maps averaged over each age group showed only left activity at every age. The right hemisphere also contributes to the melody and emotion of speech. So language is left-weighted, not left-only.

### §13.3.7 — Prediction in the Brain, and Brains Compared with Models

In §13.2.9, we described how listeners anticipate words before they hear them. Does the brain register how expected each word is? In 1980, Marta Kutas and a colleague recorded electrical activity from the scalp while people read sentences. When a sentence ended with a word that did not fit, a negative response peaked about 400 milliseconds after the word. This response, the **N400**, is larger the less expected a word is [](#f-n400). Its size tracks how often people complete a sentence with that word, with correlations as high as 0.9. Whether the N400 is a signal of a failed prediction has not been established. But the brain registers how expected each word is.

![The N400. A brain response recorded from the scalp peaks about 400 milliseconds after a word appears, and it is larger the less expected the word is. Negative voltage is plotted upward, as is conventional. The waveforms are schematic, not data (after Kutas and Hillyard, 1980, and Federmeier, 2022, Fig. 1b).](reading_images/fig-n400.svg){#f-n400 alt="Three schematic waveforms against time after a word appears, from 0 to 800 milliseconds, with negative voltage plotted upward. All three are flat and nearly identical until about 250 milliseconds. Then each rises to a peak at about 400 milliseconds, marked by a dashed vertical line, and falls again. The peak is smallest for an expected ending, larger for a less expected ending, and largest for an unexpected ending."}

The brain also predicts during natural listening, word by word. When people listened to stories, a language model’s measure of how surprising each word was predicted their brain responses to every word. In patients with electrodes placed on the brain for medical reasons, activity before a word predicted which word was coming. So listeners’ brains predict continuously, not only at the end of a sentence.

Activity inside language models can also be compared with brain activity. Researchers fit the numbers in a model’s layers to brain responses to the same sentences, and score how well the model’s numbers predict the brain’s responses, a *brain score*. Models that predict the next word better have tended to fit the language network better, up to a point. Models trained on far less text than modern systems already fit well. So next-word prediction captures something that the language network’s responses also reflect, on these measures.

Those fits need checking. A 2024 reanalysis, not yet peer reviewed, examined one large model’s brain score on the original sets of sentences. The length of each sentence and its position in the passage alone explained 39% and 61% of the score on two sets. Adding the fixed meanings of words, and simple facts about their senses and grammar, raised that to 90% and 98%. So a model that fits brain data need not compute as the brain does. This is the distinction between the same output and the same computation that we drew for theory of mind in Module 11.

<!-- MERGE 3 of 3: goes after §13.3, at the end of the file -->

## Close — Language, Minds, and Machines

At the start of this module, a sentence about a goat and a mail carrier was understood at once, although no one had written it before. We can now say some of what understanding it required, and what we still cannot say.

Language solves a problem of communication, and possibly a problem of thought. Other animals’ signals change what others do, but no taught animal produced combinations that grew in length and structure as a child’s do. The body was not the limit, and when language arose is inferred, not observed. A child learns from far less input than a language model does.

A listener hears speech in categories that a language sets, and a learner finds words with statistics and works out what they refer to across scenes. Whether people learn rules or statistics, and how much a child’s input lacks, are still disputed. Recursion is one proposal, set against the limits of what people actually produce. Prediction connects listeners, the simple recurrent network, and the transformer, and models that learn from co-occurrence absorb both meaning and bias. Such models are strong on the form of language and uneven in using it.

In the brain, speech depends on fine control of the voice, *FOXP2* is not a gene for language, and most researchers treat the classic model as history. A language network is separate from the regions used for hard tasks of many kinds, language is left-weighted, and comparisons between brains and models need checking.

In Module 14, we take up what language and symbols do for thought, including the thought view of §13.1.1, and the dispute between symbols and networks. In Module 15, we take up language as a cultural technology, including writing and reading.

## Further Reading

Eight books to read next. Several of their authors disagree with one another.

**Dorothy L. Cheney and Robert M. Seyfarth, *How Monkeys See the World: Inside the Mind of Another Species*, University of Chicago Press, 1990.** The playback studies of vervet monkey alarm calls, and what they suggest about what monkeys know of one another and of their world.

**Sue Savage-Rumbaugh and Roger Lewin, *Kanzi: The Ape at the Brink of the Human Mind*, Wiley, 1994.** The story of the bonobo who learned symbols by watching, told by the researcher who raised and tested him.

**Susan Goldin-Meadow, *The Resilience of Language: What Gesture Creation in Deaf Children Can Tell Us About How All Children Learn Language*, Psychology Press, 2003.** What deaf children who invent their own gesture systems reveal about which parts of language a child brings to learning it.

**Robert C. Berwick and Noam Chomsky, *Why Only Us: Language and Evolution*, MIT Press, 2016.** The case that language is mainly an instrument of thought, built on recursion, and that it arose recently and only in our species. Read it beside the next book, whose authors disagree on nearly every point.

**Morten H. Christiansen and Nick Chater, *The Language Game: How Improvisation Created Language and Changed the World*, Basic Books, 2022.** The case that language is learned from experience, as a skill improvised in conversation and passed on, with no built-in grammar.

**Michael S. Gazzaniga, *Tales from Both Sides of the Brain: A Life in Neuroscience*, Ecco, 2015.** A personal history of the split-brain studies, including the interpreter, by the researcher who led them.

**Christopher Summerfield, *These Strange New Minds: How AI Learned to Talk and What It Means*, Viking, 2025.** A neuroscientist and AI researcher’s account of how language models work, and of what they do and do not share with human minds.

**Steven Pinker, *The Language Instinct: How the Mind Creates Language*, William Morrow, 1994.** The classic argument for a built-in capacity for language, written for general readers. Read it as one side of the debate in §13.2.7, with Christiansen and Chater as the other.

## Glossary

**aphasia** — A loss or impairment of language caused by damage to the brain.

**arbitrariness** — The property of a signal that need not resemble what it is about, so that a language can have a signal for anything.

**attention** — In a transformer, the computation by which each position in a text uses information from earlier positions, giving more weight to earlier positions that match it better.

**behavioral modernity** — A set of behaviors, including standardized tools, ornaments, images, and the exchange of materials over long distances, that appears close together in the European archaeological record from about 50,000 years ago.

**benchmark** — A fixed set of test items used to compare AI systems. A benchmark score is a sample of what a model does on particular items, not a measure of an ability.

**categorical perception** — Sorting stimuli that vary continuously into categories, so that differences across a category boundary are heard or seen much more readily than equal differences within a category.

**compositionality** — The property of a language in which the meaning of a sentence is built from the meanings of its words and the way they are combined.

**convergent evolution** — The process that produces analogies, in which two lineages converge on the same solution from different starting points. Convergence is also evidence that the problem being solved was a real one rather than one invented after the fact to fit the finding.

**corpus callosum** — The great bundle of fibers connecting the two hemispheres in placental mammals. Other vertebrates connect their hemispheres through smaller commissures.

**critical period for language** — A period during which experience with a language has an outsized and lasting effect on what a learner ends up able to do with it.

**displacement** — The ability to talk about things that are far away in space or time.

**distributional semantics** — Describing the meaning of a word by the contexts it occurs in, on the proposal that words that occur in similar contexts tend to have similar meanings.

**duality of patterning** — The combining of a small stock of sounds that mean nothing on their own into a great many signals that do have meanings.

**embedding** — A list of numbers for a word, learned from its contexts so that words used alike have similar lists.

**formal competence** — The ability to get the form of language right.

**functional competence** — The ability to use language to accomplish things in the world, which depends on reasoning and on knowledge of the world and of other people.

**hallucination** — A fluent, confident statement from a language model that is false.

**implicature** — A meaning that a listener infers from what a speaker says, beyond what the words themselves say.

**interpreter** — A proposed capacity of the speaking, usually left, hemisphere to produce explanations of behavior, including behavior whose cause the hemisphere has no access to.

**language** — A learned, shared system that combines a finite set of signals into an unbounded number of messages.

**language model** — A model trained to predict the next token in a text from the tokens before it.

**language network** — A set of regions, usually in the left frontal and temporal lobes, that respond more to sentences than to strings of nonwords, whether heard or read.

**lateralization** — A difference between what the left and right sides of a brain do.

**meaning** — On most accounts, the mental representation linked to a word. On another view, knowing a word’s meaning is nothing more than knowing how to use the word and respond to it.

**mental lexicon** — A person’s knowledge of the words of their language, each with its sound and its meaning.

**Morgan’s Canon** — C. Lloyd Morgan’s 1894 principle that a behavior should not be explained by a higher mental process if a simpler one accounts for it. A guard against anthropomorphism, though one that has to be applied with care, since refusing a system a capacity it has earned is its own error.

**morpheme** — The smallest unit of a language that has a meaning, such as *glove* or the plural *-s* in *gloves*.

**multiple-demand network** — A set of regions in the frontal and parietal lobes of both hemispheres that become more active as many different kinds of task become harder.

**N400** — A negative brain response, recorded from the scalp, that peaks about 400 milliseconds after a meaningful word and is larger the less expected the word is.

**overregularization** — Applying a regular pattern of a language to an exception, as in *goed* for *went*.

**phoneme** — One of the smallest units of sound that can change one word into another, such as each of the three in *cat*.

**poverty of the stimulus** — The argument that children come to know things about their language for which the speech they hear contains no adequate evidence, so that some of that knowledge must be innate.

**pragmatics** — How a sentence is used in a situation, and how context of all kinds alters the meaning of a sentence.

**pretraining** — The first stage of training a language model: training it to predict the next token across a very large amount of text.

**productivity** — The ability to say things that have never been said before, and to be understood.

**recursion** — Building a structure with an operation that can apply to its own output, so that a structure of one kind can contain another of the same kind.

**reference** — What a word picks out in the world, such as the things or events it is used to talk about.

**semantics** — What words and sentences mean.

**simple recurrent network** — A network that predicts the next word from the current word and a copy of its own previous state.

**statistical learning** — Learning regularities from exposure alone, without instruction or reward.

**syntax** — The way words combine into phrases and sentences.

**token** — A word or a piece of a word, chosen by how often it occurs in text, that a language model takes as its unit.

**transformer** — A model built from stacked layers of attention, each followed by a small network applied to each position.

**transitional probability** — The probability that one item, such as a syllable, follows another.

**universal grammar** — A proposed set of principles, shared by all human languages and present at birth, that limits the grammars a child will consider.

**vocal learning** — Learning to produce new sounds, or to change sounds, by imitating sounds that are heard.
