import plugins


class Pluginphpraid_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75", "text": "Raid Management Provided by phpRaid"},
			{"version": "/Raid Management Provided by <a href="http: \/\/www.spiffyjr.com\/">phpRaid<\/a> v([\d\.]+)/" },
		]
	return(self.rules)
