import sys
import os
			
class oracle_real_user_experience_insight_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<title>Oracle Real User Experience Insight \-\[ ([^\s]+@[^\s]+) \]\-<\/title>/ },
			{ "version" : '/<title>Oracle Real User Experience Insight \-\[ ([\d\.a-z]+) \]\-<\/title>/ },
			{ "version" : '/<div class="windowWatermark">Version: ([^\s]+)/ },
			{ "url" : '/ruei/rpc.php", "text" : '{"retval":false,"error_' },
		]

