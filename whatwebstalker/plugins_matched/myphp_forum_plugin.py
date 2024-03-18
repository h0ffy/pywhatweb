import sys
import os
			
class myphp_forum_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/    <td width="50%" class="copy" height="24">Powered by: MyPHP Forum v([\d\.]+)/" },
			{ "version" : "/    <td width="50%" class="copy" height="24">Powered by: <a href="http:\/\/www.myphp.ws">MyPHP Forum v([\d\.]+)/" },
		]

