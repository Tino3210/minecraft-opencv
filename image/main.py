# import folder image
from diamondFinder import * 


if __name__ == "__main__":
    
    diamond_finder = DiamondFinder()
    
    while (True):
        if diamond_finder.isDiamond():
            print(diamond_finder.getPosition())