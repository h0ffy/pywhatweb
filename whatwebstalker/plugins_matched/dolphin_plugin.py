import plugins
			
class Plugindolphin_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Dolphin Log In</title>" },
			{ "text" : "<td><input name="PHP_AUTH_PW" type="password"></td>" },
			{ "text" : "<td NOWRAP><input name="PHP_AUTH_USER" type="text"></td>" },
			{ "text" : "<body onload="focus_username();" bottommargin="0" rightmargin="0" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">" },
		]
			return(self.rules)
