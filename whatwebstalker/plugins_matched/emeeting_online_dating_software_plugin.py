import plugins
			
class Pluginemeeting_online_dating_software_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Admin Area Login</title>" },
			{ "text" : "				<td valign="bottom"><h2>Admin Area Login</h2></td>" },
			{ "text" : "<a href="http://www.datingscripts.org" alt="Dating Software by eMeeting Ltd" target="_blank">Dating Software Powered by eMeeting Ltd</a>" },
			{ "version" : "/<p>eMeeting Dating Software <strong>Version ([\d\.]+)<\/strong>/" },
		]
		return(self.rules)
