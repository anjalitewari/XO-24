from	SceneBasic	import	*
import	random,	HelperVec2
#buttons
from	KButton	import	KButton
from	IcnBasic	import	IcnBasic
#	import	Game24

class	SceneGame(SceneBasic):
	def	__init__(self,	screenSize,	screen):
		print("SceneGAME:	init");
		SceneBasic.__init__(self,	screenSize,	screen)

	def	initOthers(self,	screenSize):
		self.initImages(screenSize)	#load	background
		self.initButtons(screenSize)

	def	initImages(s,	screenSize):
		#Use	this	to	load	assets
		#s.textureIdBG	=	TextureLoader.load(	os.path.join('assets',	'screenStart','background.png'),screenSize)

		#set	background	asset	here
		pass

	def	initButtons(s,	screenSize):
		print("SceneGAME:	initButtons");
		#set	buttons	here
		sizeLaunch	=	(39/800.0*screenSize[0],31/600.0*screenSize[1])
		s.textureIdButtonBack	=	TextureLoader.load(	os.path.join('assets',	'buttons','back_btn.png'),sizeLaunch)
		s.numberButtonImg = TextureLoader.load(	os.path.join('assets',	'game_icons','number.png'),	(114,112))
		s.bttnBack	=	KButton(10,	10,	39,	31,	s.textureIdButtonBack,True)
		center     = HelperVec2.mult(screenSize, (.5,.5) )
		
		s.numberButton1	=	KButton(center[0]-100, center[0]-200, 60, 60,	s.numberButtonImg,True)
		s.bttn1 = IcnTextBox(center[0]-100, center[0]-200, 60, 60, "#1", color=(252,90,90))
		s.numberButton2	=	KButton(center[0]-100, center[0]-100, 60, 60,	s.numberButtonImg,True)
		s.bttn2 = IcnTextBox(center[0]-100, center[0]-100, 60, 60, "#2", color=(252,90,90))
		s.numberButton3	=	KButton(center[1]+100, center[1]-100, 60, 60,	s.numberButtonImg,True)
		s.bttn3 = IcnTextBox(center[1]+100, center[1]-100, 60, 60, "#3", color=(252,90,90))
		s.numberButton4	=	KButton(center[1]+100, center[1], 60, 60,	s.numberButtonImg,True)
		s.bttn4 = IcnTextBox(center[1]+100, center[1], 60, 60, "#4", color=(252,90,90))
		s.numberButtons = [s.numberButton1, s.numberButton2, s.numberButton3, s.numberButton4]


	def	registerEvent_menu(s,e):	s.EVENT_MENU.append(e)
		
	def	initEvents(s):
		print("SceneGAME:	initEvents");
		s.EVENT_MENU	=	[]

	def	initBackground(s,screen,resolution):
		#set	background	here	with	texture	or	color
		pass

	def	EVENT_CLICK(self,	e):
		print	"EVENT_CLICK"
		self.CLICK_BUTTONS()
		

	def	EVENT_INITIALIZE(self):
		#reset
		print('reset');
		pass
	
	def	EVENT_SCENE_START(s):
		#initializes	all	items	on	screen
		print('initializes')
		s.backgroundColor	=	252,90,90
		s.screen.fill(s.backgroundColor)
		s.bttnBack.draw(s.screen)
		s.numberButton1.draw(s.screen)
		s.bttn1.draw(s.screen)
		s.numberButton2.draw(s.screen)
		s.bttn2.draw(s.screen)
		s.numberButton3.draw(s.screen)
		s.bttn3.draw(s.screen)
		s.numberButton4.draw(s.screen)
		s.bttn4.draw(s.screen)
		pygame.display.flip()
		pass

	def	CLICK_BUTTON_MENU(self):	self.helperRaiseEvent(self.EVENT_MENU)

	def	CLICK_BUTTONS(self):
		#add	button	listeners	here
		mousePos	=	pygame.mouse.get_pos()
		bttn_event	=	[
			[self.bttnBack,	self.CLICK_BUTTON_MENU],
		]
		for	bttn,event	in	bttn_event:
			if(	not	bttn.isUnder(mousePos)):continue
			event()
			return	True
		return	False

def	runGame():
	self.digits	=	test.choose4()	#available	buttons	-	only	add	or	delete	in	run
	#call initbutton and update values
	self.equation	=	[]	#	contains	
	#listen for events 
	print	"in	rungame"
	#call	each	##	button	with	digits	and	display
	self.chk	=	self.ans	=	False
	#while	not	(self.chk	and	self.ans	==	24):	#	and	#ofbuttons	>	1	and	self.running?
		#if	numberbutton.pressed	==	true:
			
			

#runGame()
