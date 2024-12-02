import plugins


class Pluginnamazu_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/This search system is powered by[\\s]+<strong><a href="http: \/\/www\.namazu\.org\/">Namazu<\/a><\/strong>/" },
			{ "regexp" : "/Powered by <a href="http:\/\/www\.namazu\.(org|cc)\/[^"]*" target="_blank">(N|n)amazu<\/a>/" },
			{ "regexp" : "/<p><strong> Total <!-- HIT -->[\d]+<!-- HIT --> documents matching your query.<\/strong><\/p>/" },
			{ "version" : "/<strong><a href="http:\/\/www\.namazu\.org\/">Namazu<\/a> <!-- VERSION --> v([\d\.]+) <!-- VERSION --><\/strong>/i },
			{ "version" : "/This search system is powered by <a href="http:\/\/www\.namazu\.org\/">Namazu<\/a> <!-- VERSION --> v([\d\.]+) <!-- VERSION --><\/p>/i },
		]
	return(self.rules)
