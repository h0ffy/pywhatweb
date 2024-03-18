import sys
import os
			
class hughes_voice_appliance_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<HTML><HEAD></HEAD><BODY onload="window.location=\'/fs/home.htm\'"></BODY></HTML>' }
			{ "text" : '<head><title>HughesNet Appliance Control Center</title></head>' }
			{ "url" : '/systeminfo/", "version" : '/<td width='50%'>Main\.bin Version<\/td><td width='50%' align='center'>([^<^\s]+)<\/td>/ }
	]

