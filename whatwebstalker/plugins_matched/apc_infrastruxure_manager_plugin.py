import sys
import os
			
class Pluginapc_infrastruxure_manager_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<title>APC | InfraStruXure Manager</title>" },
			{ "text" : "<td align="center" width="725" height="72"><img src="images/ldrISX.jpg" alt="ISX Manager" align="left" border="0"/></td>" },
			{ "text" : "<td><img src="images/Xlogo_Layer-1.gif" height="327" width="342" align="left"/></td>" },
		]
		return(self.rules)

