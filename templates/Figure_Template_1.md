<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  A figure redrawn as a free Mermaid diagram, explained in three narrated parts and a key message.

import:   https://raw.githubusercontent.com/LiaTemplates/mermaid_template/0.1.4/README.md
-->

# Template `Figure_Template_1`

- **Purpose:** Redraw a figure of an original slide (scheme, cycle, model) as a Mermaid diagram and explain it in three steps.
- **Pairs with:** `Process_Template_6`, `Interactive_Exercise_Template_2`, `Original_Slide_Template_2`
- **Variants:** Any Mermaid diagram type works (flowchart TD or LR, subgraphs, loops). Labels in quotes, no quotes inside labels.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the figure | max 10 words | Test-Operation-Test-Exit (TOTE-Einheit) |
| `%%NARRATION-0%%` | Spoken overview of the figure | 1–3 sentences | The TOTE unit shows an action as a control loop. |
| `%%MERMAID-CODE%%` | Mermaid code of the redrawn figure | 4–20 lines | see default below |
| `%%NARRATION-1%%` … `%%NARRATION-3%%` | Spoken explanation per part | 1–2 sentences | Everything starts with a target. ; Then the work is done and tested. ; If target and result differ, the loop starts again. |
| `%%PART-1%%` … `%%PART-3%%` | Name of the part | max 4 words | Soll ; Bearbeitung und Test ; identisch? |
| `%%PART-TEXT-1%%` … `%%PART-TEXT-3%%` | Explanation of the part | max 20 words | The target state. ; Work on the task, then check the result. ; No – back to the target. Yes – exit. |
| `%%NARRATION-4%%` | Spoken key message | 1 sentence | Keep one idea in mind. |
| `%%KEY-MESSAGE%%` | Core idea of the figure | 1–2 sentences | Acting is a loop of comparing target and result. |
| `%%SOURCE%%` | Source of the figure, shown small at the bottom | 1 line | Quelle: Folie R078 – Grafik nachgezeichnet |

**Default for `%%MERMAID-CODE%%`:**

```text
flowchart TD
  A(["Soll"]) ==> B(["Bearbeitung"])
  B ==> C(["Test"])
  C ==> D["identisch?"]
  D == nein ==> A
  D == ja ==> E["Exit"]
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

```mermaid @mermaid
%%MERMAID-CODE%%
```

    --{{1}}--
%%NARRATION-1%%

      {{1}}
**① %%PART-1%%:** %%PART-TEXT-1%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
**② %%PART-2%%:** %%PART-TEXT-2%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
**③ %%PART-3%%:** %%PART-TEXT-3%%

    --{{4}}--
%%NARRATION-4%%

      {{4}}
> [!NOTE] Key message
> %%KEY-MESSAGE%%

<small>%%SOURCE%%</small>

<!-- TEMPLATE:END -->
