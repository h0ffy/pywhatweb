import sys
import os
			
class zest_web_engine_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/Powered by the <br \/><img src='http:\/\/www.[^\/]+\/images\/zestlogo\.gif' style='border:0 ; ' alt='Zest Web Engine' \/><br \/>Zest web engine<br \/>V([\d\.]+)<br \/>/ },
			{ "search" : 'headers[location]", "text" : '/cgi-bin/web.asp?title"},
			{ "text" : 'Powered by the <a href='http://www.zest-leisure.com/'>Zest Web Engine</a>"},
			{ "version" : '/Powered by the <a href='http:\/\/www.zest-leisure.com\/'>Zest Web Engine<\/a>[ ]+V ([0-9\.]+)<},
		]

