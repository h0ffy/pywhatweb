import plugins
			
class Pluginbitweaver_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a id="poweredby" class="external" href="http://www.bitweaver.org">Powered by bitweaver</a>" },
			{ "text" : "<meta name="generator" content="bitweaver - http://www.bitweaver.org" />" },
		]
	return(self.rules)

