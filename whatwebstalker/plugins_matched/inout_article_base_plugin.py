import plugins
			
class Plugininout_article_base_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "function trim(stringValue){return stringValue.replace(/(^\s*|\s*$)/", "");}", "certainty" : "75 },
			{ "text" : "<title>Inout Article Base - Admin Area</title>" },
			{ "text" : "<title>Inout ArticleBase - Login</title>" },
			{ "text" : " href="http://www.inoutscripts.com/?r=0">Powered by Inoutscripts</a>", "certainty" : "75 },
		]
			return(self.rules)
