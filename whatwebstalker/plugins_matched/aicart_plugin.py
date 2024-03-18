import plugins
			
class Pluginaicart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : " for = "l_password">Password <span class="req">*</span></label>" },
			{ "text" : "<input id = "l_password" name = "l_password" class = "field text medium" type = "password" maxlength = "255" value = " />" },
			{ "text" : "<input id="l_remember_me" name="l_remember_me" class = "field checkbox" type = "checkbox" value = "1" />" },
			{ "text" : "<input name="APP_authenticate" type="hidden" id="APP_authenticate" value="frmLogin" />" },
		]
		return(self.rules)
