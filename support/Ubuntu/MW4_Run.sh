#!/bin/bash
cd $(dirname "$0")
source ./venv/bin/activate
python ./venv/lib/python3.7/site-packages/mw4/loader.py
deactivate
