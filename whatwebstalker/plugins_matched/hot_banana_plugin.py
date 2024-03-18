import plugins
			
class Pluginhot_banana_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "Powered by Hot Banana"" },
			{ "text" : "					var hbac_regFileTypes = new RegExp("\s*.(pdf|swf|gif|jpg|jpeg|jpe|xls|ppt|doc|mp3|txt|wav)");" },
			{ "text" : "<div align="right"><img src="Images/hblogo.gif" width="49" height="28" border="0" alt="Powered By Hot Banana" /></div>" },
		]
	return(self.rules)

