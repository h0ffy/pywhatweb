import plugins
			
class Pluginxwiki_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="wiki" content="xwiki"/>" },
			{ "text" : "<div id="xwikilicence">" },
			{ "version" : "/<div id="xwikiplatformversion">(Powered by )?(XWiki Enterprise )?([^\s<>]+)/", "offset" : "2 },
		]
	return(self.rules)
