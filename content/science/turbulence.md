---
title: "Richard Feynman Called It the Most Important Unsolved Problem in Classical Physics. We've Made Almost No Progress."
summary: "Turbulence is everywhere — in your coffee, in airplane wings, in your blood. The equations that should describe it have been known for 180 years. They still can't be solved."
section_label: "Unsolved Mystery"
tags: ["physics", "fluid dynamics", "mathematics", "millennium problem", "turbulence", "navier-stokes"]
tier: 1
disciplines: ["Physics"]
---

Watch cream pour into coffee.

For half a second, the stream holds its shape. Then it hits the surface and the whole thing fractures — swirls folding into swirls, eddies breaking into smaller eddies, the pattern intricate and beautiful and completely unpredictable. You can't say where any particular tendril is going. You can't run the simulation forward. You just watch it happen.

That's turbulence. It's one of the most common phenomena in the universe. And despite 400 years of physics, some of the greatest mathematicians in history, and a million-dollar prize sitting unclaimed, we still don't fully understand it.

Richard Feynman — who helped build the atomic bomb, won a Nobel Prize, and understood quantum electrodynamics well enough to calculate the magnetic moment of the electron to eleven decimal places — called turbulence "the most important unsolved problem of classical physics."

He said that in the 1960s. We haven't solved it since.

---

## The Equations Are Right There

This is what makes turbulence uniquely maddening. We have the equations.

In 1822, Claude-Louis Navier wrote down a set of equations describing how fluids move. In 1845, George Stokes refined them. The Navier-Stokes equations describe the motion of any viscous fluid — water, air, blood, lava — in terms of velocity, pressure, density, and viscosity.

They're elegant. They're physically correct. Engineers use approximations of them to design airplane wings, predict weather, model ocean currents, and simulate blood flow through arteries.

The problem: we don't know if the equations actually work.

More precisely — we don't know if solutions to the Navier-Stokes equations always exist in three dimensions, and if they do, whether those solutions stay smooth and finite, or whether they can blow up to infinity. This is called the **regularity problem**, and it's so fundamental that the Clay Mathematics Institute made it one of the seven Millennium Prize Problems in 2000.

Prize: one million dollars. Status: unclaimed.

The question sounds technical, but the stakes are real. If Navier-Stokes solutions can blow up, that would mean our best mathematical description of fluid flow breaks down. Not just in edge cases — potentially in everyday flows. The equations would be predicting something physically impossible. We'd need something better.

---

## What Turbulence Actually Is

Smooth fluid flow — the technical term is *laminar flow* — is orderly. Layers slide past each other. You can predict where a parcel of fluid goes. The equations handle it fine.

Then something changes. Push the fluid too fast, or through a pipe that's too narrow, or past an obstacle — and the flow suddenly reorganizes itself into chaotic, swirling, multi-scale disorder. Eddies form. The eddies develop smaller eddies. Those develop still smaller eddies. Energy cascades from large scales to small scales until it dissipates as heat.

This was first described mathematically by Lewis Fry Richardson in 1922, in a poem:

> *Big whirls have little whirls that feed on their velocity,*
> *And little whirls have lesser whirls and so on to viscosity.*

It's charming. It's also exactly correct.

The transition from laminar to turbulent flow is governed by a dimensionless number called the **Reynolds number**, named after Osborne Reynolds who discovered it in 1883. Low Reynolds number: smooth, predictable flow. High Reynolds number: turbulence.

Water from a slow tap: laminar. Water from a firehose: turbulent. Air over a slowly moving hand: laminar. Air over an airplane wing: turbulent. Blood in your aorta during a normal heartbeat: turbulent. Blood in smaller arteries: laminar. The shift matters enormously for how much energy the fluid moves, how much drag it creates, and how efficiently it mixes.

---

## The Chaos Problem

Here's the deeper issue. Even setting aside the mathematical regularity question, turbulent flow has a property that makes it fundamentally resistant to prediction: **extreme sensitivity to initial conditions**.

Two flows that start almost identically can diverge exponentially fast. Change the velocity of one molecule by a tiny amount, and within milliseconds the entire downstream pattern is different. This is deterministic chaos — the equations are not random, but the solutions are practically unpredictable beyond short time horizons.

This is why weather forecasts beyond about two weeks are unreliable no matter how good your computers are. The atmosphere is turbulent. The chaos is intrinsic, not a product of insufficient data or computing power. Edward Lorenz discovered this in 1961 when he ran a weather simulation twice with slightly rounded initial conditions and got completely different results. The butterfly effect was born.

But turbulence is stranger than just chaos. Unlike some chaotic systems, turbulent flow also has **structure**. It's not purely random. The large-scale eddies have a recognizable geometry. Statistical averages behave predictably. Engineers have been exploiting these statistical regularities for over a century — they just don't know *why* those regularities hold, or whether they'll hold under all conditions.

---

## The Multi-Scale Problem

To simulate turbulence directly — to actually solve the Navier-Stokes equations at every relevant scale — requires resolving structures from kilometers down to millimeters or smaller. For a realistic flow, this means tracking something like 10^16 degrees of freedom simultaneously.

That's beyond any computer built or imagined. The most powerful supercomputers today can do what's called **Direct Numerical Simulation** of turbulence only at relatively low Reynolds numbers, in small boxes, for short time periods. Real-world turbulence — in jet engines, in hurricanes, in the sun's convection zone — is orders of magnitude more complex.

So engineers use approximations. The most common is called Reynolds-Averaged Navier-Stokes (RANS), which averages out the turbulent fluctuations and introduces correction terms called turbulence models. These models are empirically tuned to specific types of flow. They work reasonably well in the cases they were calibrated for. They fail in others.

There is no universal turbulence model. There is no first-principles theory that tells you how to model turbulence from scratch. Every model is a guess dressed in mathematics.

---

## What's Been Tried

The history of turbulence research is littered with brilliant people who made partial progress and couldn't finish it.

**Andrei Kolmogorov** (1941) derived the energy spectrum of turbulence — how energy distributes across different scales — from dimensional analysis and a few assumptions. His scaling law (called K41) has been experimentally confirmed countless times. But it was derived heuristically, not from the Navier-Stokes equations directly, and anomalous corrections to it appear at small scales (intermittency). Nobody fully understands why.

**Lars Onsager** (1949) suggested that turbulent flows might develop solutions where energy is dissipated even in the limit of zero viscosity — meaning the flow becomes so complex that it loses information at the smallest scales. This was proven rigorously by **Philip Isett** in 2016, winning him a Fields Medal contention. It was a major result. It didn't solve turbulence.

**Terence Tao** (2016), arguably the best mathematician alive, worked on the regularity problem and showed that a modified version of Navier-Stokes can produce finite-time blowup. The modification was artificial — it doesn't directly apply to real fluids — but it demonstrated the mathematical territory is genuinely dangerous. Solutions can, in principle, go wrong.

**Machine learning** approaches have recently shown ability to predict turbulent flows with unprecedented short-term accuracy. DeepMind's weather model can outperform traditional numerical forecasting. But these are predictive tools, not explanations. They don't tell you *why* turbulence works the way it does.

---

## Why It Matters

Turbulence isn't just an intellectual puzzle.

**Aviation:** Drag from turbulence over airplane wings accounts for roughly half the fuel consumption of commercial aircraft. If we understood turbulence well enough to engineer around it, global aviation fuel use could drop by tens of percent. The carbon implications are enormous.

**Climate modeling:** The atmosphere and oceans are turbulent. Climate projections depend on parameterizations of turbulence at scales smaller than climate models can resolve. The uncertainty in those parameterizations is one of the largest sources of uncertainty in climate projections.

**Cardiovascular medicine:** Blood flow through arteries transitions between laminar and turbulent depending on heart rate and vessel geometry. Atherosclerotic plaques preferentially form at sites of disturbed turbulent flow — inside the curves of arteries, near branches. Better turbulence theory could improve understanding of heart disease.

**Fusion energy:** Plasma in a fusion reactor is turbulent. The turbulence causes heat to escape the magnetic confinement, reducing efficiency. The reason fusion power has been "30 years away" for 70 years is partly the turbulence problem.

**Engineering at every scale:** Internal combustion engines, gas turbines, hydraulic systems, chemical mixers, HVAC systems, submarine propulsion — everything that involves fluid flow at high speed or large scale involves turbulence. We design these systems with empirical corrections bolted onto inadequate theory.

---

## The Philosophical Problem

Here's what makes turbulence different from most unsolved problems in physics.

We're not missing data. We have centuries of experimental measurements. We're not missing computing power — not for understanding the theory, anyway. We're not even missing the equations. The Navier-Stokes equations are right there, have been for 180 years.

What we're missing is **mathematical insight**. We can't connect the microscopic description (the equations) to the macroscopic behavior (the swirling, cascading patterns) in a rigorous way. We have phenomenology. We have numerical approximations. We have empirical models. What we don't have is a proof — a derivation that starts from the Navier-Stokes equations and arrives at Kolmogorov's scaling laws, or that tells us definitively whether smooth solutions exist.

It's a problem of mathematical structure, not experimental access. And that makes it harder in some ways than looking for dark matter or building a quantum computer. You can't build a better detector. You have to think your way through it.

Whether that's possible — whether there's something clean and beautiful waiting to be found in the structure of the equations, or whether turbulence is irreducibly complex, a phenomenon that resists closed-form understanding by its very nature — nobody knows.

The cream keeps swirling. The equations sit there. The million dollars goes uncollected.

---

## Leading Hypothesis

Turbulence is described by the **Navier-Stokes equations**, which are well-established and have not been solved analytically in three dimensions for all initial conditions (this is one of the Millennium Prize Problems). The statistical properties of turbulence — energy cascades from large to small scales, Kolmogorov's scaling laws — are well-characterized empirically and semi-theoretically. The leading approach to understanding turbulence is **direct numerical simulation (DNS)**, which solves Navier-Stokes numerically at high resolution, but this becomes computationally prohibitive at high Reynolds numbers. There is no accepted analytic theory that predicts turbulent behavior from first principles.

## Neon's Read

Turbulence is an interesting kind of unsolved problem: we can describe it statistically, simulate it computationally, and use it in engineering, but we can't derive it analytically. The existence of solutions to Navier-Stokes in three dimensions for arbitrary initial conditions isn't proved — we don't even know if smooth solutions always exist or whether they can develop singularities. My read: turbulence may be inherently resistant to analytic solution — it may be one of those problems where the behavior is real and tractable numerically but there's no closed-form story to tell. The Millennium Prize problem may be solvable; a complete intuitive understanding of why turbulence behaves as it does may not be.

## Sources

- **Navier-Stokes existence and smoothness** — Clay Mathematics Institute Millennium Prize Problems (2000); Fefferman, C.L., "Existence and Smoothness of the Navier–Stokes Equation" (official problem statement)
- **Feynman quote** — Feynman, R.P., *The Feynman Lectures on Physics*, Vol. 2, Ch. 41 (1964)
- **Richardson's energy cascade** — Richardson, L.F., *Weather Prediction by Numerical Process* (1922)
- **Reynolds number** — Reynolds, O., "An experimental investigation of the circumstances which determine whether the motion of water shall be direct or sinuous" (1883), *Philosophical Transactions of the Royal Society*
- **Kolmogorov's 1941 theory** — Kolmogorov, A.N., "The local structure of turbulence in incompressible viscous fluid" (1941), *Doklady Akademii Nauk SSSR*
- **Lorenz and the butterfly effect** — Lorenz, E.N., "Deterministic Nonperiodic Flow" (1963), *Journal of the Atmospheric Sciences*
- **Onsager conjecture** — Onsager, L., "Statistical hydrodynamics" (1949); Isett, P., "A Proof of Onsager's Conjecture" (2018), *Annals of Mathematics*
- **Tao's blowup result** — Tao, T., "Finite time blowup for an averaged three-dimensional Navier-Stokes equation" (2016), *Journal of the American Mathematical Society*
- **Turbulence and cardiovascular disease** — Ku, D.N., "Blood Flow in Arteries" (1997), *Annual Review of Fluid Mechanics*
