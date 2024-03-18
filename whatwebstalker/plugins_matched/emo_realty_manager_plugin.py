import sys
import os
			
class emo_realty_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/[0-9]{4} Emophp.[com|COM]*<\/td><td[\ class='text8']* align='right'><a href=[\']*http:\/\/emophp.com[\/]*[\']*[\ target=_blank]*>Powered by [EMO|Emo]+ Realty Manager<\/a><\/td><\/tr><\/table><br>/ },
			{ "regexp" : '/[0-9]{4} Emophp.[com|COM]*<\/td><td[\ class='text8']* align='right'>Powered by <a href=[\']*http:\/\/emophp.com[\/]*[\']*[\ target=_blank]*>[Emo|EMO]+ Realty Manager<\/a><\/td><\/tr><\/table><br>/ },
		]

