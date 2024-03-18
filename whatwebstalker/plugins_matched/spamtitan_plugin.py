import plugins
			
class Pluginspamtitan_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/imgs/logo.gif", "md5" : "ab662b52fe52fa13aa13574efa7f490f" },
			{ "url" : "/imgs/favicon.ico", "md5" : "f9015ac89e34faefe9b4df73901462d9" },
			{ "regexp" : "/<link rel="stylesheet" type="text\/css" href="\/?styles\/spamtitan(\.[\d]{10})?\.css" title="SpamTitanCSS2">/" },
			{ "text" : "<table class="lhead"><tr><td class="img"><img src="/imgs/logo.gif" alt="SpamTitan Logo"></td></tr></table></div>" },
		]
	return(self.rules)
