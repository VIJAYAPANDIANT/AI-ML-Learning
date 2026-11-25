import numpy as np

def assign_customer_cluster(recency_days: int, total_orders: int, annual_spend: float) -> str:
    if annual_spend > 1500 and recency_days < 30:
        return "VIP Champions"
    elif total_orders >= 8 and recency_days < 60:
        return "Loyal Customers"
    elif recency_days > 120:
        return "At-Risk / Lapsed"
    return "Promising New"

if __name__ == "__main__":
    print("Customer 1:", assign_customer_cluster(14, 18, 2400.00))
    print("Customer 2:", assign_customer_cluster(180, 2, 90.00))
