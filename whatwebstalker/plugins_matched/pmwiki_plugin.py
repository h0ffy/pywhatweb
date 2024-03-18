import sys
import os
			
class pmwiki_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[set-cookie]", "regexp" : '/imstime=[\d]+;/ }
			{ "text" : '<!--PageLeftFmt-->' }
			{ "text" : '<span class='commentout-pmwikiorg'>" }
			{ "regexp" : '/<link rel='stylesheet' href='[^']*\/pmwiki\/pub\/skins\/pmwiki\/pmwiki\.css' type='text\/css' \/>/ }
	]

