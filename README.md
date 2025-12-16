# Customer Churn → Profit Optimization (Product DS)

## Business Context
Subscription businesses lose revenue when customers churn. 
Retention budgets are limited, so **not every at-risk customer should receive an offer**.

## Decision Problem
For each customer:
- Estimate churn probability
- Decide whether to offer a retention incentive
- Maximize **net profit**, not prediction accuracy

## Data
Based on the public **IBM Telco Customer Churn dataset**.
A small representative sample is included for reproducibility.

## Why Churn Prediction Alone Is Insufficient
- Incentives cost money
- Some customers churn regardless
- Some customers would stay without incentives

## Modeling Strategy
- Predict churn probability
- Simulate retention offers
- Assign incentive costs
- Estimate retained lifetime value (LTV)
- Optimize decision threshold using profit curves

## Business Impact (Simulated (for demonstration))
- 12–18% uplift in net retention profit
- Same incentive budget
- Reduced unnecessary discounts

## Failure Modes
- Incentive cannibalization
- Offer fatigue
- LTV misestimation
