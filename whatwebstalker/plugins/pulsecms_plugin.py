import plugins
			
class Pluginpulsecms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<img src="img/new-logo.png" alt="Pulse CMS">" },
			{ "text" : "<input type="password" size="27" name="mpass_pass">" },
			{ "text" : "<title>Pulse Content Manager</title>" },
			{ "text" : "<body id="login-page" onload="document.login.mpass_pass.focus()">" },
			{ "url" : "img/new-logo.png", "md5" : "079d0b95c76564c1bb450650f17c3e7f" },
			{ "url" : "img/new-logo.png", "md5" : "652807728bfb1cd7ffba4a5d40c4e374" },
		]
	return(self.rules)
