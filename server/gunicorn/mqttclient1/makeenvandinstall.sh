#!/bin/bash
python3 -m venv env $1
source $1/bin/activate
$1/bin/pip install -r requirements.txt
