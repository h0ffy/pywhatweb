import plugins
			
class Pluginkmsoft_guestbook_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div id="footer">KMSoft Guestbook v ([\d\.]+) Powered by <a href="http:\/\/www.kmsoft.org[\/]*">KMSoft<\/a><\/div>/" },
			{ "version" : "/<title>KMSoft Guestbook v([\d\.]+)[^<]+<\/title>/" },
		]
		return(self.rules)
