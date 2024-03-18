import sys
import os
			
class posterita_pos_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<img src="images/newUI/logo.gif" alt="Powered by Posterita POS" width="133px" height="41px" border="0px"/>' },
			{ "certainty" : '75", "text" : '<!-- chooseApplication.jsp -->' },
			{ "version" : '/<div class="footer">[\s]+<div class="floatLeft">[\s]+All Contents .[\s]+Posterita 20[\d]{2}[\s]+<b>Version &nbsp;([^\s^<]+)<\/b>[\s]+<\/div>[\s]+<\/div>/ },
		]

