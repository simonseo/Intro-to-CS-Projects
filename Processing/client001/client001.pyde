add_library('net')

client = None
txt = ''

def setup():
    global client
    client = Client(this, '192.168.1.100', 40001)
    textSize(10)
    size(800, 600)
    

def draw():
    global txt, client
    background(0)
    text('asdf', 50, 50)
    text(txt, 50, 50)
    if client.available() > 0:
        txt += client.readChar()
    