# file_organizer/config.py

import os
from pathlib import Path

# Default source folder (change as needed)
DEFAULT_SOURCE_DIR = Path.home() / "Downloads"

# Folder mapping by extension
FOLDER_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".odt"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".ogg", ".flac"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".sh", ".json", ".yaml"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
}