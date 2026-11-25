def check_track_anomaly(vibration_g: float, temp_c: float) -> dict:
    is_anomaly = vibration_g > 1.2 or temp_c > 40.0
    severity = "CRITICAL" if (vibration_g > 1.8 and temp_c > 45) else "WARNING" if is_anomaly else "NORMAL"
    return {"vibration": vibration_g, "temp": temp_c, "status": severity}

if __name__ == "__main__":
    print(check_track_anomaly(0.42, 29.0))
    print(check_track_anomaly(2.10, 48.5))
