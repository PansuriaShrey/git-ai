#!/bin/bash

# Install dependencies
poetry install

# Build the package
poetry build

# Install the package in the user's home directory
python3 -m pip install --user --force-reinstall dist/*.whl
