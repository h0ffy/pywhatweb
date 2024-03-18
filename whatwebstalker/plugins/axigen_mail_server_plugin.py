import plugins
			
class Pluginaxigen_mail_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "            top.opener.location.href="/?login=";" },
			{ "text" : "<div>Powered by <a href="http://www.axigen.com" target="_blank" class="gray">Axigen Mail Server</a></div>" },
			{ "text" : "Powered by <a href="http://www.axigen.com/" target="_blank">Axigen Mail Server</a>" },
			{ "text" : "<div class="nojsContainer"><h1>In order to access AXIGEN Webmail", "<br />you must enable Javascript in your browser!</h1></div>" },
			{ "version" : "/<title>AXIGEN Webmail - v([\d\.]+)<\/title>/" },
		]
	return(self.rules)
