#!/bin/bash

esp32_burner_path="/boot/start/esp32-burner"

export DISPLAY=:0
while true; do
    if xdpyinfo > /dev/null ; then
        break
    fi
    sleep 1
done

# 开始执行
while true; do
    cd $esp32_burner_path
    python main.py
    sleep 1
done