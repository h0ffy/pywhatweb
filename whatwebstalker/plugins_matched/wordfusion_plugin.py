import plugins
			
class Pluginwordfusion_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<head id="Head"><title>\s+WordFusion\.Web\s+\<\/title>/" },
			{ "text" : "<param name="source" value="ClientBin/WordFusion.Web.xap">" },
		]
	return(self.rules)

