def calculate_traffic_index(vehicle_count: int, road_capacity: int = 20) -> dict:
    ratio = vehicle_count / road_capacity
    status = "Congested" if ratio >= 0.8 else "Optimal" if ratio >= 0.4 else "Free-Flow"
    return {"vehicle_count": vehicle_count, "capacity_ratio": round(ratio, 2), "status": status}

if __name__ == "__main__":
    print(calculate_traffic_index(18, 20))
