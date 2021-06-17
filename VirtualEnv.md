# Virtual Environments

The main purpose of Python virtual environments is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has. At Ansys we generally use `conda` environemtns.
You can read more about virtual environment [here](https://realpython.com/python-virtual-environments-a-primer/).

To install `Miniconda`, please refer to [Install Python](InstallingPython.md) instruction. After installation, in Windows you will have a Anaconda or Miniconda terminal where you can enter command lines. In Linux, you can directly use conda in the terminal. The following commands are regularly used:
- `conda create -N SDF_Project python=3.7` creates a new conda environment with name `SDF_Project` and python `3.7`.
- `conda activate SDF_Project` activates the environment.
- `conda deactivate SDF_Project` deactivates the environment.
- `conda env remove --n SDF_Project` deletes the environment.
- `conda env list` prints a list of available environments.
You can find other conda commands [here](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
To install a new library, you can use `pip` or `conda`. It is highly recommended to use a `pip`-only/ `conda`-only approach, meaning that you want  to use one of these methods to install your needed libraries.
