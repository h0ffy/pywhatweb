import sys
import os
			
class fluid_dynamics_search_engine_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/Powered by the <a href="http:\/\/www.xav.com\/scripts\/search\/"[^>]*>Fluid Dynamics Search Engine<\/a> v([\d\.]+) &copy; 20[\d]{2}/ }
	]

