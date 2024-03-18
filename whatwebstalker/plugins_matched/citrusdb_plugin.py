import sys
import os
			
class Plugincitrusdb_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<INPUT TYPE="SUBMIT" NAME="submit" VALUE="Login"  onclick="password.value = calcMD5(password.value)" class=smallbutton>" },
			{ "certainty" : "75", "text" : "<center><table><td valign=top><img src="images/my-logo.png">" },
		]
		return(self.rules)

