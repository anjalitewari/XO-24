from  SceneBasic import *
import random, HelperVec2

class SceneMenu(SceneBasic):

	def __init__(self,  resolution,	screen):
		print("SceneMenu::init")
		SceneBasic.__init__(self,resolution, screen)
		# self.updateDisplay(self)
	
	def registerEvent_play(s,e): s.EVENT_PLAY.append(e);pass
	def registerEvent_help(s,e): s.EVENT_HELP.append(e);pass
	def registerEvent_quit(s,e): s.EVENT_QUIT.append(e);pass

	def initEvents(s):
		print("SceneMenu::initEvents")
		s.EVENT_PLAY = [ ];
		s.EVENT_HELP = [ ];
		s.EVENT_QUIT = [ ];

	def initImages(s, resolution):
		print("SceneMenu::initImages")
		#s.textureIdTitle		  = TextureLoader.load(os.path.join('assets', 'screenStart', 'title.png'), HelperVec2.mult(resolution, (.7,.13)))
		#s.textureIdTitle		   = TextureLoader.load(os.path.join('assets', 'screenStart', 'title.png') )
		#s.textureIdBG			  = TextureLoader.load(os.path.join('assets', 'screenStart', 'background.png') ,resolution);
		#s.textureIdBttnStart	   = TextureLoader.load(os.path.join('assets', 'screenStart', 'bttnStart.png') );
		#s.textureIdBttnHelp		= TextureLoader.load(os.path.join('assets', 'screenStart', 'bttnHelp.png') );
		#s.textureIdBttnExit		= TextureLoader.load(os.path.join('assets', 'screenStart', 'bttnExit.png') );
		#s.textureIdShootingStar_00 = TextureLoader.load(os.path.join('assets', 'screenCommon', 'shootingStar00.png') );
		#s.textureIdShootingStar_01 = TextureLoader.load(os.path.join('assets', 'screenCommon', 'shootingStar01.png') );
		s.textureLogo = pygame.image.load( os.path.join('assets', 'buttons', 'logo.png') )

	def initOthers(s , resolution):
		print("SceneMenu::initOthers")
		# s.initParticles(resolution)
		# s.renderScreenObjects.extend(s.arrShootingStars)
		# s.icnMouse = IcnBasic.FROM_PATH(os.path.join('assets', 'screenCommon', 'cursor.png') )
		# s.renderScreenObjects.append(s.icnMouse)

	def helperInitKButton(s, center, textureID):
		print("SceneMenu::helperInitKButton")
		# texture = TextureLoader.get( textureID)
		# size = (texture.get_width(),texture.get_height())
		# return KButton(center[0] -size[0] *.5,center[1]-size[1]*.5,size[0],size[1], textureID )

	def initButtons(s,resolution):
		print("SceneMenu::initButtons")
		# center = HelperVec2.mult(resolution, (.5,.5) )
		# Main menu buttons
		# s.bttnPlay = s.helperInitKButton ((center[0],center[1]-60),s.textureIdBttnStart)# KButton(center[0]-100, center[1] - 100, 200, 75,s.textureIdBttnStart)
		# s.bttnHow =	s.helperInitKButton ((center[0],center[1]), s.textureIdBttnHelp)
		# s.bttnQuit =	s.helperInitKButton ((center[0],center[1]+60), s.textureIdBttnExit)  #KButton(center[0]  -100,center[1] + 100, 200, 75,s.textureIdBttnExit)
		# s.buttons = [s.bttnPlay,s.bttnHow,s.bttnQuit]
		center     = HelperVec2.mult(resolution, (.5,.5) )
		s.bttnPlay = pygbutton.PygButton( (center[0]-85, s.height/2+10, 170, 45), 'Start', bgcolor=(252,90,90), fgcolor=(255,255,255) )
		s.bttnHelp = pygbutton.PygButton( (center[0]-85, s.height/2+70, 170, 45), 'Help',  bgcolor=(252,90,90), fgcolor=(255,255,255) )
		s.bttnQuit = pygbutton.PygButton( (center[0]-85, s.height/2+130, 170, 45), 'Quit',  bgcolor=(255,90,90), fgcolor=(255,255,255) )
		s.buttons  = [ s.bttnPlay, s.bttnHelp, s.bttnQuit ]
		
		
	#Update the display and show the menu buttons
	def updateDisplay(self, s):
		# if self.currentState == self.STATE_MENU:
		s.backgroundColor = 252,90,90
		s.screen.fill(s.backgroundColor)
		s.bttnPlay.draw(s.screen)
		s.bttnHelp.draw(s.screen)
		s.bttnQuit.draw(s.screen)
		s.screen.blit(self.textureLogo, (self.width/2-141, 100) )
		pygame.display.flip()
	
	def EVENT_SCENE_START(self):
		print("SceneMenu::EVENT_SCENE_START")
		self.updateDisplay(self)
		#IcnParticleShootingStar.textureBG = self.myBackground

	def EVENT_CLICK(self, e):
		print("SceneMenu::EVENT_CLICK")
		
		buttons_event = [
			[self.bttnPlay, self.EVENT_PLAY],
			[self.bttnHelp, self.EVENT_HELP],
			[self.bttnQuit, self.EVENT_QUIT]
		]
		
		for btn,event in buttons_event:
				if 'enter' in btn.handleEvent(e):
					self.helperRaiseEvent(event)
					break

	
	def initBackground(s,screen,size):
		print("SceneMenu::initBackground")
		# screen.fill((255, 255, 255))
		# DrawHelper.drawAspect(screen, s.textureIdBG,0,0)
		# DrawHelper.drawAspect(screen, s.textureIdTitle,.12,.1)
		# for button in s.buttons: button.draw(screen)

	def renderUpdate(s,timeElapsed):
		print("SceneMenu::renderUpdate")
		# s.icnMouse.pos =  pygame.mouse.get_pos()
		# s.ratio = (s.ratio+800.15*timeElapsed ) % 3.5
		# s.distortH.range = (s.ratio ,s.ratio)
		# s.distortV.range = (-s.ratio , -s.ratio)
		# s.distortH.pos = (0,pygame.mouse.get_pos()[1])
		# s.distortV.pos = (pygame.mouse.get_pos()[0],0)
		# s.distortH.pos =(0, pygame.mouse.get_pos()[1])
		# s.distortV.pos = (0,pygame.mouse.get_pos()[1]+s.distortSpacing )
		# for icn in s.arrShootingStars:
		# 	icn.drawUpdate(timeElapsed)
		s.icnMouse.pos = pygame.mouse.get_pos()
		