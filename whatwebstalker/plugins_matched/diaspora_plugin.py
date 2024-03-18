import sys
import os
			
class diaspora_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[set-cookie]", "regexp" : "/_diaspora_session=/" },
			{ "search" : "headers[x-git-update]", "string" : /^([\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2} .+)$/" },
			{ "search" : "headers[x-git-revision]", "regexp" : "/^[a-f\d]{32}$/" },
			{ "text" : "<input name="user[remember_me]" type="hidden" value="0" /><input id="user_remember_me" name="user[remember_me]" type="checkbox" value="1" />" },
		]

