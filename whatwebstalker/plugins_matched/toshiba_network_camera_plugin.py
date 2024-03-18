import sys
import os
			
class toshiba_network_camera_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<title>TOSHIBA Network Camera - User Login</title>" },
			{ "text" : "    <td height="32"><img src="toshiba.gif" width="68" height="12"><font class="netcam"><strong>&nbsp;&nbsp;Network Camera</strong></font></td>" },
		]

