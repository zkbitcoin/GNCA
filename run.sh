#!/bin/bash

# ln -s libnvinfer.so.10 libnvinfer.so.8.6.1
# ln -s libnvinfer_plugin.so.10 libnvinfer_plugin.so.8.6.1

export TF_CPP_MAX_VLOG_LEVEL=0

export LD_LIBRARY_PATH=~/miniconda3/envs/tf/lib/python3.10/site-packages/tensorrt_libs

export PYTHONPATH=.

python boids/run_boids.py
