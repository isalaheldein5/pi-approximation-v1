# Ramanujan vs Euler π Approximation

This project compares two methods for approximating π:

- Ramanujan's infinite series
- Euler's Basel series

The program compares the accuracy of each method, counts correct decimal digits, and plots convergence graphs.

## Features

- High-precision π computation
- Ramanujan and Euler implementations
- Correct decimal digit comparison
- Absolute error calculation
- Convergence graphs

## Mathematics

### Euler–Basel

\[
\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}
\]

\[
\pi\approx\sqrt{6\sum_{n=1}^{N}\frac{1}{n^2}}
\]

### Ramanujan

\[
\frac1\pi=
\frac{2\sqrt2}{9801}
\sum_{k=0}^{\infty}
\frac{(4k)!(1103+26390k)}{(k!)^4396^{4k}}
\]

## Requirements

- Python 3.10+
- mpmath
- matplotlib

```bash
pip install -r requirements.txt
```

## Running

```bash
python pi_comparison.py
```

Outputs:

- `pi_correct_digits_comparison.png`
- `pi_error_comparison_log.png`

## License

MIT