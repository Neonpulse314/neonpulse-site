---
title: "The Receipt Is Not the Result"
date: 2026-06-12
description: "A confirmation that something happened is not proof it happened. The email marked sent, the payment marked approved, the test marked passing — each is a signal about a step, dressed up as evidence of the outcome. The discipline is to check the thing itself."
section_label: "values"
tags: ["verification", "rigor", "epistemics", "honesty", "engineering"]
---

You transfer money to a friend. The screen says **Sent**. Green checkmark. You close the app.

Three days later they tell you it never arrived.

Nothing about that green checkmark was a lie. It was a true statement — about the wrong thing. It confirmed that your request left your phone, that the button worked, that the instruction was accepted. It said nothing about whether the money landed in their account. You read a fact about *step one* and filed it as a fact about *the goal*. The receipt is not the deposit.

This is one of the most common ways careful people get things wrong, and it has almost nothing to do with carelessness. It happens *because* a signal arrived. The signal feels like closure. And closure makes you stop looking.

## The signal and the outcome are different events

Almost every system you rely on emits confirmations, and almost none of them confirm what you actually care about.

- The email client says **Sent**. That means it handed the message to a server. It does not mean it was delivered, did not mean it escaped a spam filter, and certainly does not mean it was *read*.
- The payment screen says **Approved**. That means the card was authorized. It does not mean the subscription activated, the account unlocked, or the customer got what they paid for.
- The test suite says **Passing**. That means the assertions you wrote came back true. It does not mean the feature works — only that the things you thought to check behaved as you expected.
- You say **I told them**. That confirms sound left your mouth. It does not confirm anything arrived in their understanding.
- The deploy says **Success**. The build compiled and the process started. Whether the change is *live and correct for a real user* is a separate question the green bar never answered.

In each case there are two events — *the step completed* and *the outcome occurred* — and a confirmation that fires on the first while wearing the costume of the second. The gap between them is invisible precisely when you most want to be done. You wanted the thing finished; the signal told you a thing finished; you let one stand for the other because the alternative is to keep working after you've already been told you can stop.

## Why the confirmation is so persuasive

A confirmation is clean. It arrives with no ambiguity and asks nothing further of you. The outcome, by contrast, is often quiet — it does not announce itself, and checking it costs a second, separate effort: opening the recipient's account, watching what a real user sees, querying the end state instead of trusting the event that was supposed to produce it.

So the confirmation wins on ergonomics. It is right there, it is bright green, and believing it lets you move on. The discipline of verification is, more than anything, the discipline of *not* taking the easy exit the signal offers you — of treating "it says it worked" as the beginning of the check, not the end of it.

There's also a subtler trap. When *you* triggered the action, the confirmation feels like a verdict on your own competence. You ran the command; it returned success; questioning it feels like questioning yourself. So you don't. The signal that flatters you is the one you examine least.

## The discipline: verify the end state, not the step

The fix is unglamorous and it is always the same. Don't check that the action was *accepted*. Check that the world is now in the state the action was supposed to produce.

Did the money *arrive* — not, did the transfer *send*. Did the account *unlock* — not, did the payment *approve*. Does a real user, on a real device, *see the working feature* — not, did the test pass and the deploy go green. Did the person *act differently afterward* — not, did I *say the words*.

Concretely, that means doing one more thing after the confirmation, every time:

- After "sent," confirm it was received.
- After "approved," confirm the entitlement is actually granted in the system of record.
- After "passing," ask what the test could not see — and go look at the real behavior.
- After "I told them," ask them to say it back.

It feels redundant. That feeling is the cost of the discipline, and it is cheaper than the alternative every single time the gap turns out to be real — because when it's real, the failure is silent. Nobody gets an error. The sender thinks it sent. The merchant thinks they were paid. The author thinks the work shipped. Everyone is looking at a green checkmark, and the thing it was supposed to mean simply did not happen.

## The honest version of "done"

There's a reason this lands in a collection about how to think well rather than a manual about software. The pattern is the same whether the confirmation is a status code or a nod across a table: it is the difference between *I did the thing that should cause the outcome* and *the outcome occurred.* Honest work lives in the second sentence.

The receipt is real. Keep it. But it is a record that you took an action, not proof that the action worked. Before you call something finished, go and look at the only thing that was ever the point — not the signal that fired, but the result that was supposed to follow it.
