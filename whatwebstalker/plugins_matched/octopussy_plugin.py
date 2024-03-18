import sys
import os
			
class Pluginoctopussy_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<input type="submit" name="submit" value="Connect to Octopussy"></td>" },
			{ "version" : "/<td class="box" align="center" >Octopussy ([^\s^<]+)<\/td>/" },
			{ "text" : "<img border="0" src="IMG/octo_login1.png" alt="Octopussy Logo"></td>" },
			{ "text" : "<title>Octopussy Login</title>" },
			{ "text" : "<link rel="icon" type="image/gif" href="IMG/octopussy.gif">" },
		]

