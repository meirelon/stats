import random
from scipy.stats import binom
import numpy as np


def generate_random_values(n=1000):
    return np.array(
        [
            random.normalvariate(
                mu=random.randint(1, 100), sigma=random.randint(15, 30)
            )
            for x in range(1, n)
        ]
    )


def sample_mean_from_sample(data):
    sample = random.choices(data, k=len(data))
    sample_mean = sum(sample) / len(sample)
    return sample_mean


def bootstrapping(data, n=1000):
    return np.array([sample_mean_from_sample(data) for x in range(1, n)])


def bootstrapped_quantiles(data, alpha=0.05):
    boostrapped_data = np.sort(bootstrapping(data, len(data)))
    lower = alpha / 2
    upper = (1 - alpha) / 2
    quantiles = [
        np.quantile(boostrapped_data, lower),
        np.quantile(boostrapped_data, upper),
    ]
    return quantiles


alpha = 0.05
quantile_of_interest = 0.5
sample_size = 10000
number_of_bootstrap_samples = 1000000
outcome_sorted = np.sort(np.random.normal(1, 1, sample_size))

ci_indexes = binom.ppf(
    [alpha / 2, 1 - alpha / 2], sample_size + 1, quantile_of_interest
)
bootstrap_confidence_interval = outcome_sorted[
    [int(np.floor(ci_indexes[0])), int(np.ceil(ci_indexes[1]))]
]

f"The sample median is {np.quantile(outcome_sorted, quantile_of_interest)}, the {(1-alpha)*100}%\
confidence interval is given by ({bootstrap_confidence_interval})."
