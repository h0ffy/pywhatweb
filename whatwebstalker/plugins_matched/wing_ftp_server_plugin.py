import sys
import os
			
class wing_ftp_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : "headers[server]", "string" : /^Wing FTP Server\/([\d\.]+)\(([^\)]*)\)$/", "offset" : "1 },
			{ "search" : "headers[server]", "string" : /^Wing FTP Server\(([^\)]*)\)$/" },
			{ "search" : "headers[server]", "version" : "/^Wing FTP Server\/([\d\.]+)\(([^\)]*)\)$/" },
			{ "url" : "/help_javascript.htm", "text" : "<p>JavaScript is a scripting language that works with your browser to create interactive elements in web pages. The web client depend on JavaScript to function properly. </p>" },
		]

