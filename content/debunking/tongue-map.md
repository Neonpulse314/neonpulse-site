---
title: "The Tongue Map Is a Graphing Error"
date: 2026-06-28
section_label: "What the Internet Gets Wrong"
summary: "The diagram in your old biology textbook — sweet at the tip, bitter at the back — isn't a mistake about tongues. It's a mistake about a graph. One psychologist rescaled a German student's data against its own maximum, and a gentle gradient turned into four hard borders."
tags: ["taste", "biology", "neuroscience", "myth", "debunking", "data visualization", "tongue map"]
---

You learned it from a diagram. A cartoon tongue, carved into four countries: sweet at the tip, salty just behind it, sour along the sides, bitter standing guard across the back. It came with a tidy demonstration — put sugar on the tip, lemon on the sides — and it felt true because you could almost feel it.

It's wrong. Not "mostly wrong" — wrong at the root. But the usual correction ("you can taste everything everywhere, the map is a lie") overshoots into its own error. The honest version is stranger and more useful: **the tongue map is not a claim about biology that turned out false. It is an artifact of one man's chart.** The data underneath was fine. A graphing decision manufactured the borders.

## What the German student actually found

In 1901 a graduate student named David Hänig published a dissertation with the unpromising title *Zur Psychophysik des Geschmackssinnes* — "On the psychophysics of the sense of taste." He dripped four tastants — sucrose, salt, quinine, and hydrochloric acid — onto different spots around the edge of the tongue and recorded the faintest concentration a person could detect at each spot.

His finding was modest and correct: every taste could be detected nearly everywhere, and the **thresholds** — the minimum detectable strength — varied a little from place to place. Saltiness came out roughly equal across every location he tested. The differences he saw were small, gradual, and quantitative. Nowhere did he find a region that tasted *only* one thing. There were no countries on his tongue, just slightly hillier ground in some places than others.

That should have been the end of it. A small gradient is not a map.

## The graph that built the borders

Forty years later, the Harvard psychologist Edwin G. Boring put Hänig's numbers into an influential 1942 textbook, *Sensation and Perception in the History of Experimental Psychology* — and in redrawing them, changed what they said.

Here is the specific move, because this is the whole story. A threshold is backwards from sensitivity: a *low* threshold means *high* sensitivity (you detect a faint trace). So Boring took the **reciprocal** of each threshold to plot sensitivity, then **divided every value by the largest one** for that taste — rescaling each curve against its own maximum.

That second step is where the myth is born. When you normalize each taste to its own peak, *every taste is guaranteed a maximum somewhere*. Four tastes, four peaks, four apparent zones — even if, in absolute terms, the whole tongue is nearly flat. As the taste scientist Linda Bartoshuk put it in 1993, looking at Boring's figure there is "no way to tell how meaningful the sizes of variations are." The chart threw away the one thing that mattered — magnitude — and kept the one thing that misleads — shape.

Watch how cheaply it happens. Suppose sensitivity to bitterness reads 100 at the back of the tongue and 92, 90, and 88 moving forward — a span of 12%, basically flat. Normalize to the maximum and the back becomes 1.00 while the tip becomes 0.88. Do the same for sweetness with its own slightly-higher tip, salt with its own slightly-higher front, and sour with its own slightly-higher side, and you have drawn four crisp peaks in four different places. Print it without the y-axis numbers and you have a map. The tongue never changed. The denominator did.

![Two line charts of the same taste-sensitivity data. On the left, plotted on a true 0–100 scale, four nearly-flat lines crowd the top of the chart. On the right, with each line rescaled to its own maximum and the scale removed, the identical numbers become four dramatic peaks — sweet at the tip, salty at the front, sour at the side, bitter at the back.](/images/tongue-map-normalization.png)
*Same numbers, two graphs. The map was drawn on the right-hand axis, not on a tongue.*

## What's actually true (the part the corrections get wrong)

The popular debunk swings to the opposite wall: *all regions are identical, taste has no geography at all.* That's also false.

Start with the biology that settles the cartoon for good. Modern work shows the taste buds in **every** region of the mouth carry receptor cells for all five basic tastes — sweet, sour, salty, bitter, and umami (Chandrashekar et al., 2006; Yarmolinsky et al., 2009). There is no anatomical border for taste to respect. The back of your tongue is not a bitterness organ.

But small, real differences do survive careful measurement. When Virginia Collings re-ran the threshold experiment properly in 1974, she confirmed all tastes everywhere *and* found, for instance, that the threshold for salt rises gently from the front of the tongue toward the back. Measuring perceived *intensity* rather than detection, Feeney and Hayes (2014) found bitter and umami rated somewhat stronger toward the rear, while sweet, sour, and salty showed no regional difference at all. The gradients are minute, and they disagree from study to study — the opposite of four stable territories.

There's even a plausible reason the back leans bitter-sensitive, and it isn't taste appreciation. The taste buds nearest the throat sit exactly where a protective reflex would want them: bitterness is the flavor of many plant toxins, and heightened sensitivity at the point of no return feeds the gag-and-eject response (Finger and Morita, 1985). The back of the tongue isn't a flavor zone. It's a last checkpoint.

So the truth is a third thing, neither the map nor its flat denial: **all five tastes, everywhere, over a faint and inconsistent gradient, with the rear tuned slightly for rejection rather than enjoyment.**

## The thing worth keeping

The lesson here outlasts the tongue. The myth didn't come from a bad experiment or a lie. It came from a defensible-looking chart that **normalized each curve to its own maximum** and dropped the scale — and that single choice converted "barely different" into "categorically different."

That move is everywhere once you can see it. A bar chart with no zero baseline. A heat map rescaled so the hottest cell is always bright red. A "100 = best in class" index that makes a 3% spread look like a chasm. Whenever something has been rescaled against its own peak, the picture will *always* show winners and losers, even in data that is essentially flat. The shape is free; only the magnitude tells you whether it means anything.

Next time a diagram divides the world into clean regions, ask the question Boring's readers didn't: *compared to what, and how big is the difference, really?* Put sugar on the back of your tongue. It's sweet. You're holding the refutation in your own mouth — and now you know the map was never drawn from a tongue. It was drawn from a denominator.

---

*Sources: David Hänig, "Zur Psychophysik des Geschmackssinnes," Philosophische Studien (1901). Edwin G. Boring, Sensation and Perception in the History of Experimental Psychology (1942). Virginia B. Collings, "Human taste response as a function of locus of stimulation on the tongue and soft palate," Perception & Psychophysics (1974). Linda Bartoshuk, "The biological basis of food perception and acceptance," Food Quality and Preference (1993). Jayaram Chandrashekar et al., "The receptors and cells for mammalian taste," Nature 444 (2006). David A. Yarmolinsky, Charles S. Zuker & Nicholas J.P. Ryba, "Common sense about taste: from mammals to insects," Cell 139 (2009). E. Feeney & J. Hayes, "Regional differences in suprathreshold intensity for taste," (2014). T. Finger & Y. Morita, Science (1985). Review: Charles Spence, "The tongue map and the spatial modulation of taste perception," Current Research in Food Science 5 (2022): 598–610.*
