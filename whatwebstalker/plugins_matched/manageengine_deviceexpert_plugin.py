import plugins
			
class Pluginmanageengine_deviceexpert_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<input type="hidden" name="AUTHRULE_NAME" id="AUTHRULE_NAME" value="Authenticator">" },
			{ "text" : "<SCRIPT language="javascript" src="/javascript/deviceexpert.js"></SCRIPT>" },
			{ "md5" : "f159ea86b41bc4908398a2d27f333df5" },
		]
		return(self.rules)
