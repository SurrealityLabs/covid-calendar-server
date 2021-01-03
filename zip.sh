#!/bin/sh
zip -r9 ../lambda.zip * -x "bin/*" requirements.txt "*.sh" event.json "exec/*" caltest.py
