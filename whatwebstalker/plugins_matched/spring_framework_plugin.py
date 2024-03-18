import sys
import os
			
class Pluginspring_framework_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "text" : "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=" },
		]
		return(self.rules)

