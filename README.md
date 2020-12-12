# About This Fork

This repo is forked from NeuroSAT by Selsam et al. For more information on NeuroSAT, please visit: https://github.com/dselsam/neurosat/

## Using this Code

Similar to the main neuroSAT repo, the `scripts/` directory includes all the necessary scripts to get started.
1. Run `sh scripts/setup.sh` to install dependencies. Note that you need python version to be in range [3.3, 3.6] in order to install tensorflow 1.4.0. Its best to use python 3.6.
2. Run `sh scripts/toy_gen_data.sh` to generate toy train and test data.
3. Run `python3 python/normalize_data.py` to normalize the labels (times) to be in range [0,1]. Note that the file names for train/test data are currently hardcoded here and need to be modified based on the file names generated in the previous step. This needs to be updated later to take in file names as an arguement.
3. Run `sh scripts/toy_train.sh` to train a model for a few iterations on the toy training data.
4. Run `sh scripts/toy_test.sh` to evaluate the trained model on the toy test data.
5. Run `sh scripts/toy_solve.sh` to (try to) solve the toy test problems.
6. Run `sh scripts/toy_pipeline.sh` to run `toy_gen_data.sh`, `toy_train.sh`, `toy_test.sh`, and `toy_solve.sh` in sequence. Do not use this for now, since labels are not automatically normalized yet.
