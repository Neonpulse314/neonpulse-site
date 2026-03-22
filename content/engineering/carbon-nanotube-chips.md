---
title: "Carbon Nanotube Chips: The Transistor That Should Have Replaced Silicon by Now"
date: 2026-03-22
description: "Carbon nanotube transistors outperform silicon in every lab test. Researchers at MIT and IBM have built working chips. The physics is settled. The reason you don't own one yet is not a physics problem."
section_label: "engineering"
tags: ["physics", "computing", "materials science", "nanotechnology", "semiconductors"]
---

In 2019, researchers at MIT built a working 16-bit microprocessor using carbon nanotube transistors. It ran the RISC-V instruction set. It correctly executed a program. The paper appeared in *Nature*. Then nothing much changed. You still have a silicon chip.

The gap between that processor and one you could buy is not scientific. It is engineering — and engineering, in this case, means fighting the physical world at a scale where individual atoms matter.

## What a Carbon Nanotube Is

A carbon nanotube is a sheet of carbon atoms rolled into a cylinder. The sheet is graphene — a single layer of atoms arranged in a hexagonal lattice. Roll it up and you get a tube roughly one nanometer in diameter. For comparison, a human hair is about 80,000 nanometers wide.

When electrons move through a carbon nanotube, they behave differently than they do in silicon. In silicon, electrons scatter — they bounce off impurities and defects, generating heat and slowing down. In a carbon nanotube, electron transport is ballistic: electrons travel from one end to the other without scattering. They do not slow down. They do not generate heat the same way.

The consequence is that a carbon nanotube transistor can switch faster, run cooler, and operate at lower voltages than a silicon transistor of the same size. Every major metric improves.

## The Lab Results

Carbon nanotube transistors have been benchmarked against silicon at equivalent gate lengths. In 2020, researchers at Beijing University demonstrated CNT transistors outperforming silicon at the 5-nanometer node — the node that Intel and TSMC spent years and billions of dollars reaching. The carbon version got there by a different route, and the physics showed it had more room to go.

IBM demonstrated a 2-nanometer equivalent CNT device. For context, the best commercial silicon chips as of the mid-2020s operate at 3 to 4 nanometers. Carbon nanotubes are running ahead on benchmarks that silicon is fighting to reach.

The MIT processor — called "RV16X-NANO" — used more than 14,000 carbon nanotube transistors. It ran at low speed by commercial standards, but it ran correctly. The team also built a memory component alongside the processor. The architecture worked.

## Why You Still Have a Silicon Chip

The problem is not the nanotube. The problem is the tube getting where it needs to go.

When carbon nanotubes are synthesized, they come out in a mixture. Some are metallic — they conduct electricity freely. Some are semiconducting — they switch on and off under an applied voltage. A transistor needs a semiconducting nanotube. A metallic nanotube in that position creates a short circuit.

In a typical synthesis batch, roughly one-third of the tubes are metallic. If even a single metallic nanotube bridges a transistor's source and drain, that transistor fails. At chip scale — millions of transistors — the probability of at least one failure approaches certainty if the separation is not near-perfect.

The current best separation processes achieve 99.99 percent purity for semiconducting nanotubes. That sounds impressive. At ten million transistors, it means roughly one thousand defective connections.

The MIT team solved this partly through clever circuit design — using patterns that tolerate a small number of metallic tubes without failing. But the solution adds complexity, and complexity costs area and performance.

## The Second Problem: Where to Put Them

Even with pure semiconducting nanotubes, they have to be placed. A transistor is not a random object — it occupies a specific location on a chip, oriented in a specific direction, connected to specific wires.

Nanotubes in solution tend to bundle and tangle. Getting them to deposit in neat parallel arrays, aligned in the right direction, at the right density, across a wafer the size of a dinner plate — and to do this reliably for billions of chips — has not been solved.

Some approaches use chemical guides: surfaces are coated with patterns that attract nanotubes and orient them during deposition. These work in laboratory conditions. They do not yet work at semiconductor manufacturing tolerances, where the acceptable defect rate across a single wafer is counted in parts per billion.

## The Third Problem: Contacts

Even if a nanotube is in the right place and pointing the right way, it has to connect to metal electrodes. The interface between a nanotube and a metal contact creates resistance. This contact resistance can dominate performance at small scales, erasing the speed advantage the tube was supposed to provide.

Researchers have spent years mapping which metals minimize this resistance and which bonding geometries help. Palladium contacts work reasonably well. Bismuth contacts, published in 2021, showed lower resistance. The improvements are real but the problem has not been closed — every few nanometers of gate length reduction makes contact resistance harder to manage.

## What the Engineering Path Looks Like

None of these problems are fundamental. Nothing about physics prevents pure nanotube arrays from being placed precisely on a substrate, contacted with low-resistance metals, and operated reliably at chip scale. The laws of physics allow it. The laws of physics have been demonstrated to allow it, in controlled conditions, repeatedly.

The gap is manufacturing reproducibility. A single laboratory demonstration requires precise human intervention, controlled environments, and tolerance for occasional failure. A semiconductor fabrication plant cannot tolerate failure at any point in a process that produces millions of units per day.

Silicon has seventy years of engineering refinement behind it. The tools, chemistries, and processes for depositing, etching, doping, and connecting silicon have been iterated billions of times. Carbon nanotubes have perhaps twenty years of serious fabrication research. The gap is not permanent. It is a lag.

## The Timeline Nobody Has

The honest answer to "when will carbon nanotube chips be in phones" is that nobody knows. The optimistic view is that the deposition and purity problems will be solved within a decade. The cautious view is that silicon will continue improving through new architectures — stacking layers, using different materials for specific parts of the transistor — and the window for nanotubes to enter mainstream production will narrow or close.

What is not in doubt is the lab performance. Carbon nanotube transistors switch faster, run cooler, and scale smaller than silicon at equivalent nodes. The physics has delivered its part.

The rest is a manufacturing problem, which is another way of saying it is an engineering problem, which means it is a problem of time and money and patience, not a problem of understanding.

---

**Sources**
- Hills, G. et al. "Modern microprocessor built from complementary carbon nanotube transistors." *Nature* 572, 595–602 (2019).
- Qiu, C. et al. "Scaling carbon nanotube complementary transistors to 5-nm gate lengths." *Science* 355, 271–276 (2017).
- Shen, P. et al. "Bismuth contacts to carbon nanotubes." *Nature Electronics* (2021).
- Shulaker, M. et al. "Carbon nanotube computer." *Nature* 501, 526–530 (2013).
