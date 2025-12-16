
from sklearn.ensemble import GradientBoostingClassifier

def train_churn_model(X, y):
    model = GradientBoostingClassifier()
    model.fit(X, y)
    return model
