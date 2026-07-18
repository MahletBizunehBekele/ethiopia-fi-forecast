from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

def load_unified_data():
    return pd.read_csv(DATA_DIR / "ethiopia_fi_unified_data.csv")

def load_reference_codes():
    return pd.read_csv(DATA_DIR / "reference_codes.csv")

def load_impact_links():
    return pd.read_csv(DATA_DIR / "impact_links.csv")

