import random


def binary_p_value(trials):
    flips = random.choices([True, False], k=trials)
    outcomes = 2**trials
    flips_prob = 2 * (sum(flips) / outcomes)
    rare_event = 2 / outcomes
    return sum([flips_prob, rare_event])


if __name__ == "__main__":
    print(binary_p_value(5))