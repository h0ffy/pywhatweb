import sys
import os
			
class hp_officejet_printer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "model" : '/<title>HP Officejet ([^<]+)<\/title>.*<body onLoad="window.top.location.href='.\/index.htm\?cat=info&page=printerInfo/m }
			{ "model" : '/<title>HP Officejet (Pro [A-Z0-9a-z ]+)<\/title>.*(home.htm\?cat=home&page=home|printerFrame.htm)/m}
			{ "text" : 'index.htm?cat=info&page=printerInfo'}
			{ "certainty" : '25", "text" : 'home.htm?cat=home&page=home'}
	]

