import pandas as pd

def compute_bi_metric(df: pd.DataFrame, group_col: str, metric_col: str) -> dict:
    grouped = df.groupby(group_col)[metric_col].sum().to_dict()
    return {"group": group_col, "totals": grouped}

if __name__ == "__main__":
    test_df = pd.DataFrame({"Region": ["A", "B", "A"], "Sales": [100, 200, 150]})
    print(compute_bi_metric(test_df, "Region", "Sales"))
