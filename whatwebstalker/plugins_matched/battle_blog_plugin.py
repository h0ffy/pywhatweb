import plugins
			
class Pluginbattle_blog_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<br /><br /><font face="arial" size="1">Powered by <a href="http://www.battleblog.com">Battle Blog</a></font>" },
			{ "text" : "<title>Battle Blog Login</title> '},
			{ "text" : "<form name = "UserInfoCollect" action = "authenticate.asp" method = "post">" },
			{ "text" : "<table width = "10%" cellpadding = "5" style = "border-style: solid; border-color: #000000; border-width: 1px;">" },
		]
	return(self.rules)
