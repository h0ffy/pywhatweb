import plugins
			
class Pluginws_ftp_log_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/^[0-9]+.[0-9]{2}.[0-9]{2} [0-9]{2}:[0-9]{2} [A|B]{1} [^>]*> ([^\ ]+) /" },
		]
			return(self.rules)
