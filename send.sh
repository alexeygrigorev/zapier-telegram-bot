#!/usr/bin/env bash

cd "$(dirname "$0")"

eval $(cat .envrc)
COMMAND=$1

if [ -f "extras.sh" ]; then
    eval $(cat extras.sh)
fi

python send.py $1 > send.log 2>&1