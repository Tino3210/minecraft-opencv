from time import sleep
import pydirectinput
import keyboard
import time  

class Player:
    def __init__(self):
        self._isMoving = True
        self._isMining = True
        self._durationTorch = 5

    @property
    def isMoving(self):
        return self._isMoving

    @isMoving.setter
    def isMoving(self, value):
        self._isMoving = value

    def place_torch(self):
        if(self._isMoving):
            self._durationTorch -= 1
            if(self._durationTorch < 0):
                self._durationTorch = 5
                self.stop()
                time.sleep(1)
                pydirectinput.moveRel(700, 0)
                pydirectinput.rightClick()
                pydirectinput.moveRel(-700, 0)
                self._isMining = True
                self._isMoving = True
        

    def mining(self, key='o'):
        if(self._isMining):
            pydirectinput.keyDown(key)
    
    def move(self, direction='w'):
        if(self._isMoving):
            pydirectinput.keyDown(direction)
    
    def step_back(self, key='s'):
        self.stop()
        pydirectinput.keyDown(key)
        time.sleep(5)
        pydirectinput.keyUp(key)
    
    def stop(self, keyW = 'w', keyClic = 'o'):
        pydirectinput.keyUp(keyW)
        pydirectinput.keyUp(keyClic)
        self._isMining = False
        self._isMoving = False   
