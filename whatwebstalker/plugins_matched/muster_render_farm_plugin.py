import sys
import os
			
class Pluginmuster_render_farm_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<body onLoad="init_page()" name="muster_login" >" },
			{ "url" : "/dologin.html", "version" : "/<title>Muster ([\d]+) Integrated Web server login<\/title>/" },
			{ "text" : "<applet code="FileFolderSelector.class" archive="FileFolderSelector.jar" CODEBASE="js" id="FileSelector" name="FileSelector" width="1" height="1">" },
			{ "search" : "headers[server]", "version" : "/^cias-muster([\d])$/" },
		]

