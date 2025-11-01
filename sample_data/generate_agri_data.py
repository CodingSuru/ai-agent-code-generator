# generate_agri_data.py
import pandas as pd
import numpy as np
import random
from pathlib import Path

# === CONFIG ===
N_ROWS = 1000
OUTPUT_DIR = Path("sample_data")
OUTPUT_DIR.mkdir(exist_ok=True)

# === INDIAN STATES & DISTRICTS ===
STATES = [
    ("Maharashtra", ["Pune", "Nagpur", "Nashik", "Aurangabad", "Mumbai Suburban"]),
    ("Karnataka", ["Bengaluru", "Mysore", "Hubli", "Belgaum", "Mangalore"]),
    ("Punjab", ["Amritsar", "Ludhiana", "Jalandhar", "Patiala", "Bathinda"]),
    ("Uttar Pradesh", ["Lucknow", "Kanpur", "Agra", "Varanasi", "Meerut"]),
    ("Tamil Nadu", ["Chennai", "Coimbatore", "Madurai", "Salem", "Tiruchirappalli"]),
    ("Gujarat", ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Jamnagar"]),
    ("Rajasthan", ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer"]),
    ("West Bengal", ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri"]),
]

CROPS = ["Wheat", "Rice", "Sugarcane", "Cotton", "Maize", "Groundnut", "Soybean", "Pulses"]

# === GENERATE DATA ===
np.random.seed(42)
random.seed(42)

data = []

for _ in range(N_ROWS):
    state, districts = random.choice(STATES)
    district = random.choice(districts)
    crop = random.choice(CROPS)
    year = random.randint(2015, 2023)

    # Base realistic values
    if crop in ["Wheat", "Maize", "Pulses"]:
        area = random.randint(500, 3000)
        yield_per_ha = round(random.uniform(2.5, 5.5), 2)
    elif crop == "Rice":
        area = random.randint(800, 4000)
        yield_per_ha = round(random.uniform(3.0, 6.0), 2)
    elif crop == "Sugarcane":
        area = random.randint(300, 1500)
        yield_per_ha = round(random.uniform(60, 100), 2)
    else:  # Cotton, Groundnut, Soybean
        area = random.randint(600, 2500)
        yield_per_ha = round(random.uniform(1.5, 4.0), 2)

    production = round(area * yield_per_ha, 2)
    rainfall = random.randint(600, 2200)
    temperature = round(random.uniform(22, 32), 1)
    humidity = random.randint(55, 85)

    # === INTRODUCE 5% ANOMALIES ===
    if random.random() < 0.05:
        anomaly_type = random.choice(["rainfall_spike", "yield_drop", "yield_spike"])
        if anomaly_type == "rainfall_spike":
            rainfall = random.randint(3000, 5000)  # Extreme rain
        elif anomaly_type == "yield_drop":
            yield_per_ha = round(yield_per_ha * 0.3, 2)  # 70% drop
            production = round(area * yield_per_ha, 2)
        elif anomaly_type == "yield_spike":
            yield_per_ha = round(yield_per_ha * 2.5, 2)  # 150% spike
            production = round(area * yield_per_ha, 2)

    data.append({
        "year": year,
        "state": state,
        "district": district,
        "crop": crop,
        "production_tons": production,
        "area_hectares": area,
        "yield_ton_per_ha": yield_per_ha,
        "rainfall_mm": rainfall,
        "temperature_avg": temperature,
        "humidity_pct": humidity
    })

df = pd.DataFrame(data)

# === SAVE TO JSON ===
json_path = OUTPUT_DIR / "agriculture_data.json"
df.to_json(json_path, orient="records", indent=2)
print(f"JSON saved: {json_path} ({len(df)} rows)")

# === SAVE TO EXCEL ===
excel_path = OUTPUT_DIR / "agriculture_data.xlsx"
df.to_excel(excel_path, index=False, engine='openpyxl')
print(f"Excel saved: {excel_path} ({len(df)} rows)")

print("\nFiles ready! Drag into your DataViz Dashboard!")
print("   → JSON: supports direct upload")
print("   → Excel: Save as CSV first (or use online converter)")