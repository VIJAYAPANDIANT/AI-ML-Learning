def recommend_crop(n: float, p: float, k: float, rainfall: float) -> str:
    if rainfall > 180: return "Rice"
    elif k > 60: return "Chickpea"
    elif n > 90: return "Cotton"
    return "Maize"

if __name__ == "__main__":
    print("Recommended:", recommend_crop(85, 40, 40, 220))
