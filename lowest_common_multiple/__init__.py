from get_prime_number import get_prime_number

def lowest_common_multiple(num1, num2):
    prime_number = get_prime_number()
    factors = []

    lcm = 1

    quotient1 = num1
    quotient2 = num2

    while quotient1 != 1 or quotient2 != 1:
        factor_candidate = next(prime_number)

        while (
            quotient1 % factor_candidate == 0 or
            quotient2 % factor_candidate == 0
        ):
            factors.append(factor_candidate)
            if quotient1 % factor_candidate == 0:
                quotient1 = quotient1 / factor_candidate

            if quotient2 % factor_candidate == 0:
                quotient2 = quotient2 / factor_candidate

    for factor in factors:
        lcm = lcm * factor

    return lcm
