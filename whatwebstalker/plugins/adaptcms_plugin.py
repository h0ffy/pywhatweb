import plugins
			
class Pluginadaptcms_plugin(plugins.Base):
    def __init__(self):
    	super().__init__()
    def start(self):
        self.rules = [
			{ "version" : r"/Powered by <a href=\"http:\/\/www.adaptcms.com\">[<b>]*AdaptCMS([^<]*)<\/a>/" },
		]
        return self.rules