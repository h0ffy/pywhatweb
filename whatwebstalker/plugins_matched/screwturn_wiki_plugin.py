import sys
import os
			
class screwturn_wiki_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/Powered by <a class="externallink" href="http:\/\/www\.screwturn\.eu" title="ScrewTurn Wiki" target="_blank">ScrewTurn Wiki<\/a> version ([\d\.]+)/ },
		]

