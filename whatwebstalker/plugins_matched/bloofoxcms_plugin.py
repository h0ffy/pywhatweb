import plugins
			
class Pluginbloofoxcms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="bloofoxCMS ([\d\.]+)" \/>/" },
			{ "regexp" : "/<!--[\r\n\s]+This Website was generated by bloofoxCMS.[\r\n\s]+bloofoxCMS is open source published under the gnu gpl. Visit www.bloofox.com for more details![\r\n\s]+Copyrights \(c\) 2006-2007 by Alexander Lang[\r\n\s]+\/\/-->/" },
			{ "regexp" : "/Powered by <a href="http:\/\/www.bloofox.com">bloofoxCMS<\/a>/i },
		]
			return(self.rules)
