<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  One original lecture slide reproduced verbatim in two parts, followed by a key message and the source line.
-->

# Template `Original_Slide_Template_3`

- **Purpose:** Show a long original slide in two parts (e.g. features, then phases), then anchor its core idea in a key message.
- **Pairs with:** `Original_Slide_Template_2`, `Process_Template_6`, `Interactive_Exercise_Template_2`
- **Variants:** The second part may also hold an explanation from the speaker notes; say so in the source line.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the original slide | max 10 words | Fallstudie |
| `%%NARRATION-0%%` | Spoken summary of the first part | 2–4 sentences | A case study is a complex teaching method. |
| `%%SLIDE-CONTENT%%` | First part of the slide, verbatim Markdown | max 6 lines | see default below |
| `%%NARRATION-1%%` | Spoken summary of the second part | 1–3 sentences | Working on a case has four phases. |
| `%%SLIDE-CONTENT-2%%` | Second part of the slide, verbatim Markdown | max 8 lines | see default below |
| `%%NARRATION-2%%` | Spoken key message | 1 sentence | Keep one idea in mind. |
| `%%KEY-MESSAGE%%` | Core idea of the slide (a reading aid, not slide text) | 1–2 sentences | The solution is finally compared with the real decision. |
| `%%SOURCE%%` | Source of the slide, shown small at the bottom | 1 line | Quelle: Folie R074 |

**Default for `%%SLIDE-CONTENT%%`:**

```markdown
- First point of the original slide
- Second point of the original slide
```

**Default for `%%SLIDE-CONTENT-2%%`:**

```markdown
**Heading of the second part**

1. First step
2. Second step
   - sub-point kept at its level
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%SLIDE-CONTENT%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

%%SLIDE-CONTENT-2%%

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
> [!NOTE] Key message
> %%KEY-MESSAGE%%

<small>%%SOURCE%%</small>

<!-- TEMPLATE:END -->
