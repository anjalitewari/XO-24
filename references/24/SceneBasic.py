import pygame
import os
import TextureLoader
import pygbutton

#buttons
from KButton import KButton
from IcnBasic import IcnBasic
#labels
from IcnTextBox import IcnTextBox
from IcnTextDisplayer import IcnTextDisplayer

class SceneBasic(object):
	
	@staticmethod
	def helperRaiseEvent(events):
		print(events);
		for e in events: e();

	event_scene_change_start =[]
	event_scene_change_end =[]

	@staticmethod
	def registerEvent_sceneChangeStart(e): SceneBasic.event_scene_change_start.append(e);
	@staticmethod
	def registerEvent_sceneChangeEnd(e):SceneBasic.event_scene_change_end.append(e);

	@staticmethod
	def EVENT_SCENE_CHANGE_START():
		SceneBasic.helperRaiseEvent(SceneBasic.event_scene_change_start)
	@staticmethod
	def EVENT_SCENE_CHANGE_END():
		SceneBasic.helperRaiseEvent(SceneBasic.event_scene_change_end)

	def EVENT_STTAIC_DRAWN(self, obj):
		self.myBackground.blit(obj.mySurface, obj.pos)


	#init methods
	def __init__(self,  resolution, screen):
		self.screen = screen;
		self.width = resolution[0]
		self.height = resolution[1]
		self.myBackground = pygame.Surface( resolution)
		self.initBase()
		self.initEvents();
		self.initImages(resolution);
		self.initButtons(resolution)
		self.initOthers(resolution)
		self.initBackground(self.myBackground,resolution)

	def initButtons(s,screenSize):
		pass
	def initImages(s,screenSize):
		pass;
	def initEvents(s):
		pass
	def initOthers(s,screenSize):
		pass
	def initBase(s):
		s.rectBuffer = []
		s.rectBufferOld = []
		s.isMouseReleased = True
		s.renderScreenObjects = []

	def initBackground(s,surface,resolution):
		pass

	def updateDisplay(self,s):
		pass
	
	def updateStatic(self):
		pass

	#in a thread 
	def renderScreenBegin(self,screen):
		screen.fill((255, 255, 255,1)) 
		self.initBackground(self.myBackground,(screen.get_width(), screen.get_height()))
		screen.blit(self.myBackground,(0,0))
		pygame.display.update()
		self.renderUpdate(0)
		pass
	def render(self,screen):
		self.renderScreenClean(screen, self.rectBuffer)
		self.rectBufferOld = self.rectBuffer
		
		self.rectBuffer = []
		self.renderScreen(screen)

		#rectBufferOld.extend(self.rectBuffer)
		pygame.display.update(self.rectBufferOld)
		#pygame.display.update(self.rectBuffer)
	#helperMethods that will come handy
	def helperClean(self, screen, obj):
		screen.blit(self.myBackground, (obj.pos[0]-10,obj.pos[1]-10),(obj.rect[0]-10,obj.rect[1]-10,obj.rect[2]+20,obj.rect[3]+20 ) )
		#screen.blit(self.myBackground, (obj.pos[0]-5,obj.pos[1]-1),obj.rect )
		#pygame.display.update((0,0,100,100) )

	def helperCleanRect(self, screen, r):
		#screen.blit(self.myBackground, (r[0]-10,r[1]),r)
		screen.blit(self.myBackground, r,r)
		#pygame.display.update(r)

	def renderScreenClean(self,screen,rects):
		#for obj in self.renderScreenObjects :
		#	#print str(obj.pos[0]) + " " + str(obj.pos[1])
		#	self.helperClean(screen,obj)
		for r in rects:
			self.helperCleanRect(screen,r)
			pass

	def helperRenderScreen(self,screen, arr):
		for obj in arr: obj.draw(screen);

	def renderScreen(self,screen):
		for obj in self.renderScreenObjects :
			rect = obj.draw(screen)
			self.rectBuffer.append(rect)
			self.rectBufferOld.append(rect)
		pass

	def renderUpdate(self, timeElapsed):
		pass

	#BasicEvents
	def listenForEvents(s, eventStack):
		mousePressed = pygame.mouse.get_pressed()
		for event in eventStack:
		
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == 6:
				s.EVENT_CLICK(event)
				return
		"""
		if(s.isMouseReleased and mousePressed[0] is 1) :
			s.isMouseReleased = False
		elif(not s.isMouseReleased and mousePressed[0] is 0):
			s.EVENT_CLICK(e)
			s.isMouseReleased = True
		"""
		
	def EVENT_INITIALIZE(self):
		pass

	def EVENT_CLICK(self):
		pass

	def EVENT_SCENE_START(self):
		print("SCENE_BASIC_ENTER")



