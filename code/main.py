# import folder image
from diamondFinder import *
from movePlayer import *
import keyboard

if __name__ == "__main__":

    diamond_finder = DiamondFinder(name='Minecraft 1.18.2 - Singleplayer')
    player = Player()

    run = True
    while (run):
        diamond_finder.capture()
        if diamond_finder.is_diamond():
            player.stop()
            dim = diamond_finder.get_position_diamond()
            print("Diamond ", dim)
            player.focusOnDiamond(dim)
            
            for i in range(5):
                diamond_finder.capture()
                diamond_finder.is_diamond()
                dim = diamond_finder.get_position_diamond()
                player.focusOnDiamond(dim)
            
            player.mining()
            time.sleep(0.8)
            player.stop()
            time.sleep(5)

        if diamond_finder.is_lava():
            print("Lava : ", diamond_finder.get_position_lava())
            player.step_back()

        if keyboard.is_pressed('§'):
            player.stop()
            run = False
        player.move()
        player.mining()
        player.place_torch()