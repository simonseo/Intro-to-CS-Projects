add_library('net')

server = None
txt = ''

def setup():
    global server #takes the global variable 'server' instead of using a local variable
    server = Server(this, 40001)
    size(800, 600)
    

def draw():
    background(0, 0, 0)
    
    text(txt, 30, 30)
    
def keyPressed():
    global txt, server
    if type(key) != int and key.isalpha() or key == ' ':
        txt += key
    elif keyCode == 10:
        server.write(txt+'\n')
        print(txt)
        txt = ''
        