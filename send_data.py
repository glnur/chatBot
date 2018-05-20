url = 'https://billythemessenger.tk'
import os
import string
import socket               # Import socket module

os.chdir(r'./working_dir/')

f = open('checkpoint', 'r')
neededFile = []

for line in f:
    neededFile = line.split('"')
    break
number = neededFile[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = "5.101.179.23" # Get local machine name
port = 8184                 # Reserve a port for your service.

index = "seq2seq.ckpt-" + number + "index"
data = "seq2seq.ckpt-" + number + ".data-00000-of-00001"
meta = "seq2seq.ckpt-" + number + ".meta"
workFiles = ["vocab20000.enc", "vocab20000.dec", "checkpoint", index, data, meta]
s.connect((host, port))
for file in workFiles:
    f = open(file,'rb')
    print 'Starting sending'
    l = f.read(1024)
    while (l):
        print 'Sending...'
        s.send(l)
        l = f.read(1024)
    f.close()
    print "Done Sending"
    print s.recv(1024)
s.shutdown(socket.SHUT_WR)
s.close()                     # Close the socket when done