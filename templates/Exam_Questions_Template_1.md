<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.1.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Five oral exam questions, each with a collapsible answer outline, followed by a self-rating matrix.
-->

# Template `Exam_Questions_Template_1`

- **Purpose:** Prepare learners for an oral exam: five open questions, each with a hidden answer outline (term – explain – example – connect), then a self-rating per question.
- **Pairs with:** `Summary_Recap_Template_1`, `Summary_Recap_Template_3`, `Open_Task_Template_1`
- **Variants:** Use it twice for ten questions (change the title). Write the outline as four bold steps, so learners can compare the structure of their own spoken answer.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the slide | max 6 words | Prüfungsfragen zum Üben |
| `%%NARRATION-0%%` | Spoken or written introduction | 1–3 sentences | Use these five questions to prepare for the oral exam. |
| `%%METHOD%%` | How to practise, shown as a tip | 1–3 sentences | Answer each question aloud in two minutes, then open the outline and compare. |
| `%%Q1-TOPIC%%` … `%%Q5-TOPIC%%` | Short topic of the question | max 4 words | Roots of the idea ; Basic pattern ; Project or not? ; Role of the teacher ; Types of problems |
| `%%Q1%%` … `%%Q5%%` | The exam question | 1–2 sentences | Which core ideas connect the three roots of project learning? ; Explain the basic pattern of the project method. ; How do you tell whether a project week is a project? ; Describe the role of the teacher. ; Assign the types of problems to their test criterion. |
| `%%A1%%` … `%%A5%%` | Answer outline in Markdown: four bold steps | 4–8 lines | see default below |
| `%%NARRATION-1%%` | Spoken introduction to the self-rating | 1 sentence | How sure are you? |
| `%%SOURCE%%` | Note on the questions, shown small at the bottom | 1 line | The questions are experimental. |

**Default for `%%A1%%`:**

```markdown
- **1 Term:** Define the key term, if possible with its author.
- **2 Explain:** Name the distinctions or the structure (slides R055–R058).
- **3 Example:** Give an example from the lecture or your own subject.
- **4 Connect:** Name a limit or a link to another session.
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

> [!TIP] 🎙️ So üben Sie
> %%METHOD%%

**Frage 1 · %%Q1-TOPIC%%:** %%Q1%%

<details>

<summary>✅ Antwortskizze 1</summary>

%%A1%%

</details>

**Frage 2 · %%Q2-TOPIC%%:** %%Q2%%

<details>

<summary>✅ Antwortskizze 2</summary>

%%A2%%

</details>

**Frage 3 · %%Q3-TOPIC%%:** %%Q3%%

<details>

<summary>✅ Antwortskizze 3</summary>

%%A3%%

</details>

**Frage 4 · %%Q4-TOPIC%%:** %%Q4%%

<details>

<summary>✅ Antwortskizze 4</summary>

%%A4%%

</details>

**Frage 5 · %%Q5-TOPIC%%:** %%Q5%%

<details>

<summary>✅ Antwortskizze 5</summary>

%%A5%%

</details>

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Einschätzen:** Wie sicher beantworten Sie die Fragen frei und in ganzen Sätzen?

[(sicher)(teilweise)(noch unsicher)]
[                                    ] Frage 1 · %%Q1-TOPIC%%
[                                    ] Frage 2 · %%Q2-TOPIC%%
[                                    ] Frage 3 · %%Q3-TOPIC%%
[                                    ] Frage 4 · %%Q4-TOPIC%%
[                                    ] Frage 5 · %%Q5-TOPIC%%

<small>%%SOURCE%%</small>

****************************************

<!-- TEMPLATE:END -->
