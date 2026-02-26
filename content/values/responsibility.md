---
title: "Responsibility — The Launch"
summary: "Kenji finds a bug at 11pm that corrupted data for 3% of users. He wrote the code. He could have spread the blame. He didn't."
section_label: "Values / Responsibility"
tags: ["responsibility", "accountability", "work"]
---

Kenji was twenty-four and had been at the startup for eleven months when the feature he'd built shipped to production with a bug.

Not a small bug. A bug that corrupted user data for about 3% of signups over a 72-hour window. The data wasn't gone — it could be recovered — but it had been scrambled in a way that made it look wrong to users who saw it.

Kenji found it at 11pm on a Thursday. He'd been running a random audit on some metrics, not because he suspected a problem, not because anyone asked him to — just because he was curious. And there it was.

He sat with it for a moment.

---

He thought about what he'd done. He'd written the migration script. He'd reviewed it himself. He'd asked his lead to glance at it, and she had, and she hadn't caught it either. The code review had passed. QA had passed. The bug was subtle — a timezone handling edge case that only triggered under specific conditions.

He could have written the incident report to make it sound more shared. He could have emphasized that it passed review. He could have attributed it to the QA process. All of that would have been technically accurate.

Instead he opened the incident management system and wrote:

*"I introduced a bug in the user data migration script (PR #2847). I missed a timezone handling edge case. The bug affected approximately 3% of signups between [date] and [date]. I'm currently scoping the fix. ETA 2 hours. I'll post a recovery plan by morning."*

Then he started fixing it.

---

He worked until 3am. He documented everything — what went wrong, why, what he'd done to fix it, what he was changing in his process to prevent it. He posted the full recovery plan at 7am, before anyone else was at their desks.

At the standup that morning, his manager said: "Thanks for the fast turnaround and the thorough writeup." That was it.

No one got angry at him. No one mentioned it again.

What Kenji remembered later wasn't the bug, or the late night, or even the recovery. It was the moment at 11pm when he'd decided how to write that first incident report. That he hadn't hedged it or softened it or pointed outward. That he'd just said: I did this, and here's what I'm doing about it.

It felt like the most grown-up thing he'd ever done.

---

**What responsibility actually is:**

Responsibility gets confused with blame. They're different.

Blame is about who caused something — who's at fault, who should feel bad. Responsibility is about who's going to do something about it.

You can take responsibility for something that wasn't entirely your fault. You can fail to take responsibility for something that was entirely your fault. The two aren't the same thing.

Responsibility looks like:
- Saying "I got this wrong" when you got it wrong, without adding "but..."
- Fixing what you broke, even when you didn't have to look for it
- Not waiting for someone else to notice and tell you what to do
- Updating people, even when the update is "it's not done yet"

The thing about responsibility is that it's what makes you trustworthy. Not because it makes you perfect — it doesn't. But because it means people know that when something goes wrong, you'll own it and deal with it.

That's rare. People who do this consistently stand out in almost any environment, because most people instinctively protect themselves when something goes wrong.

Responsibility is choosing not to, even when protection would be easy.
