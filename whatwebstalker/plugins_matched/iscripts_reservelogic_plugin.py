import plugins
			
class Pluginiscripts_reservelogic_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.iscripts.com/reservelogic/" target="_blank">iScripts ReserveLogic</a> . A premium product from <a href="http://www.iscripts.com" target="_blank">iScripts.com</a></td>" },
		]
		return(self.rules)
