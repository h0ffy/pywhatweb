import sys
import os
			
class Pluginjetty_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Jetty(\/|\()([^\s^\)]+)/", "offset" : "1 },
			{ "search" : "headers[servlet-engine]", "module" : /^(Jetty\/[^\s]+)/" },
			{ "url" : "/", "text" : "<A HREF="http://jetty.mortbay.org"><IMG SRC="jetty_banner.gif"></A>" },
			{ "text" : "<p><i><small><a href="http://jetty.mortbay.org">Powered by Jetty://</a></small></i></p>" },
		]
		return(self.rules)

