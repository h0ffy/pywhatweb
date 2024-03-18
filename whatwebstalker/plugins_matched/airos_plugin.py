import sys
import os
			
class Pluginairos_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "cache_images(['main_top.png", "'main.png", "'link.png", "'net.png", "'4dv.png", "'srv.png", "'system.png", "'border.gif", "'spectr.gif']);" },
		]

