import plugins
			
class Pluginquescom_qportal_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<head profile="http://www.quescom.com">" },
			{ "url" : "/userframes.asp", "text" : "<FRAME src="/cticall/cticall_close.asp" name="cticlose" frameborder="no" scrolling="no" marginwidth="0" marginheight="0">" },
			{ "text" : "<link href="/qpuser.css" rel="stylesheet" type="text/css">" },
			{ "url" : "/Oem/topright.gif", "md5" : "8ddc6366869cf61044d7bc4b21ca1b1e" },
		]
	return(self.rules)
