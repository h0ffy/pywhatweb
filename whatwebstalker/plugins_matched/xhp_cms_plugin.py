import plugins
			
class Pluginxhp_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>XHP installation</title>" },
			{ "version" : "/<meta name="GENERATOR" content="XHP - eXpandable Home Page v([\d\.]+)"\/>/" },
			{ "version" : "/<a href="http:\/\/xhp.targetit.ro\/">Powered by XHP CMS v([\d\.]+)<\/a><br\/><a href="http:\/\/lars.targetit.ro\/">Site engine is copyright/" },
		]
			return(self.rules)
