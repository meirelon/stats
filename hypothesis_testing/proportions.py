import math


def record_data(n1, p1, n2, p2):
    return {"p1": {"success": p1, "n": n1}, "p2": {"success": p2, "n": n2}}


def get_proportion(p, n):
    return {"proportion": p / n, "n": n}


def get_sigma(p, n):
    return (p * (1 - p)) / n


def proportion_stats(data: dict) -> dict:
    proportions = {k: get_proportion(v["success"], v["n"]) for k, v in data.items()}
    sigmas = [get_sigma(v["proportion"], v["n"]) for k, v in proportions.items()]
    sampling_distribution = math.sqrt(sum(sigmas))

    return {
        "proportions": [v["proportion"] for k, v in proportions.items()],
        "sampling_distribution": sampling_distribution,
    }


def zscore(summary_stats: dict):
    proportion_difference = abs(
        summary_stats["proportions"][0] - summary_stats["proportions"][1]
    )
    return (proportion_difference - 0) / summary_stats["sampling_distribution"]


if __name__ == "__main__":
    data = record_data(1000, 643, 1000, 591)
    summary_stats = proportion_stats(data)
    print(zscore(summary_stats))
