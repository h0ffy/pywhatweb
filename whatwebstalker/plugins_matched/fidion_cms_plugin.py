import sys
import os
			
class Pluginfidion_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- ================== This site is powered by: ==================== -->" },
			{ "text" : "<!-- | fCMS by fidion GmbH", "Wüg.         http://www.fidion.de  | -->" },
			{ "text" : "<!-- fCMS-Template head.tpl begins -->" },
		]

