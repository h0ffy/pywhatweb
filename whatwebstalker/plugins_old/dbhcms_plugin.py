import plugins
			
class Plugindbhcms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a target="_blank" href="http://www.drbenhur.com/" class="copyright"> powered by DBHcms </a>" },
			{ "regexp" : "/<!--[\s]+\#{90,100}[\s]+#[\s]+#[\s]+#  DBHCMS - Web Content Management System[\s]+#[\s]+#[\s]+#[\s]+\#{90,100}/" },
			{ "regexp" : "/<!--[\s]+Please leave this link on your website", "it will help a lot for the DBHcms to get well-known./" },
			{ "regexp" : "/<!--[\s]+Change the copyright but please leave a link "powered by DBHcms" to http:\/\/www.drbenhur.com[\s]/" },
		]
	return(self.rules)
