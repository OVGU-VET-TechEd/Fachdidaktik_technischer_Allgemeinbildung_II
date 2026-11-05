#!/usr/bin/env python3
"""Generate Process_Template_N.md (a process with N steps) or Cycle_Template_N.md (a cycle) in this folder.

  python3 make_process_templates.py 5 6 7 9 c6      (c6 = cycle with 6 steps)

Same layout as Concept_Explanation_Template_3 (Mermaid chain, one narrated reveal step per process step,
drag & drop ordering slide) plus a source line. From 7 steps on, the steps are revealed in groups of three
(at most 6 reveal steps per slide) and the chain runs top-down.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MERMAID = "https://raw.githubusercontent.com/LiaTemplates/mermaid_template/0.1.4/README.md"
STEPS = ["Analyse", "Plan", "Decide", "Prepare", "Carry out", "Check", "Evaluate", "Document", "Reflect", "Present",
         "Archive", "Repeat"]
TEXTS = ["Understand the problem and the goal.", "Plan the steps and the material.", "Choose one of the options.",
         "Prepare tools and workplace.", "Do the work as planned.", "Compare the result with the goal.",
         "Judge the result and the process.", "Write down what was done.", "Think about what to do better.",
         "Show the result to others.", "Store the documents.", "Start the next cycle."]
BAR = "*" * 40


def groups(n):
    if n <= 6:
        return [[i] for i in range(1, n + 1)]
    return [list(range(i, min(i + 3, n + 1))) for i in range(1, n + 1, 3)]


def template(n, cycle=False):
    g = groups(n)
    name = f"{'Cycle' if cycle else 'Process'}_Template_{n}"
    kind = "cycle" if cycle else "process"
    direction = "LR" if n <= 6 else "TD"
    per_step = n <= 6
    examples = lambda items: " ; ".join(items[:n])
    narr_examples = " ; ".join(
        (f"Step {s[0]} is about {STEPS[s[0] - 1].lower()}." if per_step else f"Steps {s[0]} to {s[-1]} come next.")
        for s in g)
    head = f"""<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  A {kind} with {n} steps as a Mermaid {"loop" if cycle else "chain"}, narrated step by step, with an ordering task.

import:   {MERMAID}
-->

# Template `{name}`

- **Purpose:** Explain {f"a cycle with exactly {n} steps whose last step leads back to the first (control loop, learning or work cycle)" if cycle else f"a process, phase model or procedure with exactly {n} steps"}, then let learners put the steps in order.
- **Pairs with:** `Original_Slide_Template_2`, `Figure_Template_1`, `Interactive_Exercise_Template_2`
- **Variants:** Change {direction} to {"TD" if direction == "LR" else "LR"} in the chart for the other direction. {"The arrow from the last step back to step 1 closes the cycle." if cycle else "For a cycle use the Cycle variant."} Generate other step counts with `make_process_templates.py`.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Name of the process | max 8 words | The Work Process |
| `%%NARRATION-0%%` | Spoken overview | 1–2 sentences | The work process has {n} steps. |
| `%%STEP-1%%` … `%%STEP-{n}%%` | Step name, no quotes | max 5 words | {examples(STEPS)} |
| `%%NARRATION-1%%` … `%%NARRATION-{len(g)}%%` | Spoken explanation per {"step" if per_step else "group of three steps"} | 1–3 sentences | {narr_examples} |
| `%%STEP-TEXT-1%%` … `%%STEP-TEXT-{n}%%` | Short explanation per step | max 15 words | {examples(TEXTS)} |
| `%%SOURCE%%` | Source of the process, shown small at the bottom | 1 line | Quelle: Folie R080 |
| `%%ORDER-TITLE%%` | Title of the ordering slide | max 5 words | Put It in Order |
| `%%NARRATION-ORDER-0%%` | Spoken intro to the task | 1 sentence | Drag the steps into the right order. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{{{0}}}}--
%%NARRATION-0%%

```mermaid @mermaid
flowchart {direction}
"""
    if per_step:
        # after the first edge, refer to the previous node by its id only
        body = head + '  S1["1 · %%STEP-1%%"] --> S2["2 · %%STEP-2%%"]\n'
        body += "".join(f'  S{i} --> S{i + 1}["{i + 1} · %%STEP-{i + 1}%%"]\n' for i in range(2, n))
        if cycle:
            body += f"  S{n} --> S1\n"
    else:
        # rows of three steps; rows are linked as subgraphs so that each row keeps its left-to-right direction
        body = head
        for r, steps in enumerate(g, 1):
            nodes = " --> ".join(f'S{i}["{i} · %%STEP-{i}%%"]' for i in steps)
            body += f'  subgraph R{r} [" "]\n    direction LR\n    {nodes}\n  end\n'
        body += "".join(f"  R{r} --> R{r + 1}\n" for r in range(1, len(g)))
        if cycle:
            body += f"  R{len(g)} --> R1\n"
    body += "```\n"
    for k, steps in enumerate(g, 1):
        items = "\n".join(f"{i}. **%%STEP-{i}%%:** %%STEP-TEXT-{i}%%" for i in steps)
        body += f"\n    --{{{{{k}}}}}--\n%%NARRATION-{k}%%\n\n      {{{{{k}}}}}\n"
        body += items + "\n" if len(steps) == 1 else f"{BAR}\n\n{items}\n\n{BAR}\n"
    gaps = " → ".join(f"Step {i}: [->[ %%STEP-{i}%% ]]" for i in range(1, n + 1))
    body += f"""
<small>%%SOURCE%%</small>

## %%ORDER-TITLE%%

    --{{{{0}}}}--
%%NARRATION-ORDER-0%%

**Order:** Drag each card into the right gap.

<!-- data-randomize data-show-partial-solution data-solution-button="2" -->
{gaps}

<!-- TEMPLATE:END -->
"""
    return body


if __name__ == "__main__":
    for arg in sys.argv[1:] or ["5", "6", "9"]:
        cycle = arg.startswith("c")
        n = int(arg.lstrip("c"))
        out = HERE / f"{'Cycle' if cycle else 'Process'}_Template_{n}.md"
        out.write_text(template(n, cycle), encoding="utf-8")
        print("wrote", out.name)
