import plugins
			
class Pluginwikiwebhelp_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "style="float:left;"><img src="theme/default/images/wh32.png"" },
			{ "text" : "<script type="text/javascript" language="javascript" src="script/wicky/wiky.js" ></script>" },
			{ "md5" : "18fe76b96d4eae173bf439a9712fa5c1", "url" : "favicon.ico" },
		]
	return(self.rules)
