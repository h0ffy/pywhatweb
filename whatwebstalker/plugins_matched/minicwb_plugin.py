import sys
import os
			
class minicwb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="Author" content="GraFX srl - http://www.grafxsoftware.com" />' },
			{ "text" : '<!--Copyright link. You may not remove it if you use free GPL licence. Refer to ./LICENSE file for more-->' },
			{ "text" : '<p>Powered by <a href="http://www.grafxsoftware.com/" class="text" title="Powered by CWB - small Open CMS - Content Management System">CWB</a>' },
			{ "text" : '<a href='http://www.mini-open-cms.com' rel='external'>Powered by miniCWB</a>" },
		]

