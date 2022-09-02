
# nautilus-scripts-metasearcher

- A simple set of tools to
    - add/edit tags to files
    - search for files by tags
    - add custom attributes to files
    - show/get these custom attributes
- It is implemented as a [Nautilus scripts](https://help.ubuntu.com/community/NautilusScriptsHowto).
- It is written in Python.
- It uses zenity (app to create simple GUIs from command line) as a GUI.

## How it works

There are metadata files (somefile.meta, has json format) which holds metadata for files.
By default metadata file for file `somefile` is named `somefile.meta`
and could hold something like this:

```json
{
    "somefile": {
        "tags": ["tag1", "tag2"],
        "some_attribute": "value_of_some_attribute",
        "other_attribute": "value_of_other_attribute"
    }
}
```

(Metadata for file in metadata file are under key named by file's path,
because there could be one metadata file holding data for multiple files
in future.)

## Dependencies

- Nautilus
- Python 3
- Zenity (`sudo apt-get install zenity`)
- xdg-open
- Make (for installation)

## Installation

- Run `cd src`
- Run `make install`

## Usage

1. Right click on a file or directory in Nautilus.
2. Select Scripts > metasearcher > name of tool you want to try.

## Files

- `add-or-edit-tags` - Adds or edits tags for selected file.
- `show-tags` - Shows all tags used by files in selected directory.
- `search-tags` - Search for files with tags in selected directory.
- `set-attribute` - Sets value of attribute (a key-value pair) for selected file.
- `set-attribute-rating` - Sets rating for selected file. (GUI for search by rating not yet implemented.)
- `get-attribute` - Gets value of attribute for selected file.
- `show-attributes` - Shows all attributes for selected file.

## License

[BSD 2-Clause License](LICENSE)

