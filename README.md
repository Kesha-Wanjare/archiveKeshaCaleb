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

*The brief gave you 1100–1900. That was a decision someone made, and it has costs. 1900 excludes a modern copy of an old text. 1100 excludes anything earlier. State whether you accept these bounds or would change them, and say what your choice throws away. An undefended range scores 1 of the 4 marks.*

---

## 3\. The `c.1590` decision *(3 marks)*

*Record MS009 in* `data/messy.csv` has the year `c.1590` — circa, approximately. Manuscript dating is often approximate, and a scholar may genuinely only know the decade. Your program currently rejects it, so the record is lost.

*Choose one and argue for it:*

- **(a)** Reject it. Only exact years enter the catalogue.
- **(b)** Store the year as text, so anything can be recorded.
- **(c)** Store `1590` plus a separate `approximate` flag.

**Our choice:**

**Why:**

**What it costs us:**

---

## 4\. Our test table *(3 marks)*

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | 1655 | valid |  |  |
| Abnormal | Kesha | invalid |  |  |
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

---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report
```

[Link to the submission form](https://docs.google.com/forms/d/e/1FAIpQLSdO4trwNU4zPusr33LfYRhH2jvijj7sY42svbumH6f_15rCAQ/viewform?usp=preview)
