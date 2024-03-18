import plugins
			
class Pluginhughes_voice_appliance_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<HTML><HEAD></HEAD><BODY onload="window.location=\'/fs/home.htm\'"></BODY></HTML>" },
			{ "text" : "<head><title>HughesNet Appliance Control Center</title></head>" },
			{ "url" : "/systeminfo/", "version" : "/<td width='50%'>Main\.bin Version<\/td><td width='50%' align='center'>([^<^\s]+)<\/td>/" },
		]
		return(self.rules)
