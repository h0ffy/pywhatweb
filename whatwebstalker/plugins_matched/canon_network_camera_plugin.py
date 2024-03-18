import sys
import os
			
class canon_network_camera_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75,"ghdb" : 'intitle:liveapplet inurl:LvAppl'},
			{ "certainty" : '75,"ghdb" : '+intitle:"Network Camera VB-C50i/VB-C50iR" +"Viewer for PC"'},
			{ "text" : '<TITLE>Network Camera VB-C50i/VB-C50iR</TITLE>", "version" : ''VB-C50i'},
			{ "text" : 'function L(n,g) {var i=document.images[n]; if (i)I[n]=new H(i,i.src,"/v/"+g+".gif")}',"version" : 'VB-C50i"},
			{ "text" : 'function L(n,g) {var i=document.images[n];if (i)I[n]=new H(i,i.src,"/v/"+g+".gif")}',"version" : 'VB-C50i"},
			{ "text" : '<param name=cabbase	value="LiveApplet.cab">',"version" : 'WebView"},
			{ "text" : '<title>LiveApplet</title>',"version" : 'WebView"},
		]

