import sys
import os
			
class konica_minolta_printer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "search" : 'headers[server]", "version" : '/^LPC Http Server\/V([^\s]+)/ }
			{ "model" : '/<head><meta http-equiv=content-type content=text\/html; charset=[^\s^>]+><TITLE>KONICA MINOLTA .+ ([^<^\s]+)<\/TITLE>/ }
			{ "url" : '/wcd/js_error.xml", "text" : '<?xml-stylesheet href="js_error.xsl" type="text/xsl"?>' }
			{ "text" : '<meta http-equiv="refresh" content="0; URL=/wcd/js_error.xml">' }
	]

