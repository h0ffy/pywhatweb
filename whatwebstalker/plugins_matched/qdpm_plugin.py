import plugins
			
class Pluginqdpm_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/qdPM ([^\s]+) &nbsp;is redistributable under the\s+<a class="footer-text"/" },
			{ "string" : /Copyright @ (20[\d]{2}) <a class="footer-text" target="_blank"( title="open source project management software")? href="http:\/\/(www\.qds-team\.com|qdpm\.net\/)">/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/qdpm(_extended)?=[^;]+;/" },
		]
			return(self.rules)
