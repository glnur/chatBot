import socket               # Import socket module

index = "seq2seq.ckpt-test-index"
data = "seq2seq.ckpt-test.data-00000-of-00001"
meta = "seq2seq.ckpt-test.meta"
workFiles = ["vocab20000.enc", "vocab20000.dec", "checkpoint", index, data, meta]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8184                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
while True:
    s.listen(5)                 # Now wait for client connection.
    c, addr = s.accept()     # Establish connection with client.
    for file in workFiles:
        while True:
            f = open(file, 'wb')
            print 'Got connection from', addr
            print "Receiving..."
            l = c.recv(1024)  # this receives 13 bytes which is corrupting the data
            l = c.recv(1024)
            while (l):
                f.write(l)
                l = c.recv(1024)
            f.close()
    print "Done Receiving"
    c.send('Thank you for connecting')
    c.close()                # Close the connection