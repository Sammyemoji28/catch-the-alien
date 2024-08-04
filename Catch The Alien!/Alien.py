import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "Catch the Aliens!!"

message = ""

#creating characters! yay

bob = Actor("alien")
bob.pos = (182,374)

joe = Actor("alien3")
joe.pos = (126,294)

def draw():
    global message
    screen.clear()
    screen.fill(color = "blue")
    bob.draw()
    joe.draw()
    screen.draw.text(message,fontsize = 40,center = (250,100))

def placeBob():
    bob.x = random.randint(50,450)
    bob.y = random.randint(50,450)
    
def placeJoe():
    joe.x = random.randint(50,450)
    joe.y = random.randint(50,450)

def on_mouse_down(pos):
    global message
    if bob.collidepoint(pos):
        placeBob()
        message = "you hit bob!"

    if joe.collidepoint(pos):
        placeJoe()
        message = "you hit joe!"

        
placeBob()
placeJoe()
pgzrun.go()