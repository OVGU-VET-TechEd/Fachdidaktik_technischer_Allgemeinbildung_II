<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  One original lecture slide reproduced verbatim, followed by a key message and the source line.
-->

# Template `Original_Slide_Template_2`

- **Purpose:** Show one original lecture slide word for word, then anchor its core idea in a key message.
- **Pairs with:** `Original_Slide_Template_1`, `Original_Slide_Template_3`, `Interactive_Exercise_Template_1`
- **Variants:** Change NOTE to TIP or IMPORTANT for a different colour. Use `Original_Slide_Template_1` if the slide needs no key message.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the original slide | max 10 words | Funktion von Kontrolle und Bewertung im Unterricht |
| `%%NARRATION-0%%` | Spoken summary of the slide | 2–4 sentences | Control and assessment have four functions. |
| `%%SLIDE-CONTENT%%` | Verbatim slide content in Markdown (list, table, text) | max 8 lines or 1 table | see default below |
| `%%NARRATION-1%%` | Spoken key message | 1 sentence | Keep one idea in mind. |
| `%%KEY-MESSAGE%%` | Core idea of the slide (a reading aid, not slide text) | 1–2 sentences | Every assessment needs a standard to compare with. |
| `%%SOURCE%%` | Source of the slide, shown small at the bottom | 1 line | Quelle: Folie R069 |

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

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> [!NOTE] Key message
> %%KEY-MESSAGE%%

<small>%%SOURCE%%</small>

<!-- TEMPLATE:END -->
