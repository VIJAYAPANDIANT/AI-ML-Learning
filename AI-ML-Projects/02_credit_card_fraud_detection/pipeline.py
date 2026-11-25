import numpy as np

def score_transaction(amount: float, v1: float, v2: float) -> dict:
    risk_score = 0.1
    if amount > 500: risk_score += 0.4
    if v1 > 2.0: risk_score += 0.3
    if v2 > 2.0: risk_score += 0.2
    
    is_fraud = risk_score >= 0.7
    return {"amount": amount, "risk_score": round(risk_score, 2), "fraud_alert": is_fraud}

if __name__ == "__main__":
    print(score_transaction(45.50, 0.1, -0.2))
    print(score_transaction(1250.00, 2.5, 3.1))
