import plugins


class Pluginbeef_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<img src=".. / images / beef.gif" onclick="new Effect.Shake(\'sidebar\');"></div> BeEF</h1>" },
			{ "certainty" : "75", "text" : "<title>Browser Exploitation Framework</title>" },
			{ "regexp" : "/<script[^>]+src=['"]?[^>^="'^"]+\/hook\/beefmagic\.js\.php['"]?/", "certainty" : "75", "string" : "Hook" },
			{ "regexp" : "/<script[^>]+src=['"]?https?:\/\/[^\/]+\/hook\.js['"]?/", "certainty" : "75", "string" : "Hook" },
			{ "url" : "/ui/authentication", "text" : "<div id="centered"><img id="beef-logo" src="/ui/media/images/beef.png" alt="BeEF - The Browser Exploitation Framework" /></div>" },
			{ "url" : "/ui/media/images/beef.png", "md5" : "5f8cdcd65c5c05f875710f2c10503192" },
			{ "search" : "headers[server]", "version" : "/^BeEF ([^\s]+)$/" },
		]
	return(self.rules)
