VENV = venv
PYTHON = venv/bin/python
LIBS = pymath/cmath

.PHONY: all venv activate deactivate install test


all:
	$(MAKE) -C pymath/cmath

venv:
	python3 -m venv venv

activate:
	source $(VENV)/bin/activate

deactivate:
	deactivate

install:
	pip install -r requirements.txt

test:
	$(PYTHON) -m unittest discover test
