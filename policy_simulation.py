
import numpy as np

def simulate_policy(scores, churn, incentive_cost=50, ltv=800):
    thresholds = np.linspace(0.05, 0.9, 50)
    profits = []
    for t in thresholds:
        offer = scores >= t
        retained = offer & (churn == 1)
        profit = retained.sum() * ltv - offer.sum() * incentive_cost
        profits.append((t, profit))
    return profits
