import sys
import os
			
class dvwa_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '		<title>Damn Vulnerable Web App (DVWA) - Login</title>' }
			{ "regexp" : '/		<link rel="stylesheet" type="text\/css" href="[^"]*dvwa\/css\/login.css" \/>/ }
			{ "text" : '			<p><label for="pass">Password</label><input type="password" AUTOCOMPLETE="off" size="20" name="password"></p><br />' }
		]

