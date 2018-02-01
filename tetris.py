'''
Created on Feb 1, 2018

@author: student
'''
'''
@author:21_Century_RavenRen 
'''

import pygame, sys, os, math
from SpriteHelper import SpriteSheet
from pygame.locals import *
from random import randint

class Button:
    imgUp = None
    imgDown = None
    imgOver = None
    state = False
    x = 0
    y = 0

    def __init__(self,imgUp,imgDown,imgOver,x,y):
        self.imgUp = imgUp
        self.imgDown = imgDown
        self.imgOver = imgOver
        self.x = x
        self.y = y
        self.image = self.imgUp
        
    def getCollider(self):
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect
    
    def mouseOver(self):
        self.image = self.imgOver
        self.state = False
        
    def mouseDown(self):
        self.image = self.imgDown
        self.state = True
        
    def mouseOut(self):
        self.image = self.imgUp
        self.state = False
        
        
    def update(self):
        collider = self.getCollider()
        mouseLoc = pygame.mouse.get_pos()
        mouseLoc = pygame.Rect(mouseLoc[0],mouseLoc[1],5,5)
        mouseState = pygame.mouse.get_pressed()
        if collider.colliderect(mouseLoc):
            if mouseState[0]:
                self.mouseDown()
            else:
                if self.state==True:
                    self.state = False
                    self.click()
                self.mouseOver()
        else:
            self.mouseOut()
    
    def draw(self,surface):
        surface.blit(self.image,(self.x,self.y))
        
class Game:
    #####Variable#####
    WINDOWWIDTH = 1024
    WINDOWHEIGHT = 768
    GAMENAME = "TETRIS: War of the Fandoms"
    FRAMERATE = 60
    BGCOLOR = (128,0,0)
    playing = True
    
    #####Constructor#####
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(
            (self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption(self.GAMENAME)
        
    def main(self):
        buttonSpriteSheet = SpriteSheet("button-start-spritesheet.png")
        buttonUp = buttonSpriteSheet.get_image(0,0,200,72)
        buttonDown = buttonSpriteSheet.get_image(0,72,200,72)
        buttonOver = buttonSpriteSheet.get_image(0,144,200,72)
        centerX = self.WINDOWWIDTH/2
        centerY = self.WINDOWHEIGHT/2
        buttonRect = buttonUp.get_rect()
        buttonWidth = buttonRect.width
        buttonHeight = buttonRect.height
        buttonCenterX = centerX-buttonWidth/2
        buttonCenterY = centerY-buttonHeight/2
        
        self.startButton = Button(
            buttonUp,buttonOver,buttonDown,buttonCenterX,buttonCenterY)
        #####Game Loop#####
        while self.playing:
            delta=self.clock.tick(self.FRAMERATE)
            self.startButton.update()
                        #####Event Handeling#####
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.quit()
            self.draw()
            pygame.display.flip()
   
    def quit(self):
        pygame.quit()
        sys.exit()
    
    def draw(self):
        self.surface.fill(self.BGCOLOR)
        self.startButton.draw(self.surface)
        
if __name__=="__main__":
        game = Game()
        game.main()
