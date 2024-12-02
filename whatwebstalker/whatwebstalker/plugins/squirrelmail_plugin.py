import plugins


class Pluginsquirrelmail_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"name": "default title", "text": "<title>SquirrelMail - Login</title>"},
			{"name": "js function", "text": "function squirrelmail_loginpage_onload()"},
			{"name": "css comment", "text": "/* avoid stupid IE6 bug with frames and scrollbars */'},
			{ "text" : "<b>SquirrelMail Login</b>'},
		]
	return(self.rules)
