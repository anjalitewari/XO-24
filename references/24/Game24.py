# System Imports
import sys, pygame, os
# Plugin Imports
import pygbutton
# Initialize pygame
pygame.init()

class Game24(object):

    STATE_MENU       = 0
    STATE_GAME       = 1
    STATE_WIN_SCREEN = 2
    STATE_HELP       = 3

    # Main Screen Buttons
    startBtn = pygbutton
    helpBtn  = pygbutton
    quitBtn  = pygbutton

    def __init__(self):
        self.main()

    #Create a display
    def display(self):
        pygame.display.set_caption('XO 24')        
        self.screenSize = (self.width, self.height) = (1024, 768)
        self.screen     = pygame.display.set_mode(self.screenSize)
        self.startBtn   = pygbutton.PygButton( (self.width/2-125, self.height/2-125, 250, 90), 'START', bgcolor=(252,90,90), fgcolor=(255,255,255) )
        self.helpBtn    = pygbutton.PygButton( (self.width/2-125, self.height/2, 250, 90),     'HELP',  bgcolor=(252,90,90), fgcolor=(255,255,255) )
        self.quitBtn    = pygbutton.PygButton( (self.width/2-125, self.height/2+125, 250, 90), 'QUIT',  bgcolor=(255,90,90), fgcolor=(255,255,255) )

    #Update the display and show the menu buttons
    def update_display(self):
        self.backgroundColor = 252,90,90
        self.screen.fill(self.backgroundColor)
        
        # draw btnz
        self.startBtn.draw(self.screen)
        self.helpBtn.draw(self.screen)
        self.quitBtn.draw(self.screen)

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
                if 'click' in self.startBtn.handleEvent(event):
                    print("start btn clicked!")
                if 'click' in self.helpBtn.handleEvent(event):
                    print("Help btn clicked!")
                
        #pygame.init()

        #size = (width, height) = (1024, 768)

        #backgroundColor = 252,90,90

        #screen = pygame.display.set_mode(size)
        #screen.fill(backgroundColor)
        #pygame.display.flip()
        
        #start button
        
        #help button
        
        #pygame.mixer.pre_init(44100, -16, 1, 512*2)
        #pygame.display.init()
        #pygame.font.init()
        #pygame.mixer.init(44100)
        #pygame.mouse.set_visible(False)

        """
        width = pygame.display.Info().current_w
        height = pygame.display.Info().current_h
        
        if(float(width)/float(height) == float(4)/float(3)):
            screenSize = (width,height)
        else:
            screenSize = (800,600)
        """
        #TextureLoader.screenSize =screenSize
        #self.scnHelp = SceneHelp(screenSize)
        """
        SoundManager.init()
        SoundManager.EVENT_MUSIC_BACKGROUND()
        
        
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
