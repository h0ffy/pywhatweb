import sys
import os
			
class easylink_web_solutions_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Dieser Abschnitt darf nur mit Genehmigung des Entwicklers entfernt werden und bedarf einer' }
			{ "version" : '/<meta name="generator" content="easyLink v([\d\.]+)" \/>/ }
			{ "version" : '/[P|p]?owered by easyLink v([\d\.]+)/ }
		]

