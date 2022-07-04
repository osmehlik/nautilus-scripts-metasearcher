
DESTINATION = ~/.local/share/nautilus/scripts/metasearcher/
EXECUTABLES = add-or-edit-tags show-tags search-tags set-attribute get-attribute show-attributes
NONEXECUTABLES = metasearcher.py

install: ${EXECUTABLES} ${NONEXECUTABLES}
	install -m 755 -d ${DESTINATION}
	install -m 755 ${EXECUTABLES} ${DESTINATION}
	install -m 644 ${NONEXECUTABLES} ${DESTINATION}

