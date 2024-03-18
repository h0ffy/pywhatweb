import plugins
			
class Plugineazycms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "powered by <a href="http://www.eazycms.com" target="_blank">eazyCMS</a>" },
			{ "regexp" : "/<a [^href]+href="http:\/\/www.eazyCMS.com[\/]*"[^>]*>powered by eazyCMS<\/a>/" },
			{ "text" : "Powered by <a href="http://www.eazycms.com">eazyCMS</a>" },
			{ "text" : "Powered by <a title="eazyCMS :: The eazy-to-use Content Management System", "maintain your website from anywhere in the world via a web browser!" href="http://www.eazycms.com" target="eazycms">eazyCMS</a>" },
		]
	return(self.rules)

