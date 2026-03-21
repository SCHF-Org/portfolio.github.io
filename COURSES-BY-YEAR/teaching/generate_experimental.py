#!/usr/bin/env python3
"""
generate_experimental.py
Generates file stubs for the two experimental courses.
Run from the teaching/ root:
    python3 generate_experimental.py
"""

import os

BASE = os.path.expanduser("~/Sync/COURSES-BY-YEAR/teaching")

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  wrote {path.replace(BASE + '/', '')}")

# ============================================================
# PERSONHOOD IN THE AGE OF AI
# 15 weeks, one section, in development
# ============================================================

PERSONHOOD_WEEKS = {
    "week01": "The Puzzle/Mystery Distinction — Marcel and Hick",
    "week02": "Soul-Making Theodicy — Hick Part I and III",
    "week03": "Dostoevsky's Challenge — The Grand Inquisitor",
    "week04": "Personal Identity — Locke and Psychological Continuity",
    "week05": "What Matters in Survival — Parfit",
    "week06": "Consciousness and Other Minds — Nagel, Turing, Searle",
    "week07": "Second-Personal Knowledge — Stump",
    "week08": "Love as Perception of Value — Nussbaum",
    "week09": "Love as Caring — Frankfurt",
    "week10": "Mind and Body in Virtual Worlds — Chalmers",
    "week11": "The Avatar as Self",
    "week12": "Can You Fall in Love with an Avatar?",
    "week13": "Hick's Eschatology and the Agents' Transition",
    "week14": "Suffering from the Inside — Lewis",
    "week15": "Course Synthesis — Puzzle, Mystery, and Resolution",
}

PHILO_LAB_WEEKS = {
    "lab01": "Entering the Chamber — Ontology of Virtual Worlds",
    "lab02": "GLaDOS and the Problem of Other Minds",
    "lab03": "Trust, Cooperation, and Shared Agency",
    "lab04": "Autonomy and the Ethics of Experimentation",
    "lab05": "Identity, Memory, and What Survives",
}

def notes_stub(title, course):
    return f"""---
title: "{title}"
---

<!-- notes.qmd — {course}                                           -->
<!-- Portfolio: instructor notes visible here.                      -->
<!-- Website: .instructor-only divs hidden.                         -->

## Session Overview

::: {{.instructor-only}}
**Goal for this session:** [What should students leave understanding?]

**Opening move:** [How will you open the session?]

**Key tension to surface:** [What is the central philosophical tension?]

**Time allocation (75 min):**

- 10 min: [Opening activity]
- 20 min: [Main discussion]
- 20 min: [Close reading or case study]
- 15 min: [Small group work]
- 10 min: [Wrap-up and preview]
:::

## Discussion Questions

1. [Discussion question 1]

2. [Discussion question 2]

3. [Discussion question 3]

---

::: {{.callout-note}}
## Weekly Reflection
[Reflection prompt goes here.]
:::
"""

def lab_stub(title):
    return f"""---
title: "{title}"
---

<!-- notes.qmd — Philo Lab                                          -->
<!-- Portfolio: full lab prep notes visible here.                   -->

## Pre-Lab Reading

- [Reading TBD]

## In-Game Activity

::: {{.instructor-only}}
**Procedure:** [Step-by-step lab procedure goes here.]

**What to watch for:** [Key moments to flag during the activity.]

**Contingency:** [What to do if the game is unavailable or
players encounter technical issues.]
:::

## Debrief Questions

1. [Debrief question 1]

2. [Debrief question 2]

3. [Debrief question 3]

## Reflection Prompt

::: {{.callout-note}}
## Lab Reflection
[Reflection prompt goes here. 500–1000 words.]
:::

## Grading Notes

::: {{.instructor-only}}
**What to look for:** [Key philosophical concepts students should
demonstrate. Common errors to watch for.]
:::
"""

# Generate personhood course
print("\nGenerating personhood-ai...")
pbase = f"{BASE}/courses/personhood-ai"

# _schedule.qmd placeholder
write(f"{pbase}/_schedule.qmd", """<!-- _schedule.qmd — Personhood in the Age of AI -->
<!-- In development. Full schedule TBD.          -->

## Draft Schedule

| Week | Topic | Primary Reading |
|---|---|---|
| 1 | The Puzzle/Mystery Distinction | Marcel; Hick Part I |
| 2 | Soul-Making Theodicy | Hick Part III |
| 3 | Dostoevsky's Challenge | The Grand Inquisitor |
| 4 | Personal Identity | Locke, Essay Ch. 27 |
| 5 | What Matters in Survival | Parfit, Part III (selections) |
| 6 | Consciousness and Other Minds | Nagel; Turing; Searle |
| 7 | Second-Personal Knowledge | Stump Ch. 3–4 |
| 8 | Love as Perception of Value | Nussbaum, LK Ch. 11, 13 |
| 9 | Love as Caring | Frankfurt, Reasons of Love |
| 10 | Mind and Body in Virtual Worlds | Chalmers Ch. 14–16 |
| 11 | The Avatar as Self | TBD |
| 12 | Can You Fall in Love with an Avatar? | Discussion synthesis |
| 13 | Hick's Eschatology | Hick Part IV |
| 14 | Suffering from the Inside | Lewis, A Grief Observed |
| 15 | Course Synthesis | — |
""")

for wl, title in PERSONHOOD_WEEKS.items():
    write(f"{pbase}/weeks/{wl}/notes.qmd",
          notes_stub(title, "Personhood in the Age of AI"))
    write(f"{pbase}/weeks/{wl}/slides.qmd", f"""---
title: "{title}"
subtitle: "Personhood in the Age of AI"
format:
  revealjs:
    theme: simple
    slide-number: true
    chalkboard: true
    footer: "Personhood in the Age of AI | Dr. Reynolds | Stetson University"
---

## Today's Question

> [Central question for this session]

---

## Key Concepts

::: {{.incremental}}
- [Concept 1]
- [Concept 2]
- [Concept 3]
:::

---

## The Thought Experiment

[How does today's reading bear on the developer/agent thought experiment?]

---

## Discussion

[Discussion prompt]
""")
    write(f"{pbase}/weeks/{wl}/summary.qmd", f"""---
title: "{title} — Notes and Summary"
---

## Overview

[Summary of this week's reading and discussion goes here.]

## Key Concepts

### [Concept 1]

[Explanation]

### [Concept 2]

[Explanation]

## Connection to the Thought Experiment

[How does this week's material bear on the developer/agent
asymmetry that organizes the course?]

::: {{.callout-note}}
## Weekly Reflection
[Reflection prompt]
:::
""")

# Generate philo-lab course
print("\nGenerating philo-lab...")
lbase = f"{BASE}/courses/philo-lab"

write(f"{lbase}/_schedule.qmd", """<!-- _schedule.qmd — Philo Lab: Philosophical Laboratory -->
<!-- Phase 2 (Portal 2) schedule.                          -->

## Laboratory Sessions

| Session | Title | Primary Reading |
|---|---|---|
| Lab 1 | Entering the Chamber | Chalmers Ch. 1–2 |
| Lab 2 | GLaDOS and Other Minds | Nagel; Turing |
| Lab 3 | Trust, Cooperation, Shared Agency | Chalmers Ch. 16; Aristotle NE VIII |
| Lab 4 | Autonomy and Experimentation | Chalmers Ch. 17–18 |
| Lab 5 | Identity, Memory, and Survival | Chalmers Ch. 14–15; Locke |
""")

for wl, title in PHILO_LAB_WEEKS.items():
    write(f"{lbase}/weeks/{wl}/notes.qmd",
          lab_stub(title))
    write(f"{lbase}/weeks/{wl}/slides.qmd", f"""---
title: "{title}"
subtitle: "Philo Lab: Philosophical Laboratory"
format:
  revealjs:
    theme: simple
    slide-number: true
    chalkboard: true
    footer: "Philo Lab | Dr. Reynolds"
---

## Today's Lab

> [Central philosophical question for this session]

---

## Pre-Lab Check

- Did you complete the reading?
- Do you have your lab notebook?
- Is your game client ready?

---

## Procedure Overview

[Brief overview of today's in-game activity]

---

## Debrief

[Key debrief questions]
""")
    write(f"{lbase}/weeks/{wl}/summary.qmd", f"""---
title: "{title} — Lab Summary"
---

## Lab Overview

[What students did in this session and why.]

## Key Philosophical Questions

[The questions the lab activity raised.]

## Connection to Primary Reading

[How the in-game experience connected to the assigned text.]

::: {{.callout-note}}
## Lab Reflection Prompt
[The reflection prompt for this session.]
:::
""")

print("\nDone.")
print("Next: add both courses to _quarto.yml book chapters.")
