# import folder image
from image import capture, diamondFinder

if __name__ == "__main__":
    
    diamond_finder = diamondFinder.DiamondFinder()
    
    while (True):
        if diamond_finder.isDiamond():
            print(diamond_finder.getPosition())