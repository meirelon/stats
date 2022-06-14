import math
import click
from collections import defaultdict
import spotify_confidence as sc


def effect_size(m0, m1, s0, s1):
    # https://youtu.be/VX_M3tIyiYk?t=715
    mean_difference = abs(m0 - m1)
    pooled_estimated_stddev = math.sqrt(((s0**2) + (s1**2)) / 2)
    return mean_difference / pooled_estimated_stddev


def power_analysis_range(starting_power, increments=0.05):
    increments_transformed = 0.05 * 100.0
    power_transformed = int(starting_power * 100.0)
    return [
        p / 100.0
        for p in range(
            power_transformed,
            100,
            int(increments_transformed),
        )
    ]


@click.command()
@click.option(
    "--mde",
    type=float,
    help="minimal detectable effect size as either difference in means or proportions",
)
@click.option(
    "--baseline",
    type=float,
    help="Baseline variance or proportion for target population",
)
@click.option("--power", default=0.8, type=float, help="Power to be used for test")
@click.option(
    "--alpha",
    default=0.05,
    type=float,
    help="Significance Threshold to be used for test",
)
@click.option(
    "--method",
    default="continuous",
    type=str,
    help="continuous or binomial",
)
def power_analysis(mde, baseline, power, alpha, method):
    """
    mde: minimal detectable effect size.
    baseline: Baseline variance for target population
    power: Tells us the sample we need in order to have a high probability of rejecting null hypothesis
    alpha: Tells us the significance threshold (i.e. the % of false positives we can expect when measuring results)
    effect_size: Difference between baseline and expected distributions
    """
    sample_size = sc.SampleSize()
    powers = power_analysis_range(power)
    power_analysis_dict = defaultdict()
    for p in powers:
        if method == "continuous":
            sample_needed = sample_size.continuous(
                average_absolute_mde=mde,
                baseline_variance=baseline,
                alpha=alpha,
                power=p,
            )
        elif method == "binomial":
            sample_needed = sample_size.binomial(
                absolute_percentage_mde=mde,
                baseline_proportion=baseline,
                alpha=alpha,
                power=p,
            )
        else:
            raise Exception("Please provide method: continuous or binomial")
        power_analysis_dict[p] = sample_needed[0]
    return power_analysis_dict


if __name__ == "__main__":
    power_analysis()
