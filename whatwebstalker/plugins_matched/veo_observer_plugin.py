import sys
import os
			
class Pluginveo_observer_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Veo Observer XT</title>", "version" : "XT" },
			{ "text" : "  <frame src="/en/sitemonitor.html" name="sitecheck" scrolling="NO" noresize>", "version" : "XT" },
			{ "text" : "		<title>Veo Observer Web Client</title>", "version" : "XNC" },
			{ "text" : "		<object classid="clsid:0957C19A-D854-482A-A4F9-18856C723D7D" id="VeoNetCamAcx" width="0" height="0" codebase="XNC600NetCam.cab#version", "version" : "XNC" },
		]
		return(self.rules)

