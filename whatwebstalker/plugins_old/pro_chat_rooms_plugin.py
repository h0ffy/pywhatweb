import plugins
			
class Pluginpro_chat_rooms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Pro Chat Rooms</title>" },
			{ "text" : "<tr id="doPasswordBox"><td>Password:</td><td><input type="password" name="password" id="password" value=" onblur="def(\'password\')" class="uInput"/></td></tr>" },
			{ "text" : "	showError("char_error", "Sorry", "Username is already registered.");" },
			{ "text" : "var loginNameErrorChr = 'Your username has special characters.<br>These characters are not allowed,<br>!@#$\%SPC^&*()+=-[]\&#39;;,./{}|&#34:<>?.<br>Please remove them and try again.';" },
			{ "version" : "/<img src="images\/chat.gif" border="0" alt="Pro Chat Rooms v([\d\.]+)" title="Pro Chat Rooms v([\d\.]+)" \/>/" },
		]
	return(self.rules)
