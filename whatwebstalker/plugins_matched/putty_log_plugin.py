import plugins
			
class Pluginputty_log_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/=~=~=~=~=~=~=~=~=~=~=~= PuTTY log [0-9]{4}.[0-9]{2}.[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} =~=~=~=~=~=~=~=~=~=~=~=/" },
		]
		return(self.rules)

