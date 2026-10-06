# The Archive

**Pair:** *(your two names)* **Repository:** *(link)*

> This file is Part E of the assignment — **15 marks**. Replace every placeholder below. Delete the instruction lines in italics as you go. Marks come from the reasoning, not the length.

---

## 1\. The record *(3 marks)*

*What one manuscript looks like in our system, and what we do when a field is unknown.*

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | string | `MS001` | return a boolean with the value false and why, i.e its nonexistence |
| title | string | "Tarikh al-Sudan" | we return a boolean 'false' and the reason: i.e less than 3 characters |
| city | string | "Gao" | we return a boolean 'false' and the reason: is not in known cities|
| year | integer | 1900 | we return a boolean 'false' and the reason: i.e is not in the accepted range|
| condition | string | 'fair' | we return a boolean 'false' and the reason: It is not one of the recorded conditions |

---

## 2\. Our validation rules *(4 marks)*

| Field | Rule(s) | Rejects (example) |
| --- | --- | --- |
| id |  Must start with MS, case sensitive, and have 3 digits after| QR123  |
| title | Must be at least 3 characters long |  Ab |
| city | Must appear in the list and appear in known ciities, case doesnt matter | Calebjojo |
| year | must be between 1100 and 1900 inclusive  | 5050 |
| condition |  must be one of the possible conditions, case doesnt matter| Ew |

### Who decided the year range?

I accept those bounds, if we look at our current timeframe, it gets harder and harder to preserve original text that comes from the past, due to natural causes, malhandling and such. This means as we go past the 1100 bound (backwards), the integrity of the text offered becomes more questionable. As for what happens when we go past 1900s, a modern version of a certain literature could omit things the people recording it do not find desirable and possibly adding new information to their benefit, it also becomes difficult to maintain the trustworthiness of such a text. This is why I agree with the current range, depending on the context of the manuscripts collected, it seems most appropriate, however this is at the cost of older texts that might be valid and newer texts that are preserving the older text honestly. 
---

## 3\. The `c.1590` decision *(3 marks)*

*Record MS009 in* `data/messy.csv` has the year `c.1590` — circa, approximately. Manuscript dating is often approximate, and a scholar may genuinely only know the decade. Your program currently rejects it, so the record is lost.

*Choose one and argue for it:*
---

## 1\. The record *(3 marks)*

*What one manuscript looks like in our system, and what we do when a field is unknown.*

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | string | `MS001` | return a boolean with the value false and why, i.e its nonexistence |
| title | string | "Tarikh al-Sudan" | we return a boolean 'false' and the reason: i.e less than 3 characters |
| city | string | "Gao" | we return a boolean 'false' and the reason: is not in known cities|
| year | integer | 1900 | we return a boolean 'false' and the reason: i.e is not in the accepted range|
| condition | string | 'fair' | we return a boolean 'false' and the reason: It is not one of the recorded conditions |

---

## 2\. Our validation rules *(4 marks)*

| Field | Rule(s) | Rejects (example) |
| --- | --- | --- |
| id |  Must start with MS, case sensitive, and have 3 digits after| QR123  |
| title | Must be at least 3 characters long |  Ab |
| city | Must appear in the list and appear in known ciities, case doesnt matter | Calebjojo |
| year | must be between 1100 and 1900 inclusive  | 5050 |
| condition |  must be one of the possible conditions, case doesnt matter| Ew |

### Who decided the year range?

I accept those bounds, if we look at our current timeframe, it gets harder and harder to preserve original text that comes from the past, due to natural causes, malhandling and such. This means as we go past the 1100 bound (backwards), the integrity of the text offered becomes more questionable. As for what happens when we go past 1900s, a modern version of a certain literature could omit things the people recording it do not find desirable and possibly adding new information to their benefit, it also becomes difficult to maintain the trustworthiness of such a text. This is why I agree with the current range, depending on the context of the manuscripts collected, it seems most appropriate, however this is at the cost of older texts that might be valid and newer texts that are preserving the older text honestly. 
---

## 3\. The `c.1590` decision *(3 marks)*

*Record MS009 in* `data/messy.csv` has the year `c.1590` — circa, approximately. Manuscript dating is often approximate, and a scholar may genuinely only know the decade. Your program currently rejects it, so the record is lost.

*Choose one and argue for it:*

- **(a)** Reject it. Only exact years enter the catalogue.
- **(b)** Store the year as text, so anything can be recorded.
- **(c)** Store `1590` plus a separate `approximate` flag.

**Our choice:** a

**Why:** If the scholar only knows the approximate year, they could still input a number in the field for year, as an example, the average year between the bounds of where the actual year geniunely lies, annotating it with a character c, or approximate or possibly, will just cause further complications for the program as there are infinitely many prefixes to dictate "around". Therefore, we stand by our choice to reject but recommend and average, median or any other year of that sort that goes with our programs restrictions. 

**What it costs us:** We no longer validate academically considered and correct prefixes for the years.

---

## 4\. Our test table *(3 marks)*

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | 1655 | valid | valid | Yes |
| Abnormal | Kesha | invalid | invalid | Yes |
| Extreme (low) | 1100 | valid |  |  |
| Extreme (high) | 1900 | valid |  |  |
| Boundary (below) | 1099 | invalid |  |  |
| Boundary (above) | 1901 | invalid |  |  |

### `_______________` *(one other field of your choice)*

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |

---

## 5\. Collaboration reflection *(2 marks)*

*One paragraph each, written separately and signed. Do not write these together — the point is two honest accounts.*

***(Caleb)*:** One thing my partner did that I will steal: 
One thing I would do differently next time: 

***(Kesha)*:** One thing my partner did that I will steal: He reviewed the code in its entirety and gave actual edge cases and feedback, that probably stopped a potential crash.
One thing I would do differently next time: I would try to be more involved with our direct completion of objectives.

---

## 6\. Declaration

*Required. See the integrity section of the brief.*

- [ ] Both of us can explain every line in this repository.

- [ ] AI assistants used for explanation only, not to generate our implementation or our tests.

**If you used an AI assistant, say what you asked and what you did with the answer:**
Kesha: I used an ai assistant to give me the documentation for the python code, especially for the read write file oprations in the fucntions in storage.py, mostly to explain how it works and how to understand it better. I also used it to procide me with git commands and how they work - these were directly implemented. 
---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report
```

[Link to the submission form](https://docs.google.com/forms/d/e/1FAIpQLSdO4trwNU4zPusr33LfYRhH2jvijj7sY42svbumH6f_15rCAQ/viewform?usp=preview)
