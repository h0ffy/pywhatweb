import plugins


class Pluginphpfreechat_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"ghdb": "powered by phpfreechat"", "certainty" : "75},
			{"version": "/<img src="http: \/\/www.phpfreechat.net\/pub\/logo[2]*_80x15.gif" alt="PHP FREE CHAT \[powered by phpFreeChat-([\d\.\-a-z]*)\]"/" },
		]
	return(self.rules)
