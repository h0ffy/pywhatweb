import plugins
			
class Pluginkaibb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- THIS MUST REMAIN INTACT AND SHOWN ON ALL PAGES -->" },
			{ "version" : "/Powered by <a href="http:\/\/www\.kaibb\.co\.uk" class="normfont">KaiBB ([^\s^<]+)<\/a>/" },
			{ "version" : "/Powered by <a href="http:\/\/\www\.mi-dia\.co\.uk" class="normfont">KaiBB ([^\s^<]+)<\/a>/" },
			{ "text" : "<meta name="Description" http-equiv="Description" content="Forum powered by KaiBB - Powered by KaiBB" />" },
		]
	return(self.rules)
