import sys
import os
			
class portalapp_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : "/<img src='[\/]*images\/palogo_gr_17.gif' height=23 alt='powered by PortalApp' align=[\'|\"]*[center|middle]+[\'|\"]*><\/A>/" },
			{ "regexp" : "/<meta name=[\'|\"]*generator[\'|\"]* content=[\'|\"]*aspapp.com[\'|\"]*[\ \/]*>/" },
		]

