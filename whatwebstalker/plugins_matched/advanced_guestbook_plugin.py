import sys
import os
			
class advanced_guestbook_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "ghdb" : 'intitle:guestbook "advanced guestbook 2.2" powered'}
			{ "certainty" : '75", "text" : 'Thank you for stopping by my site. Here you can leave your mark."}
			{ "name" : 'powered by", "version" : '2.2", "regexp" : '/<b>Advanced Guestbook 2.2<br>\s+Powered by PHP}
	]

