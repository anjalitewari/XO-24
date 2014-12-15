from SceneBasic import *
import random, HelperVec2
#buttons
from KButton import KButton
from IcnBasic import IcnBasic

class SceneHelp(SceneBasic):
	def __init__(self, screenSize, screen):
		print("SceneGAME: init");
		SceneBasic.__init__(self, screenSize, screen)

	def initOthers(self, screenSize):
		self.initImages(screenSize) #load background
		self.initButtons(screenSize)

	def initImages(s, screenSize):
		s.helpImg = pygame.image.load( os.path.join('assets','buttons', 'help_screen.png') )
		pass

	def initButtons(s, screenSize):
		print("SceneGAME: initButtons");
		#set buttons here
		sizeLaunch = (39/800.0*screenSize[0],31/600.0*screenSize[1])
		s.textureIdButtonBack = TextureLoader.load( os.path.join('assets', 'buttons','back_btn.png'), sizeLaunch)
		s.bttnBack = KButton(10, 10, 39, 31,  s.textureIdButtonBack,True)

	def registerEvent_menu(s,e): s.EVENT_MENU.append(e)
		
	def initEvents(s):
		print("SceneGAME: initEvents");
		s.EVENT_MENU = []

	def initBackground(s,screen,resolution):
		#set background here with texture or color
		pass

	def EVENT_CLICK(self, e):
		print "EVENT_CLICK"
		self.CLICK_BUTTONS()
		

	def EVENT_INITIALIZE(self):
		#reset
		print('reset');
		pass
	
	def EVENT_SCENE_START(s):
		#initializes all items on screen
		print('initializes')
		s.backgroundColor = 252,90,90
		s.screen.fill(s.backgroundColor)
		s.bttnBack.draw(s.screen)
		s.screen.blit(s.helpImg, (0,50))
		pygame.display.flip()
		pass

	def CLICK_BUTTON_MENU(self): self.helperRaiseEvent(self.EVENT_MENU)

	def CLICK_BUTTONS(self):
		#add button listeners here
		mousePos = pygame.mouse.get_pos()
		bttn_event = [
			[self.bttnBack, self.CLICK_BUTTON_MENU],
		]
		for bttn,event in bttn_event:
			if( not bttn.isUnder(mousePos)):continue
			event()
			return  True
		return False
