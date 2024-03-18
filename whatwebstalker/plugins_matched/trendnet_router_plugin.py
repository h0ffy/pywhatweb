import plugins
			
class Plugintrendnet_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<link rel="stylesheet" rev="stylesheet" href="ubicom_style.css" type="text/css" />" },
			{ "version" : "/<META HTTP-EQUIV="Content-Type"CONTET="text\/html; cahrset=ks_c_5601-1987">[\s]+<TITLE>Web Client [^<]+ v([^\s^<]+)<\/TITLE>/" },
			{ "model" : "/<title>TRENDnet ([^\|]+) \|[\s]+Login[\s]+<\/title>/" },
		]
		return(self.rules)

