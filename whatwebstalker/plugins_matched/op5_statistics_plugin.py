import plugins
			
class Pluginop5_statistics_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td colspan="2"><center><img src="/statistics/plugins/op5gui/op5_statistics.gif" border="0" alt="></center></td>" },
			{ "text" : "<title>Login to op5 Statistics</title>" },
		]
		return(self.rules)
