# file_organizer/organizer.py

import os
import shutil
from pathlib import Path
from .config import DEFAULT_SOURCE_DIR, FOLDER_MAP

def get_target_folder(file_ext: str) -> str:
    """Returns folder name based on file extension."""
    for folder, extensions in FOLDER_MAP.items():
        if file_ext.lower() in extensions:
            return folder
    return "Others"  # Fallback folder

def organize_directory(source_dir: Path = DEFAULT_SOURCE_DIR):
    """
    Organizes files in source_dir into subfolders by type.
    Does NOT touch folders or hidden files (e.g., .gitignore).
    """
    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

    # Create target folders if not exist
    for folder in FOLDER_MAP.keys():
        (source_dir / folder).mkdir(exist_ok=True)
    (source_dir / "Others").mkdir(exist_ok=True)

    # Process files
    for item in source_dir.iterdir():
        if item.is_file() and not item.name.startswith("."):  # Skip hidden files
            ext = item.suffix  # e.g., ".py"
            target_folder = get_target_folder(ext)
            target_path = source_dir / target_folder / item.name

            # Avoid overwriting
            if target_path.exists():
                print(f"⚠️  Skipped (already exists): {item.name}")
                continue

            try:
                shutil.move(str(item), str(target_path))
                print(f"✅ Moved: {item.name} → {target_folder}/")
            except Exception as e:
                print(f"❌ Failed to move {item.name}: {e}")

    print("\n🎉 Organization complete!")

if __name__ == "__main__":
    organize_directory()