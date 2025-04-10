# utils/output_writer.py
import pandas as pd  # type: ignore
from config.settings import OUTPUT_DIR
from datetime import datetime
from pathlib import Path


def write_product_data(data: list[dict], domain: str, file_type: str):
    """
    Writes product data to a CSV file.

    Parameters:
        data (list of dict): The data to write.
        domain (str): The domain name (e.g., 'otto' or 'boettcher').
        file_type (str): Either 'matched' or 'unmatched' to determine filename.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(data)

    if file_type == "matched":
        filename = (
            OUTPUT_DIR
            / f"daily_prices_{domain}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        )
    elif file_type == "unmatched":
        filename = (
            OUTPUT_DIR / f"not_found_{domain}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        )
    else:
        raise ValueError("file_type must be 'matched' or 'unmatched'")

    df.to_csv(filename, index=False)
    print(f"[✓] Saved {file_type} products to {filename}")
