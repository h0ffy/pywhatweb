import plugins
			
class Pluginnukeviet_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="Nuke[vV]iet v([^\s^"]+)" \/>/" },
			{ "text" : "<div id="run_cronjobs" style="visibility: hidden; display: none;">" },
			{ "regexp" : "/<form class="loginform" method="post" action="[^"^>]*\/admin\/index\.php" onsubmit="return nv_checkadminlogin_submit\(\);">/" },
		]
	return(self.rules)
