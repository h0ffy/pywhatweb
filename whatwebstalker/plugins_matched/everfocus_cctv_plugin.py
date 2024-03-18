import sys
import os
			
class everfocus_cctv_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/^	If the page is not redirected", "please click <a href="\/login\.html\?[\d]{4}&1">here<\/a><br>$/ },
			{ "text" : '<!--mei20071101 input type="image" name="recMode" style="visibility:hidden" src="stoprec.gif" onclick="changeRecordMode()"-->' },
		]

