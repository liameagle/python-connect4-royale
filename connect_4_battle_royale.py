import turtle
from random import shuffle

column_values = {1:[0,0,0,0,0,0],2:[0,0,0,0,0,0],3:[0,0,0,0,0,0],4:[0,0,0,0,0,0],5:[0,0,0,0,0,0],6:[0,0,0,0,0,0],7:[0,0,0,0,0,0]}

window = turtle.Screen()
window.bgcolor("black")
window.setup(700,600)

window.title("Connect 4")
while True:
	try:
		player_count = window.textinput("Question", "How many players do you have?")
		player_count = int(player_count)
	except (ValueError, TypeError):
		pass
	else:
		if player_count > 1 and player_count < 6:
			colour_order=["'yellow'","'red'","'orange'","'green'","'purple'"]
			shuffle(colour_order)
			for i in range(player_count):
				exec("""player{} = turtle.Turtle()
player{}.hideturtle()
player{}.pencolor({})""".format(i+1,i+1,i+1,colour_order[i]))
			break

board = turtle.Turtle()
board.hideturtle()
board.pencolor("blue")
board.speed(1000)
board.penup()
board.pensize(10)
board.goto(-350,-300)
board.pendown()
board.left(90)
board.forward(600)
board.right(90)
board.forward(700)
board.right(90)
board.forward(600)
board.right(90)
board.forward(700)
board.right(180)
for i in range(3):
	#bottom row
	board.forward(100)
	board.left(90)
	board.forward(600)
	#reached top row
	board.right(90)
	board.forward(100)
	board.right(90)
	board.forward(600)
	#reached bottom
	board.left(90)
board.forward(100)

for i in range(3):
	board.left(90)
	board.forward(100)
	board.left(90)
	board.forward(700)
	board.right(90)
	board.forward(100)
	board.right(90)
	board.forward(700)

def check_column(column_num):
	"""0 = air	the rest of the numbers correspond to each player.
	takes column number and checks how many counters are in it, then returns what y ordinate to render at"""
	global column_values
	return(((column_values.get(column_num).index(0)+1) * 100)- 349)


def add_to_column(column_num, turn):
	global column_values
	#print("ADD TO COLUMN",column_values)
	print("COLUMN NUM", int(column_num))
	print("PLAYER", turn)
	y_num = column_values.get(int(column_num)).index(0)
	# =1 means only player 1
	column_values.get(int(column_num))[y_num] = turn
	print("PRINT CURRENT COLUMN",column_values.get(int(column_num)))


def draw_piece(player, desired_col, turn):
	player.penup()
	ypos = check_column(int(desired_col))
	player.goto(((int(desired_col)*100)-400), ypos)
	add_to_column(desired_col, turn)
	player.pendown()
	player.dot(75)

def check_connect_4():
	global column_values
	global player_count

turn = 0
def init_turn(x):
	global player_count
	global turn
	turts=[]
	for i in range(player_count):
		exec("""turts.append(player{})""".format(i+1))
		print("FUNC: INIT_TURN, TURN",i)
	if turn < player_count:
		draw_piece(turts[turn], x, turn+1)
	else:
		turn = 0
		draw_piece(turts[turn], x, 1)
	turn+=1
	check_connect_4()


def screenclick(x,y):
	x_col = (x+450)//100

	init_turn(x_col)

window.onscreenclick(screenclick)
window.mainloop()