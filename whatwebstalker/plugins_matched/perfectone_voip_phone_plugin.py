import sys
import os
			
class Pluginperfectone_voip_phone_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<body OnLoad="JavaScript:document.loginform.user.focus();">" },
			{ "text" : "<p style="margin-top: 5px"><font face="Arial"><input type=submit value=\'Login\' onClick="return saveChanges()">" },
			{ "text" : "<font face="Arial" color="#FFFFFF"><b>Login VoIP</b></font></i></td> </tr>" },
		]
		return(self.rules)

