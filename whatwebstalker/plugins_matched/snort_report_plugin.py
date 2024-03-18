import sys
import os
			
class Pluginsnort_report_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "version" : "/<br><br><br><br>Snort Report Version ([^<]+)<br>Copyright 2000-20[\d]{2}", "<a href="http:\/\/www\.symmetrixtech\.com">Symmetrix Technologies", "LLC\.<\/a><\/td>/" },
			{ "text" : "<title>SNORT Report - Signature Detail ()</title>" },
		]

