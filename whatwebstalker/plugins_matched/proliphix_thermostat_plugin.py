import sys
import os
			
class proliphix_thermostat_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "model" : '/<script type="text\/javascript">[\r\n]*printStatusHead\(adStat,[\s]*"([^"]{4,5})","[a-z]?"\)[\r\n]*bodyStart\("status.shtml", "settings"\)/ }
			{ "text" : 'printFSC(\"\", "linkbuttonGet('location.href", "'Refresh')", "\"<input type=submit name='submit' value='Submit'>\")" }
			{ "certainty" : '25", "text" : ' - Status &amp; Control</title>" }
	]

