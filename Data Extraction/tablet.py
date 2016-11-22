import os
import random

from cgkit import wintab
from cgkit.wintab.constants import *

class Tablet(object):
    """
    Tablet object for use in PyGame, for capturing tablet position, buttonpress,
    and pressure.
    """

    def __init__(self, screen, hwnd=None):
        

        # There is probably a much smarter way than this, but I havn't figured
        # it out yet....
        if hwnd == None:
            self.hwnd = random.randint(1024, 16777216)
        else:
            self.hwnd = int(hwnd)

        os.environ["SDL_WINDOWID"] = str(hwnd)

        self.context = wintab.Context()
        # Define the type of data we want the Packets to return:
        self.context.pktdata = ( PK_X | PK_Y | PK_BUTTONS | PK_NORMAL_PRESSURE  )
        self.context.open(self.hwnd, True)

        self.prevBut = 0
        self.prevX = 0
        self.prevY = 0
        self.prevPressure = 0
        self.updateScreen(screen)

    def updateScreen(self, screen):
        """
        Should be used if the PyGame Screen is resized to update tablet mapping.
        """
        self.screensize = screen.get_size()
        # Define how we need to scale our vals so they map to the pygame screen:
        self.xfactor = float(self.screensize[0]) / float(self.context.inextx)
        self.yfactor = float(self.screensize[1]) / float(self.context.inexty)

    def getData(self):
        """
        Can be called to every loop to capture the tablet info.

        return : tuple of four values:
            (int ID of button pressed, int x pos, int y pos, int pressure)
            Pressure is mapped from 0->1023
        """
        packetExtents = self.context.queuePacketsEx()
        if packetExtents[1] is not None:
            # This is a sub-list of Packet objects:
            packets = self.context.packetsGet(packetExtents[1])
            # Get the last Packet object:
            packet = packets[-1]

            # Capture packet info, and pressure data:
            buttons = packet.buttons
            x = packet.x * self.xfactor
            # Y axis is opposite for tablet and pygame:
            y = self.screensize[1] - (packet.y * self.yfactor)
            pressure = packet.normalpressure

            # fill our "previous" values in case the user takes the pen away
            # from the PyGame screen:
            self.prevBut = buttons
            self.prevX = int(x)
            self.prevY = int(y)
            self.prevPressure = pressure
            return (buttons, int(x), int(y), pressure)
        else:
            return(self.prevBut, self.prevX, self.prevY, self.prevPressure)
