import sys
import os
			
class Pluginafterlogic_webmail_pro_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.afterlogic.com/products/webmail-pro" target="_blank">AfterLogic WebMail Pro</a><br />" },
			{ "version" : "/AfterLogic Corporation<\/a>\s?<\/div>\s+<\/body>\s<\/html>\s<!--\s?([\d\.]+)\s?-->/" },
			{ "version" : "/AfterLogic Corporation<\/a>\s?<\/div>\s+<!--\s?([\d\.]+)\s?-->\s<\/body>\s<\/html>/" },
			{ "name" : "PHPWEBMAILSESSID cookie", "search" : "headers[set-cookie]", "regexp" : "/^PHPWEBMAILSESSID=[^;]+;/" },
			{ "name" : "PHPWMADMINSESSID cookie", "search" : "headers[set-cookie]", "regexp" : "/^PHPWEBMAILSESSID=[^;]+;/" },
		]
		return(self.rules)

