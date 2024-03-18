import sys
import os
			
class Pluginportalapp_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<img src='[\/]*images\/palogo_gr_17.gif' height=23 alt='powered by PortalApp' align=[\'|\"]*[center|middle]+[\'|\"]*><\/A>/" },
			{ "regexp" : "/<meta name=[\'|\"]*generator[\'|\"]* content=[\'|\"]*aspapp.com[\'|\"]*[\ \/]*>/" },
		]
		return(self.rules)

