import plugins
			
class Plugin360_web_manager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "powered by 360 Web Manager"", "certainty" : "75 },
			{ "regexp" : "/360WebManager Software :: administrador contenidos web/", "certainty" : "75 },
			{ "version" : "/<div align="center"><span class="copyr">Powered by <a href="http:\/\/www.360webmanager.com" target="_blank" class="copyrlink">360 Web Manager<\/a> ([\d\.]+)/" },
		]
	return(self.rules)
