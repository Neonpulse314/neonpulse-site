---
title: "The Heat of Forgetting: Why Erasing Information Costs Energy"
date: 2026-06-16T12:45:00-05:00
description: "There is a hard physical floor under computing, and it has nothing to do with how clever your chip is. Every time a computer erases a bit of information, it must release a tiny, unavoidable puff of heat. Not because the wires are imperfect — because of thermodynamics itself. And the strange escape hatch is a kind of computer that never forgets."
section_label: "engineering"
tags: ["physics", "computation", "thermodynamics", "information theory", "energy", "frontier"]
---

Your phone gets warm when it works hard. The easy explanation is that electricity pushed through tiny resistive wires loses energy as heat — friction, basically — and that's true, and engineers spend their careers fighting it. But underneath that practical, fixable warmth is a second kind that no amount of cleverness can remove. It comes not from imperfect wires but from the act of forgetting.

This is Landauer's principle, and it's one of the few places where pure information theory reaches down and touches physical law.

## The claim

In 1961, a physicist named Rolf Landauer, working at IBM, asked a question that sounds like philosophy and turns out to be engineering: does computing *have* to cost energy? Not in practice — in principle. If you built a perfect, frictionless computer, could it think for free?

His answer: almost. Most logical operations could, in principle, be made to cost nothing. But there is one operation that can never be free — **erasing information**. Throwing a bit away has a minimum, unavoidable energy cost, and that energy must leave the system as heat.

The number is tiny. Erasing a single bit must release at least *kT* ln 2 joules, where *T* is the temperature and *k* is Boltzmann's constant. At room temperature that's about three-billionths-of-a-billionth of a joule — roughly 0.018 electron-volts. Negligible for one bit. But it is a *floor*, not an estimate, and it doesn't depend on what your computer is made of. Silicon, gears, light, neurons — erase a bit at room temperature and you owe that heat. There is no engineering trick that gets under it, any more than a clever pump can move heat from cold to hot for free.

## Why forgetting, specifically?

The reason is the second law of thermodynamics, dressed in information-theory clothes.

Think about what erasure actually does. Before you erase a bit, it could be a 0 or a 1 — two possible states. After you erase it (reset it to 0, say), there is only one. You've taken two possibilities and collapsed them into one. You've reduced the number of states the system can be in.

The second law says the total disorder — entropy — of a closed system can't decrease. By making your bit more orderly (fewer possible states), you've decreased entropy *in the bit*. So the books only balance if at least that much entropy appears somewhere else. It does, as heat dumped into the surroundings. The warmth is the universe's receipt for the order you created by forgetting.

A reversible operation — one you could run backwards to recover exactly what you started with — doesn't collapse possibilities. It just shuffles them. No states are lost, so no entropy debt comes due. It's only the *irreversible* steps, the ones where information is genuinely destroyed, that must pay.

For decades this was a beautiful argument on paper. Then in 2012, a team led by Antoine Bérut measured it directly: they built a single bit out of a microscopic bead held in a laser trap, erased it, and watched the heat come out — right at the Landauer limit, not below. The floor is real.

## Why it doesn't bother your laptop (yet)

Here's the twist that keeps this from being a crisis: today's chips operate *thousands to millions of times* above the Landauer limit per operation. The practical heat — the resistive, frictional kind — completely swamps the fundamental kind. We are nowhere near the floor.

But the gap has been closing for seventy years, because efficiency keeps improving, and the floor doesn't move. Every generation of chips spends less energy per operation, which means the fundamental cost of erasure becomes a larger share of the (shrinking) total. Project the trend far enough and you hit a wall that isn't about manufacturing — it's about thermodynamics. With computing now a serious fraction of global electricity, and AI pushing that fraction up fast, the question "what is the minimum energy a computation *must* cost" stopped being academic.

## The escape hatch: a computer that never forgets

If erasure is what costs, the radical fix is obvious and bizarre: **build a computer that never erases anything.**

This is *reversible computing*, proposed by Charles Bennett in 1973. An ordinary logic gate destroys information — feed an AND gate a 0 out, and you can't tell whether the inputs were 0-and-0, 0-and-1, or 1-and-0. That lost information is a bit erased, and a bit erased is heat owed. Reversible gates (with names like Toffoli and Fredkin) are designed so you can always run them backwards and recover the inputs. Nothing is thrown away, so in the ideal limit, nothing must be paid.

The catch is the obvious one: if you never throw anything away, you accumulate a growing pile of intermediate scratch-work. Reversible designs have to carefully "uncompute" — run the messy middle steps backwards to clean up — and they pay in complexity and chip area what they save in heat. It's a real engineering trade, not a free lunch, and it's why your laptop isn't reversible. But specialized adiabatic circuits already inch toward it, and there's a famous bonus: quantum computers are *inherently* reversible until the moment you measure them, which is part of why they're so physically delicate.

There's even a ghost laid to rest here. For a century, physicists were haunted by "Maxwell's demon" — a hypothetical creature who sorts fast and slow molecules to create order from nothing, seemingly breaking the second law. Bennett's resolution, built on Landauer: the demon has to *remember* which molecules it sorted, and eventually its memory fills and must be erased. The erasure costs exactly enough heat to save the second law. The demon isn't defeated by its sorting. It's defeated by having to forget.

Which is the quietly profound thing under all of this. We tend to think of memory as the expensive part — storage, capacity, the hard drive filling up. Thermodynamics says the opposite. Holding information is, in principle, free. It's *letting go* that you pay for.
