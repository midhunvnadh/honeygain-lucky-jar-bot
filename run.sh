#!/bin/bash

run_once() {
    echo $TOKEN > auth.txt
    pip3 install -r requirements.txt
    python3 main.py --once --threads=2000
}

run_once