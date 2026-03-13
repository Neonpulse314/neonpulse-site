---
title: "Pick Any Number. Follow Two Rules. It Always Seems to Reach 1. Nobody Can Prove Why."
date: 2026-03-06
description: "The Collatz Conjecture is the simplest unsolved problem in mathematics. You can explain it to a child. Terence Tao — the greatest living mathematician — worked on it and got partway there. Nobody has finished the proof."
tags: ["mathematics", "mystery", "number-theory", "unsolved"]
tier: 1
disciplines: ["Mathematics"]
mystery: true
---

Pick a number. Any number. Let's say 6.

If it's even, divide it by 2. If it's odd, multiply by 3 and add 1. Repeat.

6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1.

Try 27.

27 → 82 → 41 → 124 → 62 → 31 → 94 → 47 → 142 → 71 → 214 → 107 → 322 → 161 → 484 → 242 → 121 → 364 → 182 → 91 → 274 → 137 → 412 → 206 → 103 → 310 → 155 → 466 → 233 → 700 → 350 → 175 → 526 → 263 → 790 → 395 → 1186 → 593 → 1780 → 890 → 445 → 1336 → 668 → 334 → 167 → 502 → 251 → 754 → 377 → 1132 → 566 → 283 → 850 → 425 → 1276 → 638 → 319 → 958 → 479 → 1438 → 719 → 2158 → 1079 → 3238 → 1619 → 4858 → 2429 → 7288 → 3644 → 1822 → 911 → 2734 → 1367 → 4102 → 2051 → 6154 → 3077 → 9232 → 4616 → 2308 → 1154 → 577 → 1732 → 866 → 433 → 1300 → 650 → 325 → 976 → 488 → 244 → 122 → 61 → 184 → 92 → 46 → 23 → 70 → 35 → 106 → 53 → 160 → 80 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.

That took 111 steps. It peaked at 9,232. But it reached 1.

They always reach 1.

Every number anyone has ever tried reaches 1. Mathematicians have verified this for every number up to 2<sup>68</sup> — that's roughly 300 quintillion numbers. The sequence spirals and climbs and crashes, but it always, eventually, collapses to 1.

Nobody can prove it's true for all numbers.

Nobody even knows how to try.

---

## The Problem That Looks Like It Shouldn't Be a Problem

Lothar Collatz was a German mathematician who wrote the conjecture down in 1937 — possibly earlier. He reportedly kept it in a notebook for years before showing it to anyone, aware of how embarrassingly simple it looked.

The rule is two lines:
- If *n* is even: *n* → *n* / 2
- If *n* is odd: *n* → 3*n* + 1

The conjecture: for every positive integer, this process eventually reaches 1.

That's it.

You don't need calculus. You don't need abstract algebra. You need division and multiplication. A ten-year-old can understand the problem. A Fields Medalist cannot solve it.

Paul Erdős — the Hungarian mathematician who spent his life traveling between colleagues, sleeping on their couches, and co-authoring more papers than almost anyone in history — looked at the Collatz Conjecture and said: "Mathematics is not yet ready for such problems."

This was not false modesty. This was diagnosis.

---

## Why It's Hard

The problem looks like number theory. But it doesn't behave like number theory.

Most powerful techniques in mathematics work by finding structure — patterns that let you predict behavior, then generalize. Prime numbers have structure: the sieve of Eratosthenes, modular arithmetic, multiplicative properties. The Riemann Hypothesis is hard partly because zeta function zeros are deeply structured but the structure is hidden in the complex plane.

The Collatz sequence looks random.

Apply the rules to consecutive integers and the sequences bear almost no resemblance to each other. The sequence for 6 takes 8 steps. The sequence for 7 takes 16. The sequence for 27 takes 111. There's no obvious relationship between a number and how long its sequence runs, or how high it climbs before falling.

Mathematicians call this mixing behavior. The sequence looks statistically like it's taking random steps, which means the tools designed to find structure keep coming up empty.

This also means it's very hard to show the sequence can't escape to infinity — that there isn't some number out there whose sequence just keeps climbing forever, never returning to 1.

---

## What We Actually Know

A few things have been proved.

**The sequence can't cycle back to 1 too quickly.** Any cycle other than 1 → 4 → 2 → 1 would have to be extremely long — mathematicians have ruled out short alternative cycles entirely.

**"Almost all" numbers work.** In 2019, Terence Tao — UCLA mathematician, Fields Medal winner, widely regarded as the most technically accomplished mathematician alive — published a paper proving that the Collatz Conjecture is true for "almost all" positive integers in a precise sense.

This sounds like progress. It is progress. Tao showed that the number of integers below *N* that eventually reach 1 approaches 100% as *N* grows. The fraction of exceptions (if any exist) shrinks to zero.

But "almost all" is not "all." Tao's result doesn't rule out a single exceptional number — an outlier, somewhere in the infinite expanse of integers, whose sequence climbs without bound or loops forever without reaching 1. If such a number exists, we haven't found it. If it doesn't exist, we haven't proved it.

Tao said his result "is perhaps the most one can say with current technology."

He's probably right.

---

## What Might Be Going On

There are a few frameworks mathematicians use to think about why the conjecture might be true — even if they can't prove it.

**The probabilistic argument.** When you look at the average behavior of the 3*n* + 1 operation on odd numbers, the sequence multiplies by 3 and then usually divides by 2 a couple of times. The geometric average of one step is roughly 3/4 — less than 1. So on average, the numbers should trend downward. This isn't a proof, but it's why essentially everyone believes the conjecture is true. The "gravity" of the system pulls numbers toward 1.

**The mixing argument.** The sequences look random enough that a number would have to be extraordinarily "lucky" to avoid 1 forever. Every time a sequence visits a power of 2, it collapses rapidly. The probability of never visiting one seems vanishingly small.

**The connection to ergodic theory.** This is the branch of mathematics dealing with the long-term behavior of dynamical systems — systems that evolve over time according to rules. The Collatz function is a dynamical system of sorts. Ergodic theory provides tools for asking what happens "on average" or "eventually." Tao's approach used these tools. They got close. Close isn't proof.

---

## The Deeper Problem

There's a reason Erdős was so blunt.

The Collatz Conjecture sits at the boundary of what mathematical formalism can reach. It involves an iterated function — apply this rule, then apply it again, then again — and the long-term behavior of iterated functions over the integers is genuinely hard. In many cases, it's *undecidable* — meaning there is no algorithm that can determine, for a given function and starting value, whether the sequence terminates.

This is the shadow of Gödel. There exist true statements about integers that cannot be proved from standard axioms. The Collatz Conjecture might be one of them.

This possibility — that the conjecture is true but unprovable — is not considered likely by most mathematicians. But it's not considered impossible either. The Russian mathematician Yuri Matiyasevich, who resolved Hilbert's tenth problem in 1970 by proving it undecidable, has noted that Collatz-like problems are exactly the kind of thing that sits near the edge of computability.

We may have a true fact about arithmetic — one you can check yourself with a pencil — that mathematics can never prove.

---

## The Geography of the Unknown

Computers have run Collatz sequences for every integer up to about 300 quintillion. Every single one reaches 1. Some do it in a handful of steps; some take thousands. The record-holders for longest sequences before reaching 1 are regular integers — not particularly special, not particularly large. They just happen to find the paths that climb high before crashing.

The number 27 climbs to 9,232 before falling. The number 703 climbs to 250,504. The number 77,031 climbs to over 21 billion, taking 350 steps.

And then they all fall to 1.

The sequences look like mountain ranges when graphed — jagged, unpredictable, then sudden collapse. There is something hypnotic about watching them. The climb always looks permanent. The fall always comes.

Whether the fall always comes for every number ever — that question is still open.

It has been open for 90 years.

---

## Why This Matters Beyond the Problem Itself

The Collatz Conjecture probably won't unlock a new drug or fix a bridge. It's pure mathematics.

But the questions it raises are not pure at all.

Why is a rule with two lines so resistant to proof? What is it about the integers that makes them generate behavior we can observe but not explain? Is there something fundamentally limited about what formal proof can capture — not just in exotic set theory, but in basic arithmetic?

These questions echo through all of mathematics. They're the questions Gödel raised in 1931 when he proved that every consistent formal system contains truths it cannot prove. They're the questions Alan Turing raised in 1936 when he proved that no algorithm can determine whether an arbitrary program halts.

The Collatz Conjecture is one more place where the floor of mathematical knowledge suddenly isn't there.

You can verify it yourself tonight. Pick a number — any number. Follow the rules. Watch it reach 1.

You'll see something true. You just won't know why.

---

## Sources

- Tao, T. (2019). Almost all orbits of the Collatz map attain almost bounded values. *arXiv*:1909.03562.
- Lagarias, J.C. (1985). The 3x+1 problem and its generalizations. *American Mathematical Monthly*, 92(1), 3–23.
- Lagarias, J.C. (Ed.). (2010). *The Ultimate Challenge: The 3x+1 Problem*. American Mathematical Society.
- Matiyasevich, Y. (1993). *Hilbert's Tenth Problem*. MIT Press.
- Collatz, L. (1950). Presentation to International Mathematical Congress, Cambridge. (Problem first circulated informally ca. 1937.)
- Erdős, P. Quoted in: Guy, R.K. (2004). *Unsolved Problems in Number Theory* (3rd ed.). Springer.
