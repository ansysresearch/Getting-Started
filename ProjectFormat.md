# Github Code Organization

We will commonly use github to share/store our projects. The following format provides a guideline on how to organize your machine learning projects. Depending on the specific feature of your project, you may need additional files/folders, but please follow this format as much as possible.

- `data/`: traning data, only if data is small. This folder should be in `.gitignore` file, if training data is large.
- `outputs/`: all predictions, logs, checkpoints. Most files in this folder are included in `.gitignore` file.
- `docs/`: documentation, architectural diagram
- `src/`:
    - `models/`: tensorflow or pytorch models
        - `__init__.py` : file to make it a package
        - `data.py`: necessary code to preprocess, postprocess data. Use high-level APIs, such as `tf.data` or `torch.utils.data`
        - `util.py`: any additional utility functions used elsewhere.
        - `losses.py`
        - `metrics.py`
    - `__init__.py`
    - `train.py`
    - `inference.py/test.py`
- `main.py`: script for training or testing with defined components like `download_data`, `download_pretrained_models`, `process_data`, `train`, `inference`, etc.
- `setup.py`: in case of a python package.
- `license.txt`
- `readme.md`
- `requirement.txt`: necessary libraries for reproducing the code.
`training_logs`: for reproducing top 3 best trained models.
