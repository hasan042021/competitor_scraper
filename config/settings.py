# settings.py
from pathlib import Path
from datetime import datetime

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Input directory (where uploaded CSV/Excel files are placed)
INPUT_DIR = BASE_DIR / "data" / "input"
# Input file names (configurable if needed)
INPUT_CSV_FILENAMES = [""]

# Intermediate storage per day (manufacturers, models, products JSONs)
DATE_STR = datetime.now().strftime("%Y-%m-%d")
INTERMEDIARY_DIR = BASE_DIR / "data" / "raw" / DATE_STR

# Output directory for final CSVs
OUTPUT_DIR = BASE_DIR / "data" / "output" / DATE_STR

# Directory for logs
LOG_DIR = BASE_DIR / "logs"

# Retention (in days) before intermediate data is deleted
DATA_RETENTION_DAYS = 7
