There were five AIs. Four of the five followed perfectly deterministic strategies as long as noise is set to 0.

### Michael - Random
Michael did not try to predict or respond to the opponent at all.
He simply chose each move with equal probability.
With noise set to 0, he was still unpredictable — his behavior contained no structure.
This made Michael a useful “baseline” opponent. 
Any improvement over random play suggests that a strategy is exploiting patterns or using memory.

### Kevin: Nice / Dove / Always-Cooperate
Kevin always cooperated, assuming noise = 0.
He never initiated defection, and he never retaliated — even if repeatedly exploited.
Kevin represents an extreme trust-first strategy.

### Angela: Mean / Hawk / Always Defect
Angela always defected when noise = 0.
She never cooperated, regardless of the opponent’s behavior.
Angela represents a pure exploitation strategy.
She avoids being exploited herself but prevents cooperation and mutual benefit.

### Pam - Tit for Tat (TFT)
Pam used a classic reciprocity rule:
- First move: Always cooperate
- Every subsequent move: Repeat the opponent’s last move (if noise = 0)

Pam effectively “mirrors” others:
- With Kevin or another TFT agent, she cooperates indefinitely
- With Angela, she cooperates only once, then defects forever
- Withh Michael, she appears random, because she copies his chaotic play
This strategy rewards cooperation and punishes defection 
— a simple theory-of-mind model based on memory (“what did you do last time?”).

### Oscar - Win-Stay, Lose-Shift (WSLS)
Oscar followed a conditional strategy designed to stick with what’s working and change when it isn’t:
- If the previous outcome was beneficial (he exploited or mutually cooperated), he repeats his last move
- If the previous outcome was harmful (he was exploited or mutually defected), he switches moves

Oscar is more flexible than Tit-for-Tat: where Pam often stays locked in retaliation once trust breaks down, Oscar sometimes restores cooperation after mutual conflict.

In practice (with noise = 0):

| Last Round Outcome                              | Oscar’s Interpretation | Next Move        |
|-------------------------------------------------|------------------------|------------------|
| **Mutual cooperation**                          | “This is working”      | Cooperate again  |
| **You defect & Oscar cooperates** *(Oscar loses)* | “That hurt”            | Switch to defect |
| **Mutual defection**                            | “This is not great”    | Switch to cooperate |
| **Oscar defects & you cooperate** *(Oscar wins)* | “That worked”          | Defect again     |

### Noise and AI Behavior (Important Note)
All strategies above behave exactly as written only when noise = 0.
With noise > 0, each agent still attempts to follow its rule, but:
- On each move, with probability = noise, its chosen action flips
- This models real-world uncertainty, mistakes, or impulsivity