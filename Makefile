VENV_DIR ?= .venv

ifeq ($(OS),Windows_NT)
PYTHON ?= python
VENV_BIN := $(VENV_DIR)/Scripts
else
PYTHON ?= python3
VENV_BIN := $(VENV_DIR)/bin
endif

ACTIVATE := . $(VENV_BIN)/activate

.PHONY: build run up

build:
	$(PYTHON) -m venv --clear $(VENV_DIR)
	$(ACTIVATE) && pip install -r requirements.txt

run: up

up:
	$(ACTIVATE) && uvicorn main:app --reload
