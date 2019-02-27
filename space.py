import turtle
import os
import math
import random 

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)

border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#coose number of enemies 
number_of_enemies = 5
#create an empty list of enemies
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
	#create the enemy
	enemies.append(turtle.Turtle())

#create enemy 
for enemy in enemies:
	
	enemy.color("red")
	enemy.shape("circle")
	enemy.penup()
	enemy.speed(-100)
	x= random.randint(-200,200)
	y = random.randint(100,250)
	enemy.setposition(x,y)

enemyspeed = 2

#create player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready-fire
#fire-bullet is firing 

bulletstate = "ready"

def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x= -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	#make bulletstate as global
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()

	#move the bullet to the just above player 
	
def isCollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

#create keyborad bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet, "space")

#main game loop
while True:

	for enemy in enemies:
		#move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#move the enemy back and down
		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
				#change enemy direction
			enemyspeed *= -1

		if enemy.xcor() < -280:
			for e in enemies:
				y = enemy.ycor()
				y -= 40
				enemy.sety(y)

			enemyspeed *= -1

		if isCollision(bullet,enemy):

		#Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0,-400)
			#reset the enemy
			x = random.randint(-200,200)
			y = random.randint(100,250)
			enemy.setposition(x,y)

		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("Game Over")
			break

		#move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"
	
	


turtle.done()