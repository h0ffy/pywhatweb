import sys
import os
			
class Pluginakiva_webboard_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- --- AKIVA COPYRIGHT NOTICE --- -->" },
			{ "text" : "<!-- Under the terms of the WebBoard License Agreement -->" },
			{ "text" : "<!-- wbmain 8/22/2005 11:11AM -->" },
			{ "text" : "<img src="images/branding-bottom.gif" width="46" height="44" alt="Powered by WebBoard">" },
			{ "version" : "/<td class="botBrandingLeft"  nowrap >Powered by <a href="http:\/\/get\.webboard\.com\?pid=WB80&sid=9999999999999" target="_blank" class="topicsSmallLink">WebBoard ([\d])<\/a><br>&copy;20[\d]{2} Akiva Corporation/" },
		]
		return(self.rules)

