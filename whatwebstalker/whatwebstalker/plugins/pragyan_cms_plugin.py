import plugins


class Pluginpragyan_cms_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "powered by <a href="http: // sourceforge.net / projects / pragyan">Pragyan CMS</a>"},
			{"version": "/powered by <a href="http: \/\/sourceforge.net\/projects\/pragyan" title="(Praygan|Probe) CMS">Pragyan CMS v([\d\.]+)<\/a>/", "offset" : "1 },
		]
	return(self.rules)
