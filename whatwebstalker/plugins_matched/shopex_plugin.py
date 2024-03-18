import sys
import os
			
class shopex_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "regexp" : '/<title>[^<]* -- Powered by Shop(e|E)x<\/title>/ },
			{ "text" : '<p align=center><font color=black style='font-size:9pt;font-family:Arial'>Powered by </font><a href='http://www.shopex.cn' target='_blank'><font color=navy style='font-size:9pt;font-family:Arial;text-decoration:under-line'>Shop<font><font color=orange style='font-size:9pt;font-family:Arial;text-decoration:under-line'>Ex<font></a>" },
			{ "regexp" : '/<link href="syssite\/home\/shop\/[\d]+\/images\/[\d]+\/css\.css" rel="stylesheet" type="text\/css">/ },
			{ "version" : '/<meta name="generator" content="ShopEx ([\d\.]+)" \/>/ },
		]

