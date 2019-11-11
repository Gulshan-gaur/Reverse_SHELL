# Reverse_SHELL
## Reverse shell program based on socket programming on python 

This is a multi-client, multi-threaded reverse shell written in Python. There is still a lot of work to do, so feel free to help out with development.

Disclaimer: This reverse shell should only be used in the lawful, remote administration of authorized systems. Accessing a computer network without authorization or permission is illegal.

## How to Use
To use this reverse shell, two scripts need to be running

* **server.py** - runs on a public server and waits for clients to connect
* **client.py** - connects to a remote server and then wait for commands

***
To set up server script, simply run **server.py** using Python 3.6

`python3 server.py`

You will then enter an interactive prompt where you are able to view connected clients, select a specific client, and send commands to that client remotely.
## Client

In **client.py**, first change the IP address to that of the server and then run on target machine.
`python client.py `

![IMAGE](https://github.com/Gulshan-gaur/Reverse_SHELL/blob/master/images/Screenshot%20from%202019-11-07%2008-57-41.png)
