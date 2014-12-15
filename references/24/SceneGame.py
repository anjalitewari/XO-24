from SceneBasic import *
import random, HelperVec2

class SceneGame(SceneBasic):
	def __init__(self, screenSize, screen):
		print("SceneGAME: init");
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
		s.bttnBack = pygbutton.PygButton( (10, 10, 39, 31), '', bgcolor=(252,90,90), fgcolor=(255,255,255), normal="assets/buttons/back_btn.png" )

	def registerEvent_menu(s,e): s.EVENT_MENU.append(e)
		
	def initEvents(s):
		print("SceneGAME: initEvents");
		s.EVENT_MENU = []

	def initBackground(s,screen,resolution):
		#set background here with texture or color
		pass

	def EVENT_CLICK(self, e):
		print "EVENT_CLICK"
		#self.CLICK_BUTTONS(e)
		buttons_event = [
			[self.bttnBack, self.EVENT_MENU],
		]
		for btn,event in buttons_event:
				if 'enter' in btn.handleEvent(e):
					self.helperRaiseEvent(event)
					break

	def EVENT_INITIALIZE(self):
		#reset
		print('reset');
		
	def EVENT_SCENE_START(s):
		#initializes all items on screen
		print('initializes')
		s.backgroundColor = 252,90,90
		s.screen.fill(s.backgroundColor)
		s.bttnBack.draw(s.screen)
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
