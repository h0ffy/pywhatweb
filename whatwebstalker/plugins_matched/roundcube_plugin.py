import sys
import os
			
class roundcube_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>RoundCube Webmail :: Welcome to RoundCube Webmail</title>"}
			{ "text" : 'var rcmail = new rcube_webmail();"}
			{ "text" : '<input name="_user" id="rcmloginuser"'}
			{ "text" : '$(document).ready(function(){ rcmail.init(); });'}
	]

