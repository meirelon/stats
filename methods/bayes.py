import math

def bayes_coin_probability(n_fair: int = 1, n_unfair: int = 0, unfair_bias: float = 1.0, num_flips: int = 1, num_heads: int = 0) -> float:
    """
    Calculate the probability that a coin is unfair given the observed data using Bayes' Theorem.
    
    Parameters:
    -----------
    n_fair : int, optional
        The number of fair coins. Defaults to 1.
        
    n_unfair : int, optional
        The number of unfair coins. Defaults to 0.
        
    unfair_bias : float, optional
        The bias (probability of heads) for the unfair coins. Defaults to 1.0.
        
    num_flips : int, optional
        The total number of coin flips observed. Defaults to 1.
        
    num_heads : int, optional
        The number of heads observed in the coin flips. Defaults to 0.
        
    Returns:
    --------
    float
        The probability that the coin is unfair given the observed data.
    
    Example:
    --------
    >>> bayes_coin_probability(2, 1, 0.7, 10, 7)
    0.8723

    This example calculates the probability that a coin is unfair given that 
    there are 2 fair coins and 1 unfair coin (with a bias of 0.7), after observing
    10 flips with 7 heads.
    """
    # Prior probabilities
    P_fair = n_fair / (n_fair + n_unfair)
    P_unfair = n_unfair / (n_fair + n_unfair)

    # Likelihoods
    # For a fair coin, the probability of getting the observed number of heads
    P_E_given_fair = math.comb(num_flips, num_heads) * (0.5 ** num_flips)
    
    # For an unfair coin, the probability of getting the observed number of heads
    P_E_given_unfair = math.comb(num_flips, num_heads) * (unfair_bias ** num_heads) * ((1 - unfair_bias) ** (num_flips - num_heads))
    
    # Marginal likelihood
    P_E = (P_E_given_fair * P_fair) + (P_E_given_unfair * P_unfair)
    
    # Posterior probability using Bayes' Theorem
    P_unfair_given_E = (P_E_given_unfair * P_unfair) / P_E
    
    return P_unfair_given_E
