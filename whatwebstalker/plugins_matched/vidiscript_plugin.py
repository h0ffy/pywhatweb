import plugins
			
class Pluginvidiscript_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<span  style="font-size:12px"><a href="http://www.VidiScript.com"><b>Free Open Source Video Script</b></a>&nbsp;Powered By&nbsp;<a href="http://www.VidiScript.com"><b>VidiScript.com</b></a> |    <b>" },
			{ "text" : "<a href='http://www.VidiScript.com'><b>Free Video Script</b></a>&nbsp;Powered By&nbsp;<a href='http://www.VidiScript.com'><b>VidiScript.com</b></a>" },
		]
	return(self.rules)
