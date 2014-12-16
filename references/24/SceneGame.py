from	SceneBasic	import	*
import	random,	HelperVec2
#buttons
from	KButton	import	KButton
from	IcnBasic	import	IcnBasic
from	IcnTextBox import IcnTextBox
from 	GameButton import	GameButton
from 	OperatorButton import	OperatorButton
import test


class	SceneGame(SceneBasic):

	# past number combinations (before move was made)
	PAST_NUMS = []
	# original combinations of numbers - holds button pair
	NUMS_AVAILABLE = []
	NUMS_REMOVED = []
	CUR_EQ = []

	# marks if these requirements have been met
	FIRST_NUM_HIT = False
	OPERATER_HIT = False
	SEC_NUM_HIT = False

	STATE_NORMAL = 0
	STATE_SOLVED = 1
	rendered = 0


	def	__init__(self,	screenSize,	screen):
		print("SceneGAME:	init");
		SceneBasic.__init__(self,screenSize,screen)

	def	initOthers(self,screenSize):
		print("SceneGAME:	initOthers")
		self.initImages(screenSize)	#load	background
		self.myState = self.STATE_NORMAL
		self.runGame()
		self.rendered +=1

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
			[s.numberButton4, s.bttn4Label],
		]

		# Operators
		textureAddbtn =	TextureLoader.load( os.path.join('assets', 'game_icons', 'add.png'))
		textureAddbtnPressed = TextureLoader.load( os.path.join('assets', 'game_icons', 'add_pressed.png'))
		s.opbutton1 = OperatorButton('+', center[1]-80, center[1]+120, 84, 82,	textureAddbtn, textureAddbtnPressed, True)

		textureSubbtn = TextureLoader.load(	os.path.join('assets', 'game_icons', 'subtract.png'))
		textureSubbtnPressed = TextureLoader.load(	os.path.join('assets', 'game_icons', 'subtract_pressed.png'))
		s.opbutton2 = OperatorButton('-', center[1]+10, center[1]+120, 84, 82,	textureSubbtn, textureSubbtnPressed,True)

		textureMultbtn = TextureLoader.load( os.path.join('assets', 'game_icons', 'multiply.png'))
		textureMultbtnPressed = TextureLoader.load(	os.path.join('assets',	'game_icons', 'multiply_pressed.png'))
		s.opbutton3 = OperatorButton('x', center[1]+100, center[1]+120, 84, 82,	textureMultbtn, textureMultbtnPressed, True)

		textureDivbtn = TextureLoader.load(	os.path.join('assets',	'game_icons', 'divide.png'))
		textureDivbtnPressed = TextureLoader.load( os.path.join('assets', 'game_icons', 'divide_pressed.png'))
		s.opbutton4 = OperatorButton('/', center[1]+190, center[1]+120, 84, 82,	textureDivbtn, textureDivbtnPressed, True)

		# Array for operators
		s.opBttns = [s.opbutton1, s.opbutton2, s.opbutton3, s.opbutton4]

		# text box equations
		myfont = pygame.font.Font(os.path.join('assets', 'font','Roboto-Black.ttf') , 26)
		s.bttn1Label.setFont(myfont)
		s.equationLabel = IcnTextBox(center[0]-100, 70, 200, 60, "Equation Here")


	def	registerEvent_menu(s,e):	s.EVENT_MENU.append(e)

	def	registerEvent_numbutton(s,e):	s.EVENT_NUM_BUTTON.append(e)

	def	registerEvent_opbutton(s,e):	s.EVENT_OP_BUTTON.append(e)


	def	initEvents(s):
		print("SceneGAME:	initEvents");
		s.EVENT_MENU = []
		s.EVENT_NUM_BUTTON = []
		s.EVENT_OP_BUTTON = []

	def	initBackground(s,screen,resolution):
		#set	background	here	with	texture	or	color
		pass

	def resetGame(s):
		# past number combinations (before move was made)
		PAST_NUMS = []
		# original combinations of numbers
		NUMS_AVAILABLE = []
		NUMS_REMOVED = []
		CUR_EQ = []

		# marks if these requirements have been met
		FIRST_NUM_HIT = False
		OPERATER_HIT = False
		SEC_NUM_HIT = False

	def	EVENT_CLICK(self,e):
		print	"EVENT_CLICK"
		self.CLICK_BUTTONS()
		if(self.myState is self.STATE_NORMAL):
			if(self.CLICK_NUMBUTTON()):
				print "back in event_click numBtn clicked"
				#self.doUpdateAnswer()
			elif(self.CLICK_OPBUTTON()): #TypeError: CLICK_OPBUTTON() takes no arguments (1 given)
					print "back in event_click opBtn clicked"
			elif (self.CLICK_BUTTONS()):pass
			else : self.icnTextBottom.display("HooYa! You cannot click that.")
		if(self.myState is self.STATE_SOLVED):
			pass


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

		s.updateEquation()
		# only draw available buttons
		s.drawNumButtons()
		# draw operator
		s.drawOperators()

		pygame.display.flip()
		pass
	
	def updateDisplay(s):
		s.EVENT_SCENE_START()

	def updateEquation(s):
		s.equation = '';
		for value in s.CUR_EQ:
			s.equation = s.equation + ' ' + value
		
		s.equationLabel.setContent(s.equation);
		s.equationLabel.draw(s.screen)
		
	def drawNumButtons(s):
		print "Draw NumButtons"
		# only draw available buttons
		for	numBttn,label	in	s.numBttnPairs:
			if( numBttn.on == True ):
				numBttn.draw(s.screen)
				label.draw(s.screen)

	def drawOperators(s):
		print "Draw Operators"
		for opBtn in s.opBttns:
			if(opBtn.tapped):
				opBtn.drawPressed()
			opBtn.draw(s.screen)




	def	CLICK_BUTTON_MENU(self):	self.helperRaiseEvent(self.EVENT_MENU)

	def	CLICK_NUMBER_BUTTON(self):	self.helperRaiseEvent(self.EVENT_NUM_BUTTON)

	def	CLICK_OP_BUTTON(self):	self.helperRaiseEvent(self.EVENT_OP_BUTTON)

	def	CLICK_BUTTONS(self):
		#add	button	listeners	here
		print "click_buttons"
		mousePos	=	pygame.mouse.get_pos()
		bttn_event	=	[
			[self.bttnBack, self.CLICK_BUTTON_MENU],
			[self.numberButton1, self.CLICK_NUMBER_BUTTON],
			[self.numberButton2, self.CLICK_NUMBER_BUTTON],
			[self.numberButton3, self.CLICK_NUMBER_BUTTON],
			[self.numberButton4, self.CLICK_NUMBER_BUTTON],
			[self.opbutton1, self.CLICK_OP_BUTTON],
			[self.opbutton2, self.CLICK_OP_BUTTON],
			[self.opbutton3, self.CLICK_OP_BUTTON],
			[self.opbutton4, self.CLICK_OP_BUTTON],

		]
		for	bttn,event	in	bttn_event:
			if(	not	bttn.isUnder(mousePos)):continue
			event()
			return	True
		return	False

	def CLICK_OPBUTTON(self):
		print "in click_opbutton"
		pos = pygame.mouse.get_pos()
		for i in range(0, len( self.opBttns  )) :
			btn = self.opBttns[i]
			#choice = self.questionChoices[i]
			if(btn.isUnder(pos) or btn.isUnder(pos)):
				print "isunder"
				if(btn.select() or btn.select()):
					print "selected"
					if self.FIRST_NUM_HIT:
						if self.SEC_NUM_HIT:
							pass
						else:
							self.CUR_EQ.append(btn.getOperation())
							self.OPERATER_HIT = True
							btn.tapped = True
							print self.CUR_EQ
		self.updateDisplay()

	def CLICK_NUMBUTTON(self):
		print "in click_numbutton"
		pos = pygame.mouse.get_pos()
		for i in range(0, len( self.numBttnPairs  )) :
			#print(self.numBttnPairs)
			btn = self.numBttnPairs[i]
			#choice = self.questionChoices[i]
			if(btn[0].isUnder(pos) or btn[1].isUnder(pos)):
				print "isunder"
				if(btn[0].select() or btn[1].select()):
					print "selected"
					if not self.FIRST_NUM_HIT:
						print "if not self.FIRST_NUM_HIT"
						self.FIRST_NUM_HIT = True
						found = False
						for n in range(0, len(self.NUMS_AVAILABLE)):
							print self.NUMS_AVAILABLE
							print len(self.NUMS_AVAILABLE)
							if self.NUMS_AVAILABLE[n][0].getValue() == btn[0].getValue(): # this will only pas if NUMS_AVAILABLE has more than 1 button
								print "A.getValue() test passed!!s!!!!!!!!!!!!!!!!!!!!"
								cur = self.NUMS_AVAILABLE[n][0].getValue()
								self.NUMS_AVAILABLE.remove(self.NUMS_AVAILABLE[n])
								self.NUMS_REMOVED.append(self.NUMS_AVAILABLE[n])
								self.CUR_EQ.append(cur)
								print self.CUR_EQ
								self.updateDisplay()
								found = True
								return found
						print "cureq:", self.CUR_EQ
						self.updateDisplay()
						return found


					else:
						print "if self.FIRST_NUM_HIT"
						#replace first number with this number
						if not self.OPERATER_HIT:
							print "if not self.OPERATER_HIT:"
							if not len(self.NUMS_REMOVED) == 0:
								self.NUMS_AVAILABLE = self.NUMS_REMOVED.pop()
							found = False

							for m in range(0,len(self.NUMS_AVAILABLE)/2):
								
								print m
								print len(self.NUMS_AVAILABLE)
								if self.NUMS_AVAILABLE[m].getValue() == btn[0].getValue():
									found = True
									self.NUMS_AVAILABLE.remove(self.NUMS_AVAILABLE[m])
									self.NUMS_REMOVED.append(self.NUMS_AVAILABLE[m])
									self.CUR_EQ.remove(self.NUMS_AVAILABLE[m])
									self.CUR_EQ.append(self.NUMS_AVAILABLE[m])
									print "removed an available num"
									self.updateDisplay()
							return found

						else:
							found = False
							for a in self.NUMS_AVAILABLE:
								if a[0].getValue() == btn[0].getValue():
									found = True
									self.NUMS_AVAILABLE.remove(a)
									self.NUMS_REMOVED.append(a)
									self.CUR_EQ.append(a[0].getValue())
									self.SEC_NUM_HIT = True
									print "removed an available num"
									print self.CUR_EQ
									self.updateDisplay()
									return True
							self.updateDisplay()
							return found





					#if(self.getCurrentAns() <= 24):
						#can process

					#btn[0].setSelect(False)
					#btn[1].setContent("")
					return True

				return True
		return False

	def	runGame(self):
		self.initButtons((800,600))	#screenSize
		game =	test.Game()
		self.digits	= game.choose4()
		print self.digits
		i = 0
		for button in self.numBttnPairs:
			button[0].setValue(self.digits[i])
			button[1].setContent(button[0].getValue(),color=(252,90,90))
			i += 1
			self.NUMS_AVAILABLE.append(button)

			#button[0].on = True
		#self.drawNumButtons()
		#call initbutton and update values
		self.equation	=	[]	#	contains
		#listen for events
		print	"in	rungame"
		#call	each	##	button	with	digits	and	display
		self.chk	=	self.ans	=	False
		while self.rendered > 1 and not(self.chk and self.ans == 24):	#	and	#ofbuttons	>	1	and	self.running?
			#if	numberbutton.pressed	==	true:
			if len(self.CUR_EQ) == 3:
				self.ans = self.solveEquation()
				self.SEC_NUM_HIT = False
				#self.equationLabel.setContent(self.ans)
				#self.equationLabel.draw(s.screen)

		#pygame.display.flip()
		pass

	def solveEquation(self):
		first = False

		for a in range(0, len(self.CUR_EQ)):
			if (self.CUR_EQ[a]) in ['1','2','3','4','5','6','7','8','9','0']:
				if not first:
					f = self.eqDict(self.CUR_EQ[a])
					first = true
				else:
					s = self.eqDict(self.CUR_EQ[a])
			else:
				if self.CUR_EQ[a] in ['+','-','*','/']:

					if first:
						s = self.CUR_EQ[a + 1]
						if self.CUR_EQ[a] == '+':
							return f + s
						elif self.CUR_EQ[a] == '-':
							return f - s
						elif self.CUR_EQ[a] == '*':
							return f * s
						elif self.CUR_EQ[a] == '/':
							return f / s


	def eqDict(self, x):
		return {
			'1':1,
			'2':2,
			'3':3,
			'4':4,
			'5':5,
			'6':6,
			'7':7,
			'8':8,
			'9':9,
			'0':0,
			'+':'+',
			'-':'-',
			'*':'*',
			'/':'/'
		}[x]
