import mpmath as mp
import matplotlib.pyplot as plt

TARGET_DIGITS_TO_CHECK = 80
MAX_RAMANUJAN_TERMS = 6
MAX_EULER_TERMS = 50_000
EULER_GRAPH_POINTS = 400

mp.mp.dps = TARGET_DIGITS_TO_CHECK + 30
TRUE_PI = mp.pi


def fixed_decimal(x, decimal_digits):
    """Return x as a non-rounded decimal string."""
    integer_part = int(mp.floor(x))
    frac = x - integer_part

    digits = []
    for _ in range(decimal_digits):
        frac *= 10
        digit = int(mp.floor(frac))
        digits.append(str(digit))
        frac -= digit

    return f"{integer_part}." + "".join(digits)


def check_matching_digits(estimate, digits_to_check):
    """Checks where the estimate stops matching pi."""
    est_str = fixed_decimal(estimate, digits_to_check)
    pi_str = fixed_decimal(TRUE_PI, digits_to_check)

    est_decimals = est_str.split(".")[1]
    pi_decimals = pi_str.split(".")[1]

    for position, (est_digit, true_digit) in enumerate(
        zip(est_decimals, pi_decimals), start=1
    ):
        if est_digit != true_digit:
            return {
                "correct_digits": position - 1,
                "first_wrong_position": position,
                "estimate_digit": est_digit,
                "true_digit": true_digit,
                "estimate_string": est_str,
                "pi_string": pi_str,
            }

    return {
        "correct_digits": digits_to_check,
        "first_wrong_position": None,
        "estimate_digit": None,
        "true_digit": None,
        "estimate_string": est_str,
        "pi_string": pi_str,
    }


def ramanujan_pi(terms):
    """
    Ramanujan formula:

    1/pi = (2sqrt(2) / 9801) * sum(...)
    """
    total = mp.mpf(0)

    for k in range(terms):
        numerator = mp.factorial(4 * k) * (1103 + 26390 * k)
        denominator = (mp.factorial(k) ** 4) * (396 ** (4 * k))
        total += numerator / denominator

    inverse_pi = (2 * mp.sqrt(2) / 9801) * total
    return 1 / inverse_pi


def euler_pi(terms):
    """
    Leonhard Euler / Basel approximation:

    pi = sqrt(6 * (1 + 1/4 + 1/9 + 1/16 + ...))
    """
    total = mp.mpf(0)

    for n in range(1, terms + 1):
        total += mp.mpf(1) / (n ** 2)

    return mp.sqrt(6 * total)


def print_report(name, estimate, terms):
    result = check_matching_digits(estimate, TARGET_DIGITS_TO_CHECK)
    error = abs(TRUE_PI - estimate)

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)
    print(f"Terms used: {terms}")
    print(f"Estimate:  {result['estimate_string']}")
    print(f"Real pi:   {result['pi_string']}")
    print(f"Error:     {mp.nstr(error, 20)}")
    print(f"Correct decimal digits: {result['correct_digits']}")

    if result["first_wrong_position"] is None:
        print(f"It matched all {TARGET_DIGITS_TO_CHECK} checked digits.")
    else:
        print(f"It stops being pi at decimal digit: {result['first_wrong_position']}")
        print(f"Estimate has: {result['estimate_digit']}")
        print(f"Pi has:       {result['true_digit']}")


def make_data():
    ramanujan_x = []
    ramanujan_digits = []
    ramanujan_errors = []

    for terms in range(1, MAX_RAMANUJAN_TERMS + 1):
        estimate = ramanujan_pi(terms)
        result = check_matching_digits(estimate, TARGET_DIGITS_TO_CHECK)

        ramanujan_x.append(terms)
        ramanujan_digits.append(result["correct_digits"])
        ramanujan_errors.append(float(abs(TRUE_PI - estimate)))

    euler_x = []
    euler_digits = []
    euler_errors = []

    euler_sum = mp.mpf(0)
    step = max(1, MAX_EULER_TERMS // EULER_GRAPH_POINTS)

    for n in range(1, MAX_EULER_TERMS + 1):
        euler_sum += mp.mpf(1) / (n ** 2)

        if n == 1 or n % step == 0 or n == MAX_EULER_TERMS:
            estimate = mp.sqrt(6 * euler_sum)
            result = check_matching_digits(estimate, TARGET_DIGITS_TO_CHECK)

            euler_x.append(n)
            euler_digits.append(result["correct_digits"])
            euler_errors.append(float(abs(TRUE_PI - estimate)))

    return ramanujan_x, ramanujan_digits, ramanujan_errors, euler_x, euler_digits, euler_errors


def plot_graphs(r_x, r_digits, r_errors, e_x, e_digits, e_errors):
    plt.figure(figsize=(10, 6))
    plt.plot(r_x, r_digits, marker="o", label="Ramanujan formula")
    plt.plot(e_x, e_digits, marker="o", label="Euler/Basel formula")

    plt.xscale("log")
    plt.xlabel("Number of terms used")
    plt.ylabel("Correct decimal digits of pi")
    plt.title("How many digits of pi are correct?")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig("pi_correct_digits_comparison.png", dpi=200)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(r_x, r_errors, marker="o", label="Ramanujan formula")
    plt.plot(e_x, e_errors, marker="o", label="Euler/Basel formula")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of terms used")
    plt.ylabel("Error compared with real pi")
    plt.title("Pi approximation error: Ramanujan vs Euler/Basel")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig("pi_error_comparison_log.png", dpi=200)
    plt.show()


def main():
    r_x, r_digits, r_errors, e_x, e_digits, e_errors = make_data()

    final_ramanujan = ramanujan_pi(MAX_RAMANUJAN_TERMS)
    final_euler = euler_pi(MAX_EULER_TERMS)

    print_report("Ramanujan pi formula", final_ramanujan, MAX_RAMANUJAN_TERMS)
    print_report("Leonhard Euler / Basel pi approximation", final_euler, MAX_EULER_TERMS)

    plot_graphs(r_x, r_digits, r_errors, e_x, e_digits, e_errors)

    print("\nGraphs saved as:")
    print("- pi_correct_digits_comparison.png")
    print("- pi_error_comparison_log.png")


if __name__ == "__main__":
    main()