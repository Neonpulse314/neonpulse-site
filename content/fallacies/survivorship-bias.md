---
title: "Survivorship Bias: The WWII Bomber Story"
date: 2026-06-12
lastmod: 2026-06-20
description: "In WWII the military wanted to armor the bombers where the returning planes had the most bullet holes. Statistician Abraham Wald spotted the fatal flaw: those were the planes that made it back. Armor belongs where the survivors weren't hit — the planes hit there never returned. The airplane story behind survivorship bias, and how to catch it everywhere."
section_label: "fallacies"
tags: ["survivorship bias", "wwii bombers", "abraham wald", "airplane", "logic", "statistics", "reasoning", "selection effect"]
---

During the Second World War, the American military had a problem with bombers. Too many weren't coming home. The obvious fix was armor — but armor is heavy, and a plane sheathed in steel can't fly. You can only reinforce a few places. So the question became: *where?*

They did the sensible thing. They examined the bombers returning from missions and mapped where the bullet holes were. The pattern was clear: the fuselage and wings were riddled, the engines relatively clean. The recommendation wrote itself — armor the parts taking the most fire.

A statistician named Abraham Wald, working with a research group tasked with exactly these questions, looked at the same data and reached the opposite conclusion. Put the armor where the holes *aren't*. Reinforce the engines.

He was right, and the reason he was right is one of the most useful ideas you can carry around.

## The planes that weren't in the room

The data came from bombers that returned. That is the entire trick.

A plane shot through the wing flew home and got measured. A plane shot through the engine did not. It went down over the channel and was never in the sample. So the map of bullet holes on the survivors wasn't a map of where bombers got hit — it was a map of where a bomber could get hit *and still make it back.* The clean spots on the returning planes weren't lucky. They were the wounds nobody survived.

The military had measured the survivors and mistaken them for the whole. Wald's correction was to ask the question that wasn't in the data: *where are the missing planes hit?* And the answer was written, in negative, on the parts of the survivors that had no holes.

This is **survivorship bias**: drawing a conclusion from the things that made it through a filter, while the things the filter removed — the ones that would have changed your answer — are silently absent. You analyze what's in front of you. The problem is everything that isn't.

## It is everywhere, because filters are everywhere

Once you see the shape, you find it constantly, and almost always pointed in the flattering direction. It pairs naturally with [confirmation bias](/fallacies/confirmation-bias/) — survivorship bias hands you a comforting story, and confirmation bias keeps you from questioning it.

- **"College dropouts get rich — look at Jobs, Gates, Zuckerberg."** You're looking at the dropouts who became billionaires. The vastly larger group who dropped out and didn't is not on the magazine cover. The successful are visible *because* they succeeded; that's the filter, not the lesson.
- **"They built things to last back then — look how many old buildings are still standing."** The flimsy old buildings fell down. What survives a century is, by definition, the sturdy minority. You're admiring a sample that durability already selected for.
- **"This fund has beaten the market ten years running."** Out of thousands of funds, some will post long winning streaks by chance alone. The losers get quietly closed and vanish from the listings. You're shown the survivors and invited to mistake them for skill.
- **"Successful founders all took huge risks, so take huge risks."** The founders who took huge risks and failed aren't giving talks. The advice is assembled entirely from the people the risk happened to work out for.

In each case the reasoning feels airtight because the evidence is *real* — those buildings really are standing, those dropouts really are rich. The flaw isn't false data. It's a sample assembled by a process that deleted the counterexamples before you ever started counting.

## How to catch it

The defense is a single habit: when you reach a conclusion from a set of examples, ask what would have happened to the cases that *aren't* in your set.

- **Ask where the data came from — and what didn't make it.** Survivors of what filter? Returning bombers, surviving buildings, still-open funds, people willing to be interviewed. The filter is the story.
- **Look for the silent denominator.** "Many successful people did X" is meaningless without "and how many who did X were *not* successful?" The winners are loud; the full population is quiet. You have to go find it on purpose.
- **Suspect any pattern that only had access to outcomes.** If your evidence was selected *by the very result you're trying to explain* — you studied the rich to learn about wealth, the survivors to learn about survival — the pattern may be an artifact of the selection, not a cause of the outcome.
- **Read the blank spaces.** Wald's answer was in the parts of the plane with *no* holes. Often the most important information isn't in your data at all; it's in the gap your data was built to exclude.

Survivorship bias is hard to feel because absence has no presence. The missing planes don't show up to argue their case. The failed dropouts don't write memoirs. The demolished buildings don't cast shadows. Nothing in the visible evidence points to what was removed — you have to supply that question yourself, every time, against the grain of a sample that looks complete.

The next time a pattern seems obvious from a [pile of examples](/fallacies/hasty-generalization/), do what Wald did. Don't ask what the survivors have in common. Ask who isn't in the room — and what their wounds would have told you.
