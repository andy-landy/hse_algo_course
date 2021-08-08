#!/bin/bash
source /docker/bashrc_patch

# EDIT THIS IF NEEDED
(
    cd /problem
    python3 ./main.py $@
)
