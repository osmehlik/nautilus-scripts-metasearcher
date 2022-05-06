import glob
import json
import os
import subprocess


def get_files():
    """
    Returns list of selected files in Nautilus.
    """
    selected_file_paths = os.environ["NAUTILUS_SCRIPT_SELECTED_FILE_PATHS"]
    selected_file_paths = selected_file_paths.strip().split("\n")
    return selected_file_paths


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
        with open(metadata_file, "r", encoding="utf8") as f:
            metadata = json.load(f)
            for value in metadata.values():
                tags.update(set(value["tags"]))
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
