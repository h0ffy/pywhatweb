import sys
import os
			
class Pluginmeitrack_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "var _TrackerMain_GTVTSeries = "GT Series\\\\VT Series";'},
			{ "text" : "<form name="form1" method="post" action="trackerlogin.aspx" id="form1">" },
		]
		return(self.rules)

