import sys, pygame
import os


class Game24(object):

    STATE_MENU = 0
    STATE_GAME = 1
    STATE_WIN_SCREEN =2
    STATE_HELP = 3
    
    def __init__(self):
        self.screenSize = (self.width, self.height) = (1024, 768)
        self.backgroundColor = 252,90,90
        
        pygame.mixer.pre_init(44100, -16, 1, 512*2)
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init(44100)
        pygame.mouse.set_visible(False)
        """
        width = pygame.display.Info().current_w
        height = pygame.display.Info().current_h
        
        if(float(width)/float(height) == float(4)/float(3)):
            screenSize = (width,height)
        else:
            screenSize = (800,600)
        """
        #TextureLoader.screenSize =screenSize
        self.screen = pygame.display.set_mode(self.screenSize, pygame.FULLSCREEN)
        self.screen.fill(self.backgroundColor)
        pygame.display.flip()
        
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
  
    #def main(self):
        #pygame.init()

        #size = (width, height) = (1024, 768)

        #backgroundColor = 252,90,90

        #screen = pygame.display.set_mode(size)
        #screen.fill(backgroundColor)
        #pygame.display.flip()
        
        #start button
        
        #help button
    
game = Game24()
#game.main()
