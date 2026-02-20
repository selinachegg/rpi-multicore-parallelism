<p align="center">
  <img src="logo.png" alt="Project Logo" width="200"/>
</p>

# Multicore Parallelism & Power Analysis on Raspberry Pi 3

**Course:** Parallélisme & Architecture multicores — TP 1
**Date:** 2021/2022
**Hardware:** Raspberry Pi 3 B+ — Quad-core ARM Cortex-A53 @ 1.4 GHz
**Author:** Selina CHEGGOUR
**Supervisor:** Cecile BELLEUDY

---

## Overview

This lab studies the real impact of core-level parallelism on both **execution speed** and **energy consumption** on an embedded multicore board (Raspberry Pi 3 B+). Three interconnected experiments are carried out:

1. **Grayscale image filtering** — same algorithm applied with 0, 2, and 4 cores in parallel
2. **Video frame edge detection** — car detection use case for surveillance, benchmarked across CPU governors
3. **Power consumption modeling** — 3D linear regression fitted from real RPi measurements, then used in ILP optimization and task scheduling

---

## Hardware — Raspberry Pi 3 B+

| Property | Value |
|----------|-------|
| Processor | Broadcom BCM2837B0 — ARM Cortex-A53 64-bit |
| Cores | 4 |
| Frequency range | 0.6 GHz (min) → 1.4 GHz (max) |
| Voltage | 5V |
| CPU governors | Ondemand, Powersave, Performance, Conservative, Schedutil, Userspace |

---

## Experiment 1 — Grayscale Filter (`01_grayscale_filter/`)

The grayscale formula applied pixel by pixel: `gray = (R + G + B) / 3`

The image (lena.jpg) is split into N equal parts, each processed by a separate core using Python's `multiprocessing.Process`, then reassembled.

| Parallelism level | Cores used | Execution time | Max current | Max energy |
|-------------------|-----------|----------------|-------------|------------|
| Sequential (x0)   | 1         | 33.09 s        | 0.59 A      | 97.6 J     |
| Parallel x2       | 2         | **14.70 s**    | 0.77 A      | **56.59 J**|
| Parallel x4       | 4         | 18.47 s        | 0.81 A      | 74.80 J    |

> Parallel x2 outperforms x4: the overhead of splitting into 4 quadrants and reassembling costs more than the parallelism gain on a 4-core board at this image size.

---

## Experiment 2 — Edge Detection (`02_edge_detection/`)

**Use case:** Video surveillance — detect a car passing in front of a camera.

**Method:**
1. Convert both the reference frame and the new frame to grayscale
2. Split each into 4 quadrants → 8 sub-images total
3. Compute pixel-wise difference between paired quadrants: `mean = (ΔR + ΔG + ΔB) / 3`
4. Threshold at 70: pixel → white (edge detected) or black (no change)
5. Reassemble into a binary edge map

The algorithm runs with parallelism level 4 (one core per quadrant pair), benchmarked across CPU governors:

| Governor | Execution time | Max current | Max energy |
|----------|----------------|-------------|------------|
| Ondemand | 29.97 s | 0.81 A | 121.37 J |
| Powersave | 57.36 s | 0.59 A | **169.21 J** ← most energy |
| **Performance** | **29.70 s** | **0.62 A** | **92.07 J** ← best overall |
| Conservative | 30.26 s | 0.84 A | 127.09 J |

> For edge detection, Performance governor is both the fastest and most energy-efficient — the opposite of intuition.

---

## Experiment 3 — Power Modeling (`03_power_modeling/`)

See [`03_power_modeling/POWER_MODELING.md`](03_power_modeling/POWER_MODELING.md) for full explanation.

**Power model derived from real RPi 3 measurements:**

```
p = -12.64 + 15.96·f + 3.66·n
```

where `p` = power (W), `f` = CPU frequency (GHz), `n` = number of active cores.

---

## Installation

```bash
pip install -r requirements.txt
```

## Usage

> Each script uses relative file paths — always run from inside its own folder.

```bash
# Grayscale filter — sequential
cd 01_grayscale_filter/sequential
python Filtre_gris_sans_parallelisme.py

# Grayscale filter — 2 cores
cd 01_grayscale_filter/parallel_x2
python Filtre_gris_avec_parallelisme_taux2.py

# Grayscale filter — 4 cores
cd 01_grayscale_filter/parallel_x4
python Filtre_gris_avec_parallelisme_niveau4.py

# Edge detection
cd 02_edge_detection
python Detection_de_contour.py

# Power modeling
cd 03_power_modeling
python 3D_linear_regression_model.py
python Power_solver.py
python Proba_combinatoire.py
python Proba_combinatoire2.py
python iteration.py
```

> The multiprocessing scripts require `if __name__ == '__main__':` — already in place for Windows compatibility.
