# Ramanujan vs Euler π Approximation

This project compares two methods for approximating the mathematical constant π:

- Ramanujan's infinite series
- Euler's Basel series

The program measures the accuracy of each method, counts the number of correct decimal digits, and plots graphs showing their convergence. :contentReference[oaicite:0]{index=0}

---

## Features

- High-precision π computation
- Ramanujan and Euler/Basel implementations
- Correct decimal digit comparison
- Absolute error calculation
- Convergence graphs using Matplotlib :contentReference[oaicite:1]{index=1}

---

## Mathematics

### Euler–Basel Formula

The Basel identity is

\[
\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}.
\]

Therefore,

\[
\pi \approx \sqrt{6\sum_{n=1}^{N}\frac{1}{n^2}}.
\]

---

### Ramanujan Formula

The Ramanujan series is

\[
\frac{1}{\pi}
=
\frac{2\sqrt2}{9801}
\sum_{k=0}^{\infty}
\frac{(4k)!(1103+26390k)}
{(k!)^4396^{4k}}.
\]

This series converges much faster than the Euler approximation. :contentReference[oaicite:2]{index=2}

---

## Requirements

- Python 3.10+
- mpmath
- matplotlib

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running

```bash
python pi_comparison.py
```

The program prints the approximation results and saves two graphs:

- `pi_correct_digits_comparison.png`
- `pi_error_comparison_log.png` :contentReference[oaicite:3]{index=3}

<img width="1051" height="600" alt="image" src="https://github.com/user-attachments/assets/c8725f66-3799-496d-8d05-20d72cf558fc" />

<img width="977" height="595" alt="image" src="https://github.com/user-attachments/assets/30598e4d-5ffd-48e1-a803-2b21f46e68b1" />

---

## Repository

```
.
├── pi_comparison.py
├── README.md
├── requirements.txt
├── LICENSE
├── pi_correct_digits_comparison.png
└── pi_error_comparison_log.png
```

---
