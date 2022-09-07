import glob
import json
import os
import re
import subprocess


NON_STRING_VALUED_ATTRIBUTES = ["tags", "rating"]


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


def get_data_file_path(metadata_file_path: str) -> str:
    """
    Returns path to data file for the given metadata file.
    """
    return re.sub("\.meta$", "", metadata_file_path)


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
        if "tags" in metadata:
            tags.update(set(metadata["tags"]))
    return tags


def run(cmd):
    """
    Runs command, returns commands return code, stdout
    """
    completed_process = subprocess.run(cmd, capture_output=True)
    retcode = completed_process.returncode
    stdout = completed_process.stdout.decode("utf8").strip()
    return retcode, stdout


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
    retcode, stdout = run(cmd)
    return stdout if retcode == 0 else None


def show_info(text):
    """
    Shows info dialog.
    """
    cmd = [
        "zenity",
        "--info",
        "--text", text,
    ]
    retcode, stdout = run(cmd)


def show_list(title, text, columns: list[str], values: list[str]):
    cmd = [
        "zenity",
        "--list",
        "--title", title,
        "--text", text
    ]

    for column in columns:
        cmd.extend(["--column", column])

    for value in values:
        cmd.append(value)

    retcode, stdout = run(cmd)
    return retcode, stdout


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
    retcode, stdout = run(cmd)
    new_tags = stdout.split(" ")
    return new_tags


def show_gui_set_rating(
    val_init=50,
    val_min=0,
    val_max=100,
    val_step=1
):
    """
    Shows GUI dialog for setting rating of file.
    """
    cmd = [
        "zenity",
        "--scale",
        "--value", str(val_init),
        "--min-value", str(val_min),
        "--max-value", str(val_max),
        "--step", str(val_step),
        "--title", "Rate the file",
        "--text", "Set rating for file"
    ]
    retcode, stdout = run(cmd)
    if (len(stdout) == 0): # nothing selected
        return None
    else:
        return int(stdout) # selected value


def show_gui_find_by_results(find_by_results):
    values = []
    for find_by_result in find_by_results:
        values.extend(find_by_result)
    return show_list(
        "Search Results",
        "The following files have been found:",
        ["File", "Rating", "Tags"],
        values
    )


def find_by(directory_path, rating_ge = None, tags = None):
    # make a list of all files to be filtered
    find_by_results = []
    metadata_files = find_metadata_files_in_directory(directory_path)
    for metadata_file in metadata_files:
        data_file = get_data_file_path(metadata_file)
        metadata = load_metadata(metadata_file)
        data_file_tags = metadata.get("tags", None)
        data_file_rating = metadata.get("rating", None)
        find_by_results.append(
            (data_file, data_file_rating, data_file_tags)
        )
    # filter by rating
    if rating_ge is not None:
        find_by_results = list(filter(
            lambda item: item[1] is not None and item[1] >= rating_ge,
            find_by_results
        ))
    # filter by tags
    if tags is not None:
        find_by_results = list(filter(
            lambda item: item[2] is not None and
            all([tag in item[2] for tag in tags]),
            find_by_results
        ))
    # convert non string values to strings
    find_by_result_final = []
    for find_by_result in find_by_results:
        find_by_result_final.append((
            find_by_result[0],
            str(find_by_result[1]),
            ", ".join(find_by_result[2])
        ))
    return find_by_result_final
