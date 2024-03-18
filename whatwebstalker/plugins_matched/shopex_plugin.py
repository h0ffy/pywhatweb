import plugins
			
class Pluginshopex_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "regexp" : "/<title>[^<]* -- Powered by Shop(e|E)x<\/title>/" },
			{ "text" : "<p align=center><font color=black style='font-size:9pt;font-family:Arial'>Powered by </font><a href='http://www.shopex.cn' target='_blank'><font color=navy style='font-size:9pt;font-family:Arial;text-decoration:under-line'>Shop<font><font color=orange style='font-size:9pt;font-family:Arial;text-decoration:under-line'>Ex<font></a>" },
			{ "regexp" : "/<link href="syssite\/home\/shop\/[\d]+\/images\/[\d]+\/css\.css" rel="stylesheet" type="text\/css">/" },
			{ "version" : "/<meta name="generator" content="ShopEx ([\d\.]+)" \/>/" },
		]
		return(self.rules)
