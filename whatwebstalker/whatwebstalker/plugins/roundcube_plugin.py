import plugins


class Pluginroundcube_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<title>RoundCube Webmail :: Welcome to RoundCube Webmail</title>"},
			{"text": "var rcmail = new rcube_webmail();"},
			{"text": "<input name="_user" id="rcmloginuser"'},
			{ "text" : "$(document).ready(function(){ rcmail.init(); });'},
		]
	return(self.rules)
