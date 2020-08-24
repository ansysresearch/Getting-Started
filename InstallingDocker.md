# Docker Setup

## What is Docker and why use it?
Docker is a lightweight, open source, secure platform for building, shipping and running applications. It enables us to ship software
using containers for code and binaries accross environments. A container is a unit of software that packages up code and all its
dependencies so the application can run smoothly accross computing environments. Docker runs natively on Windows Server and Linux. 
On Windows and Mac it can be run via a virtual machine. In short Docker is a virtual machine without the overheads of a virtual machine. 

Using Docker will allow us to ship code faster and accelerate developer onboaring. For example, developers can write code 
locally and sharetheir work with each other through Docker containers. It will prevent application and version conflicts caused
by mismatches of the framework, so we will be able to develop, stage and produce on different environments. 
A more comprehensive overview can be found on the 
[Docker website](https://docs.docker.com/get-started/overview/#:~:text=The%20Docker%20client%20(%20docker%20)%20is,with%20more%20than%20one%20daemon).

### Docker Engine
A Docker Engine is a client-server application with:
* a server: daemon process (the `dockerd` commmand)
* a REST API which specifies interfaces that programs can use to talk to the daemon
* a command line interface client (the `docker` command). This is the primary way many users interact with Docker.

The command line interface uses the Docker REST API to interact with the Docker daemon through scripting or direct 
CLI commands. The daemon creates and manages Docker objects. The Docker client and daemon can either run on the same system 
or you can connect a Docker client to a remote Docker daemon.

### Docker objects
The main components of Docker are **containers** and **images**.

#### Images
An image is a read-only template with instructions to create a Docker container, it is the Blueprint ot get a running container.
Images are stored in a Docker registry like [Docker Hub](https://hub.docker.com/). Docker Hub is a public registry that anyone 
can use. Alternatively you might create your own images, with a *Dockerfile*. You can also download Dockerfiles from DockerHub and modify 
them. For example, [tensorflow:latest-gpu-py3-jupyter](https://hub.docker.com/layers/tensorflow/tensorflow/latest-gpu-py3-jupyter/images/sha256-901b827b19d14aa0dd79ebbd45f410ee9dbfa209f6a4db71041b5b8ae144fea5?context=explore) can be used as a base container for our machine learning projects.
#### Containers
A container is a runnable instance of an image. You can create, start, stop, move or delete a container with the Docker API or 
command line interface. A container can be connected to one or more networks and can have storage attached to it. A container is
defined by its image and configuration options you provide when you create or start is. The container can be for different kind 
of shipments of the software: Development, Staging or Production.

## Installation 
Docker has to be installed on your local computer where you will be developing code.
### Windows
To install Docker for Windows please follow the instructions listed [here](https://docs.docker.com/docker-for-windows/install/). 
Use Linux containers in the install. 

After the installation, you open a command line terminal like PowerShell to check the version:
```
> docker --version
```

Next you can test the Docker installation with an existing image:
1. To test the installation run the `hello-world` Docker image from the terminal run
	```
	docker run hello-world
	```
	This may prompt Docker to pull from library/hello-world. If the installation is successful you will then see the message `Hello from Docker!`.
1. To list the `hello-world` image run 
	```
	docker image ls
	```
1. To list the `hello-world` container run 
	```docker ps --all```. 
	If the container is still running, you do not need the --all 
	option. 


## Quick Tutorial
A more comprehensive tutorial can be found [here](https://docs.docker.com/get-started/part2/). We will now show you how 
to **build** and **run** individual containers with an example project given in the Docker tutorial. If you have experience creating containers in Docker feel free to skip this. 
feel free to skip this. 
First clone the project from Github:
```
git clone https://github.com/dockersamples/node-bulletin-board
cd .\node-bulletin-board\bulletin-board-app
```
After Downloading the project open the Dockerfile
```
notepad Dockerfile
```
You will find the following lines:
```
# Use the official image as a parent image.
FROM node:current-slim

# Set the working directory.
WORKDIR /usr/src/app

# Copy the file from your host to your current location.
COPY package.json .

# Run the command inside your image filesystem.
RUN npm install

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8080

# Run the specified command within the container.
CMD [ "npm", "start" ]

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .
```

To **build** your image from the ```node-bulletin-board\bulletin-board-app``` run the following
command to build an image:
```
docker build --tag bulletinboard:1.0 .
```
if the build is successful the process should end with the message ```Successfully tagged bulletinboard:1.0```. 

To **run** the image as a container, run:
```
docker run --publish 8000:8080 --detach --name bb bulletinboard:1.0
```
* The ```--publish``` flag asks Docker to forward traffic inocming on the hosts port to the container's port. 
* The ```--detach``` flag asks Docker to run the container in the background.
* The ```---name``` flag specifies a name that you can refer your container to. 

To see your application running you can visit it in a browser at ```localhost:8000```. After verifying that 
the container works correctly you can **delete** it with:
```
docker rm --force bb
```

Now you know how to build and run a Docker container!

### More example commands
* To build a container:
	```
	docker build --rm PATH -f FILE -t NAME:TAG
	```
	* The `--rm` flag removes the old image with the same name and creates a new one. 
	* The `-f` flag specifies the path to the Dockerfile. 
	* The `-t` flag specifies the name for the tag of the built image. 
* To run a container:
	```
	docker run -rm -d -p HOST_PORT:CONTAINER_PORT IMAGE COMMAND
	```
* To run a container to poke around:
	```
	docker run  -it --rm IMAGE COMMAND
	```
	This will start a container, drop it into a shell and destroy the container after you exit. 
	
	* The ```-it``` flag runs Doker interactively. 
	* The ``-rm``` flag asks Docker to automatically remove the container upon exit.
* To run a container in the background:
	```
	docker run -d -p 8888:6000 tensorflow/tensorflow:latest-gpu-py3jupyterdocker
	```
* To run a container and keep it running for an interactive session
	```
	docker run -it -p 8888:6000 tensorflow/tensorlfow:latest-gpu-py3-jupyter
	```
	
* To clean up any dangling resources:
	```
	docker system prune 
	```
	Optionally you can add the ```-a``` flag to remove any stopped containers and all unused images. 

* Other important *container* commands:
	```
	docker ps -a		# shows all containers running or not
	docker stop CONTAINERID		# stops a running container using its ID
	docker container ls		# lists all running containers
	docker container kill CONTAINER		# force stops a running container
	docker container rm CONTAINER		# removes a container
	docker inspect CONTAINER		# shows detailed info about running container
	```
* Other important *image* commands:
	```
	docker image ls		# lists all locally available images
	docker image rm	IMAGE	# removes an image
	docker image prune		# removes dangling images
	docker image prune -a		# removes all images
	docker image tage IMAGE IMAGE 	# tages an image from one image id or tag to a new tag e.g my-app:latest to my-app:1.0.0	```	

