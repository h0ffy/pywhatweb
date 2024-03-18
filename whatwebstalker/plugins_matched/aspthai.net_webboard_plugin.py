import sys
import os
			
class aspthai.net_webboard_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<meta name="copyright" content="Copyright (C) 2002-2005 Supap Wanawan" />" },
			{ "version" : "/  <br \/><br \/><span class="text" style="font-size:10px">Powered by <a href="http:\/\/www.aspthai.net\/" target="_blank" style="font-size:10px">ASPThai.Net Webboard<\/a> version ([\d\.]+)<\/span><br \/>/" },
			{ "version" : "/<!-- ASPThai.Net Webboard ver. ([\d\.]+) is written and produced by Supap Wanawan/" },
		]

