#!/bin/bash
g++ -O3 -std=c++17 ../../../src/updater/updater_backend.cpp -o updater_backend -lcurl

if [ $? -eq 0 ]; then
    echo "Compilation successful: updater_backend"
else
    echo "Compilation failed: updater_backend"
    exit 1
fi
