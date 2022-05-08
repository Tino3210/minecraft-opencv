from time import sleep
import pydirectinput
import time

class Player:
    '''
    The Player class is used to move the player and to mine the diamond
    '''
    def __init__(self):
        self._isMoving = True
        self._isMining = True
        self._durationTorch = 20

    @property
    def isMoving(self):
        return self._isMoving

    @isMoving.setter
    def isMoving(self, value):
        self._isMoving = value

    def place_torch(self):
        '''Stop the player and place a torch evry 5 seconds'''
        self._durationTorch -= 1
        if(self._durationTorch < 0):
            self._durationTorch = 20
            self.stop()
            time.sleep(1)
            pydirectinput.moveRel(700, 0)
            pydirectinput.rightClick()
            pydirectinput.moveRel(-700, 0)
            self._isMining = True
            self._isMoving = True

    def mining(self, key='o'):
        '''Mining the diamond'''
        pydirectinput.keyDown(key)

    def focusOnDiamond(self, position):
        '''Move the mouse to the diamond position'''
        pydirectinput.moveRel(position[0], position[1])
    
    def move(self, direction='w'):
        '''Move the player forward'''
        pydirectinput.keyDown(direction)

    def step_back(self, key='s'):
        '''Step back the player to avoid the lava'''
        self.stop()
        pydirectinput.keyDown(key)
        time.sleep(3)
        pydirectinput.keyUp(key)
            
    def stop(self, keyW='w', keyClic='o'):
        '''Stop the player'''
        pydirectinput.keyUp(keyW)
        pydirectinput.keyUp(keyClic)