import sys
import os
			
class sony_network_camera_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '	setWindowVar = window.open("/adm/file.cgi?next_file=setting.htm", "adminWin", "setWinoptions);", "model" : '["SNC-M"] },
			{ "text" : '<TITLE>Server Push Viewer</TITLE>' },
			{ "regexp" : '/<FRAME SRC="bar.html" SCROLLING="NO" NAME="sonyhome[0-9]*" NORESIZE[\ MARGINHEIGHT="0-9"]* MARGINWIDTH="0">/i },
			{ "model" : '/<TITLE>Sony Network Camera ([0-9A-Z\-]+)<\/TITLE>/i },
			{ "model" : '/<TITLE>(SNC\-[R]?Z[0-9]+)<\/TITLE>/ },
			{ "model" : '/<TITLE>(SNC\-[R]?Z[0-9]+) HOME<\/TITLE>/ },
		]

