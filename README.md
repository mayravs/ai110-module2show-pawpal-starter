# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output
```bash
========================================
  Conflict Report
========================================
  WARNING: Luna's 'exercise' (09:00, 30 min) overlaps with Luna's 'vet' (09:15, 30 min)
  WARNING: Luna's 'exercise' (09:00, 30 min) overlaps with Mochi's 'bath' (09:00, 20 min)
  WARNING: Luna's 'vet' (09:15, 30 min) overlaps with Mochi's 'bath' (09:00, 20 min)
========================================

========================================
  Today's Schedule for Alex's Pets
========================================
  [○] 2026-07-05 07:00 | Luna | feeding — Morning kibble | 10 min | medium (daily)
  [✓] 2026-07-05 08:00 | Mochi | medication — Give Apoquel with food | 5 min | high (daily)
  [○] 2026-07-06 08:00 | Mochi | medication — Give Apoquel with food | 5 min | high (daily)
  [✓] 2026-07-05 09:00 | Luna | exercise — 30-minute walk | 30 min | high (daily)
  [○] 2026-07-06 09:00 | Luna | exercise — 30-minute walk | 30 min | high (daily)
  [○] 2026-07-05 09:00 | Mochi | bath — Monthly bath | 20 min | medium (once)
  [○] 2026-07-05 09:15 | Luna | vet — Annual checkup | 30 min | high (once)
  [○] 2026-07-05 13:00 | Mochi | playtime — Interactive toy session | 20 min | low (daily)
  [○] 2026-07-05 17:00 | Mochi | grooming — Brush coat | 15 min | low (weekly)
  [○] 2026-07-05 18:30 | Luna | feeding — Evening kibble | 10 min | medium (daily)
========================================

========================================
  Pending Tasks for Alex's Pets
========================================
  ○ 07:00 | Luna | feeding — Morning kibble | priority: medium
  ○ 18:30 | Luna | feeding — Evening kibble | priority: medium
  ○ 09:15 | Luna | vet — Annual checkup | priority: high
  ○ 09:00 | Luna | exercise — 30-minute walk | priority: high
  ○ 17:00 | Mochi | grooming — Brush coat | priority: low
  ○ 13:00 | Mochi | playtime — Interactive toy session | priority: low
  ○ 09:00 | Mochi | bath — Monthly bath | priority: medium
  ○ 08:00 | Mochi | medication — Give Apoquel with food | priority: high
========================================
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Schedule.get_tasks_sorted_by_time()` | Primary sort by start time (converted to minutes); priority as tiebreaker within the same slot. |
| Filtering | `Schedule.get_all_pending_tasks()`, `Schedule.get_all_completed_tasks()`, `Schedule.get_tasks_by_time(time)`, `Schedule.get_tasks_by_type(task_type)` | Filters on `is_complete`, exact time match, or task type across all pets. |
| Conflict detection | `Schedule.get_conflicts()` | Interval overlap check (`a_start < b_end AND b_start < a_end`); scoped to same `due_date` to avoid cross-day false positives. Returns warning strings, never raises. |
| Recurring tasks | `Task.mark_complete()`, `Schedule.mark_task_complete(pet, task)` | `mark_complete()` returns the next `Task` using `timedelta`; `mark_task_complete()` appends it to the pet automatically. `"once"` tasks return `None`. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
