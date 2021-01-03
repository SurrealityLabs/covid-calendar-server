#!/bin/sh
python-lambda-local -f lambda_handler -l . lambda-function.py event.json
