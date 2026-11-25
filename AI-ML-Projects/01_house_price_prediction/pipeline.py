import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

def train_and_predict(sqft: float, bedrooms: int, bathrooms: float, age: int, location_score: float):
    # Simulated trained model deployment inference
    base_price = (sqft * 180) + (bedrooms * 18000) + (bathrooms * 14000) - (age * 750) + (location_score * 35000)
    return round(base_price, 2)

if __name__ == "__main__":
    sample_price = train_and_predict(2400, 3, 2.5, 5, 4.2)
    print(f"Predicted Property Valuation: ${sample_price:,.2f} USD")
