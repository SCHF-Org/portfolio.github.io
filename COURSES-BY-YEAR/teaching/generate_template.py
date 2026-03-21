#!/usr/bin/env python3
"""
generate_template.py
Generates all boilerplate .qmd files for the teaching repository template.
Run from /home/claude/teaching/:
    python3 generate_template.py
"""

import os

# ============================================================
# COURSE DEFINITIONS
# ============================================================

COURSES = {
    "phil-mind": {
        "title": "PHIL 3XX — Philosophy of Mind",
        "subtitle": "Love, Knowledge, and the Suffering Self",
        "semester": "Fall 2026",
        "days": "Mon/Wed 2:30–3:45 PM",
        "room": "Flagler Hall 213",
        "weeks": 15,
    },
    "phil-intro": {
        "title": "PHIL 101B — Introduction to Philosophy",
        "subtitle": "Value, Meaning, and Humanity's Place in the Modern World",
        "semester": "Spring 2026",
        "days": "Tue/Thu 10:30–11:45 AM",
        "room": "Sage Hall 242",
        "weeks": 16,
    },
    "phil-logic": {
        "title": "PHIL 101B — Introduction to Logic",
        "subtitle": "Spring 2026",
        "semester": "Spring 2026",
        "days": "Mon/Wed 9:00–10:15 AM",
        "room": "TBD",
        "weeks": 16,
    },
}

BASE = "/home/claude/teaching"

# ============================================================
# HELPERS
# ============================================================

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  wrote {path.replace(BASE + '/', '')}")


def week_label(n):
    return f"week{n:02d}"


# ============================================================
# COURSE _quarto.yml
# ============================================================

def course_quarto_yml(course_id, course):
    weeks = course["weeks"]
    title = course["title"]

    # Build sidebar week entries
    sidebar_entries = ""
    for n in range(1, weeks + 1):
        wl = week_label(n)
        sidebar_entries += f"""          - href: weeks/{wl}/slides.qmd
            text: "Week {n:02d}"
            contents:
              - href: weeks/{wl}/slides.qmd
                text: "👨‍🏫 Slides"
              - href: weeks/{wl}/summary.qmd
                text: "💻 Notes and Summary"
"""

    return f"""# courses/{course_id}/_quarto.yml
# Course-specific website configuration.
# Merged with root _quarto.yml when rendering --profile website.

project:
  type: website
  output-dir: ../../_output/website/{course_id}
  render:
    - "syllabus.qmd"
    - "weeks/*/slides.qmd"
    - "weeks/*/summary.qmd"

website:
  title: "{title}"
  favicon: ../../shared/figures/icons/course_favicon.png
  sidebar:
    style: docked
    contents:
      - section: "Syllabus"
        contents:
          - href: syllabus.qmd
            text: "Syllabus"
      - section: "🗓️ Course Schedule"
        contents:
{sidebar_entries}
  navbar:
    background: primary
  page-footer:
    background: light
    left: "Copyright 2026, Montaque Reynolds"

format:
  html:
    theme:
      light:
        - journal
        - ../../shared/css/custom.scss
    css:
      - ../../shared/css/custom_style.css
      - ../../shared/css/syllabus.css
    toc: true
"""


# ============================================================
# COURSE _schedule.qmd
# ============================================================

def course_schedule_qmd(course_id, course):
    weeks = course["weeks"]
    title = course["title"]
    semester = course["semester"]

    week_entries = ""
    for n in range(1, weeks + 1):
        wl = week_label(n)
        week_entries += f"""
### Week {n:02d} {{#{wl}}}

**Mon/Wed** *(dates TBD)*

**Mon:**

- Reading TBD

**Wed:**

- Reading TBD

---
"""

    return f"""<!-- _schedule.qmd for {course_id} -->
<!-- SINGLE SOURCE OF TRUTH for all dates and readings.      -->
<!-- Include this file wherever the schedule is needed:      -->
<!--   {{{{< include _schedule.qmd >}}}}                        -->
<!-- Never edit the schedule in any other file.              -->

## Important Dates

| Date | Event |
|---|---|
| TBD | First day of class |
| TBD | Last day of class |
| TBD | Final Examinations |

---

{week_entries}
"""


# ============================================================
# COURSE syllabus.qmd
# ============================================================

def course_syllabus_qmd(course_id, course):
    title = course["title"]
    subtitle = course["subtitle"]
    semester = course["semester"]
    days = course["days"]
    room = course["room"]

    return f"""---
title: "{title}"
subtitle: "{subtitle}"
date: "{semester}"
---

# Course Information

**Instructor:** Dr. Montaque Reynolds
**Email:** mreynolds1@stetson.edu
**Office:** Elizabeth Hall 104
**Office Hours:** Tuesdays 1:00–3:00 PM | Thursdays 1:00–3:00 PM
**Meeting Times:** {days}
**Room:** {room}

<!-- Replace the course description below with your own. -->

# Course Description

[Course description goes here.]

# Required Texts

[Required texts go here.]

# Grading

| Assignment | Points |
|---|---|
| Weekly Reflections (best 8 of 12, 8 pts each) | 32 pts |
| Reflective Analysis 1 & 2 (80 pts each) | 160 pts |
| Essay 1 & 2 (40 pts each) | 80 pts |
| DND Presentation / Participation | 96 pts |
| Attendance | 32 pts |
| **Total** | **400 pts** |

# Course Schedule

{{{{< include _schedule.qmd >}}}}

# Academic Policies

## Academic Integrity
All work must be your own. Sign all submissions: *"Pledged, [your name]."*
Violations will be referred to the Academic Honor Council.
Honor code: http://www.stetson.edu/honorsystem/

## Late Work
Late work is docked a half-letter grade per day unless an extension
is approved before the due date.

## Accommodations
Register with the Academic Success Center (386-822-7127;
www.stetson.edu/asc) if disability-related accommodations are necessary.

## Counseling Center
Phone: 386-822-8900 | Griffith Hall | Weekdays 8 AM–4:30 PM
After-hours: Public Safety 386-822-7300 (ask for on-call counselor).
"""


# ============================================================
# WEEK notes.qmd (portfolio — instructor-facing)
# ============================================================

def week_notes_qmd(course_id, course, n):
    wl = week_label(n)
    title = course["title"]

    return f"""---
title: "Week {n:02d} — [Title TBD]"
subtitle: "[Dates TBD]"
---

<!-- notes.qmd — Week {n:02d} of {course_id}                        -->
<!-- This file appears in the PORTFOLIO profile with all content.  -->
<!-- .instructor-only divs are hidden on the website profile.      -->

{{{{< include ../../_schedule.qmd >}}}}

---

## Session Prep: Monday

::: {{.instructor-only}}
**Opening move:** [Describe how you plan to open the session.]

**Key tension to surface:** [What is the central philosophical tension
for this session?]

**Likely sticking point:** [What do students usually find difficult?
How will you address it?]

**Time allocation (75 min):**

- 10 min: [Activity]
- 20 min: [Activity]
- 20 min: [Discussion]
- 15 min: [Activity]
- 10 min: [Wrap-up and preview]
:::

### Discussion Questions — Monday

1. [Discussion question 1]

2. [Discussion question 2]

3. [Discussion question 3]

---

## Session Prep: Wednesday

::: {{.instructor-only}}
**Goal for this session:** [What should students leave understanding?]

**The key move:** [What is the central argument or idea to develop?]

**Time allocation (75 min):**

- 5 min: Recap Monday
- 25 min: [Activity]
- 20 min: Discussion
- 15 min: [Activity]
- 10 min: Assign next week's readings

**Weekly Reflection prompt** (write on board):
"[Weekly reflection prompt for this week]"
:::

### Discussion Questions — Wednesday

1. [Discussion question 1]

2. [Discussion question 2]

3. [Discussion question 3]

---

::: {{.callout-note}}
## Weekly Reflection {n:02d}
[Weekly reflection prompt goes here.]
:::

---

## DND Notes — Week {n:02d}

::: {{.instructor-only}}
[DND session prep notes if applicable. Otherwise delete this section.]
:::
"""


# ============================================================
# WEEK slides.qmd (website — student-facing RevealJS)
# ============================================================

def week_slides_qmd(course_id, course, n):
    wl = week_label(n)
    title = course["title"]
    semester = course["semester"]

    return f"""---
title: "Week {n:02d} — [Title TBD]"
subtitle: "{title} | {semester}"
format:
  revealjs:
    theme: simple
    slide-number: true
    chalkboard: true
    footer: "{title} | Dr. Reynolds | Stetson University"
    logo: ../../../../shared/figures/logos/logo-x2.png
---

## Today's Question

> [Central question for this week goes here.]

---

## Key Concepts

::: {{.incremental}}
- [Concept 1]
- [Concept 2]
- [Concept 3]
:::

---

## [Slide Title]

[Slide content goes here.]

---

## [Slide Title]

[Slide content goes here.]

---

## Discussion

[Discussion prompt or activity for class.]

---

## Coming Up

- **Next session:** [Preview of next topic]
- **Reading due:** [Reading assignment]

::: {{.callout-important}}
## Reading for Next Class
[Reading assignment details]
:::
"""


# ============================================================
# WEEK summary.qmd (website — student reading summary)
# ============================================================

def week_summary_qmd(course_id, course, n):
    wl = week_label(n)
    title = course["title"]

    return f"""---
title: "Week {n:02d} — Notes and Summary"
subtitle: "[Title TBD]"
---

## Overview

[Brief overview of this week's topics and their significance
in the context of the course goes here.]

---

## Key Concepts

### [Concept 1]

[Explanation of concept 1 goes here. Write this for students
who are reviewing after class or preparing for discussion.]

### [Concept 2]

[Explanation of concept 2 goes here.]

### [Concept 3]

[Explanation of concept 3 goes here.]

---

## The Central Question for This Week

[Articulate the central question or tension of the week in a
way that connects the readings to each other and to the
broader course arc.]

---

::: {{.callout-note}}
## Weekly Reflection {n:02d}
[Weekly reflection prompt goes here — should match the prompt
in notes.qmd for this week.]
:::

---

## Looking Ahead

[Brief preview of next week's topic and how it follows from
this week.]
"""


# ============================================================
# MAIN
# ============================================================

def main():
    for course_id, course in COURSES.items():
        print(f"\nGenerating {course_id}...")
        base = f"{BASE}/courses/{course_id}"

        # Course-level files
        write(f"{base}/_quarto.yml",
              course_quarto_yml(course_id, course))
        write(f"{base}/_schedule.qmd",
              course_schedule_qmd(course_id, course))
        write(f"{base}/syllabus.qmd",
              course_syllabus_qmd(course_id, course))

        # Week files
        for n in range(1, course["weeks"] + 1):
            wl = week_label(n)
            wbase = f"{base}/weeks/{wl}"
            write(f"{wbase}/notes.qmd",
                  week_notes_qmd(course_id, course, n))
            write(f"{wbase}/slides.qmd",
                  week_slides_qmd(course_id, course, n))
            write(f"{wbase}/summary.qmd",
                  week_summary_qmd(course_id, course, n))

    print("\nDone. All template files generated.")
    print("Next steps:")
    print("  1. Replace the chicago-author-date.csl placeholder:")
    print("     curl -o shared/references/chicago-author-date.csl \\")
    print("       https://raw.githubusercontent.com/citation-style-language/styles/master/chicago-author-date.csl")
    print("  2. Add a favicon to shared/figures/icons/course_favicon.png")
    print("  3. Add a logo to shared/figures/logos/logo-x2.png")
    print("  4. Run: quarto preview courses/phil-mind --profile website")


if __name__ == "__main__":
    main()
