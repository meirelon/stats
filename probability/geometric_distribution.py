import math
import numpy as np
import click


def check_p(p: float):
    if p >= 0 and p <= 1:
        return True
    else:
        raise (ValueError("P must be between 0 and 1"))


def geometric_mean(p: float) -> float:
    if check_p(p):
        return 1 / p


def geometric_std(p: float) -> float:
    if check_p(p):
        return (math.sqrt(1 - p)) / p


class GeometricDistribution:
    def __init__(self, p: float, trials: int, bound: str) -> None:
        self.p = p
        self.trials = trials
        self.bound = bound

    def geometric_probability_simulation(self, simulations: int) -> float:
        return (
            sum([self.prob_success_trial_bound() for x in range(1, simulations)])
            / simulations
        )

    def prob_success_trial_bound(self) -> float:
        if self.trials > 0 and check_p(self.p):
            results = np.random.geometric(p=self.p, size=self.trials) == 1
            l = len(results)
            if self.bound == "exact":
                return results[l - 1] and not any(results[: l - 1])
            if self.bound == "before":
                return any(results)
            if self.bound == "after":
                return sum(results) == 0
            else:
                raise (ValueError("Please specify bound as exact, before, or after"))


@click.command()
@click.option(
    "--p",
    type=float,
    help="probability of success",
)
@click.option(
    "--trials",
    type=int,
    help="Number of Trials",
)
@click.option(
    "--bound",
    type=str,
    help="Probability Bounded by Exact, Lower, or Upper",
)
@click.option("--simulations", type=int, help="Number of Simulations", default=10**4)
@click.option(
    "--local",
    type=bool,
    default=True,
)
def geometric_probability(p, trials, bound, simulations, local=False):
    g = GeometricDistribution(p=p, trials=trials, bound=bound)
    gprob = g.geometric_probability_simulation(simulations=simulations)
    if local:
        print(gprob)
    return gprob


if __name__ == "__main__":
    geometric_probability()
