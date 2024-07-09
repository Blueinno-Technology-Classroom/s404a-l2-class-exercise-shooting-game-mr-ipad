import pgzrun
import random

# define window size
WIDTH=2000
HEIGHT=1000


#targets initialize
target1=Actor("target_red1")
target1.x=WIDTH/2
target1.y=HEIGHT/2

target2=Actor("duck_target_yellow")
target2.right=WIDTH
target2.bottom=HEIGHT

target3=Actor("duck_target_white")
target3.right=0
target3.bottom=300

cursor=Actor("crosshair_outline_large")

rifle=Actor("rifle")

score=0

def update():
    target1.x += random.randint(1,5)
    target2.x += random.randint(1,5)
    target3.x += random.randint(1,5)
#    target1.y += random.randint(-5,5)
#    target2.y += random.randint(-5,5)
#    target3.y += random.randint(-5,5)
    if target1.left>=WIDTH:
        target1.right=0
    if target2.left>=WIDTH:
        target2.right=0
    if target3.left>=WIDTH:
        target3.right=0
    if target1.top<=0:
        target1.botton=HEIGHT
    elif target1.bottom>=HEIGHT:
        target1.top=0
    if target2.top<=0:
        target2.botton=HEIGHT
    elif target2.bottom>=HEIGHT:
        target2.top=0
    if target3.top<=0:
        target3.botton=HEIGHT
    elif target3.bottom>=HEIGHT:
        target3.top=0


def on_mouse_move(pos):
    cursor.pos=pos
    rifle.top=pos[1]
    rifle.left=pos[0]

def on_mouse_down(pos):
    global score
    if cursor.colliderect(target1):
        target1.right=0
        target1.y=random.randint(0,HEIGHT)
        score+=10
    elif cursor.colliderect(target2):
        target2.right=0
        target2.y=random.randint(0,HEIGHT)
        score-=5
    elif cursor.colliderect(target3):
        target3.right=0
        target3.y=random.randint(0,HEIGHT)
        score-=5


#draw the actors
def draw():
    screen.clear()
    target1.draw()
    target2.draw()
    target3.draw()
    #cursor.draw()
    rifle.draw()
    screen.draw.text(str(score), (10,10),fontsize=72)

#to start
pgzrun.go()