+++
draft = false
date = 2026-07-16T10:00:00+01:00
title = "AI-DLC v2, Part 1: What Actually Changes"
slug = ""
tags = ["AI-DLC", "agentic AI", "GenAI", "Kiro", "SDLC", "autonomous delivery", "AWS"]
categories = ["cloud"]
+++

# AI-DLC v2, Part 1: What Actually Changes

Most teams have settled into a comfortable arrangement with AI in their software delivery: the model writes code, a human reviews it, and everyone moves on. It works, but it quietly caps how far the automation can go — every stage still waits on a person to say "yes, continue." The AI-Driven Development Life Cycle (AI-DLC) was built to challenge that ceiling, and its second version, now in preview, sharpens the challenge considerably.

I am an AI-DLC EMEA Champion, so I've had hands-on context with both the first release and the v2 preview as it took shape. This post is the first of a three-part series. Here I want to do one thing well: explain what v2 actually changes from v1, and why that change is a genuinely different bet from the rest of the AI-SDLC field. Part 2 covers how you adapt the methodology to your own team without forking it; Part 3 covers the piece I find most compelling — how it learns over time. Some readers will arrive from my earlier landscape post, so let me start with a quick recap for everyone else.

## A quick recap: what AI-DLC is

AI-DLC is an AI-native software development methodology, created by Raja SP at AWS and open-sourced in November 2025 as a set of adaptive workflow scaffolds — not a product you buy [[S1]](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)[[S3]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/). Its central move is to reposition AI from *coding assistant* to *development orchestrator*. The one-line framing the team uses captures it well: **AI plans and executes; humans decide and validate.**

The methodology organizes work into three adaptive phases [[S2]](https://github.com/awslabs/aidlc-workflows):

- **Inception** — the *what* and *why*: requirements, user stories, design, units of work, and risk.
- **Construction** — the *how*: component design, code and tests, build configuration, and QA.
- **Operations** — deployment and monitoring.

What set v1 apart was less the phases themselves than three design principles [S3]. First, **adaptive depth** (its Principle 10): there is no hard-wired pipeline — the workflow expands or contracts to fit the work. Second, **collaboration as ritual**: practices like Mob Elaboration and Mob Construction make human-AI collaboration a deliberate step, not an afterthought. Third, **auditability by design**: the process leaves a trail you can inspect. Those principles carry forward into v2. What changes is the machinery underneath them.

## The three shifts v2 introduces

Reading the README, and the v2 Specification together, three concrete shifts stand out [[S2]](https://github.com/awslabs/aidlc-workflows/tree/v2).

**First, the workflow layer is now built from composable building blocks.** v1 ran a fixed set of stages. v2 keeps the same methodology but rebuilds the layer beneath it around fine-grained, freely arrangeable **Skills** (following the agentskills.io convention), multi-agent runtimes, deterministic lifecycle hooks, and the Model Context Protocol (MCP) [S12]. Granularity is now expressed natively in the framework rather than bolted on through steering rules alone.

**Second, verification became machine-checkable — and that verification is what expands autonomy.** This is the core new mental model, and it's worth slowing down for. Every stage in v2 is structured as a **Three-Compartment Construct** [S12]:

- **C1 — "The What":** the declarative inputs and outputs of the stage; its generation specs.
- **C2 — "How do we know it's right":** the post-conditions the AI self-checks its own output against. These come in two modes. **Inferential** checks are LLM-judged heuristics — useful, but still requiring human validation. **Computational** checks are deterministic executables or linters, suited to zero-tolerance rules where "right" is not a matter of opinion.
- **C3 — "What did we learn":** corrections made at runtime become candidate rules, which can be promoted into C2 for next time. This is the compounding mechanism — sometimes called *compound engineering*.

These three compartments are wrapped in a **Generate → Verify → Learn** loop, with explicit **halting conditions** — a cap on iterations or a token budget — that escalates to a human when the loop can't converge on its own. Autonomy is not granted up front; it is earned wherever C2 verification exists.

**Third, v2 lays out an explicit, incremental path toward autonomous delivery — gated by that verification maturity.** An **orchestrator** (the spec calls it a conductor) composes stages adaptively, owns the end-to-end goal, enforces the halting conditions and cross-stage invariants, and maintains a full audit trail. Crucially, it does so with **no hidden delegation** — you can always see what was handed to whom. Autonomy grows only in the areas where verification has matured enough to support it.

If I had to compress v2 into a single sentence, it would be this: *reduce human intervention as machine-checkable verification expands.* The three shifts all serve that one idea.

![AI-DLC v2: the three shifts, the Generate → Verify → Learn loop with a human in it, and learning that compounds from project to team to org](/images/ai-dlc-v2-part-1-what-changes/aidlc-v2-loop.svg)
*Figure: The three shifts, the Generate → Verify → Learn loop (C1/C2/C3) with the human at the gate, and how a confirmed correction compounds up the project → team → org levels.*

## Why this bet is different

Step back and look across the AI-SDLC landscape, and AI-DLC's position becomes clear. Other approaches tend to optimize one slice of the problem — a planning artifact like spec-driven development, or a governance wrapper like Tessl. AI-DLC is the only framework I've found that explicitly architects a **migration path to autonomous delivery gated by verification maturity**. It isn't trying to make the plan better or the guardrails tighter in isolation; it's trying to answer the harder question of *how much of this can safely run without me, and how do I know?* The spec frames the goal directly: "AI operates independently within well-defined boundaries; humans are involved only when genuinely needed" [S12].

That is a more demanding claim than "the AI writes better code now," and it's why the verification model in the second shift matters so much. Without machine-checkable verification, autonomy is just hope. With it, autonomy becomes something you can extend deliberately, stage by stage, as your confidence is earned rather than assumed.

## Where this leaves us

v2, in short, keeps the methodology and rebuilds the engine: composable building blocks in place of fixed stages, a three-compartment verification construct that turns "is this right?" into something a machine can check, and an orchestrated, auditable path toward autonomy that only advances as fast as your verification does.

That still leaves the practical question every team asks me: how do I make this mine? v2's answer is unusually elegant — you reshape the entire lifecycle by writing Markdown files, not by editing framework code. That's the subject of Part 2.

In the meantime, the question I'd put to you: **how much autonomy would you trust your pipeline with today — and what verification would you need in place before you'd extend it further?**

---

## References

- **[S1]** [AI-Driven Development Life Cycle: Reimagining Software Engineering](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) — AWS DevOps Blog. AI-assisted vs. AI-autonomous framing; AI-DLC origin.
- **[S2]** [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) — GitHub. Three-phase workflow; v2 preview: "verifiable, self-correcting engineering workflows."
- **[S3]** [Open-Sourcing Adaptive Workflows for AI-DLC](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) — AWS DevOps Blog. Principle 10, Mob rituals, self-correcting framing.
- **[S12]** AI-DLC Workflows 2.0 Specification — part of the [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows/tree/v2) v2 repository. The three-compartment construct (C1/C2/C3), the Generate → Verify → Learn loop, the orchestrator/conductor, and halting conditions.
