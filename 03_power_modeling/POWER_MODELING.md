# Power Modeling — Explanation

This module builds and uses a power consumption model for the Raspberry Pi 3 B+ based on real measurements taken on the board.

---

## The Problem

When running a parallel workload on a multicore processor, two parameters control performance and energy:
- **CPU frequency `f`** (GHz) — higher frequency = faster but more power
- **Number of active cores `n`** — more cores = more parallelism but more power

The goal is to find the `(f, n)` combination that minimizes power consumption while respecting performance constraints.

---

## Step 1 — Data (`data/`)

The model is fitted from 24 data points covering:
- 3 frequency levels: `f ∈ {1.60, 1.99, 2.40}` GHz
- 8 core configurations: `n ∈ {1, 2, 3, 4, 5, 6, 7, 8}`

Stored in:
- `data/1.txt` — columns: `(frequency, n_cores)`
- `data/2.txt` — corresponding power values in Watts

> Note: these frequency values exceed the RPi 3 B+ hardware cap (1.4 GHz) and represent model data points used to fit and extrapolate the regression, not direct on-board measurements at those exact frequencies.

---

## Step 2 — 3D Linear Regression (`3D_linear_regression_model.py`)

A linear model is fitted using `scikit-learn`:

```
p = a + b·f + c·n
```

Result from the fitted model:

```
p = -12.64 + 15.96·f + 3.66·n
```

The script plots a 3D scatter of the real measurements alongside the fitted regression plane, with axes:
- X = frequency (f)
- Y = number of cores (n)
- Z = power (p)

This confirms that power grows linearly with both frequency and core count on this hardware.

---

## Step 3 — Power Minimizer by Iteration (`iteration.py`)

Using the regression equation, the script iterates over all combinations of:
- 20 random frequency values sampled from `[1.2, 2.4]` GHz
- Core counts `n ∈ {1, ..., 8}`

It finds the `(f, n)` pair that minimizes `p = -12.64 + 15.96·f + 3.66·n` and prints the optimal number of cores and frequency.

---

## Step 4 — ILP Optimization (`Power_solver.py`)

For cases where `(s, n)` (speed and core count) must be integers and subject to hard constraints, an **Integer Linear Program** is solved using `cvxopt`/`glpk`:

- **Objective:** maximize performance (or minimize power), modeled as `−10s + 5n`
- **Constraints:** keep `(s, n)` within valid hardware bounds
- Returns the optimal integer `(s, n)` pair

---

## Step 5 — Task Scheduling Analysis (`Proba_combinatoire.py / 2 / 3`)

Given a set of tasks with known execution times (workload), this part answers:

> *How many ways can you distribute N tasks across K cores, and how many of those distributions overload a core?*

### Setup
- Tasks: `T1=10, T2=5, T3=60, T4=20, T5=22, T6=90, T7=11, T8=51` (execution times)
- Cores: `n = 4` (matching the Raspberry Pi's physical core count)
- A core is considered **overloaded** if its total task load exceeds 100

### Method
1. Enumerate all combinations of n tasks from the task list using a bitmask approach (`combinliste`)
2. For each combination assigned to a core, pair it with the remaining tasks on the other cores
3. Compute total load per core
4. Count and filter out distributions where any core exceeds the load threshold of 100

### Variants
| Script | Tasks | Cores | Extra |
|--------|-------|-------|-------|
| `Proba_combinatoire.py` | 8 | 4 | Counts rejected distributions |
| `Proba_combinatoire2.py` | 7 | 4 | Adds bar chart visualization of core loads |
| `Proba_combinatoire3.py` | 7 | 2 | 2-core variant |

`Proba_combinatoire2.py` also plots a horizontal bar chart showing the load on each core for a chosen distribution, which makes it easy to visualize load imbalance across cores.

---

## Summary

```
Real RPi measurements
        │
        ▼
3D Linear Regression  →  p = -12.64 + 15.96·f + 3.66·n
        │
        ├──► Iteration search  →  optimal (f, n) minimizing power
        │
        └──► ILP solver        →  optimal integer (speed, cores)

Task scheduling  →  enumerate distributions → filter overloaded cores → visualize
```
