# System Imports
import sys, pygame, os
# Plugin Imports
import pygbutton
# Import Scenes
from SceneBasic import SceneBasic
from SceneGame import SceneGame
# Initialize pygame
pygame.init()

class Game24(object):

    STATE_MENU       = 0
    STATE_GAME       = 1
    STATE_WIN_SCREEN = 2
    STATE_HELP       = 3


    # Main Screen Logo
    logo     = pygame.image.load(os.path.join('assets','buttons','logo.png'))
    logoRect = logo.get_rect()

    # Main Screen Buttons
    startBtn = pygbutton
    helpBtn  = pygbutton
    quitBtn  = pygbutton

    def __init__(self):
        self.currentState = self.STATE_MENU
        self.main()

    #Create a display
    def display(self):
        pygame.display.set_caption('XO 24')        
        self.screenSize = (self.width, self.height) = (1024, 768)
        self.screen     = pygame.display.set_mode(self.screenSize)
        # define main screen buttons (oh god so sloppy)
        self.startBtn   = pygbutton.PygButton( (self.width/2-75, self.height/2-105, 150, 50), 'START', bgcolor=(252,90,90), fgcolor=(255,255,255) )
        self.helpBtn    = pygbutton.PygButton( (self.width/2-75, self.height/2, 150, 50),     'HELP',  bgcolor=(252,90,90), fgcolor=(255,255,255) )
        self.quitBtn    = pygbutton.PygButton( (self.width/2-75, self.height/2+105, 150, 50), 'QUIT',  bgcolor=(255,90,90), fgcolor=(255,255,255) )
        


    #Update the display and show the menu buttons
    def update_display(self):
        # On the main menu: Draw background, buttons, and logo.
        if self.currentState == self.STATE_MENU:
            self.backgroundColor = 252,90,90
            self.screen.fill(self.backgroundColor)
            self.startBtn.draw(self.screen)
            self.helpBtn.draw(self.screen)
            self.quitBtn.draw(self.screen)
            self.screen.blit(self.logo, (self.width/2-141, 100) )
        
        # On the Game Screen:
        if self.currentState == self.STATE_GAME: 
            print("state is game!")

        # on the Help screen:
        

        # flip yo shiz
        pygame.display.flip()
        
    # Main Game Loop
    def main(self):
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or 'click' in self.quitBtn.handleEvent(event):
                    pygame.quit()
                    sys.exit()

                if self.currentState == self.STATE_MENU:
                    if 'click' in self.startBtn.handleEvent(event):
                        print("start btn clicked!")
                        self.currentState = self.STATE_GAME
                    if 'click' in self.helpBtn.handleEvent(event):
                        print("Help btn clicked!")

                if self.currentState == self.STATE_GAME:
                    print("todo: handle game state")

                if self.currentState == self.STATE_WIN_SCREEN:
                    print("todo: handle game win state")

                if self.currentState == self.STATE_HELP:
                    print("todo: handle help state")
                
        
        """
        DrawHelper.init(screenSize[0],screenSize[1])
        self.myFont = pygame.font.Font(os.path.join('assets', 'Minecraftia.ttf') , 24)
        IcnTextBox.setFont( self.myFont)


        self.isRunning = True
        self.isRenderFirstFrame = True

        self.myState = self.STATE_MENU
        #self.lockRender = threading.Lock()
        self.savePath = os.path.join('assets', 'save.json') 
        self.clock = pygame.time.Clock()# Set up a clock for managing the frame rate.

        
        self.scnMenu     = SceneMenu(screenSize)
        self.scnGame     = SceneGame(screenSize)
        self.scnWin     = SceneWin(screenSize)
        self.scnHelp     = SceneHelp(screenSize)
        
        
        self.registerEvents(self.scnMenu,self.scnGame,self.scnWin,self.scnHelp)
        self.dicScenes ={self.STATE_MENU: self.scnMenu,
                self.STATE_GAME: self.scnGame ,
                self.STATE_WIN_SCREEN: self.scnWin,
                self.STATE_HELP:  self.scnHelp}
        """


game = Game24()
#game.main()
