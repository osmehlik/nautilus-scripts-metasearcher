
DESTINATION = ~/.local/share/nautilus/scripts/metasearcher/
EXECUTABLES = show-tags find-by-tags find-by-rating find-by-tags-and-rating set-attribute set-attribute-tags set-attribute-rating get-attribute show-attributes
NONEXECUTABLES = metasearcher.py

install: ${EXECUTABLES} ${NONEXECUTABLES}
	install -m 755 -d ${DESTINATION}
	install -m 755 ${EXECUTABLES} ${DESTINATION}
	install -m 644 ${NONEXECUTABLES} ${DESTINATION}

