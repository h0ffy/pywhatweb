import sys
import os
			
class Pluginkontaktformular_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!--Copyright darf NICHT entfernt werden!!-->" },
			{ "text" : "<!-- Hinweis darf nicht entfernt werden! -->" },
			{ "text" : "Script Powered by <a target="_blank" href="http://www.radbekleidung.eu/gratis-kontaktformular.html">Kontaktformular</a>" },
			{ "text" : "&copy; Script Powered by kontaktformular.org </span>" },
		]
		return(self.rules)

