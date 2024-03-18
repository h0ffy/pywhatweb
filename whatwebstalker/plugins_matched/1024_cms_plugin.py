import plugins
			
class Plugin1024_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id='otatfpowered'><a href='http://www.1024cms.com' target='_blank'>Powered by 1024 CMS</a></div></div>" },
			{ "text" : "<meta name="generator" content="1024 CMS (c) 2008 Treble Designs. This is free software", "and you may redistribute it under the Attribution-Non-Commercial-Share Alike 2.0 license (http://creativecommons.org/licenses/by-nc-sa/2.0/uk/). 1024 CMS comes with absolutely no warranty", "for details", "see the license (http://creativecommons.org/licenses/by-nc-sa/2.0/uk/)." />" },
		]
	return(self.rules)

