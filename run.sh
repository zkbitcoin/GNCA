#!/bin/bash

# ln -s libnvinfer.so.10 libnvinfer.so.8.6.1
# ln -s libnvinfer_plugin.so.10 libnvinfer_plugin.so.8.6.1

export TF_CPP_MAX_VLOG_LEVEL=0

export LD_LIBRARY_PATH=~/miniconda3/envs/tf/lib/python3.10/site-packages/tensorrt_libs

export PYTHONPATH=.

python voronoi/run_voronoi.py
python voronoi/run_voronoi_entropy.py
python voronoi/run_entropy_v_th.py

python boids/run_boids.py --epochs 1
python boids/run_boids.py --epochs 1 --test_complexity_every 10
python boids/evaluate_boids.py

python voronoi/run_learn_exact_mlp.py

python fixed_target/run_fixed_target.py --epochs 1 # By default, t=10

python fixed_target/run_fixed_target.py --epochs 1--min_steps 10 --max_steps 21  # t \in [10, 20]

python fixed_target/make_plots.py --path results/Grid2d  # Replace with target folder for each graph
