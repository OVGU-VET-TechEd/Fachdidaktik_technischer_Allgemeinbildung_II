<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Open question or dilemma with a vote before the discussion and two individual or plenary phases.
-->

# Template `Discussion_Template_1`

- **Purpose:** Start a discussion or role play: present the question, take a vote, then guide two phases (alone, then plenary). No pair work.
- **Pairs with:** `Discussion_Template_2` (vote after, may follow later in the session), `Original_Slide_Template_1`, `Summary_Recap_Template_1`
- **Variants:** Phase titles are free text, so names and durations can be adapted (e.g. a working phase, then a press conference). Slides may stand between this template and `Discussion_Template_2`.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the discussion | max 6 words | Repair or Replace the Bridge? |
| `%%NARRATION-0%%` | Spoken dilemma | 2–3 sentences | The old bridge is a listed monument but too weak for modern trucks. |
| `%%DILEMMA%%` | Dilemma, thesis or open question (Markdown) | 1–3 sentences | The town must decide: reinforce the historic bridge or build a new one next to it. |
| `%%VOTE-QUESTION%%` | Question of the vote | 1 sentence | What should the town do? |
| `%%OPTION-A%%`, `%%OPTION-B%%`, `%%OPTION-C%%` | Possible positions | max 6 words | Reinforce the old bridge ; Build a new bridge ; Both, one after the other |
| `%%NARRATION-1%%` | Spoken instruction for phase 1 | 1 sentence | First, think alone and write down your arguments. |
| `%%PHASE-1-TITLE%%` | Title of phase 1 with duration | max 5 words | 🧠 Alone · 3 min |
| `%%PHASE-1-TASK%%` | Task of phase 1, answered in the text box | 1–2 sentences | Note two arguments for your position. |
| `%%NARRATION-2%%` | Spoken instruction for phase 2 | 1 sentence | Now we collect your arguments. |
| `%%PHASE-2-TITLE%%` | Title of phase 2 with duration | max 5 words | 📣 Plenary · 5 min |
| `%%PHASE-2-TASK%%` | Task of phase 2 | 1–2 sentences | Volunteers present their strongest argument in one sentence. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%DILEMMA%%

**Vote (before):** %%VOTE-QUESTION%%

[(a)] %%OPTION-A%%
[(b)] %%OPTION-B%%
[(c)] %%OPTION-C%%
[(undecided)] Undecided

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

> [!TIP] %%PHASE-1-TITLE%%
> %%PHASE-1-TASK%%

[[___ ___ ___]]

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
> [!TIP] %%PHASE-2-TITLE%%
> %%PHASE-2-TASK%%

<!-- TEMPLATE:END -->
