import sys
import os
			
class w_agora_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "ghdb" : 'inurl:"w-agora" ext:php3' }
			{ "text" : '<CAPTION><B>System Administrator's Informations (login : <u>admin</u>)</B></CAPTION>" }
			{ "version" : '/<META NAME="GENERATOR" Content="w-agora version ([\d\.]+)"[\/]?>/i }
			{ "text" : '<table border bgcolor="#eeeeee" align="center" cellspacing=0 cellpadding=5 width=400><tr><td align=center><font face="Arial", "Verdana" color="#FF2020">Cannot access configuration file: ./conf/site_agora.php3</td></tr></table>' }
	]

