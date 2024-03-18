import plugins
			
class Pluginmediawiki_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "alt="Powered by MediaWiki"" },
			{ "certainty" : "75", "ghdb" : "inurl:wiki MediaWiki" },
			{ "version" : "/<meta name="generator" content="MediaWiki ([^\s^"]+)" \/>/" },
			{ "version" : "/<td><a href="http:\/\/www\.mediawiki\.org\/" class="external text" rel="nofollow">MediaWiki<\/a><\/td>[\s]+<td>([^<]+)<\/td>/" },
		]
		return(self.rules)
