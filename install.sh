#!/bin/bash

poetry install

poetry build

pip install --editable .
