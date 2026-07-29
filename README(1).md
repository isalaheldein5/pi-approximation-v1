# Ramanujan vs Euler π Approximation

This project compares two methods for approximating the mathematical constant π:

- Ramanujan's infinite series
- Euler's Basel series

The program measures the accuracy of each method, counts the number of correct decimal digits, and plots graphs showing their convergence.

---

## Features

- High-precision π computation
- Ramanujan and Euler/Basel implementations
- Correct decimal digit comparison
- Absolute error calculation
- Convergence graphs using Matplotlib

---

## Mathematics

### Euler–Basel Formula

\[
\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}
\]

Therefore,

\[
\pi \approx \sqrt{6\sum_{n=1}^{N}\frac{1}{n^2}}
\]

### Ramanujan Formula

\[
\frac{1}{\pi}
=
\frac{2\sqrt2}{9801}
\sum_{k=0}^{\infty}
\frac{(4k)!(1103+26390k)}
{(k!)^4396^{4k}}
\]

Ramanujan's series converges significantly faster than the Euler approximation.

---

## Results

### Correct Decimal Digits


<img width="977" height="595" alt="image" src="https://github.com/user-attachments/assets/859a2e4f-045a-4313-a19d-05935095e304" />



### Approximation Error

<img width="1051" height="600" alt="Screenshot 2026-07-29 231043" src="https://github.com/user-attachments/assets/56b48da1-2521-4bc0-808b-e1cb26194928" />

---

## Requirements

- Python 3.10+
- mpmath
- matplotlib

```bash
pip install -r requirements.txt
```

---

## Running

```bash
python pi_comparison.py
```

The program generates:

- `pi_correct_digits_comparison.png`
- `pi_error_comparison_log.png`

---

## License

MIT License
