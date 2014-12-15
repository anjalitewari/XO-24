from SceneBasic import *
import random, HelperVec2

class SceneGame(SceneBasic):
	def __init__(self, screenSize, screen):
		SceneBasic.__init__(self, screenSize, screen)

	def initOthers(self, screenSize):
		self.initImages(screenSize) #load background
		self.initButtons(screenSize)

	def initImages(s, screenSize):
		#Use this to load assets
		#s.textureIdBG = TextureLoader.load( os.path.join('assets', 'screenStart','background.png'),screenSize)

		#set background asset here
		pass

	def initButtons(s, screenSize):
		#set buttons here
		pass

	def registerEvent_menu(s,e):s.EVENT_MENU.append(e)
		
	def initEvent(s):
		s.EVENT_MENU = []

	def initBackground(s,screen,resolution):
		#set background here with texture or color
		pass

	def EVENT_CLICK(self):
		print "EVENT_CLICK"
		self.CLICK_BUTTONS()

	def EVENT_INITIALIZE(self):
		#reset
		print('reset');
		
	def EVENT_SCENE_START(self):
		#initializes all items on screen
		print('initializes');
	
	
	#def CLICK_BUTTON_MENU(self): self.helperRaiseEvent(self.EVENT_MENU)

	def CLICK_BUTTONS(self):
		#add button listeners here
		"""
	mousePos = pygame.mouse.get_pos()
	bttn_event = [
		[self.bttnMenu, self.CLICK_BUTTON_MENU]]
	for bttn,event in bttn_event:
		if( not bttn.isUnder(mousePos)):continue
		event()
			return  True
			
	return False
	"""
