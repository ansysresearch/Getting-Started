# Getting-Started

This repository contains instructions to get started with ANSYS Machine Learning. It is intended to set up and guide
you through the workflow.
Typically, we use Docker containers or virtual environments to transport our code accross platforms from our local machines to our more computationally powerful remote machines.

The Machine Learning group workflow will typically consist of the following steps:
1. Develop on your local computer.
1. Build and run your code in a Docker container (more info below) or vm.
1. Transfer the contents to ANSYS Machine Learning's remote DGX machine or your own remote machine.
1. Build and run the container on a linux machine. 
1. Connect to DGX and run the container on DGX.

## Configuring your ANSYS laptop
To get started follow the steps below:
1. [Install Python](InstallingPython.md)
  1. Install Git (optional)
  1. Install your IDE of choice (I like Pycharm).
1. [Install Docker](InstallingDocker.md)

## Using the DGX machine
1. [Accessing the DGX machine](DGX Station)
1. Demo on DGX using SimNet
1. Starting your own ML Project


