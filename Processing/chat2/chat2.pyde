add_library('net')
import os

server = None
client = None
sendtxt = ''
gettxt = 'get\n'
move = 0

def setup():
    global server, client #takes the global variable 'server' instead of using a local variable
    server = Server(this, 40002)
    client = Client(this, '192.168.1.100', 40001)

    while not client.active():
        #os.sleep(1)
        client = Client(this, '192.168.1.100', 40001)
    textSize(10)
    size(800, 600)
    

def draw():
    background(0)
    global sendtxt, gettxt, client
    text('send\n'+sendtxt, 50, 60)
    if client.available() > 0:
        gettxt += client.readChar()
    text(gettxt, 400, 60 - move)
    
def keyPressed():
    global sendtxt, server, move
    if type(key) != int and key.isalpha() or key == ' ':
        sendtxt += key
    elif key == BACKSPACE:
        sendtxt.pop()
    elif key == ENTER or key == RETURN:
        server.write(sendtxt+'\n')
        print(sendtxt)
        sendtxt = ''
    elif keyCode == UP:
        move += 10
    elif keyCode == DOWN:
        move -= 10
        