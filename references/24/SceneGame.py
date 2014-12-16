from	SceneBasic	import	*
import	random,	HelperVec2
#buttons
from	KButton	import	KButton
from	IcnBasic	import	IcnBasic
from GameButton import	GameButton

class	SceneGame(SceneBasic):
	
	# past number combinations (before move was made)
	PAST_NUMS = []
	# original combinations of numbers
	NUMS_AVAILABLE = []
	
	# marks if these requirements have been met
	FIRST_NUM_HIT = False
	OPERATER_HIT = False
	SEC_NUM_HIT = False
	
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
		s.textureIdButtonBack	=	TextureLoader.load(	os.path.join('assets',	'buttons','back_btn.png'))
		s.numberButtonImg = TextureLoader.load(	os.path.join('assets',	'game_icons','number.png'))
		s.bttnBack	=	KButton(10,	10,	39,	31,	s.textureIdButtonBack,True)
		center     = HelperVec2.mult(screenSize, (.5,.5) )
		
		# number buttons and corresponding labels
		s.numberButton1	=	GameButton(1, center[0]-125, center[0]-250, 116, 120,	s.numberButtonImg,True)
		s.bttn1Label = IcnTextBox(center[0]-97, center[0]-220, 60, 60, "#1", color=(252,90,90))
		
		s.numberButton2	=	GameButton(2, center[0]-125, center[0]-130, 116, 120,	s.numberButtonImg,True)
		s.bttn2Label = IcnTextBox(center[0]-97, center[0]-100, 60, 60, "#2", color=(252,90,90))
		
		s.numberButton3	=	GameButton(3, center[1]+100, center[1]-150, 116, 120,	s.numberButtonImg,True)
		s.bttn3Label = IcnTextBox(center[1]+125, center[1]-120, 60, 60, "#3", color=(252,90,90))
		
		s.numberButton4	=	GameButton(4, center[1]+100, center[1]-30, 116, 120,	s.numberButtonImg,True)
		s.bttn4Label = IcnTextBox(center[1]+125, center[1], 60, 60, "#4", color=(252,90,90))
		
		s.numberButtons = [s.numberButton1, s.numberButton2, s.numberButton3, s.numberButton4]
		s.numberIcons = [s.bttn1Label, s.bttn2Label, s.bttn3Label, s.bttn4Label] 
		
		# Array Will Be Referenced Throughout
		# pair numbuttons with their labels
		s.numBttnPairs = [
			[s.numberButton1, s.bttn1Label],
			[s.numberButton2, s.bttn2Label],
			[s.numberButton3, s.bttn3Label],
			[s.numberButton4, s.bttn4Label]
		]
		
		
		# Operators
		

	def	registerEvent_menu(s,e):	s.EVENT_MENU.append(e)

	def	registerEvent_numbutton(s,e):	s.EVENT_NUM_BUTTON.append(e)
	
	
	def	initEvents(s):
		print("SceneGAME:	initEvents");
		s.EVENT_MENU = []
		s.EVENT_NUM_BUTTON = []

	def	initBackground(s,screen,resolution):
		#set	background	here	with	texture	or	color
		pass

	def resetGame(s):
		# past number combinations (before move was made)
		PAST_NUMS = []
		# original combinations of numbers
		NUMS_AVAILABLE = []

		# marks if these requirements have been met
		FIRST_NUM_HIT = False
		OPERATER_HIT = False
		SEC_NUM_HIT = False
	
	def	EVENT_CLICK(self,e):
		print	"EVENT_CLICK"
		self.CLICK_BUTTONS()		

	def	EVENT_INITIALIZE(self):
		#reset
		print('reset');
		self.resetGame()
		pass
	
	def	EVENT_SCENE_START(s):
		#initializes	all	items	on	screen
		print('Begin Creating Scene')
		s.backgroundColor	=	252,90,90
		s.screen.fill(s.backgroundColor)
		s.bttnBack.draw(s.screen)
		
		# only draw available buttons
		s.drawNumButtons()
		
		pygame.display.flip()
		pass
	
	def drawNumButtons(s):
		print "Draw NumButtons"
		# only draw available buttons
		for	numBttn,label	in	s.numBttnPairs:
			print(numBttn)
			if( numBttn.on == True ):
				numBttn.draw(s.screen)
				label.draw(s.screen)
	
	
	def	CLICK_BUTTON_MENU(self):	self.helperRaiseEvent(self.EVENT_MENU)

	def	CLICK_NUMBER_BUTTON(self):	self.helperRaiseEvent(self.EVENT_NUM_BUTTON)	
	
	def	CLICK_BUTTONS(self):
		#add	button	listeners	here
		mousePos	=	pygame.mouse.get_pos()
		bttn_event	=	[
			[self.bttnBack, self.CLICK_BUTTON_MENU],
			[self.numberButton1, self.CLICK_NUMBER_BUTTON],
			[self.numberButton2, self.CLICK_NUMBER_BUTTON],
			[self.numberButton3, self.CLICK_NUMBER_BUTTON],
			[self.numberButton4, self.CLICK_NUMBER_BUTTON],
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
