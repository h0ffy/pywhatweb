import sys
import os
			
class Pluginmjniohttpdaemon_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^MJNioHttpDaemon\/([^\s]+)/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/MJNIOHTTPDSESSIONID=/" },
		]

