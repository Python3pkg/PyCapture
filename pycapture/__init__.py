# PyCapture: Take a screenshot from Python Script(Only Mac)
# Apache license
# Manato0x2cc manato0x2cc@gmail.com (Send me feedback & suggestions!)

__version__ = '0.0.0'

try:
    import pyautogui as pa
except ImportError:
    pass

import subprocess

from random import randint

#The Mac's Menubar's height
MAC_MENUBAR_HEIGHT = 22
#short ver
MMH = MAC_MENUBAR_HEIGHT

s_size = pa.size()

def capture(fileName=None, region=None, mouseMotion=False, sound=False, cursor=False):
    """

    Description: Take a screenshot as fileName.

    Args:
      fileName (string)   - If None, The Image Name is PyCapture-(random-int).png.
      region (list)       - If None, This takes a full-screen screenshot. The list must be [x,y,width,height].
      mouseMotion (bool)  - If True, This control mouse to drag region
      sound (bool)        - If True, This sounds the shutter.
      cursor (bool)       - If True, The Mouse cursor appears on the screenshot

    """

    #Command
    cmd = ["screencapture"]


    if fileName == None:
        fileName = "PyCapture-"+str(randint(100000,1000000))


    #If region is undefined
    if region == None:
        region = [0,0,s_size[0],s_size[1]]


    #If region is wrong
    elif not len(region) == 4:
        region = [0,0,s_size[0],s_size[1]]


    #If not hope to play sounds
    if not sound:
        cmd.append("-x") #do not play sounds


    if cursor:
        cmd.append("-C") #capture the cursor as well as the screen.


    if mouseMotion:
        cmd.append("-i")# capture screen interactively, by selection or window


        cmd.append(fileName)# where to save the screen capture, 1 file per screen


        #Execute screencapture command with PIPE
        stdout = subprocess.Popen(cmd, stdout=subprocess.PIPE)


        #Move Mouse Carsor to lefttop
        pa.moveTo(region[0], region[1], 0.1)


        #Drag Mouse Carsor to right bottom
        pa.dragTo(region[0]+region[2], region[1]+region[3], 3)


        #Take a screeenshot
        pa.click()

        #Exit screencapture command
        stdout.stdout.close()

        return

    else:
        #Region list to
        strdata = ",".join([str(x) for x in region])

        cmd.append("-R"+strdata)# capture screen rect

        cmd.append(fileName)# where to save the screen capture, 1 file per screen

        subprocess.check_output(cmd)# Execute Command


def size():
    return s_size
