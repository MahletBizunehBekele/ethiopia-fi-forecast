from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"


def _load_csv(filename: str) -> pd.DataFrame:
    """
    Load a CSV file from the project's raw data directory.

    Parameters
    ----------
    filename : str
        Name of the CSV file.

    Returns
    -------
    pandas.DataFrame
        Loaded dataframe.

    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist.
    ValueError
        If the CSV file is empty.
    """

    file_path = DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError(f"{filename} is empty.")

    return df


def load_unified_data():
    """Load the unified financial inclusion dataset."""
    return _load_csv("ethiopia_fi_unified_data.csv")


def load_reference_codes():
    """Load the reference codes dataset."""
    return _load_csv("reference_codes.csv")


def load_impact_links():
    """Load the impact links dataset."""
    return _load_csv("impact_links.csv")