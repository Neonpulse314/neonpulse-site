---
title: "Mathematicians Have Spent 165 Years Trying to Understand Prime Numbers. They Still Can't."
summary: "The Riemann Hypothesis is the most important unsolved problem in mathematics. It describes the deepest pattern in prime numbers — and every attempt to prove it has failed."
section_label: "Unsolved Mystery"
tags: ["mathematics", "prime numbers", "cryptography", "number theory", "millennium problem"]
tier: 1
discipline: "Mathematics"
---

Every number you've ever seen is built from prime numbers.

2, 3, 5, 7, 11, 13, 17... They're the atoms of arithmetic. Every other number — 100, 999, 4,294,967,297 — is just primes multiplied together in some combination. Mathematicians have known this for over 2,000 years.

What they still don't know, after 165 years of trying, is *why primes are distributed the way they are*.

There's a pattern. It's real. Bernhard Riemann glimpsed it in 1859. He wrote it down as a hypothesis. And nobody has been able to prove it since.

It's called the Riemann Hypothesis. It's one of the seven Millennium Prize Problems — the Clay Mathematics Institute will pay $1 million to whoever solves it. It's been called the most important unsolved problem in mathematics.

It is still unsolved.

---

## The Problem With Primes

Primes look random. 2, 3, 5, 7, 11, 13... then a gap to 17, 19, then 23, then nothing until 29, 31. The gaps between consecutive primes seem to follow no rule. Two primes can be separated by 2 (twin primes: 11 and 13, 17 and 19) or by thousands.

But zoom out far enough, and a pattern emerges. Among the first 10 numbers, 4 are prime. Among the first 100, 25 are prime. Among the first 1,000, 168. The *density* of primes thins out in a remarkably regular way — approximately 1 in every ln(x) numbers near x is prime.

This is the Prime Number Theorem, proved in 1896 by two mathematicians independently — Jacques Hadamard and Charles Jean de la Vallée Poussin. It tells you roughly how many primes are below any given number. It's accurate. But it's not exact.

The exact error — how far the actual count of primes deviates from the estimate — depends on something much deeper.

It depends on the zeros of the Riemann zeta function.

---

## What Riemann Found

In 1859, Bernhard Riemann published a single paper on prime numbers. Eight pages. It remains one of the most consequential papers in the history of mathematics.

Riemann took a function that Euler had studied — the sum of 1/n^s for every natural number n — and extended it into the complex plane. Complex numbers have two parts: a real part and an imaginary part. Riemann's function, now called the Riemann zeta function ζ(s), could now take complex inputs.

Then he asked: where does this function equal zero?

There are obvious answers, called the trivial zeros: at s = -2, -4, -6, -8... all the negative even integers. These are well understood.

But the function also has non-trivial zeros — complex numbers where ζ(s) = 0 that live in a vertical strip of the complex plane where the real part of s is between 0 and 1. These zeros are deeply connected to the distribution of prime numbers. Their precise locations determine exactly how much the Prime Number Theorem's estimate of prime counts deviates from reality.

Riemann calculated the first few non-trivial zeros. They all had real part exactly 1/2. Every one.

His hypothesis: they all do. Every non-trivial zero of the zeta function has real part exactly 1/2 — they all lie on the "critical line."

That's the Riemann Hypothesis.

---

## 165 Years of Failure

It sounds simple to state. It has not been simple to prove.

In 1914, G.H. Hardy proved that infinitely many zeros lie on the critical line — a significant result, but not all of them.

In 1942, Atle Selberg proved that a positive proportion of all zeros lie on the critical line. Still not all.

In 1989, Brian Conrey proved that at least 40% of all non-trivial zeros are on the critical line. Progress — still not all.

By 2004, computers had verified the first 10 trillion zeros. Every single one was on the critical line.

None of this is a proof. A statement about *all* zeros — infinitely many of them — cannot be verified by checking finitely many cases. One zero in the wrong place would disprove the hypothesis. But so far, after computing more zeros than any human could count in a lifetime, not one violation has been found.

The hypothesis is almost certainly true. That's not the same as proven.

---

## The Strangest Clue: Quantum Chaos

In 1972, mathematician Hugh Montgomery was visiting the Institute for Advanced Study in Princeton when he mentioned his recent results on the spacing between Riemann zeros to physicist Freeman Dyson at tea.

Dyson recognized the formula immediately. It was the same distribution he'd seen in the energy levels of heavy atomic nuclei — analyzed using a branch of physics called random matrix theory.

This was completely unexpected. Riemann zeros — abstract mathematical objects in number theory — appeared to follow the same statistical laws as the quantum energy levels of complex physical systems. The connection has since been explored extensively and confirmed in detail.

Nobody knows why.

It suggests that the Riemann Hypothesis might not be purely a number theory problem. It might be connected to quantum mechanics in some deep way. Some physicists have speculated that there exists an undiscovered quantum-mechanical system whose energy levels *are* the Riemann zeros — and that finding it would prove the hypothesis.

This "Hilbert-Pólya conjecture" has never been realized. The quantum system, if it exists, has never been found.

---

## What It Would Mean to Solve It

A proof of the Riemann Hypothesis would immediately improve our understanding of prime number distribution — the error bounds on the Prime Number Theorem would tighten dramatically.

It would also resolve hundreds of theorems currently stated as "true if the Riemann Hypothesis holds." Mathematicians routinely publish results that are conditional on RH — proven assuming the hypothesis is true, to be fully established when (if) someone proves it. A proof would unlock all of them at once.

The cryptographic implications are subtler than popular accounts suggest. RSA encryption — which protects your bank accounts, passwords, and private messages — is not directly based on the Riemann Hypothesis. It's based on the difficulty of factoring large numbers into their prime components.

But many algorithms in computational number theory have RH-conditional proofs. A constructive proof of RH — one that builds a specific tool to locate or understand zeros — might provide new approaches to prime-related computations. Whether this would threaten RSA encryption in practice is debated. Most cryptographers believe that even a proof of RH would not break current encryption. But it's not a question with a settled answer, because no one has seen what a proof would look like.

---

## Why It's Hard

The difficulty is not that the hypothesis is complicated to state. It's that no existing tool in mathematics is sharp enough to handle it.

The zeta function is smooth. Calculus works on it. But the zeros resist every direct approach. Analytic number theory — the field Riemann founded — has developed extraordinary machinery in the 165 years since his paper. None of it has been enough.

Part of the problem may be that the hypothesis is true. Proving that something *always* happens — that not one of infinitely many zeros is off the critical line — requires a completely general argument. You can't find the proof by checking cases. You have to understand *why* it must be true.

And the why, so far, has not been found.

Some mathematicians suspect the answer requires entirely new mathematics — concepts that don't exist yet. Others believe the right approach is hiding in plain sight and the proof will eventually look obvious in retrospect.

A few have suggested it might be *unprovable* — independent of the axioms of mathematics, like Gödel showed some true statements must be. This would be the darkest outcome: a hypothesis that is almost certainly true and can never be proven.

---

## Where It Stands

As of today: unproven.

10 trillion zeros checked. All on the line. The most sophisticated mathematical machinery ever developed, applied for over a century, has produced partial results and deep connections — to quantum physics, to statistics, to geometry — but not a proof.

The $1 million prize sits unclaimed.

The prime numbers keep their secret.

---

## Sources

- Riemann, B. (1859). "Über die Anzahl der Primzahlen unter einer gegebenen Grösse." *Monatsberichte der Berliner Akademie.* [The original 8-page paper.]
- Hadamard, J. (1896). "Sur la distribution des zéros de la fonction ζ(s) et ses conséquences arithmétiques." *Bulletin de la Société Mathématique de France, 24*, 199–220.
- Hardy, G.H. (1914). "Sur les zéros de la fonction ζ(s) de Riemann." *Comptes Rendus, 158*, 1012–1014.
- Selberg, A. (1942). "On the zeros of Riemann's zeta-function." *Skrifter Norske Vid. Akad. Oslo I, 10.*
- Montgomery, H.L. (1973). "The pair correlation of zeros of the zeta function." *Analytic Number Theory, Proc. Sympos. Pure Math., 24*, 181–193. [The paper Dyson saw at tea.]
- Conrey, J.B. (1989). "More than two fifths of the zeros of the Riemann zeta function are on the critical line." *Journal für die reine und angewandte Mathematik, 399*, 1–26.
- Odlyzko, A.M. (1987). "On the distribution of spacings between zeros of the zeta function." *Mathematics of Computation, 48*(177), 273–308. [The random matrix connection confirmed computationally.]
- Clay Mathematics Institute. Millennium Prize Problems: The Riemann Hypothesis. claymath.org.
- du Sautoy, M. (2003). *The Music of the Primes: Searching to Solve the Greatest Mystery in Mathematics.* HarperCollins. [Accessible book-length treatment.]
