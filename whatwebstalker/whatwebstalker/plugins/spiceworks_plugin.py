import plugins


class Pluginspiceworks_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<meta name="author" content="Spiceworks", "Inc." />"},
			{"text": "<p>Spiceworks is compatible with <a href="http: // community.spiceworks.com / help / Spiceworks_Requirements  # Browser">modern browsers</a>", "and requires JavaScript", "Cookies", "and Stylesheets (CSS) to function correctly.</p>" },
			{"text": "<title>Spiceworks - Login Required</title>"},
		]
	return (self.rules)
