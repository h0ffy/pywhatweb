import sys
import os
			
class Pluginnetgear_print_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<title>NetGear Print Server Setup</title>" },
			{ "text" : "<p>To provide an enhanced user interface", "this Print Server uses JavaScript extensively." },
			{ "url" : "/start.htm", "text" : "<title>NETGEAR Print Server </title>" },
			{ "url" : "/settings.gif", "md5" : "d6b979c739a809658a0e8833bc64b900" },
			{ "certainty" : "25", "version" : "/^PRINT_SERVER WEB ([\d\.]+)$/", "search" : "headers[server]" },
		]

