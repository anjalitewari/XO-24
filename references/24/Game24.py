# System Imports
import sys, pygame, os
# Plugins and Utils
import pygbutton, TextureLoader
# Import Scenes
from SceneBasic import SceneBasic
from SceneMenu import SceneMenu
from SceneGame import SceneGame
#from SceneHelp import SceneHelp
#from SceneWin import SceneWin
# Initialize pygame
pygame.init()

class Game24(object):

	STATE_MENU	   = 0
	STATE_GAME	   = 1
	STATE_WIN_SCREEN = 2
	STATE_HELP	   = 3

	def __init__(self):
		# start the game with the MENU scene
		self.currentState = self.STATE_MENU


		# define the width and height of our display
		width = pygame.display.Info().current_w
		height = pygame.display.Info().current_h
		if(float(width)/float(height) == float(4)/float(3)):
			screenSize = (width,height)
		else:
			screenSize = (800,600)
		TextureLoader.screenSize =screenSize
		self.screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
		

		# define our scenes and game clock
		self.clock		= pygame.time.Clock()
		self.scnMenu	  = SceneMenu(screenSize, self.screen)
		#self.scnGame	  = SceneGame(screenSize,  self.screen)
		#self.scnWin	   = SceneWin(screenSize,  self.screen)
		#self.scnHelp	  = SceneHelp(screenSize,  self.screen)


		# Register application events for each scene
		# self.registerEvents(self.scnMenu,self.scnGame,self.scnWin,self.scnHelp)
		self.registerEvents(self.scnMenu)
		self.dicScenes = {
			self.STATE_MENU: self.scnMenu,
			#self.STATE_GAME: self.scnGame,
			#self.STATE_WIN_SCREEN: self.scnWin,
			#self.STATE_HELP:  self.scnHelp
		}
		self.main()
		
	#Create a display
	def display(self):
		pygame.display.set_caption('XO 24')		
		self.screenSize = (self.width, self.height) = (800, 600)
		self.screen	 = pygame.display.set_mode(self.screenSize)
		# define main screen buttons (oh god so sloppy)
		
		self.startBtn   = pygbutton.PygButton( (self.width/2-85, self.height/2+10, 170, 45), 'Start', bgcolor=(252,90,90), fgcolor=(255,255,255) )
		self.helpBtn	= pygbutton.PygButton( (self.width/2-85, self.height/2+70, 170, 45), 'Help',  bgcolor=(252,90,90), fgcolor=(255,255,255) )
		self.quitBtn	= pygbutton.PygButton( (self.width/2-85, self.height/2+130, 170, 45), 'Quit',  bgcolor=(255,90,90), fgcolor=(255,255,255) )
		


	#Update the display and show the menu buttons
	def update_display(self):
		pass
		# if self.currentState == self.STATE_MENU:
		#	 self.backgroundColor = 252,90,90
		#	 self.screen.fill(self.backgroundColor)
		#	 self.startBtn.draw(self.screen)
		#	 self.helpBtn.draw(self.screen)
		#	 self.quitBtn.draw(self.screen)
		#	 self.screen.blit(self.logo, (self.width/2-141, 100) )
		# if self.currentState == self.STATE_GAME: 
		#	 print("state is game!")
		# pygame.display.flip()
		
	# Main Game Loop
	def main(self):
		self.isRunning = True
		# threadRender = threading.Thread(target = self.loopRender);
		self.scnMenu.EVENT_SCENE_START()
		# threadRender.start();
		self.loopUpdate();
		# threadRender.join();		
		# self.display()
		# while True:
		#	 self.update_display()
		#	 for event in pygame.event.get():
		#		 if event.type == pygame.QUIT or 'click' in self.quitBtn.handleEvent(event):
		#			 pygame.quit()
		#			 sys.exit()
		#		 if self.currentState == self.STATE_MENU:
		#			 if 'click' in self.startBtn.handleEvent(event):
		#				 print("start btn clicked!")
		#				 self.currentState = self.STATE_GAME
		#			 if 'click' in self.helpBtn.handleEvent(event):
		#				 print("Help btn clicked!")
		#				 self.currentState = self.STATE_HELP
		#		 elif self.currentState == self.STATE_GAME:
		#			 print("todo: handle game state")
		#		 elif self.currentState == self.STATE_WIN_SCREEN:
		#			 print("todo: handle game win state")
		#		 elif self.currentState == self.STATE_HELP:
		#			 print("todo: handle help state")


	def loopUpdate(self):
		try :
			while self.isRunning:
				eventStack = pygame.event.get();
				for event in eventStack:
					if event.type == pygame.QUIT:
						self.EVENTHDR_QUIT()
						return
				self.dicScenes[self.currentState].listenForEvents(eventStack)
		except :
			print "CRITICAL ERROR : RESTARTING LOOP loopUpdate"
			#self.loopUpdate()
		self.isRunning = False
			
		
	def registerEvents(self, sceneMenu,sceneGame=None,sceneWin=None, sceneHelp=None):
		print "Register Events"
		SceneBasic.registerEvent_sceneChangeStart(self.EVENTHDR_SCENE_CHANGE_START)
		SceneBasic.registerEvent_sceneChangeEnd(self.EVENTHDR_SCENE_CHANGE_END)

		sceneMenu.registerEvent_play(self.EVENTHDR_SCENE_START_GAME)
		sceneMenu.registerEvent_help(self.EVENTHDR_SCENE_START_HELP)
		sceneMenu.registerEvent_quit(self.EVENTHDR_QUIT)

		# sceneGame.registerEvent_menu(self.EVENTHDR_SCENE_START_MENU)
		#sceneGame.registerEvent_win(self.EVENTHDR_SCENE_START_WIN)
		#sceneWin.registerEvent_finished(self.EVENTHDR_SCENE_CONTINUE_GAME)
		#sceneHelp.registerEvent_menu(self.EVENTHDR_SCENE_START_MENU)
		pass



	"""""""""""
	EVENTS
	"""""""""""
	# Event - Starts the Game Scene
	def EVENTHDR_SCENE_START_GAME(self):
		# SoundManager.BTTN_START()
		self.scnGame.EVENT_INITIALIZE()
		self.changeState(self.STATE_GAME)

	# Event - Starts the Help Scene
	def EVENTHDR_SCENE_START_HELP(self):
		self.changeState(self.STATE_HELP)
  
	# Event - Quits the game
	def EVENTHDR_QUIT(self):
		self.isRunning = False
		pygame.quit()
		sys.exit()
		pass	
  
	# Event - Starts the Main Menu Scene
	def EVENTHDR_SCENE_START_MENU(self):
		self.changeState(self.STATE_MENU)		

	# Event - Fired when a Scene Change begins
	def EVENTHDR_SCENE_CHANGE_START(self):
		self.lockRender.acquire()
		pass

	# Event - Fired when a Scene Change ends
	def EVENTHDR_SCENE_CHANGE_END(self):
		self.lockRender.release()
		pass

game = Game24()
