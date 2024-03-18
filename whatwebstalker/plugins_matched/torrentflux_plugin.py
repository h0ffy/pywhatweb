import plugins
			
class Plugintorrentflux_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<font class="title">TorrentFlux Login</font>" },
			{ "text" : "<td><input type="password" name="iamhim" value=" size="15" style="font-family:verdana,helvetica,sans-serif; font-size:9px; color:#000" /></td>" },
		]
		return(self.rules)
