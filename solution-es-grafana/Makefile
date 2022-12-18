# Makefile
VENV=venv

install : clean
	@echo "Installing $(VENV)"
	python3 -m venv venv
	(source ./$(VENV)/bin/activate)
	@echo "You're now connected to $(VENV)"
	pip install -r requirements.txt

import :
	@echo "Importing data from the API"
	python3 import_crimes.py

clean :
	@echo "Cleaning the $(VENV)"
	rm -rf $(VENV)
	@echo "$(VENV) is now clean"

delete-index : 
	@echo "Deleting the database"
	python3 clean_index_es.py
	@echo "Database is now deleted"
	