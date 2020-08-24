# Working on the DGX machine

Part of our compute resources include an [Nvidia DGX machine](https://www.nvidia.com/en-us/data-center/dgx-station/). In this 
document we will go over connecting to the DGX machine so that you can train and deploy your neural networks on this 
powerful machine.

## Prerequisites
For security purposes accessing the DGX machine requires a VPN connection to one of our servers. Please contact IT if you
do not have your VPN connection from your ANSYS laptop set up yet. 

## Logging in
We can connect to the DGX station through ssh. You can ask your supervisor for the password if you do not know it yet.
```
ssh ansysai@cdcdgx1
```

You may find it useful to connect with the following useful flags:
```
ssh -N -f -L localhost:9000:localhost:8888 ansysai@cdcdgx1
```
* The `-N` flags specifies that no remote commands will be executed and is useful for port forwarding.
* The `-f` flag will send the ssh process to the background so that local tunnel-enabling terminal remains usable.
* The `-L` flag specifies the port forwarding configureation (remote port 90000 to local port 8888). 

## Set up your workspace
Once you have logged in please make a directory in the home directory named after your ANSYS username. 
