# Getting-Started

This repository contains instructions to get started with Ansys Machine Learning and is intended to guide you through the workflow and common practices we encourage at Ansys. In the following sections, you can find instructions on how to prepare code in python, how to setup virtual environments or Docker containers and how to organize github repository.

### Code Development in Python
A significant portion of machine learning development at Ansys takes place in Python.
1. In order to install Python, follow the instruction given at [Install Python](InstallingPython.md).
2. You can use any IDE you prefer. Most developers use [PyCharm](https://www.jetbrains.com/pycharm/download) which provides user-friendly interface for code preparation and debugging.
3. We strongly encourage you to use [virtual environments](VirtualEnv.md) or [Docker containers](InstallingDocker.md) to compartmentalize your libraries/projects.
4. When you develop your code, please follow the [PEP 8 coding style](PythonCodeStyle.md).
5. Another consideration is writing unittests. Unittest can help tremendously when multiple developers contribute to a single project. When a new developer adds new feature to an existing, they will run the exisiting unittest to ensure they have not broken any of the already implemented features. Then, they write additional unittests for the newly added features. A fairly popular way of writing unittest is to use the `unittest` library which is package with python. A light introduction is provided in [unittest](unittest.md).

### Code Development in C++
TBA

### Version Control
Version control is an essential part of any software engineering project.
1. At Ansys we use Git for version control. A short instruction on how to install and use Git for project development can be found at [Git](Git.md).
2. To share your code with others, interns can use our [Ansys Research Github](https://github.com/ansysresearch).
3. We strongly encourage you to follow the common [project format](ProjectFormat.md) for your machine learning projects.

### Additional resources
(TO BE COMPLETED)
- If you're using Pytorch, have a look at [Pytorch guidelines](Pytorch.md)

- If you're using Tensorflow, have a look at [Tensorflow guidelines](Pytorch.md)

- If you're interested to see if you can run your code faster, have a look at [faster code guidelines](Parallel.md)
