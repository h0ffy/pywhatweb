import sys
import os
			
class Plugingpsgate_server_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<input name="LoginControl$TextBoxPassword" type="password" id="LoginControl_TextBoxPassword" tabindex="2" class="form" onfocus="document.getElementById(\'LoginControl_TextBoxPassword\').select()" value="password"" },
			{ "regexp" : "/<head><title>\r?\n\tGpsGate Server - Login\r?\n<\/title><\/head>/" },
		]

