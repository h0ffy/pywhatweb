import plugins
			
class Pluginindico_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td class="menuConfTopCell" align="left" valign="bottom">" },
			{ "version" : "/<\/span>&nbsp;Powered by(\ CERN)? <a href="http:\/\/cern\.ch\/indico">Indico ([^<]+)<\/a>&nbsp;<span class="separator">/", "offset" : "1 },
		]
		return(self.rules)
