import sys
import os
			
class sx_shop_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<a href="http:\/\/www.source-worx.de[^>]+>powered[\s]+by sX-Shop<\/a>/ }
			{ "text" : '<meta name="author" content="Source WorX - Software Development">' }
			{ "text" : 'alert("Ihr Suchbegriff muss mind. aus 3 Zeichen bestehen.");' }
	]

