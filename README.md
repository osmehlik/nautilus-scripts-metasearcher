
# metasearcher

- A simple set of tools to add/edit tags to files and search for files by tags.
- It is implemented as a [Nautilus scripts](https://help.ubuntu.com/community/NautilusScriptsHowto).
- It is written in Python.
- It uses zenity (app to create simple GUIs from command line) as a GUI.

## How it works

There are metadata files (somefile.meta, has json format) which holds metadata for files.
By default metadata file for file `somefile` is named `somefile.meta`
and holds this:

```json
{
    "somefile": {
        "tags": ["aaa", "bbb"]
    }
}
```

## Dependencies

- Nautilus
- Python 3
- Zenity (`sudo apt-get install zenity`)
- xdg-open
- Make (for installation)

## Installation

- Run `make install`

## Usage

1. Right click on a file or directory in Nautilus.
2. Select Scripts > metasearcher > name of tool you want to try.

## Files

- add-or-edit-tags - Adds or edits tags for selected file.
- show-tags - Shows all tags used by files in selected directory.
- search-tags - Search for files with tags in selected directory.

## License

[BSD 2-Clause License](LICENSE)

