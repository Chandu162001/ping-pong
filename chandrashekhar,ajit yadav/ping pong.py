import pygame,sys,random

def ball_animation():
	global ball_speed_x,ball_speed_y
	ball.x +=ball_speed_x
	ball.y +=ball_speed_y

	if ball.top <= 0 or ball.bottom >=screen_height:
		ball_speed_y *= -1
	if ball.left <=0 or ball.right >= screen_width:
		ball_restart()
	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1

def player_animation():
	player.y += player_speed
	if player.top <= 0:
		player.top = 0
	if player.bottom >=screen_height:
		player.bottom = screen_height

def opponent_animation():
	if opponent.top < ball.y:
		opponent.top += opponent_speed
	if opponent.bottom > ball.y:
		opponent.bottom -= opponent_speed
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >=screen_height:
		opponent.bottom = screen_height

def ball_restart():
	global ball_speed_y,ball_speed_x
	ball.center = (screen_width / 2, screen_height / 2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))

class Score():
	def __init__(self):
		self.score1= 0
		self.score2= 0
		self.score_font =pygame.font.SysFont(None,100)
		self.win_font=pygame.font.SysFont(None,70)
		self.player1_win=self.win_font.render("PLAYER 1 WINS",True,color_white,light_grey)
		self.player2_win=self.win_font.render("PLAYER 2 WINS",True,color_white,light_grey)
		
	def update(self):
		#if a player scores#'
		if ball.right < 0:
			self.score2 += 1
			ball_animation()
		if ball.left > screen_width:
			self.score1 += 1
			ball_animation()
		self.player1_score = self.score_font.render(str(self.score1),True,color_white,light_grey)
		self.player2_score = self.score_font.render(str(self.score2),True,color_white,light_grey)

	def draw(self):
		screen.blit(self.player1_score,(screen_width / 4,screen_height / 8))
		screen.blit(self.player2_score,(screen_width *3  / 4,screen_height / 8))
		if self.score1 == 5:
			screen.blit(self.player1_win,(55,screen_height /4))
			ball_restart()
		if self.score2 == 5:
			screen.blit(self.player2_win,(55,screen_height /4))
			ball_restart()


#General Setup
pygame.init()
clock=pygame.time.Clock()

#Setting up the main window
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('pong')

#Game Rectangles
ball=pygame.Rect(screen_width / 2 - 15,screen_height / 2 - 30,15,15)
player=pygame.Rect(screen_width  - 20,screen_height / 2 - 50,7,120)
opponent=pygame.Rect(10,screen_height / 2 - 50,7,120)

bg_color=pygame.Color('grey12')
light_grey=(200,200,200)
color_white = (255,255,255)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

while True:
	#Handling event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				player_speed += 7
			if event.key == pygame.K_UP:
				player_speed -= 7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				player_speed -= 7
			if event.key == pygame.K_UP:
				player_speed += 7

	#----score----#
	score=Score()
	score.__init__()

	ball_animation()
	player_animation()
	opponent_animation()
	score.update()
	score.draw()

	#visuals
	screen.fill(bg_color)
	pygame.draw.rect(screen,light_grey,player)
	pygame.draw.rect(screen,light_grey,opponent)
	pygame.draw.ellipse(screen,light_grey,ball)
	pygame.draw.aaline(screen,light_grey,(screen_width / 2,0),(screen_width / 2,screen_height))
	pygame.draw.circle(screen,light_grey,(screen_width // 2,screen_height // 2),80,1)

	#Updating the window
	pygame.display.flip()
	clock.tick(60)