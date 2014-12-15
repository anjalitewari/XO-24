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
from IcnTextBox import IcnTextBox
# Initialize pygame
pygame.init()

class Game24(object):

	STATE_MENU	     = 0
	STATE_GAME	     = 1
	STATE_WIN_SCREEN = 2
	STATE_HELP	     = 3

	def __init__(self):
		print "Game24::init()"
		# start the game with the MENU scene
		self.currentState = self.STATE_MENU
		
		#set font
		self.myFont = pygame.font.Font(os.path.join('assets', 'font','Roboto-Black.ttf') , 24)
		IcnTextBox.setFont(self.myFont)
		
		# define the width and height of our display
		width  = pygame.display.Info().current_w
		height = pygame.display.Info().current_h
		if(float(width)/float(height) == float(4)/float(3)):
			screenSize = (width,height)
		else:
			screenSize = (800,600)
		TextureLoader.screenSize =screenSize
		self.screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE) # change to FULLSCREEN for prod.
		

		# define our scenes and game clock
		self.clock		= pygame.time.Clock()
		self.scnMenu	  = SceneMenu(screenSize, self.screen)
		self.scnGame	  = SceneGame(screenSize,  self.screen)
		#self.scnWin	   = SceneWin(screenSize,  self.screen)
		#self.scnHelp	  = SceneHelp(screenSize,  self.screen)


		# Register application events for each scene
		# self.registerEvents(self.scnMenu,self.scnGame,self.scnWin,self.scnHelp)
		self.registerEvents(self.scnMenu, self.scnGame)
		self.dicScenes = {
			self.STATE_MENU: self.scnMenu,
			self.STATE_GAME: self.scnGame,
			#self.STATE_WIN_SCREEN: self.scnWin,
			#self.STATE_HELP:  self.scnHelp
		}
		self.isRunning = True
		
		self.main()
		

	#Update the display and show the menu buttons
	def update_display(self):
		print "Game24::update_display()"
		self.dicScenes[self.currentState].update_display()
		pass
		
	# Main Game Loop
	def main(self):
		print "Game24::main()"
		self.isRunning = True
		self.scnMenu.EVENT_SCENE_START()
		self.loopUpdate();

	def loopUpdate(self):
		print "Game24::loopUpdate()"
		pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
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
			self.loopUpdate()
		self.isRunning = False
		
	# sets the current state in Game24 to stateNew
	# calls the run event of stateNew
	def changeState(self, stateNew):
		print "Game24::changeState()"
		self.currentState = stateNew
		self.dicScenes[stateNew].EVENT_SCENE_START()

		
	def registerEvents(self, sceneMenu,sceneGame=None,sceneWin=None, sceneHelp=None):
		print "Game24::registerEvents()"
		SceneBasic.registerEvent_sceneChangeStart(self.EVENTHDR_SCENE_CHANGE_START)
		SceneBasic.registerEvent_sceneChangeEnd(self.EVENTHDR_SCENE_CHANGE_END)

		sceneMenu.registerEvent_play(self.EVENTHDR_SCENE_START_GAME)
		sceneMenu.registerEvent_help(self.EVENTHDR_SCENE_START_HELP)
		sceneMenu.registerEvent_quit(self.EVENTHDR_QUIT)

		sceneGame.registerEvent_menu(self.EVENTHDR_SCENE_START_MENU)
		#sceneGame.registerEvent_win(self.EVENTHDR_SCENE_START_WIN)
		#sceneWin.registerEvent_finished(self.EVENTHDR_SCENE_CONTINUE_GAME)
		#sceneHelp.registerEvent_menu(self.EVENTHDR_SCENE_START_MENU)
		pass



	"""""""""""
	EVENTS
	"""""""""""
	# Event - Starts the Game Scene
	def EVENTHDR_SCENE_START_GAME(self):
		print "Game24::EVENTHDR_SCENE_START_GAME()"
		self.scnGame.EVENT_INITIALIZE()
		self.changeState(self.STATE_GAME)

	# Event - Starts the Help Scene
	def EVENTHDR_SCENE_START_HELP(self):
		print "Game24::EVENTHDR_SCENE_START_HELP()"
		self.changeState(self.STATE_HELP)
  
	# Event - Quits the game
	def EVENTHDR_QUIT(self):
		print "Game24::EVENTHDR_QUIT"
		self.isRunning = False
		pygame.quit()
		sys.exit()
		pass	
  
	# Event - Starts the Main Menu Scene
	def EVENTHDR_SCENE_START_MENU(self):
		print "Game24::EVENTHDR_SCENE_START_MENU()"
		self.changeState(self.STATE_MENU)		

	# Event - Fired when a Scene Change begins
	def EVENTHDR_SCENE_CHANGE_START(self):
		print "Game24::EVENTHDR_SCENE_CHANGE_START()"
		self.lockRender.acquire()
		pass

	# Event - Fired when a Scene Change ends
	def EVENTHDR_SCENE_CHANGE_END(self):
		print "Game24::EVENTHDR_SCENE_CHANGE_END()"
		self.lockRender.release()
		pass

game = Game24()
