def classify_waste_item(material_density: float, reflectivity: float) -> str:
    if material_density > 5.0: return "Metal"
    elif reflectivity > 0.8: return "Glass"
    elif material_density < 1.2: return "Plastic"
    return "Organic / Paper"

if __name__ == "__main__":
    print("Classified:", classify_waste_item(0.95, 0.4))
