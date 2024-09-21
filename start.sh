#!/bin/bash

git checkout poetry.lock ; git pull ; poetry update ; poetry run python3 start.py
