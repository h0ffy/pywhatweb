import plugins
			
class Pluginvideo_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p style="color:#aaaaaa;text-align:center">Powered by <a style="color:#aaaaaa" href="http://www.codemight.com" target="_blank">Video CMS</a><br /><br /></p></body>" },
		]
	return(self.rules)
