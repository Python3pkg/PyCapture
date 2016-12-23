import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pycapture as pc

#Test App's WIDTH
WIDTH = 1000

#Test App's HEIGHT
HEIGHT = 600

#To take a screenshot without title
T_HEIGHT = 22

#To take a screenshot without Mac's Menubar and Docks
M_D_HEIGHT = 22+50

top = []

def main():
	# Calc the test App the top of left
	calcTestAppTop()

	pc.capture("test.png",[top[0], top[1], WIDTH, HEIGHT],mouseMotion=True)

def calcTestAppTop():
    #Get Display size
    size = pc.size()

    #Test game appears on Center
    top.append(int((size[0] - WIDTH) / 2)) #X
    top.append(int((size[1] - (HEIGHT + M_D_HEIGHT)) / 2 + 20)) #Y

if __name__ == '__main__':
	main()
