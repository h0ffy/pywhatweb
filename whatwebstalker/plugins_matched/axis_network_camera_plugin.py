import sys
import os
			
class Pluginaxis_network_camera_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<TITLE>AXIS Video Server</TITLE>" },
			{ "text" : "<FRAME NAME="WhatEver" SRC="/incl/whatever.shtml" SCROLLING=NO MARGINGHEIGHT=0 MARGINWIDTH=0>" },
			{ "text" : "	<FRAME NAME="Trash" SRC="/view/trash.shtml" SCROLLING=NO MARGINGHEIGHT=0 MARGINWIDTH=0>" },
			{ "text" : "      <FRAME NAME="Temp" SRC="/view/temp.shtml" SCROLLING=NO MARGINGHEIGHT=0 MARGINWIDTH=0>" },
			{ "text" : "Your browser has JavaScript turned off.<br>For the user interface to work effectively", "you must enable JavaScript in your browser and reload/refresh this page." },
			{ "text" : "<img SRC="/pics/AxisLogo.gif" WIDTH="95" HEIGHT="40" BORDER="0" ALIGN="right" ALT="" },
			{ "model" : "/<TITLE>Live View \/? - AXIS ([^<]*) Video Server<\/TITLE>/i", "module" : "Live View" },
			{ "model" : "/<TITLE>Axis ([0-9]+)[^<]*Network Camera[^<]*<\/TITLE>/i },
			{ "version" : "/<TITLE>Axis [0-9]+[^<]*Network Camera ([\d\.]+)<\/TITLE>/i },
			{ "version" : "/<TITLE>Live View \/? - AXIS [\da-z]+ [^<]*version ([\d\.]+)<\/TITLE>/i", "module" : "Live View" },
			{ "model" : "/<TITLE>Live View \/? - AXIS ([\da-z]+) [^<]*<\/TITLE>/i", "module" : "Live View" },
		]

