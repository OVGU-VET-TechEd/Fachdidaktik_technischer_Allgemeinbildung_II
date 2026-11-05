<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  One open task with a text box, a tiered hint and a model answer to compare with.
-->

# Template `Open_Task_Template_1`

- **Purpose:** One open task (plan, design, transfer to the own subject) answered in a text box, then compared with a model answer.
- **Pairs with:** `Application_Transfer_Template_1`, `Process_Template_6`, `Summary_Recap_Template_3`
- **Variants:** The task may contain a small table as a writing frame. For three related questions use `Application_Transfer_Template_1`.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the task | max 6 words | Plan Your Own Test |
| `%%NARRATION-0%%` | Spoken or written introduction to the task | 1–4 sentences | Now transfer the idea to your own subject. |
| `%%TASK%%` | Task in Markdown, may include a writing frame | 1–8 lines | Describe one activity of your subject as a control loop. Where exactly is the test? |
| `%%HINT%%` | Hint for learners who are stuck | 1–2 sentences | Think of a measuring tool you use to check your work. |
| `%%MODEL-ANSWER%%` | Model answer or example solution | 1–6 lines | Target: shaft diameter 20 mm. Work: turn the shaft. Test: measure with a micrometer. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%TASK%%

[[___ ___ ___ ___]]

<details>

<summary>💡 Hint 1</summary>

%%HINT%%

</details>

<details>

<summary>✅ Solution</summary>

%%MODEL-ANSWER%%

</details>

<!-- TEMPLATE:END -->
