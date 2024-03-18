import sys
import os
			
class mission_control_application_shield_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<img id="logo" src="/srm-error-pages/images/logo.gif" alt="mission control application shield" ></td><td><p class="notification">Notification</p></td>' }
			{ "search" : 'headers[server]", "regexp" : '/^Mission Control Application Shield$/ }
		]

