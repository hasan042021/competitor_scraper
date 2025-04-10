# utils/file_manager.py
import json
from pathlib import Path
from datetime import datetime, timedelta
from config.settings import INTERMEDIARY_DIR, DATA_RETENTION_DAYS


def save_json(data: dict, filename: str):
    """Saves a dictionary to a JSON file in the intermediate directory."""
    INTERMEDIARY_DIR.mkdir(parents=True, exist_ok=True)
    path = INTERMEDIARY_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(filename: str) -> dict:
    """Loads a JSON file from the intermediate directory."""
    path = INTERMEDIARY_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def cleanup_old_data(base_dir: Path):
    """Deletes intermediate folders older than retention period."""
    now = datetime.now()
    for folder in base_dir.glob("*"):
        if folder.is_dir():
            try:
                folder_date = datetime.strptime(folder.name, "%Y-%m-%d")
                age = (now - folder_date).days
                if age > DATA_RETENTION_DAYS:
                    print(f"[!] Deleting old intermediate folder: {folder}")
                    for f in folder.glob("**/*"):
                        f.unlink()
                    folder.rmdir()
            except ValueError:
                continue  # Skip non-date-named folders
