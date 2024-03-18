import plugins
			
class Plugingpsgate_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<input name="LoginControl$TextBoxPassword" type="password" id="LoginControl_TextBoxPassword" tabindex="2" class="form" onfocus="document.getElementById(\'LoginControl_TextBoxPassword\').select()" value="password"" },
			{ "regexp" : "/<head><title>\r?\n\tGpsGate Server - Login\r?\n<\/title><\/head>/" },
		]
		return(self.rules)
