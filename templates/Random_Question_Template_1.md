<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.1.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Oral exam simulation, a click draws a random question from a pool and names where the answer outline is.
-->

# Template `Random_Question_Template_1`

- **Purpose:** Simulate an oral exam: each click on the dice field draws a random question from a pool; learners answer aloud, then compare with the answer outline named below the question.
- **Pairs with:** `Exam_Questions_Template_1`, `Open_Task_Template_1`, `Summary_Recap_Template_1`
- **Variants:** Restrict the pool to the questions of one session for focused practice. The fourth part of an entry may name any place where the outline is found.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the slide | max 6 words | Prüfungssimulation |
| `%%NARRATION-0%%` | Spoken or written introduction | 1–3 sentences | Draw a random question from all sessions. |
| `%%INSTRUCTION%%` | How to work with the drawn question | 1–3 sentences | Answer aloud in three minutes, then compare with the outline. |
| `%%POOL%%` | All questions in one line; entries separated by space-semicolon-semicolon-space; each entry has four parts separated by a vertical bar: unit, topic, question, where the answer outline is – no ASCII quotes, backticks or backslashes | 5–100 entries | see default below |
| `%%NARRATION-1%%` | Spoken introduction to the tip | 1 sentence | Compare your answer afterwards. |
| `%%TIP%%` | What to do after answering | 1–3 sentences | Note the questions where you hesitated and draw them again later. |

**Default for `%%POOL%%`:**

```text
S01|Technik|Worin unterscheiden sich Technik- und Naturwissenschaften?|S01, Prüfungsfragen zum Üben ;; S03|Grundmuster|Erläutern Sie das Grundmuster nach Frey.|S03, Prüfungsfragen zum Üben
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%INSTRUCTION%%

**Ziehen:** Klicken Sie auf das Würfelfeld.

<script input="button" value="Neue Frage ziehen" output="zug">
window.liaZug = (window.liaZug || 0) + 1
"🎲 Neue Frage ziehen · Zug " + window.liaZug
</script>

<script>
const zug = "@input(`zug`)"
const pool = "%%POOL%%".split(" ;; ").map(e => e.split("|"))
const pick = pool[Math.floor(Math.random() * pool.length)]
"LIASCRIPT: > **" + pick[0] + " · " + pick[1] + "**\n>\n> " + pick[2] + "\n\n<small>Antwortskizze: " + pick[3] + "</small>"
</script>

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> [!TIP] 💡 Nach der Antwort
> %%TIP%%

<!-- TEMPLATE:END -->
