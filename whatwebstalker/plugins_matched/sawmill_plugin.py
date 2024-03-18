import sys
import os
			
class sawmill_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<tr><td>Username:<\/td><td>Administrator<input type="hidden" name="cgionly_authentication_username" value="([^\"]+)"><\/td><\/tr>/ },
			{ "text" : '<td><input id="password" class="username-psw text" type="password" value=" /><div id="password:error" class="form-error"></div></td>' },
			{ "search" : 'headers[server]", "version" : '/^Sawmill\/([^\s]+)/ },
		]

