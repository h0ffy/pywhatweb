import sys
import os
			
class pcpin_chat_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<!-- Please don't remove next line. Thank You! -->" },
			{ "text" : "<a href="http://www.pcpin.com" style="font-size:10; color:#990000;" target="_blank">Powered by PCPIN.com</a>" },
			{ "text" : "Powered by <a href="http://www.pcpin.com/" target="_blank" title="Powered by PCPIN Chat">PCPIN Chat</a>" },
			{ "regexp" : "/<INPUT type="submit" class="buttons" value="[^"]+" onClicK="document.loginform.register.value=0; document.loginform.lostpassword.value=0">/" },
		]

