#!/usr/bin/env bash

cd "$(dirname "$0")"

eval $(cat .envrc)
COMMAND=$1

python send.py $1 > send.log 2>&1