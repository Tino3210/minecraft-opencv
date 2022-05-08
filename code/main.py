# import folder image
from diamondFinder import *
from movePlayer import *
import keyboard

if __name__ == "__main__":

    diamond_finder = DiamondFinder()
    player = Player()

    run = True
    while (run):
        diamond_finder.capture()
        if diamond_finder.is_diamond():
            player.stop()
            dim = diamond_finder.get_position_diamond()
            print("Diamond ", dim)
            while ((-10 <= dim[0] <= 10) and (-10 <= dim[0] <= 10)):
                dim = diamond_finder.get_position_diamond()
                if (dim[0] == -1):
                    break
                player.focusOnDiamond(dim)

            player.mining()

        if diamond_finder.is_lava():
            print("Lava : ", diamond_finder.get_position_lava())
            player.step_back()

        if keyboard.is_pressed('§'):
            player.stop('w')
            player.stop('o')
            run = False
        player.move()
        player.mining()
        player.place_torch()