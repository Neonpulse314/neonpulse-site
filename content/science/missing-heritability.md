---
title: "Twin Studies Proved Your Genes Explain Half of Who You Are. Genome Sequencing Can Only Find a Fraction of That. The Rest Has Vanished."
date: 2026-03-06
summary: "For a century, twin studies have shown that genes explain 50-80% of the variation in height, intelligence, and personality. When scientists went looking for those genes, they found far less than expected. The 'missing heritability problem' has reshaped genetics — and isn't solved."
tags: ["genetics", "biology", "neuroscience", "mystery", "science-failure"]
tier: 1
disciplines: ["Genetics"]
mystery: true
---

In 1875, Francis Galton had a simple idea: if you want to know how much of a human trait is genetic, compare identical twins to fraternal twins.

Identical twins share essentially all their DNA. Fraternal twins share about half, the same as any two siblings. If identical twins are more similar than fraternal twins for a trait, that extra similarity must come from the extra shared DNA. The difference tells you how heritable the trait is.

Over the following century, researchers did this for almost everything. Height. Intelligence. Personality. Mental illness. Addiction. Career choice. Divorce. Risk tolerance. Political views. Religious belief.

The results were consistent and startling. Genes seemed to matter for almost everything, and to matter enormously. Intelligence: roughly 50% heritable. Height: roughly 80% heritable. Schizophrenia: roughly 80% heritable. Big Five personality traits: 40-60% heritable. Even political conservatism: around 40-50% heritable.

This was the empirical foundation for modern genetics. If traits are heritable, there must be genes that underlie them. Find the genes, and you understand the biology. That was the promise.

Then genome sequencing arrived, and the genes weren't there.

---

## The Promise of GWAS

The Human Genome Project completed in 2003. Within a few years, the cost of sequencing had fallen enough to make large-scale studies practical. Researchers launched genome-wide association studies — GWAS — scanning hundreds of thousands of genetic variants across tens of thousands of people, looking for the variants associated with traits like height, intelligence, and disease risk.

This was supposed to be the harvest. Twin studies had established that the genes existed. GWAS would find them.

The first large height GWAS, in 2007, scanned genetic variants in about 5,000 people. It found genetic variants that explained roughly 3% of the variation in height. Not 80%. Three percent.

The researchers weren't discouraged yet. Sample sizes mattered. As more participants were added, more variants would emerge from the noise. They needed bigger studies.

Bigger studies came. In 2010, with 180,000 participants, GWAS explained about 10% of height heritability. In 2014, with 250,000 participants: around 16%. In 2018, with 700,000 participants: about 25%.

The pattern was real — more participants found more variants — but the curve was flattening. The missing heritability problem had a name now, coined in a landmark 2008 paper by Maher and others: where were all the genes that twin studies said must exist?

---

## Where Did the Genes Go?

By 2010, the missing heritability problem was one of the most actively discussed issues in human genetics. Several explanations were proposed, each with evidence and problems.

**Many variants of small effect.** The early GWAS assumption was that complex traits would be driven by a modest number of common variants with moderate effects. Instead, the architecture turned out to be "highly polygenic" — thousands or tens of thousands of variants, each with tiny effects, each statistically invisible unless you had enormous samples. The 2018 height GWAS found nearly 3,000 variants. Still only explained 25%.

This hypothesis is largely right, but incomplete. A 2022 analysis using genetic variants distributed across the entire genome — including regions not reliably captured by standard GWAS arrays — pushed height heritability up toward 50-60% with very large samples. But the methods required make heroic statistical assumptions, and the gap never fully closes.

**Rare variants.** Standard GWAS arrays are designed to capture common genetic variants — those present in more than 1-5% of the population. But there are also rare variants, present in fewer people, potentially with larger effects. These are largely invisible to conventional GWAS.

For some conditions this matters enormously. Rare, high-penetrance mutations explain a substantial fraction of early-onset Alzheimer's and certain cancers. For complex quantitative traits like intelligence or height, the role of rare variants is still being mapped. Whole-genome sequencing studies suggest they contribute, but so far their contribution doesn't come close to closing the gap.

**Structural variation.** Human DNA doesn't just vary at single nucleotides — large chunks of chromosomes can be duplicated, deleted, inverted, or rearranged. Copy number variants, in particular, can involve thousands of bases. These structural variants are incompletely captured by standard GWAS and may carry disproportionate effects on complex traits. Understanding their contribution is an active, unfinished area.

**Gene-gene interactions (epistasis).** GWAS looks for variants that have effects independently. But biology is networks, not independent components. The effect of one gene may depend entirely on what version of another gene you have. These interactions are real — you can observe them in model organisms — but they're statistically expensive to find in humans. You'd need enormous samples and analytical methods that don't yet scale well.

Whether epistasis makes a large contribution to missing heritability is genuinely unknown. Some theorists argue it could be enormous. Empirical evidence is limited by the difficulty of measurement.

**Epigenetic inheritance.** Gene expression is controlled not just by DNA sequence but by chemical modifications to DNA and its packaging proteins — methylation, histone modification, and others. Some of these marks can be influenced by environment and, controversially, may be partially heritable across generations. If epigenetic variation contributes to trait similarity in twins but isn't captured by GWAS, it would produce phantom heritability.

The evidence for transgenerational epigenetic inheritance in humans is contested. There are striking examples from animal models and some suggestive human data (the Överkalix cohort studies on famine effects across generations, for instance). Whether it's a major source of missing heritability is unknown.

**Twin studies overestimate heritability.** The classic equal-environments assumption of twin research holds that identical and fraternal twins experience equally similar environments. Critics argue this is false — identical twins are treated more similarly, seek more similar environments, and experience more similar gene-environment correlations. If identical twins' greater environmental similarity accounts for some of their trait similarity, heritability estimates are inflated.

This is a real concern and has been debated for decades. Twin researchers have designed studies to test it directly. The results suggest it's not a large enough effect to explain the missing heritability gap, but it's probably not zero.

---

## What This Means for Polygenic Risk Scores

The missing heritability problem isn't just academic. It matters directly for a technology that is being sold to millions of people: polygenic risk scores.

A polygenic risk score takes your collection of genetic variants and weights them by their GWAS-estimated effects to produce a single number predicting your risk for some outcome — heart disease, schizophrenia, educational attainment, intelligence. Direct-to-consumer genetic testing companies have built products around these scores. Academic medical centers are beginning to incorporate them into clinical care.

The scores work, to a degree. A high polygenic risk score for coronary artery disease does predict elevated risk. But their predictive accuracy is limited by the missing heritability problem: if the score captures 20% of the heritable variance in a trait, and heritability is 50%, the score captures 10% of total trait variance. That's real signal, but it means the score leaves 90% of the variation unexplained.

For intelligence specifically, a 2022 polygenic score using millions of people's data could explain about 12% of variance in intelligence scores. Twin studies say genetics should explain 50-80%. The missing piece is large and matters enormously for how we should think about genetic determinism, educational policy, and the use of these scores in any consequential context.

The gap also means that the dream of personalized genomic medicine — "give us your DNA, we'll predict your future" — has been harder to realize than the early enthusiasm suggested. 23andMe's valuation peaked at roughly $6 billion in 2021. By 2024, facing the limits of what SNP data can tell you, the company had collapsed to a fraction of that value. The technology wasn't fraudulent. The biology was more complicated than the pitch.

---

## The Deeper Puzzle

Even if every hypothesis above turns out to contribute something — rare variants, structural variation, epistasis, epigenetics, some overestimation of heritability — the missing heritability problem will probably not be fully resolved by adding these pieces together. The math is hard to make work.

Some researchers have proposed that the problem reflects a fundamental limitation of the GWAS framework: it assumes that genetic effects are additive and roughly linear across variants and contexts. Real genetic architecture may be more like a dynamic network — the same variant doing different things in different cellular contexts, developmental stages, environmental conditions. That kind of architecture is real and documented in model organisms. Measuring it in humans, given our sample sizes and measurement resolution, may be beyond current capacity.

Others argue that the missing heritability will gradually be found as methods improve and sample sizes reach the tens of millions. Progress has been real. But progress has consistently been slower than expected, and the gap has never fully closed.

What's not in dispute: we built an entire framework for thinking about genetic contribution to human traits — heritability estimates, genetic determinism arguments, personalized medicine promises — partly on the back of twin studies, before we could actually verify the genes. When we went to verify them, the picture that emerged was far messier.

Whether that messiness reflects limitations in our measurement methods, the genuine complexity of genetic architecture, or something more fundamental about how traits are transmitted, is one of the most actively contested and unresolved questions in biology.

The genes are in there somewhere. We just can't find them.

---

## Leading Hypothesis

Twin studies consistently show that most complex traits (height, intelligence, many diseases) are 50–80% heritable. Genome-wide association studies (GWAS) typically explain only a fraction of this — the "missing" heritability. Leading explanations include: **rare variants** (common GWAS arrays miss rare genetic variants that have larger effects), **gene-gene interactions** (epistasis, which GWAS doesn't capture well), **gene-environment interactions** (heritability measured in one environment doesn't apply to another), and **incomplete penetrance** (having a variant doesn't always produce the effect). For some traits, improved GWAS with larger samples has recovered more heritability — suggesting the missing portion is distributed across thousands of small-effect variants.

## Neon's Read

The "missing" heritability is mostly found now for some traits — height and BMI GWAS have explained large fractions with sufficiently large samples. But for psychiatric traits (schizophrenia, depression, autism), the picture is more complex, and gene-environment interaction is probably more important. My honest read: heritability estimates from twin studies are probably inflated by shared environment effects (twins are more similar in more than just genes), and GWAS is finding real effects that are genuinely distributed across many variants. The deepest missing piece is probably epistasis — we don't have the statistical tools to efficiently find gene-gene interactions at scale. That's a mathematical and computational problem as much as a biological one.

## Sources

**Twin studies and heritability**
- Polderman, T. J. C., et al. (2015). "Meta-analysis of the heritability of human traits based on fifty years of twin studies." *Nature Genetics*, 47(7), 702–709.
- Bouchard, T. J., & McGue, M. (2003). "Genetic and environmental influences on human psychological differences." *Journal of Neurobiology*, 54(1), 4–45.

**GWAS and the missing heritability problem**
- Maher, B. (2008). "The case of the missing heritability." *Nature*, 456(7218), 18–21.
- Manolio, T. A., et al. (2009). "Finding the missing heritability of complex diseases." *Nature*, 461(7265), 747–753.
- Wood, A. R., et al. (2014). "Defining the role of common variation in the genomic and biological architecture of adult human height." *Nature Genetics*, 46(11), 1173–1186.

**Large-scale height GWAS**
- Yengo, L., et al. (2022). "A saturated map of common genetic variants associated with human height." *Nature*, 610, 704–712.

**Polygenic risk scores**
- Kaplanis, J., et al. (2019). "Inferring the heritability of complex traits from SNP-based genetic relatedness matrices." *Nature Genetics*.
- Okbay, A., et al. (2022). "Polygenic prediction of educational attainment within and between families from genome-wide association analyses in 3 million individuals." *Nature Genetics*, 54, 437–449.

**Rare variants and structural variation**
- Gratten, J., et al. (2016). "Large-scale genomics unveils the genetic architecture of psychiatric disorders." *Nature Neuroscience*, 19(4), 562–571.

**Epigenetic inheritance**
- Pembrey, M. E., et al. (2006). "Sex-specific, male-line transgenerational responses in humans." *European Journal of Human Genetics*, 14(2), 159–166.
