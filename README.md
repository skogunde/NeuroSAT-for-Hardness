# About This Fork

This repo is forked from NeuroSAT by Selsam et al. For more information on NeuroSAT, please visit: https://github.com/dselsam/neurosat/

## Playing with NeuroSAT

The `scripts/` directory includes a few scripts to get started.
1. `sh scripts/setup.sh` installs dependencies.
2. `sh scripts/toy_gen_data.sh` generates toy train and test data.
3. `sh scripts/toy_train.sh` trains a model for a few iterations on the toy training data.
4. `sh scripts/toy_test.sh` evaluates the trained model on the toy test data.
5. `sh scripts/toy_solve.sh` tries to solve the toy test problems.
6. `sh scripts/toy_pipeline.sh` runs `toy_gen_data.sh`, `toy_train.sh`, `toy_test.sh`, and `toy_solve.sh` in sequence.

Note that you will need python 3.6 (or 3.4, 3.5) in order to install tensorflow 1.4.0