# Lab 13

In the Opening of the reading, we began with a sentence that no one had written before and that anyone who knows English understands at once. In §13.2.1 we asked what a listener has to work with when such a sentence arrives, and what a learner has to work with when a language arrives for the first time. In this lab you follow that question up the levels of §13.2.1: from the sound, to the word, to what the word refers to, to the word that comes next.

In this lab you take three positions. In Part 1 you are the listener: you read pictures of sounds, label syllables by what you hear, and then train a small network to label them. In Parts 2 and 3 you are the learner: you hear a made-up language with no pauses and find its words, and you hear new words with new objects and work out what each one names. In every part you are also the experimenter: you run programs that find words, learn reference, and predict the next word, and you compare what they do with what you and the people in the published studies did.

Three threads run through the lab, and they are the reading’s. The signal does not come labeled (§13.1.8, §13.2.2, §13.2.3): one speech sound has many physical forms, a stream of speech has no marked word boundaries, and a word heard in a scene could name many things in it. Statistics in the input go a long way (§13.2.2, §13.2.3, §13.2.4, §13.2.10): which syllable follows which marks the words, which object comes with which word marks what the words refer to, and which words occur near which marks what the words are like. And a procedure is judged by what it predicts, step by step (§13.2.4, §13.2.9, §13.2.12): Part 3 compares two accounts by what each one does after a wrong guess, and Part 4 opens three predictors and shows what each one’s prediction depends on.

Two rules run through every part. The first is the rule of the lab, which you have followed since Lab 6: nothing an experiment would tell you is shown until you commit your answers. The second is a distinction we have kept since Lab 7. You are the only one in this lab who hears, remembers, and chooses. Every learner, every model, and every predictor is a program with a procedure, and a line on each panel says so. Several of them learn, and they learn by rules too.

Plan on about 80 minutes. The lab is built to be left and returned to, as explained under *How the lab is laid out*, below.

## Part 0: Opening the Simulation (≈3 minutes)

1. Open the simulation in your web browser: [Sounds, Words, and Predictions](https://jonwillits.github.io/bcogapp/#/m13-language). It runs in any modern browser, and there is nothing to install. Nothing you do is sent anywhere; your results stay in the browser.
2. Download the lab report Microsoft Word document. It is available here: [Lab 13 Report](https://github.com/jonwillits/intro_to_bcs/blob/master/language/sounds_words_lab/sounds_words_lab_report.docx). This document is what you will turn in to the course website.

### The five tabs

- **Open** is Part 0: the general instructions, your saved progress, and your gathered results.
- **Sounds** is Part 1: spectrograms, six syllables to label, a series of synthetic syllables, and a classifier.
- **Stream** is Part 2: a minute of a made-up language, its words found from counts, three learners, and real speech.
- **Words** is Part 3: new words with new objects, a test, and two models of what you did.
- **Predictors** is Part 4: a corpus, a count model, a simple recurrent network, and a transformer.

Under the tabs on every part sit a line saying that your results are saved in this browser on this computer only, and the **Run seed**, which fixes the order of the syllables, your stream of the made-up language, which word names which object, and the order of every trial. Your seed differs from your neighbor’s, so your numbers will be close to theirs and not identical.

### How the lab is laid out

The window holds two panels. The navigation panel, on the left, has the part tabs, each part’s step buttons, your progress, and the buttons that move you on. The main panel, on the right, has two tabs of its own: **This Step**, which shows the step you are on, and **All Results**, which gathers every finished step’s results. Every part, and every step within a part, opens with a screen in the main panel that says what you will do, about how long it takes, whether you must finish it in one sitting, and what keys or buttons it uses. Read it, then press **“Begin”**. Each screen ends with a section headed *When you are done*, which names the button that comes next.

Your progress is saved in this browser on this computer. A step you have finished does not need to be redone. The experiments behave in one of two ways if you leave them partway, and each screen says which. Part 1, Step 2, Part 2, Step 1, and Part 3’s Steps 1 and 2 start over from their beginning, in Part 3 with a new set of words and objects. The blocks of Part 1, Step 3 are saved as each one ends, and a block you leave partway starts again. Part 2, Step 2 is saved as you go, and goes on from where you stopped. The explorations can be left and returned to; your predictions stay committed. No tab is locked. The parts can be done in any order, and nothing in one of them tells you what another tests. Four steps show how another step’s material is divided, and before each of those opens you will see one line and two buttons: open anyway, or go to the step it depends on. If you need to move to another computer, **“Export my results”** on the Open tab writes a small file, and **“Load my results”** on the other computer reads it.

**Do not press “Clear my saved results”** unless you mean to start the whole lab again with a new seed. A second run is not a first run: someone who knows what an experiment tests is no longer a naive subject, and the screen says the same before it lets you.

Parts 1, 2, and 3 play sound. Use headphones or earbuds if you have them. Press **“Play a test sound”** on the Open tab to hear a short tone and set a comfortable volume once. Every sound in this lab was made by a computer before the lab was posted; nothing is recorded from you.

## Part 1: Sounds (≈21 minutes)

### Step 1 — Reading a spectrogram

**Goal.** In §13.2.2 we said that the first problem for a listener is to hear which speech sounds were said, and that no acoustic property marks a speech sound in every context. To see why, you need to be able to read a picture of a sound. Step 1 is an exploration on one synthesized vowel and then on three.

**Instructions and What to Record.** Open the Sounds tab, read the screen, and press **“Begin”**. There are seven screens, chosen by **“Next”** and **“Back”** or by a name at the top of the panel, and each has a **“Play”** button. Screens 1 to 4 are about one sound, the vowel *ah*: time runs from left to right, frequency from bottom to top, and brightness shows energy. On screen 4, switch between **“Wide bands”** and **“Narrow bands”**. In the narrow-band view you see thin, evenly spaced horizontal lines, the harmonics of the voice; the lowest is the pitch. In the wide-band view you see broad bright bands, the formants, the frequencies at which the throat and mouth resonate. On the Pitch screen, choose a prediction and press **“Commit my prediction”** before the two spectrograms appear. Then look at the Voice screen and the Vowels screen.

- **Q1.** Report your prediction on the Pitch screen and what the two spectrograms showed: when the pitch of *ah* went from 100 Hz to 200 Hz, did the harmonics move, the formants, both, or neither? Then report what the Voice screen showed when every formant was raised by 15% at the same pitch. In one or two sentences, say what the harmonics depend on and what the formants depend on, and which of the two makes one vowel sound different from another.

- **Q2.** Fill in the table from the Vowels screen, reading each vowel’s first and second formant from the marked lines or from the plot under the three spectrograms.

| Vowel | First formant, Hz | Second formant, Hz |
|---|---|---|
| *ee* | | |
| *ah* | | |
| *oo* | | |

### Instructions for Step 2

**Read only this section before you start Step 2, and do not read past the line marked below until Step 2’s results screen is up.** Step 2 is an experiment on what you hear, and reading about the syllables first would change what it measures.

**Step 2 — One consonant, different neighbors.** Press **“Go on to Step 2”**, read the screen, and press **“Begin”**. Six spectrograms appear without labels, in an order drawn by your seed. Each syllable begins with *b* or *d* and ends in *ee*, *ah*, or *oo*. Press **“Play”** under each one as often as you like, and label it **“b”** or **“d”** by what you hear. When all six are labeled, press **“Commit my labels”**.

---

**Do not read on until Step 2’s results screen is up.**

---

### What Step 2 tested

The six syllables were *bee*, *bah*, *boo*, *dee*, *dah*, and *doo*, spoken by one synthetic voice. After you commit, the six spectrograms are named in the center, each with its measured first and second formant tracks over the first 100 milliseconds after the consonant’s release, and your six labels sit beside the right ones on the right, with the number correct out of 6. Under the six, a section headed *The same consonant in different contexts* says what the tracks show, and an optional screen, **“Show voice timing”**, shows *tot* and *dot* with the gap between the release and the start of voicing marked.

- **Q3.** Report your number correct out of 6. For each of the six syllables, say from its drawn track whether the second formant rose or fell into the vowel over the first 100 milliseconds. In §13.2.2 we said that the same consonant sounds a little different before different vowels, so that a listener cannot recognize speech sounds by matching them to fixed patterns. Using your six tracks, say what *b* and *d* have in common across their three vowels, and what differs, and say why a listener who looked for one fixed pattern for *d* would fail.

### Instructions for Step 3

**Read only this section before you start Step 3, and do not read past the line marked below until Step 3’s results screen is up.** Step 3 is an experiment on how you sort sounds into categories, and reading about the series first would change what it measures.

**Step 3 — Labeling and telling apart.** Press **“Go on to Step 3”**, read the screen, and press **“Begin”**. There are two blocks, each on its own screen with its own start button. In block 1, 54 trials, you hear one synthetic syllable three times and press **“B”** or **“D”**, or the keys B and D. In block 2, 28 trials, you hear three syllables; the first two differ, the third is the same as one of them, and you press **“3rd sounds like the 1st”** or **“3rd sounds like the 2nd”**, or the keys 1 and 2. There is no feedback in either block. Each block runs in real time; keep the tab in front of you until it ends.

---

**Do not read on until Step 3’s results screen is up.**

---

### What Step 3 tested

The syllables were nine steps of a synthetic series of the kind we described in §13.2.2: nine sounds that differ only in where the second formant begins, from 1,320 to 2,280 Hz in steps of 120 Hz, with everything else the same. Block 1 played each of the nine six times. Block 2 played pairs of sounds two steps apart, four times each, with the third sound matching one of the two. The results screen has six numbered sections. Section 1 draws your two labeling curves, the share of trials on which you pressed *b* and the share on which you pressed *d*, across the nine sounds. Section 2 draws how often you told each pair apart, across the seven pairs. Section 3 computes, from your labels alone, how often you should have told each pair apart if you could hear only the label, by the formula the 1957 paper used, and draws that line over your own. Section 4 says where your boundary between *b* and *d* fell. Section 5 shows the one listener from the figure in §13.2.2 over the same nine sounds. Section 6 states what the 1957 paper found about the prediction, and the mean gap between your told-apart curve and the predicted one.

- **Q4.** Fill in the table from Sections 1 to 4.

| | Your value |
|---|---|
| The sound at which your labels crossed from mostly *b* to mostly *d* (Section 4) | |
| The pair you told apart most often, and how often (Section 2) | |
| The pair you told apart least often, and how often (Section 2) | |
| The mean gap between your discrimination and the prediction from your labels (Section 6) | |

- **Q5.** Step 3’s reveal draws your own curves. In §13.2.2 we described **categorical perception**: listeners switch abruptly between labels with small changes in the signal, and tell two sounds apart far more readily when the sounds tend to be given different labels. Say whether your own labeling curves switched abruptly or gradually, and whether your told-apart curve peaked at your boundary and dipped away from it. Then compare your curves with the 1957 listener’s in Section 5. Section 6 states that the 1957 listeners told pairs apart somewhat better than their labels alone predicted. Say whether your own gap was in the same direction, and what a told-apart score above the prediction means about what a listener hears within a category.

### Step 4 — A classifier learns the labels

**Goal.** In Module 7 you trained a network with a hidden layer to sort patterns by a passed-back error. Step 4 trains a network of the same kind on spectrogram patches of natural syllables, and asks how it generalizes to voices and pitches it never learned from, and what it does with the synthetic series you just heard. Step 4 is an exploration.

**Instructions and What to Record.** Press **“Go on to Step 4”**, read the screen, and press **“Begin”**. The panel states what the network takes in: 400 numbers for each syllable, the energy in 40 frequency bands over 10 frames of 10 milliseconds, cut from the same spectrogram you see; 12 hidden units; 3 outputs, one for each of *b*, *d*, and *g*. The training sounds are *b*, *d*, and *g* before five vowels, from 12 synthetic voices, each at its own pitch and at two shifted pitches, 540 syllables in all; voices 11 and 12 are held out. Before each run, choose a prediction and press **“Commit my prediction”**. In run 1, press **“Train”**. In run 2, press **“Train on one pitch”** and **“Train on one voice”**. In run 3, press **“Run on the 9 sounds”**. The panel states each run’s result when training ends.

- **Q6.** Fill in the table from the three runs, and report your three predictions.

| Run | What the network was trained on | What it was tested on | Percent correct, or the labels | Your prediction, and was it right? |
|---|---|---|---|---|
| 1 | | | | |
| 2, one pitch | | | | |
| 2, one voice | | | | |
| 3 | the run 1 network | the 9 sounds of Step 3 | | |

- **Q7.** The network never receives a voice’s number, a pitch, or a vowel, only the 400 numbers. Say what run 1 shows about whether what it learned from ten voices applies to two it never heard. Run 2 trained it on far fewer syllables in two ways, one pitch from every voice or one voice at three pitches. Say which of the two lowered the score more, and, using what Step 1 showed about pitch and formants, why training on one voice gives the network less to learn from than training on one pitch does. In run 3, the network labeled the synthetic series of Step 3. Report the order of its labels across the nine sounds, say whether it crossed from *b* to *d* as you did, and read the panel’s explanation of why the synthetic sounds, which have no energy above about 2,500 Hz, are unlike any natural syllable the network learned from.

## Part 2: Stream (≈16 minutes)

### Instructions for Step 1

**Read only this section before you start Step 1, and do not read past the line marked below until Step 1’s results screen is up.** Step 1 is an experiment on what you can hear in a language you do not know, and reading about the language first would change what it measures.

Before you begin, reread §13.1.8 and §13.2.3 of the reading, on the stream of speech and the words in it.

**Step 1 — A minute of the language.** Open the Stream tab, read the screen, and press **“Begin”**. Press **“Play the minute”**. A synthetic voice speaks a made-up language for 60 seconds with no pauses between its words, and a large timer counts down. Listen, and try to find the words. When the minute ends, answer one question, how many different words the language has, from a list from 1 to 20, and type any words you think you heard in the box under it, as they sound. Then press **“Commit my answer”**.

---

**Do not read on until Step 1’s results screen is up.**

---

### What Step 1 tested

The language has six words, each of three syllables, built from twelve syllables, and the minute was 72 words in a row in a random order, with no pause between them, as in the experiment we described in §13.2.3. The results screen shows your answer beside the number of words the language has, and the words you typed. It does not name the words: finding them is Step 2.

- **Q8.** Report how many words you answered and which words you typed. In §13.1.8 we said that fluent language has no reliable pauses between words. Say what you had to go on in the minute, and what you could not hear.

### Step 2 — Find the words

**Goal.** In §13.2.3 we described one way to find words in a stream: track which syllables tend to follow which. Step 2 gives you the counts from the first 300 syllables of your own stream, and nothing else, and asks you to find the six words. Step 2 is an exploration, saved as you go.

**Instructions and What to Record.** Press **“Go on to Step 2”**, read the screen, and press **“Begin”**. Click a syllable in the palette to highlight it; the panel of counts then lists how many times it occurs in the 300 syllables, which syllables come right after it and how often, and which come right before it. Build a word in the tray by dragging tiles from the palette or by pressing **“Add to the tray”**, and press **“Check this word”**. A word that is one of the language’s joins *Words found* in a color of its own, and a wrong check is not counted against you. If you cannot find a word, press **“Show me the words”** to end the search. When every word is found or shown, the results appear in five numbered sections: the 300 syllables printed and divided into words, the minute of Step 1 again with its words marked and with each word’s last syllable lengthened, the six words in the order you found them, the table of transitional probabilities from your whole stream, and each word’s average transitional probability inside it.

- **Q9.** Fill in the table from Section 3 of the results.

| Order found | The word | Words you checked before it | Found, or shown? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

- **Q10.** In §13.2.3 we defined the **transitional probability** from one syllable to the next, and said that transitions with low transitional probabilities are a good cue to word boundaries. Pick one pair of syllables inside a word and one pair that spans a boundary between two words, read their counts from the panel after the search has ended, and compute each pair’s transitional probability as the count of the pair divided by the count of the first syllable. Then read the same two values from the table in Section 4, and say what the shaded cells in that table have in common. Section 5 reports that in the original experiment the three words with the highest average transitional probabilities were learned better than the three with the lowest. Report which words your first three found were, and whether they were among the three highest.

- **Q11.** Press **“Play again, with the words marked”** and then **“Play again, with each word’s last syllable lengthened”**. Say what you heard differently in the second replay. The original experiment lengthened the last syllable of some words and not others, and the panel states what that did to learning. Using §13.2.3, say why a lengthened last syllable is a cue of a different kind from a transitional probability, and name one other cue to word boundaries that infants use in English.

### Step 3 — Three learners, and how much they hear

**Goal.** In §13.2.3 we called learning regularities like these from exposure alone **statistical learning**, and reported that 8-month-olds told the words apart after 2 minutes of a stream. Step 3 runs three programs on your stream, called learners here, and asks how much of the stream each needs to do what the adults and the infants did. Step 3 is an exploration with three predictions.

**Instructions and What to Record.** Press **“Go on to Step 3”**, read the screen, and press **“Begin”**. The panel opens on what the people did in the original experiments, then the three learners as three explanations of what people compute, and what would count as success for each. Read them, then choose your three predictions and press **“Commit my predictions”**. Press **“Run the learners”** once: each learner takes the test having taken in nothing, then after 30 seconds of your stream, then after every minute from 1 to 21, and the same is done on 19 other streams of the same language. The plot fills in as each amount is done, with the adults’ two means and the infants’ result marked. Under the plot are a table of eight amounts, four questions to answer from the plot and the table, and how each learner takes the test.

- **Q12.** Report your three predictions, and fill in the table from *Scores at eight of the amounts*.

| Learner, test | 30 seconds | 2 minutes | 21 minutes |
|---|---|---|---|
| Cut at the dips, against nonwords | | | |
| Cut at the dips, against part-words | | | |
| A simple recurrent network, against nonwords | | | |
| A simple recurrent network, against part-words | | | |
| PARSER, against nonwords | | | |
| PARSER, against part-words | | | |

- **Q13.** The adults in the original experiment scored 76% against nonwords and 65% against part-words after 21 minutes, and the infants told words from both kinds of foil after 2 minutes. Say which learners reached the adults’ two scores, and with how much of the stream, and which told the words from the foils after the infants’ 2 minutes. Then answer the panel’s third question: which test was harder for each learner, and was it the one the adults found harder? Two of the three learners reach the adults’ scores with far less of the stream than the adults heard. Say what that could mean about the learners, and what it could mean about the test, and which of the two you find more likely.

- **Q14.** The three learners store different things: counts of pairs of syllables, the weights of a network trained to predict the next syllable, and a set of units with weights that grow as they recur. In §13.2.9 we described a **simple recurrent network**, which predicts the next item from the current one and a copy of its own previous state. Using the panel’s drawing of that learner and its plot of prediction error by syllable, say where in a word its error is high and where it is low, and why a learner that is never given the words can find their boundaries from that pattern alone. Then say what cut at the dips computes that the recurrent network never computes, and what the recurrent network has that cut at the dips does not.

### Step 4 — Real speech

**Goal.** In §13.2.3 we said that transitional probabilities are not the only cue to word boundaries, and that infants use several others. Step 4 shows real speech spoken to young children, written out as syllables, and runs the first learner of Step 3 on it. Step 4 is an exploration.

**Instructions and What to Record.** Press **“Go on to Step 4”**, read the screen, and press **“Begin”**. Choose an utterance from the menu. Above each pair of neighboring syllables is its transitional probability, computed over the whole sample of real speech, and the true word boundaries are marked under the strip. Press **“Show stress”** to mark the stressed syllables. Under the strip, a histogram compares transitional probabilities inside words with those across word boundaries, for real speech and for the made-up language, and a table gives two shares for the dips learner run on the whole sample.

- **Q15.** Fill in the table from *The dips learner on real speech*.

| | Real speech to children | The made-up language |
|---|---|---|
| Share of the learner’s cuts that fall on a word boundary | | |
| Share of word boundaries the learner found | | |

- **Q16.** Pick one utterance and report one pair of syllables inside a word whose transitional probability is lower than one pair across a boundary in the same utterance. Using the histogram, say how the two distributions differ between the made-up language and real speech, and why the same learner that found every word of the made-up language finds less than half of the boundaries in real speech. Then, using §13.2.3, name two other cues infants use, and say what the stressed syllables you marked show about one of them.

## Part 3: Words (≈14 minutes)

### Instructions for Steps 1 and 2

**Read only this section before you start Step 1, and do not read past the line marked below until the test’s results screen is up.** Steps 1 and 2 are one experiment on how you learn what new words refer to, and reading about it first would change what it measures.

Before you begin, reread §13.2.4 of the reading, on what a word refers to.

**Step 1 — Words and objects.** Open the Words tab, read the screen, and press **“Begin”**. On each trial, two objects appear and a word plays once. Press **“Hear it again”** to hear it again. Click the object you think the word names; if you are not sure, click anyway. Your choice shows for a moment, and the next trial begins. There are 60 trials. No one will say whether a choice was right.

**Step 2 — The test.** When the 60 trials are done, the test begins on its own: one trial for each word, with four objects on the screen. Click the object the word names. When the test is done, the results of both steps appear.

---

**Do not read on until the test’s results screen is up.**

---

### What Steps 1 and 2 tested

There were 12 made-up words and 12 objects, and each word named one object. Each word occurred 5 times in the 60 trials, each time with its own object and one other, and the other object was never the same object on more than two of a word’s five trials. The design is the one Trueswell and his colleagues used in 2013 to ask what a learner stores from a trial, which we describe in Step 3. The results screen has three numbered sections: your accuracy at each occurrence of a word, from the first to the fifth, as a line with chance at 50%; your test score out of 12, with chance at 25%; and every word spelled with its object and your five choices, each marked right or wrong.

- **Q17.** Fill in the table from Sections 1 and 2.

| | Occurrence 1 | Occurrence 2 | Occurrence 3 | Occurrence 4 | Occurrence 5 | The test, of 12 |
|---|---|---|---|---|---|---|
| Correct, of 12 words | | | | | | |
| Percent correct | | | | | | |

- **Q18.** In §13.2.4 we said that a word heard while a scene is in view could refer to many things in it, and that a learner can narrow the possibilities by combining many moments. We used the terms **reference** and **meaning** because the research does. Say what a single trial of Step 1 could and could not tell you about a word’s reference, and what the second occurrence of a word added. From Section 3, pick one word you got right on its last three occurrences and one you did not, and say from the row what happened on each one’s first two trials.

### Step 3 — Two models on your trials

**Goal.** In §13.2.4 we gave two accounts of how a learner works out reference across scenes: on one, the learner tallies which words occur with which things across all the scenes; on the other, the learner forms one guess for each word and checks it the next time the word occurs. We said that the infants’ results fit both accounts. Step 3 runs both accounts as programs on your own 60 trials, and compares them on the one measure that tells them apart. Step 3 is an exploration with one prediction.

**Instructions and What to Record.** Press **“Go on to Step 3”**, read the screen, and press **“Begin”**. The panel opens on what the adults of the original experiment did on the same trials, with their accuracy at each occurrence drawn as a line and yours drawn over it in white, and how they did after a right click and after a wrong one. Then come the two models as two explanations of what a person stores from a trial, and what would count as success for each. Choose your prediction and press **“Commit my prediction”**. Then press **“Next trial”** through six short trials made for the purpose, and watch each model’s pick and its memory under it. After you commit you see your own key measure, and in the section *You, the two models, and the adults*, press **“Run the models”**. Each model runs 200 times on your trials at the setting that matches your overall accuracy, and its row shows the mean and the range of the middle 90% of the runs. Move each slider, and press **“Back to the fitted value”** to return it.

- **Q19.** Report your prediction, and fill in the table from your key measure and the rows. For the two models, copy the mean and the bracket.

| | After a right choice | After a wrong choice | Overall, occurrences 2 to 5 |
|---|---|---|---|
| You | | | |
| Guess and check, at its fitted α | | | |
| Tallying, at its fitted β | | | |
| The adults of the original experiment | | | |
| Chance | | | |

- **Q20.** In the six demonstration trials, guess and check stored object B for *word 1* on trial 1, found it gone on trial 3, and picked at random, while tallying still had a count for object A and picked it. Say what each model stores from a trial and what each does not store, and why that difference appears only after a wrong pick. The adults were at chance after a wrong click and well above it after a right one. Say which model showed that pattern in your rows, and which did not. Then say whether your own row matched the adults’, and what that says about which account fits what you did.

- **Q21.** Your key measure rests on 48 pairs of choices, and the panel states how often 48 pairs separate the two models: near 60% accuracy, almost never; at about 85% and above, most of the time. Report your overall accuracy, and say how strongly your 48 pairs can decide between the two accounts. Move the α slider to 1 and the β slider to 0 and then to 8, and report what happens to each model’s share after a wrong choice. Say whether any setting makes guess and check above chance after a wrong choice, and what that shows about the models rather than about their settings.

## Part 4: Predictors (≈23 minutes)

### Step 1 — The corpus

**Goal.** In §13.2.9 and §13.2.12 we described programs that predict the next word, and in §13.2.13 we said that a model trained to do so learns from the text itself. Every program in Part 4 learned from one small made-up corpus, and from nothing else. Step 1 shows the corpus and the rules that made it. Step 1 is an exploration.

**Instructions and What to Record.** Open the Predictors tab, read the screen, and press **“Begin”**. The panel shows the vocabulary of 52 tokens in groups, the grammar as four rewrite rules with every symbol defined, and the rules the symbols leave out, among them that a verb agrees in number with the noun that begins the sentence even when a relative clause comes between them. Press **“Show me sentences”** for 20 sentences, and again for 20 more.

- **Q22.** Copy two sentences from the corpus, one with the word *who* and one without. For the sentence with *who*, say which noun is the subject of the main verb, which words make up the relative clause, and whether the noun before *who* is the subject or the object inside that clause, using the rule RC → VP | NP V as the panel reads it. In §13.2.8 we described recursion. Say how the grammar lets a relative clause contain another, and find or build a sentence of the corpus in which one does.

### Step 2 — A count model

**Goal.** In §13.2.10 we described **distributional semantics**: words that occur in similar contexts tend to have similar meanings, so the contexts a word occurs in are evidence about its meaning. Step 2 builds a count model of the corpus and shows what such a model recovers. Step 2 is an exploration with one prediction.

**Instructions and What to Record.** Press **“Go on to Step 2”**, read the screen, and press **“Begin”**. Choose your prediction, which noun will lie closest to *cat*, from the menu, and press **“Commit my prediction”**. Then press **“Count”**. The table of counts fills as the model moves its window through the corpus, with every token as a row and as a column. Under it are a demonstration of similarity on ten tokens, the tokens as points on a plane, the five nearest neighbors of any token you choose under **“Nearest neighbors of”**, and a tree of clusters.

- **Q23.** Report your prediction and fill in the table from *The nearest neighbors*, for *cat* and for one verb of your choice.

| Token | Its five nearest neighbors, nearest first | Their correlations |
|---|---|---|
| *cat* | | |
| | | |

- **Q24.** A token’s row of counts is its **embedding**, a list of numbers learned from its contexts so that tokens used alike have similar lists. Say what two tokens have to share, in this corpus, for their rows to be alike, and why *cat* and its nearest neighbor are alike although the two words may rarely occur next to each other. From the plane and the tree, say which groups of the vocabulary the model separated and which it mixed, and relate what it separated to the rules of the grammar in Step 1. In §13.2.10 we said that a program told nothing about meaning can recover some of it from which words occur near which. Say what the model recovered here, and what it could not have recovered from this corpus.

### Step 3 — What counts cannot do

**Goal.** In §13.2.9 we described a simple recurrent network that learned that after *boys who Mary chases* the next verb should be plural, to agree with *boys*, and in §13.2.10 we noted that a count model places words by their contexts and nothing more. Step 3 shows two things the counts of Step 2 leave out. Step 3 is an exploration with one prediction.

**Instructions and What to Record.** Press **“Go on to Step 3”**, read the screen, and press **“Begin”**. There are three screens, named at the top of the panel. On **“Order”**, two sentences with the same words in different orders stand side by side with what each adds to the table of counts; try the switch **“Count words before and after separately”** on and off. On **“Prediction from counts”**, choose your prediction and press **“Commit my prediction”**, then press **“Compute”**: for each of three prompts, the probability of each next token from the one word before it and from the two words before it, each a count divided by a count. On **“One point per word”**, the word *chases* in two sentences, and where its embedding lies in each.

- **Q25.** Report your prediction. From the *Order* screen, say whether the two sentences add the same counts with the switch off and with it on, and what the switch changes. From *Prediction from counts*, report, for the prompt *girls who dogs chase*, which kind of token the prediction from one word made most probable, which kind the prediction from two words did, and which kind the grammar allows next. Say why a prediction from counts of the last one or two words cannot agree with a noun three words back, and what we said in §13.2.9 about how a listener uses the words in between.

### Step 4 — A simple recurrent network and a transformer

**Goal.** In §13.2.9 we described a simple recurrent network, which compresses everything before the current word into one state, and in §13.2.12 a **transformer**, which consults every earlier position directly through **attention**. Both are programs trained to predict the next **token**, which is what a **language model** is. Step 4 runs both, trained on the corpus before the lab was posted, on prompts you build. Step 4 is an exploration with one prediction.

**Instructions and What to Record.** Press **“Go on to Step 4”**, read the screen, and press **“Begin”**. Read the drawing and the explanation of each network. Choose your prediction, which verb form each network will favor after *boys who Mary chases*, and press **“Commit my prediction”**. Build that prompt from the palette of tokens; the tokens the grammar allows next are outlined. Three bar charts show the probability of every token as the next one, from the prediction from counts, the recurrent network, and the transformer. Under them, for the transformer, lines run from the last token back to each earlier token, one panel for each layer and each attention computation, with the thickness of each line set by its weight. At the bottom, set **“Temperature”** and press **“Generate a sentence”** several times at two settings.

- **Q26.** Report your prediction, and fill in the table from the three bar charts after the prompt *boys who Mary chases*.

| Predictor | Probability of *chase* | Probability of *chases* | The most probable next token |
|---|---|---|---|
| Prediction from counts | | | |
| The recurrent network | | | |
| The transformer | | | |

- **Q27.** From the attention panels, report which earlier token gets the thickest line from *chases* in each of the four panels. In §13.2.12 we said that attention lets a model use any earlier word directly, weighted by its relevance to the current one, and in §13.2.9 that a simple recurrent network compresses everything before the current word into one state. Say what the transformer’s lines show that the recurrent network has no way to show, and whether the token it weighted most is the one the verb has to agree with. Then say why the two designs can still make the same prediction here.

- **Q28.** Generate five sentences at a temperature of 0.2 and five at 2.0, and report how many of each five the grammar allows. In §13.2.13 we said that a model generates text by sampling from its probabilities, and that temperature controls how strongly the sampling favors the most likely tokens. Say what changed between the two settings in the sentences themselves, and why a sentence the grammar does not allow can still come from a model that has learned the grammar’s statistics.

### Step 5 — Watching it learn

**Goal.** In §13.2.13 we called the first stage of training **pretraining**: training a model to predict the next token, where the text itself supplies the target. Step 5 shows eight snapshots of the two networks of Step 4, saved during that training, from before any training to its end. Step 5 is an exploration.

**Instructions and What to Record.** Press **“Go on to Step 5”**, read the screen, and press **“Begin”**. Move the **“Snapshot”** slider through the eight snapshots. At each one, the three bar charts show the next-token probabilities after the current prompt, the plot of agreement by depth shows the share of probe sentences on which each predictor favors the verb that agrees with its subject, with 0, 1, 2, and 3 relative clauses between them, and three tables list every snapshot’s held-out accuracy and agreement by depth. In every probe sentence, the noun just before the verb differs in number from the subject, so a predictor that went by the nearest noun would get every probe wrong.

- **Q29.** Fill in the table from the three tables under the plot.

| Updates | The transformer: agreement at depth 0 / 1 / 2 / 3 | The recurrent network: agreement at depth 0 / 1 / 2 / 3 | The count model: agreement at depth 0 / 1 / 2 / 3 |
|---|---|---|---|
| 200 | | | |
| 500 | | | |
| 3,000 | | | |
| 20,000 | | | |

- **Q30.** At 500 updates the recurrent network agrees with the subject on 0% of the probes with three relative clauses between. Say what it must have been using at that snapshot, and why every probe is built so that using the nearest noun gives the wrong verb. Then say what changed by 3,000 updates in each network, and whether the count model ever reached either network at depth 3. In §13.2.9 we said that the network of 1991 learned agreement across a relative clause only when given simple sentences first. Say whether that was needed here, and what in the plot is your evidence.

## Completing the Lab Assignment

- Make sure you answer all the questions in the document sounds_words_lab_report.docx.
- Make sure you have added everyone’s name on your lab report who worked on your lab.
- When you are done, submit the lab report document on the course website. Remember, even though you worked in a group, each lab member must submit their own lab report.
