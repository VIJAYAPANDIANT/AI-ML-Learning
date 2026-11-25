import numpy as np

def forecast_next_day(lag_1: float, lag_7: float, rolling_7: float) -> float:
    # Weighted ensemble forecast
    return round(0.5 * lag_1 + 0.3 * lag_7 + 0.2 * rolling_7, 2)

if __name__ == "__main__":
    print(f"Forecasted Tomorrow Sales: ${forecast_next_day(7450.0, 7120.0, 7300.0):,.2f}")
