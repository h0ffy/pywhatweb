import sys
import os
			
class myhobbysite_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : ' (Powered by MyHobbySite)</title>' },
			{ "text" : '					<!-- Removing the copyright notice without purchasing the MyHobbySite Copyright Removal License voids the MyHobbySite End User License Agreement -->' },
			{ "text" : '		<a name="top"></a> <!-- Necessary for the "jump to the top of the page" links -->' },
			{ "version" : '/Powered by <a href="http:\/\/www.myhobbysite.net" target="_blank">MyHobbySite<\/a> ([\d\.]+) / },
		]

