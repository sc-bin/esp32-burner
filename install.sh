#!/bin/bash

# 获取当前脚本所在的实际路径
script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

cp $script_dir/boot-start/* /boot/start/
