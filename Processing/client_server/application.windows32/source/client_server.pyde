add_library('net')

server = None
client = None
sendtxt = ''
gettxt = 'get\n'

def setup():
    global server, client #takes the global variable 'server' instead of using a local variable
    server = Server(this, 40001)
    client = Client(this, '192.168.1.100', 40001)
    textSize(10)
    size(800, 600)
    

def draw():
    background(0)
    global sendtxt, gettxt, client
    text('send\n'+sendtxt, 50, 60)
    if client.available() > 0:
        gettxt += client.readChar()
    text(gettxt, 400, 60)
    
def keyPressed():
    global sendtxt, server
    if type(key) != int and key.isalpha() or key == ' ':
        sendtxt += key
    elif keyCode == 10:
        server.write(sendtxt+'\n')
        print(sendtxt)
        sendtxt = ''
        