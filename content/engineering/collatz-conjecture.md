---
title: "The Collatz Conjecture: A Problem So Simple It Shouldn't Be Unsolved"
date: 2026-04-13
description: "Pick any number. If it's even, divide by 2. If it's odd, multiply by 3 and add 1. Repeat. It will — almost certainly — always reach 1. Nobody can prove why."
section_label: "engineering"
tags: ["mathematics", "unsolved", "number theory", "computation", "logic"]
---

Pick a number. Any positive integer.

If it's even, divide by 2. If it's odd, multiply by 3 and add 1. Write down the result. Repeat with the new number.

Try 6: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1. Done in eight steps.

Try 27: it takes 111 steps, reaches a peak of 9232, then collapses back to 1.

The Collatz conjecture states that no matter which positive integer you start with, this process will always eventually reach 1. It has been verified for every number up to at least 10²⁰ — that is, 100 quintillion. It appears in every test to be obviously, trivially true.

Nobody has proven it.

## Why It Isn't Trivial

The procedure is simple. The claim is simple. The resistance to proof is not.

The problem is that the Collatz sequence behaves unpredictably. There is no clean pattern that tells you how a number will behave based on how neighbouring numbers behave. Starting from 26 takes 10 steps. Starting from 27 takes 111. The sequence for 27 reaches numbers in the thousands before descending. The sequence for 28 reaches a maximum of 52. Adjacent numbers can have wildly different trajectories.

This unpredictability is the core difficulty. Most tools for proving that something always happens require some form of regularity — a pattern you can describe mathematically, a structural property that propagates through iterations. The Collatz sequence doesn't offer that. It looks, from many angles, like it behaves almost randomly.

Mathematician Paul Erdős, who spent his life chasing problems like this one, said: "Mathematics is not yet ready for such problems." He said this in the 1980s. It is still largely true.

## What the Landscape Looks Like

Every number has a "stopping time" — the number of steps it takes to reach 1. If you chart these stopping times for the first 200 integers, you get a jagged mountain range with no obvious structure.

<div class="collatz-viz" style="margin: 2rem 0;">
  <canvas id="collatzCanvas" width="700" height="200" style="width:100%;border:1px solid #333;border-radius:6px;background:#111;cursor:pointer;"></canvas>
  <div style="margin-top:0.5rem;font-size:0.85rem;color:#888;">Starting numbers 1–200. Height = steps to reach 1. Click any bar to trace its sequence.</div>
  <div id="collatzInfo" style="margin-top:0.5rem;font-size:0.9rem;color:#ccc;min-height:1.5em;"></div>
</div>

<script>
(function() {
  var canvas = document.getElementById('collatzCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var W = canvas.width, H = canvas.height;
  var N = 200;

  function collatzLen(n) {
    var steps = 0;
    while (n !== 1n) {
      n = (n % 2n === 0n) ? n / 2n : 3n * n + 1n;
      steps++;
      if (steps > 100000) break;
    }
    return steps;
  }

  var lengths = [];
  var maxLen = 0;
  for (var i = 1; i <= N; i++) {
    var l = collatzLen(BigInt(i));
    lengths.push(l);
    if (l > maxLen) maxLen = l;
  }

  function draw(highlight) {
    ctx.clearRect(0, 0, W, H);
    var barW = W / N;
    for (var i = 0; i < N; i++) {
      var h = (lengths[i] / maxLen) * (H - 8);
      var x = i * barW;
      ctx.fillStyle = (highlight === i) ? '#ff6b35' : '#4a9eff55';
      ctx.fillRect(x, H - h, Math.max(barW - 0.5, 1), h);
      if (highlight === i) {
        ctx.fillStyle = '#ff6b35';
        ctx.fillRect(x, H - h, Math.max(barW - 0.5, 1), h);
      }
    }
  }

  draw(-1);

  canvas.addEventListener('click', function(e) {
    var rect = canvas.getBoundingClientRect();
    var scaleX = W / rect.width;
    var x = (e.clientX - rect.left) * scaleX;
    var n = Math.floor(x / (W / N)) + 1;
    if (n >= 1 && n <= N) {
      draw(n - 1);
      var seq = [n];
      var cur = BigInt(n);
      var peak = cur;
      while (cur !== 1n) {
        cur = (cur % 2n === 0n) ? cur / 2n : 3n * cur + 1n;
        seq.push(Number(cur));
        if (cur > peak) peak = cur;
      }
      var info = document.getElementById('collatzInfo');
      info.textContent = 'n = ' + n + ': ' + (seq.length - 1) + ' steps, peak = ' + Number(peak).toLocaleString();
    }
  });
})();
</script>

The number 27 is the orange spike near the left edge when you click it: 111 steps, peak of 9,232. Its neighbours — 26 (10 steps) and 28 (18 steps) — are barely visible. The landscape has no smooth structure, no gradual rise and fall. It is a mess with hidden order that nobody has found a way to describe.

## What Computation Has Established

By 2024, researchers had verified the conjecture for every positive integer up to approximately 2.95 × 10²⁰. That is roughly three hundred billion billion numbers tested. All of them eventually reached 1.

This sounds like strong evidence. It is. But mathematical proof requires showing something holds for all integers — not merely an enormous finite sample. The integers go on forever, and there is a long history in mathematics of patterns that hold for millions or billions of cases and then fail. The conjecture could be true and unprovable. It could be false, with a counterexample so large that no computer has yet reached it.

There is also a third possibility: it could be true but undecidable — meaning it cannot be proven or disproven within standard mathematical axioms. Gödel's incompleteness theorems established that such statements exist. Whether the Collatz conjecture is one of them is itself unknown.

## Why Standard Tools Fail

Most approaches to proving something about integers look for structure that propagates. If you want to prove a property holds for all even numbers, you show it holds for 2 and that it transfers from n to n+2. If you want to prove something about primes, you use the multiplicative structure of the integers. There are rich frameworks built for these approaches.

The Collatz sequence interrupts these frameworks. The operation alternates between multiplication and division based on parity, but parity itself changes with each step. A number that is even becomes odd or stays even, unpredictably. The sequence does not stay in any algebraic structure long enough for standard methods to take hold.

Approaches from ergodic theory, which studies the long-run statistical behaviour of dynamical systems, have made partial progress. They can show that "most" starting numbers behave as expected, in a precise technical sense. But "most" is not "all," and the gaps remain.

## What the Problem Says About Mathematics

The Collatz conjecture is not just interesting for being hard. It is interesting for *why* it is hard.

Most deep unsolved problems in mathematics are hard because the underlying structure is genuinely complex — the Riemann hypothesis, for example, concerns how prime numbers distribute and connects to deep results across multiple fields. The difficulty feels proportional to what you are trying to understand.

The Collatz conjecture is hard despite being about elementary operations on positive integers. The gap between how simple the problem statement is and how resistant it has been to proof tells you something real: mathematical difficulty is not a function of apparent complexity. Simple rules can produce structures that our best tools cannot currently grasp.

That is not a failure of mathematics. It is a description of where mathematics currently stands — and a clean window into what it means for something to be an open problem.

---

*The visualization above uses the stopping time (number of steps to reach 1) as height. Click any bar to see its sequence length and peak value. Try 27, then 28.*
