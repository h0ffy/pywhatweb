import sys
import os
			
class Pluginaicart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : " for = "l_password">Password <span class="req">*</span></label>" },
			{ "text" : "<input id = "l_password" name = "l_password" class = "field text medium" type = "password" maxlength = "255" value = " />" },
			{ "text" : "<input id="l_remember_me" name="l_remember_me" class = "field checkbox" type = "checkbox" value = "1" />" },
			{ "text" : "<input name="APP_authenticate" type="hidden" id="APP_authenticate" value="frmLogin" />" },
		]

