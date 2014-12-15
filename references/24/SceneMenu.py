from  SceneBasic import *
import random, HelperVec2
#buttons
from KButton import KButton
from IcnBasic import IcnBasic

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
		s.textureLogo = pygame.image.load( os.path.join('assets', 'buttons', 'logo.png') )

	def initOthers(s , resolution):
		print("SceneMenu::initOthers")


	def helperInitKButton(s, center, textureID):
		texture = TextureLoader.get( textureID)
		size = (texture.get_width(),texture.get_height())
		return KButton(center[0] -size[0] *.5,center[1]-size[1]*.5,size[0],size[1], textureID )


	def initButtons(s,resolution):
		print("SceneMenu::initButtons")
		# Main menu buttons
		center     = HelperVec2.mult(resolution, (.5,.5) )
		s.bttnPlay = IcnTextBox(center[0]-85, center[1]+10, 170, 45, "Start")
		s.bttnHelp = IcnTextBox(center[0]-85, center[1]+70, 170, 45, "Help")
		s.bttnQuit = IcnTextBox(center[0]-85, center[1]+130, 170, 45, "Quit")
		s.buttons  = [ s.bttnPlay, s.bttnHelp, s.bttnQuit ]
		
	#Update the display and show the menu buttons
	def updateDisplay(self, s):
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
		pass

	def EVENT_CLICK(self, e):
		print("SceneMenu::EVENT_CLICK")
		mousePos = pygame.mouse.get_pos()
		# print(self.bttnPlay)
		bttn_event = [
			[self.bttnPlay, self.EVENT_PLAY],
			[self.bttnHelp, self.EVENT_HELP],
			[self.bttnQuit, self.EVENT_QUIT]
		]

		for bttn,event in bttn_event:
			if( not bttn.isUnder(mousePos)):continue
			self.helperRaiseEvent(event);
			return  True
		return False 

	def initBackground(s,screen,size):
		print("SceneMenu::initBackground")
		s.backgroundColor = (252,90,90)
		s.screen.fill(s.backgroundColor)

	def renderUpdate(s,timeElapsed):
		print("SceneMenu::renderUpdate")
