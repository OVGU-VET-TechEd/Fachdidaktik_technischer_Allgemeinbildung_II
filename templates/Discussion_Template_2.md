<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Second vote after a discussion or role play with a reflection question and a key message.
-->

# Template `Discussion_Template_2`

- **Purpose:** Close a discussion: repeat the vote from `Discussion_Template_1`, reflect, and compare before and after.
- **Pairs with:** `Discussion_Template_1` (same question and options), `Summary_Recap_Template_1`, `Summary_Recap_Template_3`
- **Variants:** Use it right after the discussion or at the end of the session to show whether the session changed opinions.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the slide | max 6 words | What Do You Think Now? |
| `%%NARRATION-0%%` | Spoken intro to the second vote | 1 sentence | Vote again – did the discussion change your mind? |
| `%%VOTE-QUESTION%%` | Same question as in the first vote | 1 sentence | What should the town do? |
| `%%OPTION-A%%`, `%%OPTION-B%%`, `%%OPTION-C%%` | Same positions as in the first vote | max 6 words | Reinforce the old bridge ; Build a new bridge ; Both, one after the other |
| `%%NARRATION-1%%` | Spoken intro to the reflection | 1 sentence | Look back on the discussion. |
| `%%REFLECT-QUESTION%%` | Reflection question | 1 sentence | Which argument convinced you most, and why? |
| `%%NARRATION-2%%` | Spoken key message | 1 sentence | Compare the two votes. |
| `%%KEY-MESSAGE%%` | What the comparison shows | 1–2 sentences | Comparing the votes before and after shows how the arguments worked. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**Vote (after):** %%VOTE-QUESTION%%

[(a)] %%OPTION-A%%
[(b)] %%OPTION-B%%
[(c)] %%OPTION-C%%
[(undecided)] Undecided

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Reflect:** %%REFLECT-QUESTION%%

[[___ ___]]

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
> [!NOTE] Key message
> %%KEY-MESSAGE%%

<!-- TEMPLATE:END -->
