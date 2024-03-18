import sys
import os
			
class bestshoppro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<td width=300 height=18 colspan=2 align=center class=tdn><b>Logowanie</b></td></tr>' },
			{ "text" : '<meta content="www.bst.pl" name="author"/>' },
			{ "text" : '<META CONTENT="www.bst.pl" NAME=AUTHOR>' },
		]

