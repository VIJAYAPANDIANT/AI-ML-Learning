def assess_flood_risk(rain_mm: float, elev_m: float) -> dict:
    risk_score = (rain_mm / 250.0) * 0.7 + max(0, (50 - elev_m) / 50.0) * 0.3
    tier = "High" if risk_score > 0.6 else "Moderate" if risk_score > 0.3 else "Low"
    return {"risk_score": round(risk_score, 2), "tier": tier}

if __name__ == "__main__":
    print(assess_flood_risk(195, 8))
