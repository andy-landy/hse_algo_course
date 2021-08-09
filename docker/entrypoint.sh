#!/bin/bash
source /docker/bashrc_patch

# EDIT THIS IF NEEDED
(
    cd /py_code/problem
    python3 ./main.py $@
    cat /shared/feedback.json
)
