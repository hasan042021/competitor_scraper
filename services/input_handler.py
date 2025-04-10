# utils/input_handler.py
import pandas as pd  # type: ignore
from config.settings import INPUT_DIR, INPUT_CSV_FILENAME
from pathlib import Path


def read_input_file(filename):
    input_path = INPUT_DIR / f"{filename}"

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix == ".csv":
        df = pd.read_csv(input_path)
    elif input_path.suffix in [".xls", ".xlsx"]:
        df = pd.read_excel(input_path)
    else:
        raise ValueError("Unsupported input file format")

    required_columns = [
        "Internal Product No",
        "OEM Number",
        "Article",
    ]

    # check if any column is missing in input file
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Missing one or more required columns: {required_columns}")

    return df
