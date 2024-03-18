import sys
import os
			
class scrutinizer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div id='testAlertDivTitle'>Scrutinizer ([^<]+)<\/div>/ }
			{ "regexp" : '/<link id='scrutStyle' rel="stylesheet" href="\/css\/classic\.css/ }
			{ "regexp" : '/<div id='testAlertHdrMsg'>For the best Scrutinizer experience possible", "please address the issues below:<\/div>/ }
		]

