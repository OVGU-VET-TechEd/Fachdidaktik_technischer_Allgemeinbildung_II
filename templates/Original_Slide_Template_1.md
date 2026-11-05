<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  One original lecture slide reproduced verbatim with narration and its source line.
-->

# Template `Original_Slide_Template_1`

- **Purpose:** Show the content of one original lecture slide word for word (list, table or text) and name its source.
- **Pairs with:** `Original_Slide_Template_2`, `Interactive_Exercise_Template_1`, `Interactive_Exercise_Template_2`
- **Variants:** Use `Original_Slide_Template_2` to add a key message, `Original_Slide_Template_3` to reveal the slide in two parts.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the original slide | max 10 words | Ablauf des Rollenspiels |
| `%%NARRATION-0%%` | Spoken summary of the slide | 2–4 sentences | The role card describes the organic farm and its three worries. |
| `%%SLIDE-CONTENT%%` | Verbatim slide content in Markdown (list, table, text) | max 8 lines or 1 table | see default below |
| `%%SOURCE%%` | Source of the slide, shown small at the bottom | 1 line | Quelle: Folie R083 |

**Default for `%%SLIDE-CONTENT%%`:**

```markdown
- First point of the original slide
- Second point of the original slide
  - sub-point kept at its level
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%SLIDE-CONTENT%%

<small>%%SOURCE%%</small>

<!-- TEMPLATE:END -->
