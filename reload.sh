#!/bin/bash
if [ -f pid ]; then
  kill $(cat pid)
fi

source ./.env/bin/activate

pip install -r requirements.txt
python3 ./src/main.py &
PID=$!

echo $PID > pid
