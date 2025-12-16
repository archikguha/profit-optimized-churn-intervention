
import numpy as np

def profit_at_threshold(scores, churn, incentive_cost, ltv, threshold):
    offer = scores >= threshold
    retained = offer & (churn == 1)
    profit = retained.sum() * ltv - offer.sum() * incentive_cost
    return profit
