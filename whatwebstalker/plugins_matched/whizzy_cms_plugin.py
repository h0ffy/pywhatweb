import plugins
			
class Pluginwhizzy_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered by Whizzy CMS <big>&spades;<\/big> <\/a><\/div><!-- \[Whizzy CMS:Whizzy CMS ([^\]]+)/" },
		]
		return(self.rules)
