from SceneBasic import *
import random, HelperVec2
#buttons
from KButton import KButton
from IcnBasic import IcnBasic
# import Game24

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
        print("SceneGAME: initButtons");
        #set buttons here
        sizeLaunch = (39/800.0*screenSize[0],31/600.0*screenSize[1])
        s.textureIdButtonBack = TextureLoader.load( os.path.join('assets', 'buttons','back_btn.png'), sizeLaunch)
        s.bttnBack =    KButton(10, 10, 39, 31,  s.textureIdButtonBack,True)

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

def runGame():
    #self.game = Game24()
    self.digits = Game24.choose4() #available buttons - only add or delete in run
    self.equation = [] # contains 
    print "in rungame"
    #call each ## button with digits and display
    self.chk = self.ans = False
    #while not (self.chk and self.ans == 24): # and #ofbuttons > 1 and self.running?
        #if numberbutton.pressed == true:
            
            

#runGame()
