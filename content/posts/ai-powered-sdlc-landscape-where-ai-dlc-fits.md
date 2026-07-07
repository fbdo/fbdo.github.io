+++
draft = false
date = 2026-07-06T10:00:00+01:00
title = "The AI-Powered SDLC Landscape: Where AI-DLC Fits"
slug = ""
tags = ["AI-DLC", "spec-driven development", "agentic AI", "GenAI", "Kiro", "SDLC", "AWS"]
categories = ["cloud"]
+++

# The AI-Powered SDLC Landscape: Where AI-DLC Fits

*AI-DLC v2 just hit preview ([awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows)). To mark it, I'm running a short series on AI-DLC over the coming weeks. This first post steps back to map the whole AI-powered SDLC landscape and show where AI-DLC fits; the follow-ups go deeper into what v2 changes and how to put it to work. As the AI-DLC EMEA Champion, this is the terrain I live in day-to-day — so treat this as a practitioner's map, not a marketing recap.*

![The journey toward an autonomous SDLC — from autocomplete through SDD to an agentic SDLC](/images/ai-powered-sdlc-landscape-where-ai-dlc-fits/ai-dlc-journey-4-waypoints.svg)
*Figure: The journey to an autonomous SDLC — Autocomplete → SDD → Human-managed SDLC → Agentic SDLC, with a fully-autonomous aspirational endpoint. The single axis — how much of the lifecycle does AI drive? — sorts every framework.*

## We got great coding agents. We didn't get faster.

Here's the uncomfortable finding. In a randomized controlled trial, METR gave experienced open-source developers access to early-2025 AI tools on real issues in their own repos. The developers *believed* AI made them about 20% faster. They were actually **19% slower** [\[S19\]](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/).

That's not an isolated result. DORA's 2024 State of DevOps report found the same paradox at the organizational level: a 25% increase in AI adoption correlated with a **1.5% drop in delivery throughput and a 7.2% drop in delivery stability** — even as individual developers reported feeling more productive [\[S20\]](https://dora.dev/report/2024).

The tools got genuinely good. The *operating model* around them didn't move. We bolted powerful coding agents onto workflows designed for humans typing every line, and the promised gains largely failed to show up. Tellingly, DORA's 2025 follow-up saw throughput turn positive — once teams learned *how* to work with AI [\[S20\]](https://dora.dev/report/2024). The missing piece was never model quality. It was process.

That gap is why, across 2025–2026, we suddenly have *so many* AI-powered SDLC frameworks. They're all answers to the same question.

## A Cambrian explosion of frameworks

In barely eighteen months we've seen a Cambrian explosion of AI-coding frameworks — Spec Kit, OpenSpec, Kiro, Taskmaster, Cursor, Antigravity, BMAD, AI-DLC. An explosion this sudden is never random: something in the environment shifts and a wave of empty niches opens at once. Four pressures opened these:

**1. Two failure modes left a gap in the middle.** On one side, AI-*assisted* coding — autocomplete per keystroke, no view of the lifecycle. On the other, AI-*autonomous* — "generate the whole app," no human oversight. Both break at production scale [\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/)[\[S1\]](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/). Every framework below is filling the middle ground. The specific failure modes they target: **intent drift** (underspecified prompts), **context decay** (the agent forgets earlier decisions as the codebase grows), and **unverifiable output** (no acceptance criteria to check against) [\[S2\]](https://thebcms.com/blog/spec-driven-development).

**2. Context is the real bottleneck — not code generation.** The winning idea is a *durable layer* underneath the agents: specs and plans that persist across sessions, memory that survives across teammates. That's what lets AI safely take on more of the lifecycle [\[S6\]](https://www.augmentcode.com/guides/what-is-aidlc-ai).

**3. The "best" coding agent changes every month.** So frameworks compete on being *portable* planning layers you can carry between agents, rather than betting on one [\[S4\]](https://openspec.dev/)[\[S7\]](https://github.com/github/spec-kit).

**4. The industry framing has converged** on a single journey: from specs as *static planning documents* toward AI that *drives more and more of the lifecycle* [\[S15\]](https://www.augmentcode.com/tools/best-spec-driven-development-tools). That journey is the axis everything else sorts on.

Which raises the real question behind all of them: **how much of the SDLC are you ready to let AI drive?**

## The journey: from spec-driven to autonomous SDLC

Line every framework up on one axis — *how much of the lifecycle does AI drive?* — and the noise resolves into a single continuum of increasing AI autonomy. It helps to fix the two ends first, because everything else lives between them:

- **Spec-Driven Development (SDD)** — the **specification is the durable artifact and the source of truth**. You write and refine a living spec; the agent generates the implementation from it; the spec stays in the repo as living documentation. Scope: *plan → build a feature*. Lightweight, agent-agnostic, brownfield-friendly. Most SDD tools converge on the same four-phase loop — **Specify → Plan → Tasks → Implement** — each with a human checkpoint [\[S2\]](https://thebcms.com/blog/spec-driven-development). *AI executes; humans specify and approve.*

- **Autonomous, AI-native SDLC** — a full **operating model across the classic SDLC phases** (requirements & design → build & test → deploy & operate), with human-in-the-loop checkpoints and an audit trail built in. *AI plans and executes across the lifecycle; humans decide and validate.* Here the **methodology and its checkpoints** are the product.

Here's where the major frameworks land:

| Framework | Primary identity | Placement on the journey |
| --- | --- | --- |
| **GitHub Spec Kit** [\[S7\]](https://github.com/github/spec-kit)[\[S15\]](https://www.augmentcode.com/tools/best-spec-driven-development-tools) | SDD toolkit: constitution → specify → plan → tasks → implement; static markdown specs; 18+ agents | Pure SDD, agent-agnostic (broadest reach) |
| **OpenSpec** [\[S4\]](https://openspec.dev/)[\[S12\]](https://medium.com/@richardhightower/agentic-coding-gsd-vs-spec-kit-vs-openspec-vs-taskmaster-ai-where-sdd-tools-diverge-0414dcb97e46) | SDD planning layer; per-change proposals with spec *deltas*; strict proposal→apply→archive state machine; specs-in-repo; 20+ tools | Pure SDD, brownfield-first |
| **Taskmaster AI** [\[S12\]](https://medium.com/@richardhightower/agentic-coding-gsd-vs-spec-kit-vs-openspec-vs-taskmaster-ai-where-sdd-tools-diverge-0414dcb97e46) | AI-as-project-manager: parses a PRD into a hierarchical, dependency-aware task graph, hands tasks to any agent; multi-model tiers; Cursor-first via MCP | SDD, decomposition-focused |
| **Cursor (Plan Mode + rules)** [\[S13\]](https://thebcms.com/blog/spec-driven-development)[\[S15\]](https://www.augmentcode.com/tools/best-spec-driven-development-tools) | IDE-native: read-only Plan Mode drafts spec+plan; `.cursor/rules`/`AGENTS.md` act as a lightweight constitution; pseudo-specs, no lifecycle validation | SDD — IDE-embedded (ephemeral, tool-local spec) |
| **Kiro (Specs)** [\[S8\]](https://kiro.dev/docs/specs/)[\[S15\]](https://www.augmentcode.com/tools/best-spec-driven-development-tools) | Spec mode in the IDE: requirements/design/tasks in EARS notation; 2026 Requirements Analysis uses SMT solvers to catch contradictions pre-codegen | SDD built into an agent/IDE |
| **Google Antigravity** [\[S13\]](https://thebcms.com/blog/spec-driven-development) | Agent-first desktop IDE where every action originates from a spec; built for deeply autonomous agents operating under spec constraints | Agentic IDE, spec-constrained autonomy |
| **BMAD** [\[S10\]](https://docs.bmad-method.org/)[\[S16\]](https://labs.sogeti.com/transforming-the-agentic-sdlc-with-bmad-a-graphic-overview/) | Governed team of role-based agents (Analyst/PM/Architect/PO/Dev/QA/SM) — ~12 in v4, 19+ in v6; two-phase (agentic planning → context-engineered implementation); supports both greenfield and brownfield [\[S18\]](https://bmad-code-org-bmad-method-6.mintlify.app/workflows/document-project) | Human-managed SDLC — **human-orchestrated** multi-agent (you invoke and gate each persona) |
| **AI-DLC** [\[S1\]](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)[\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) | AI-native methodology: Inception/Construction/Operations, Mob rituals, adaptive depth | **Agentic SDLC — furthest along**; AI-orchestrated full lifecycle (methodology) |

## Where AI-DLC lands

**What it is** [\[S1\]](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)[\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/): an AI-native methodology developed by AWS's AI Engineering team that repositions AI from *coding assistant* to *development orchestrator* — "AI plans and executes; humans decide and validate." The methodology was **introduced in July 2025** (method paper + first AWS blog); the **adaptive workflow scaffolds** (Amazon Q Developer Rules and Kiro Steering Files) that implement it were **open-sourced in November 2025**. It's a methodology with an open-source reference implementation, not a product.

It sits **furthest along the journey** for three reasons [\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/):

1. **Adaptive breadth and depth** ("no hard-wired, opinionated SDLC workflows"). AI recommends which stages to run and how deep to go, per intent. Most SDD tools run a fixed pipeline.
2. **Collaboration as a ritual** — Mob Elaboration and Mob Construction, where stakeholders assemble to review and validate AI's plans and artifacts live.
3. **Auditability by design** — every AI plan, decision, and human approval is logged; documentation-first [\[S11\]](https://eleks.com/blog/aws-ai-dlc-explained/).

And a crucial clarification: **"autonomous" doesn't mean "unsupervised."** AI-DLC pushes AI to drive the widest span of the lifecycle of any framework here — but the human rituals and the audit trail are *precisely what make that autonomy safe*. The journey isn't toward removing humans. It's toward AI owning execution while humans own decisions and validation.

### This isn't hypothetical — partners are already operating here

The clearest sign AI-DLC is more than a thought experiment: global SIs are already productizing it, and the numbers are showing up in AWS's own AI-DLC customer proof points.

- **A global systems integrator has built on it.** Wipro — one of AI-DLC's early adopters — now ships a public [Agentic AI SDLC Orchestrator](https://aws.amazon.com/marketplace/pp/prodview-rfxhvo4wl2xxo) on AWS Marketplace that autonomously drives the lifecycle from ideation through deployment. In AWS partner enablement, Wipro reported using AI-DLC to stand up a production-ready enterprise healthcare-payer platform in roughly **20 hours** — with three geographically distributed teams and domain-driven design.
- **The proof points repeat across AWS's AI-DLC adopter stories.** A leading Philippines bank built and shipped a new application in **two days** (a ~50× velocity jump); a leading media network delivered six applications in two days (~**4× productivity**, ~223 engineer-days saved — roughly ten months of work); and a global ratings-and-analytics provider compressed **eight months of work into one week**. Different industries, same signal: the gains land when the *operating model* changes, not just the tool — the mirror image of the METR/DORA paradox that opened this post.
- **And from my own seat:** across the EMEA partner rollouts I've led, the moment AI-DLC "clicks" is almost never the code generation. It's the first Mob Elaboration — a room of stakeholders watching AI turn a fuzzy intent into a validated plan in minutes — and the audit trail that means no one has to reconstruct *why* a decision was made three sprints later. The teams that get value are the ones ready to change how they operate, not the ones shopping for a faster autocomplete.

### AI-DLC vs. Spec-Driven Development — different altitudes, not competitors

The most common confusion I hear is "isn't AI-DLC just another SDD tool?" No — they operate at **different altitudes**. SDD lives at the *feature* altitude (the spec is the durable artifact). AI-DLC lives at the *lifecycle* altitude (the methodology and its checkpoints are the product). They actually compose: you can run SDD-style specs *inside* an AI-DLC construction phase.

| | **Spec-Driven Development** | **AI-DLC** |
|---|---|---|
| **Unit of work** | A feature / change [\[S2\]](https://thebcms.com/blog/spec-driven-development) | An end-to-end lifecycle, inception → operations [\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) |
| **Source of truth** | The living spec in the repo [\[S2\]](https://thebcms.com/blog/spec-driven-development) | The methodology + its logged decisions [\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/)[\[S11\]](https://eleks.com/blog/aws-ai-dlc-explained/) |
| **AI's role** | Executes from a spec you author [\[S2\]](https://thebcms.com/blog/spec-driven-development) | Plans *and* executes across stages; drives the loop [\[S1\]](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)[\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) |
| **Human's role** | Specify & approve each phase [\[S2\]](https://thebcms.com/blog/spec-driven-development) | Decide & validate at rituals (Mob Elaboration/Construction) [\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) |
| **Process shape** | Mostly a fixed four-phase loop [\[S2\]](https://thebcms.com/blog/spec-driven-development) | Adaptive breadth/depth — AI recommends which stages run (Principle 10) [\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) |
| **Onboarding cost** | Low — drop into one repo, one feature [\[S2\]](https://thebcms.com/blog/spec-driven-development) | Higher — it's a team operating model, not a tool [\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) |

**Pick SDD when** you want a lightweight, agent-agnostic way to make a single team's coding more reliable — brownfield changes, a feature at a time, spec-in-repo as living documentation. Low ceremony, fast to adopt [\[S2\]](https://thebcms.com/blog/spec-driven-development)[\[S4\]](https://openspec.dev/).

**Pick AI-DLC when** the bottleneck isn't code generation but the *whole delivery loop* — you want AI driving across requirements, design, build, and operations, with explicit human-validation rituals and an audit trail for governance. It asks more of the team (it's a methodology, not a plugin) but reaches further along the autonomy journey [\[S1\]](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)[\[S3\]](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/).

> In one line: **SDD makes your coding trustworthy; AI-DLC makes your whole lifecycle AI-native.** Start with SDD for a fast win in one repo; adopt AI-DLC when you're ready to change how the team operates.

A quick way to self-place, without overthinking it: if the work is a **throwaway experiment**, vibe-code it and move on; if it's **a feature your team must own and maintain**, reach for SDD; if it's **a whole lifecycle a team must own, evolve, and answer for**, you're in AI-DLC territory.

### Why (and when) a framework like AI-DLC pays off

Recall the lesson from Section 1: **the bottleneck was never code generation — it was the operating model around it.** Faster code generation doesn't fix intent drift, context decay, or unverifiable output; it accelerates them. That's precisely the gap a full-lifecycle framework like AI-DLC is built to close.

**Why the whole-lifecycle model earns its keep:**

1. **It targets the delivery loop, not the keystroke.** AI-DLC pushes AI across requirements, design, build, and operations rather than optimizing one editor session — so the productivity that a per-feature tool leaks back into rework and handoffs is captured at the level where it's actually lost [S1][S3].
2. **Governance is a first-class output, not an afterthought.** Every AI plan, decision, and human approval is logged; documentation is produced as you go, not reconstructed later [S3][S11]. For regulated or audited environments, that trail is often the difference between "AI-assisted" being a pilot and being allowed in production.
3. **Adaptivity keeps the ceremony proportional.** Principle 10 — no hard-wired workflow — means AI recommends which stages to run and how deep for a given intent, so a small change doesn't drag the full apparatus behind it while a complex epic still gets the rigor it needs [S3].
4. **The human rituals make autonomy safe.** Mob Elaboration and Mob Construction put the team in the loop *together*, validating AI's plans live rather than one developer rubber-stamping output alone [S3]. Autonomy widens what AI drives; the rituals keep humans owning the decisions.

**When teams benefit most:**

- The pain is the **whole delivery loop** — misaligned requirements, decisions lost between sessions, output no one can verify — not just "we type code slowly." [S2][S19][S20]
- Work spans **full epics or sprints** with **multiple stakeholders** who need to review at gates, and where **architectural decisions must be explicit and defensible** [S21].
- **Governance, auditability, or regulatory pressure** make a logged decision trail valuable in its own right [S3][S11].
- The team is **ready to change how it operates** — AI-DLC is a methodology, not a plugin, so the return comes from adopting the operating model, not from dropping a tool into one repo [S1][S3].

**When it's overkill:** throwaway prototypes and single-feature work don't need a lifecycle methodology. If the goal is a fast, reliable win in one repo, spec-driven development (or plain vibe-based prototyping for experiments) is the lighter, right-sized choice — and, as noted above, SDD-style specs compose neatly *inside* an AI-DLC construction phase when you later scale up [S2][S4].

> The question isn't "which framework wins?" — it's *"is my bottleneck a single feature, or the way my whole team delivers?"* AI-DLC is built for the second answer.

## The takeaway

Every framework on this map is really answering one question: **how much of your lifecycle are you ready to let AI drive?** The frameworks aren't rivals fighting over the same territory — they're waypoints on a journey from AI-assisted editing to a fully AI-native SDLC, each appropriate at a different level of rigor and ambition.

So here's the practitioner's question to sit with: **where on that journey is your team ready to operate today** — and what's the one process change that would let you take the next step?

*I'd genuinely like to know: how much of your delivery loop is AI driving right now? Reply and tell me where you land on the map.*

---

## References

- **[S1]** [AI-Driven Development Life Cycle: Reimagining Software Engineering](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) — AWS DevOps Blog. AI-assisted vs. AI-autonomous framing; AI-DLC methodology introduced (31 Jul 2025).
- **[S2]** [Spec-Driven Development: The Definitive 2026 Guide](https://thebcms.com/blog/spec-driven-development) — BCMS. The four-phase loop (Specify → Plan → Tasks → Implement), the three failure modes (intent drift, context decay, unverifiable output), and EARS notation.
- **[S3]** [Open-Sourcing Adaptive Workflows for AI-DLC](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/) — AWS DevOps Blog. Open-source scaffolds release; the three challenges, Principle 10, and Mob Elaboration/Construction (29 Nov 2025).
- **[S4]** [OpenSpec](https://openspec.dev/) — Spec deltas, specs-in-repo, brownfield-first, agent-agnostic planning layer.
- **[S6]** [What is AIDLC?](https://www.augmentcode.com/guides/what-is-aidlc-ai) — Augment Code. The durable context layer; context and memory across sessions.
- **[S7]** [GitHub Spec Kit](https://github.com/github/spec-kit) — SDD toolkit: constitution → specify → plan → tasks → implement.
- **[S8]** [Kiro Specs documentation](https://kiro.dev/docs/specs/) — Requirements/design/tasks, EARS notation, three-phase specs.
- **[S10]** [BMAD Method documentation](https://docs.bmad-method.org/) — Ideation → agentic implementation; specialized role-based agents.
- **[S11]** [How AWS Labs Brings Structure to AI Coding](https://eleks.com/blog/aws-ai-dlc-explained/) — ELEKS. Documentation-first; human approvals at each stage.
- **[S12]** [Agentic Coding: GSD vs. Spec Kit vs. OpenSpec vs. Taskmaster AI](https://medium.com/@richardhightower/agentic-coding-gsd-vs-spec-kit-vs-openspec-vs-taskmaster-ai-where-sdd-tools-diverge-0414dcb97e46) — Rick Hightower (Medium). Tool profiles; Taskmaster multi-model/PM framing; OpenSpec change isolation.
- **[S13]** [Spec-Driven Development: The Definitive 2026 Guide](https://thebcms.com/blog/spec-driven-development) — BCMS. Cursor Plan Mode and Google Antigravity as SDD flavors.
- **[S15]** [6 Best Spec-Driven Development Tools for AI Coding in 2026](https://www.augmentcode.com/tools/best-spec-driven-development-tools) — Augment Code. Static-planning-vs-lifecycle framing; Kiro SMT solver; comparison table.
- **[S16]** [Transforming the Agentic SDLC with BMAD](https://labs.sogeti.com/transforming-the-agentic-sdlc-with-bmad-a-graphic-overview/) — Sogeti Labs. BMAD role-based agent team; two-phase planning → implementation.
- **[S18]** [BMAD Document Project Workflow](https://bmad-code-org-bmad-method-6.mintlify.app/workflows/document-project) — Official BMAD docs. First-class brownfield support: Document Project workflow, brownfield PRD/architecture templates, Test Architect for regression risk.
- **[S19]** [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) — METR. Randomized controlled trial: experienced developers were 19% slower with AI, despite believing they were ~20% faster.
- **[S20]** [Accelerate State of DevOps Report 2024](https://dora.dev/report/2024) — DORA / Google Cloud. A 25% increase in AI adoption correlated with a 1.5% drop in delivery throughput and a 7.2% drop in stability; the 2025 follow-up shows throughput turning positive as teams learn the operating model.


