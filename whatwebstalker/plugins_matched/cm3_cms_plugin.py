import sys
import os
			
class Plugincm3_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "JavaScript Object (CM2)',"text" : "top.cm2_home.location.href'},
			{ "name" : "HTML Body (CM2)',"text" : "name="cm2_top" id="cm2_top"'},
			{ "name" : "HTML Body (CM2)',"text" : "name="cm25_main"'},
			{ "name" : "HTML Body (CM3)',"text" : "name="id="cm3top" name="cm3top"'},
			{ "name" : "HTML Body (CM3)',"text" : "logo_cm3_top.gif" border="0"'},
			{ "name" : "HTML Body (CM3)',"text" : "alt="Content management system: cm3 built and powered"'},
			{ "name" : "HTML Body (CM3)',"text" : "cm3powered_green.gif"'},
			{ "name" : "Set-Cookie Header (CM3)", "search" : "headers[set-cookie]", "regexp" : "/cm3session},
		]
		return(self.rules)

