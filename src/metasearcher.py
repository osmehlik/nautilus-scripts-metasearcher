import glob
import json
import os
import subprocess


def get_selected_files():
    """
    Returns list of selected files in Nautilus.
    """
    selected_file_paths = os.environ["NAUTILUS_SCRIPT_SELECTED_FILE_PATHS"]
    selected_file_paths = selected_file_paths.strip().split("\n")
    return selected_file_paths


def get_metadata_file_path(data_file_path: str) -> str:
    """
    Returns path to metadata file for the given data file.
    """
    return data_file_path + ".meta"


def load_metadata(metadata_file_path: str) -> dict:
    """
    Loads metadata from file.
    """
    if os.path.exists(metadata_file_path):
        with open(metadata_file_path, "r", encoding="utf8") as f:
            return json.load(f)
    else:
        return {}


def save_metadata(metadata: dict, metadata_file_path: str) -> None:
    """
    Saves metadata to file.
    """
    with open(metadata_file_path, "w", encoding="utf8") as f:
        json.dump(metadata, f)


def find_metadata_files_in_directory(path_to_directory):
    """
    Returns list of paths to metadata files in directory.
    """
    return glob.glob(f"{path_to_directory}/**/*.meta", recursive=True)


def find_tags_in_metadata_files(metadata_files):
    """
    Returns set of tags present in metadata_files.
    """
    tags = set()
    for metadata_file in metadata_files:
        metadata = load_metadata(metadata_file)
        for metadata_for_file in metadata.values():
            if "tags" in metadata_for_file:
                tags.update(set(metadata_for_file["tags"]))
    return tags


def show_gui_add_edit_tags(old_tags=[]):
    """
    Shows GUI dialog for adding or editing tags.
    """
    cmd = [
        "zenity",
        "--entry",
        "--text", "Enter tags (separated by space)",
        "--entry-text", " ".join(old_tags)
    ]
    completed_process = subprocess.run(cmd, capture_output=True)
    returncode = completed_process.returncode
    stdout = completed_process.stdout.decode("utf8").strip()
    new_tags = stdout.split(" ")
    return new_tags


def show_entry(text):
    """
    Shows entry dialog.
    If user clicked Ok, returns text entered into entry dialog.
    If user clicked Cancel, returns None.
    """
    cmd = [
        "zenity",
        "--entry",
        "--text", text,
    ]
    completed_process = subprocess.run(cmd, capture_output=True)
    returncode = completed_process.returncode
    stdout = completed_process.stdout.decode("utf8").strip()
    return stdout if returncode == 0 else None

def show_info(text):
    """
    Shows info dialog.
    """
    cmd = [
        "zenity",
        "--info",
        "--text", text,
    ]
    completed_process = subprocess.run(cmd, capture_output=True)

