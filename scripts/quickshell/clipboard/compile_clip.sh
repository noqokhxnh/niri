#!/bin/bash
g++ -O3 -std=c++17 clip_fetcher.cpp -o clip_fetcher -lpthread
if [ $? -eq 0 ]; then
    echo "Compilation successful: clip_fetcher"
else
    echo "Compilation failed"
    exit 1
fi
