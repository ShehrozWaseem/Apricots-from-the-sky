import turtle
import random
score=0
lives=3

wn = turtle.Screen()
wn.title("Eat them all")
wn.bgcolor("green")
wn.bgpic("bg.gif")

wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("deer.gif")
wn.register_shape("obj.gif")
wn.register_shape("obj2.gif")
wn.register_shape("deer2.gif")
wn.register_shape("bg.gif")

player=turtle.Turtle()
player.speed(0)
player.shape("deer.gif")
player.color("white")
player.penup()
player.goto(0,-250)
player.direction = "rest"

objects=[]

for i in range(10):
    obj=turtle.Turtle()
    obj.speed(0)
    obj.shape("obj.gif")
    obj.color("blue")
    obj.penup()
    obj.goto(100,250)
    obj.speed = random.randint(1,2)
    objects.append(obj)
    
objects2=[]
for k in range(7):
    obj2=turtle.Turtle()
    obj2.speed(0)
    obj2.shape("obj2.gif")
    obj2.color("red")
    obj2.penup()
    obj2.goto(-100,250)
    obj2.speed = random.randint(1,1)
    objects2.append(obj2)

write=turtle.Turtle()
write.hideturtle()
write.speed(0)
write.shape("square")
write.color("black")
write.penup()
write.goto(0,260)
font=("Courier",24,"bold")
write.write("Score: {} Lives: {}".format(score, lives),align="center", font=font)

write1=turtle.Turtle()
write1.hideturtle()
write1.speed(0)
write1.shape("square")
write1.color("black")
write1.penup()
write1.goto(400,290)
font1=("Courier",24,"bold")
write1.write("GAME OVER",align="center", font=font)



def go_left():
    player.direction = "left"
    wn.register_shape("deer2.gif")

def go_right():
    player.direction = "right"
    wn.register_shape("deer.gif")


wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()

    if player.direction == "left":
        x= player.xcor()
        x -=1
        player.setx(x)

    if player.direction == "right":
        x= player.xcor()
        x +=1
        player.setx(x)

    for obj in objects:
        
        y=obj.ycor()
        y -=obj.speed
        obj.sety(y)
        #obj.sety(obj.ycor()-3)

          
        if y < -300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            obj.goto(x,y)

        if obj.distance(player) <40:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            obj.goto(x,y)
            score+=10
            write.clear()
            #print("Score: {} Lives: {}".format(score, lives))
            write.write("Score: {} Lives: {}".format(score, lives),align="center", font=font)

            
    for obj2 in objects2:
        
        y=obj2.ycor()
        y -=obj2.speed
        obj2.sety(y)
        #obj.sety(obj.ycor()-3)

          
        if y < -300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            obj2.goto(x,y)

        if obj2.distance(player) <40:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            obj2.goto(x,y)
            score-=10
            lives -= 1
            write.clear()
            write.write("Score: {} Lives: {}".format(score, lives),align="center", font=font)
        if lives==0:
            write1.write("GAME OVER",align="center", font=font)

wn.mainloop()
