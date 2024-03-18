import sys
import os
			
class Pluginkontaktformular_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!--Copyright darf NICHT entfernt werden!!-->" },
			{ "text" : "<!-- Hinweis darf nicht entfernt werden! -->" },
			{ "text" : "Script Powered by <a target="_blank" href="http://www.radbekleidung.eu/gratis-kontaktformular.html">Kontaktformular</a>" },
			{ "text" : "&copy; Script Powered by kontaktformular.org </span>" },
		]

