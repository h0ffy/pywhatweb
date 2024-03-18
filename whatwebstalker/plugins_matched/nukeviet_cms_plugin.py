import sys
import os
			
class nukeviet_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<meta name="generator" content="Nuke[vV]iet v([^\s^"]+)" \/>/ },
			{ "text" : '<div id="run_cronjobs" style="visibility: hidden; display: none;">' },
			{ "regexp" : '/<form class="loginform" method="post" action="[^"^>]*\/admin\/index\.php" onsubmit="return nv_checkadminlogin_submit\(\);">/ },
		]

