import sys
import os
			
class Pluginwebsidestory_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- WebSideStory HTML for Search -->" },
			{ "text" : "<!--END WEBSIDESTORY CODE-->" },
			{ "regexp" : "/<!--COPYRIGHT 1997-[0-9]{4} WEBSIDESTORY,INC. ALL RIGHTS RESERVED. U.S.PATENT No. 6,393,479B1. MORE INFO:http:\/\/websidestory.com\/privacy-->/" },
			{ "version" : "/<!--WEBSIDESTORY CODE ([^\ ]+) /" },
			{ "text" : "Search powered by <a class="external" href="http://www.websidestory.com/">WebSideStory</a>" },
			{ "text" : "<a href="http://websidestory.com/" target="_blank">Powered by WebSideStory</a>" },
		]

