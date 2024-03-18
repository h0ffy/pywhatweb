import sys
import os
			
class snom_phone_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'copyright snom.com", "regexp" : '/&copy; 2000-20[0-9]+ <a href="http:\/\/snom.com">snom AG<\/a><br>/ }
			{ "name" : 'link to manual1", "regexp" : '/<tr><td class="flyoutLink" colspan="2"><b><a href=http:\/\/(wiki|www).snom.com/ }
			{ "text" : 'You can enter a simple telephone number (e.g. 0114930398330) or URI like info@snom.com.' }
			{ "certainty" : '75", "regexp" : '/<td[^>]+>Welcome to Your Phone!<\/td>/ }
	]

