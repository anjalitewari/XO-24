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
		s.bttnPlay = pygbutton.PygButton( (s.width/2-85, s.height/2+10, 170, 45), 'Start', bgcolor=(252,90,90), fgcolor=(255,255,255) )

	def registerEvent_menu(s,e):s.EVENT_MENU.append(e)
		
	def initEvent(s):
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
		
	def EVENT_SCENE_START(self):
		#initializes all items on screen
		print('initializes')
		self.backgroundColor = 252,90,90
		self.screen.fill(self.backgroundColor)
		pygame.display.flip()
	
	
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
