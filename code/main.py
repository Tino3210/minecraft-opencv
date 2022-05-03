# import folder image
from diamondFinder import *
from movePlayer import *

if __name__ == "__main__":

    diamond_finder = DiamondFinder()
    player = Player()

    run = True
    while (run):
        if diamond_finder.is_diamond():
            print("Diamond ",diamond_finder.getPosition())
            player.stop()
        
        # if diamond_finder.is_lava():
        #     print("Lava : ", diamond_finder.getPosition())
        #     player.step_back()

        if keyboard.is_pressed('§'):
            player.stop('w')
            player.stop('o')
            run = False
        player.move()
        player.mining()
        player.place_torch()
        time.sleep(1)
