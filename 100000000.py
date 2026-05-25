import math

def basel_pi_approximation(n: int) -> float:

   
    series_sum = sum(1 / (k ** 2) for k in range(1, n + 1))
    
    
    pi_approx = math.sqrt(6 * series_sum)
    return pi_approx


for terms in [10, 100, 1000, 10000]:
    result = basel_pi_approximation(terms)
    error = abs(math.pi - result)
    print(f"Terms (n): {terms:5} | Approx: {result:.6f} | Error: {error:.6f}")
