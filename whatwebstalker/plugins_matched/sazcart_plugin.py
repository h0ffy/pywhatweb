import plugins
			
class Pluginsazcart_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/[^&]+&raquo; Powered by SazCart<\/title>/" },
			{ "text" : "<a href="http://www.sazcart.com">Powered by SazCart</a> | <a href="http://www.sazcart.com">Copyright &#169; 2005 - 2006 SazCart.com</a>  </div>" },
		]
		return(self.rules)

