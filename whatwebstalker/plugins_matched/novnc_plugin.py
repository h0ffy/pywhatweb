import sys
import os
			
class Pluginnovnc_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "module" : "Auto", "text" : "<div id="VNC_status_bar" class="VNC_status_bar" style="margin-top: 0px;">" },
			{ "module" : "Auto", "string" : /<html>[\s]+<!-- [\s]+noVNC Example: Automatically connect on page load\.[\s]+Copyright \(C\) (20[\d]{2}) Joel Martin[\s]+Licensed under LGPL-3 \(see LICENSE\.txt\)[\s]+Connect parameters are provided in query string:[\s]+http:\/\/example\.com\/\?host=HOST&port=PORT&encrypt=1&true_color=1[\s]+-->[\s]+<head>[\s]+<title>noVNC<\/title>/" },
			{ "module" : "Simple", "string" : /<html>[\s]+<!-- [\s]+noVNC example: simple example using default UI[\s]+Copyright \(C\) (20[\d]{2}) Joel Martin[\s]+Licensed under LGPL-3 \(see LICENSE\.txt\)[\s]+-->[\s]+<head>[\s]+<title>noVNC<\/title>/" },
		]

