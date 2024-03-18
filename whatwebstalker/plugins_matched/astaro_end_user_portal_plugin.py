import plugins
			
class Pluginastaro_end_user_portal_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<script src="eup/eup_50_change_password.js" type="text/JavaScript"></script>" },
			{ "url" : "/jape/ellipsis.xml", "md5" : "9639763b8c7f8caef097be4f3ffe5106" },
		]
		return(self.rules)
