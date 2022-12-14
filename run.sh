#!/bin/bash

run_once() {
    echo $TOKEN > auth.txt
    pip3 install -r requirements.txt
    python3 honeygain-bot.py
}

run_once