import sys
import os
			
class webpa_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<td align="right"><div id="inst_logo"><img src="[^"]+" alt="([^"]*)" \/><\/div>/ },
			{ "regexp" : '/<iframe src="https?:\/\/[^\/]+\/keep_alive\.php" height="1" width="1" style="display: none;">keep alive<\/iframe>/ },
			{ "md5" : '4bfb4898e9927666d6d5a35c7570a960", "url" : '/images/tool/appbar_webpa_logo.png" },
		]

