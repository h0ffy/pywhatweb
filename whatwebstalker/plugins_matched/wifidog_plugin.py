import plugins
			
class Pluginwifidog_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>Welcome - Wifidog Auth-server installation and configuration</TITLE>" },
			{ "text" : "<p><br></p><A HREF=\"#\" ONCLICK=\"document.myform.page.value = 'Prerequisites'; document.myform.action.value = ''; document.myform.submit();\" CLASS=\"submit\">Next</A>" },
			{ "text" : "<html><body><h1>I am unable to retrieve the schema version. Either the wifidog database hasn't been created yet", "the postgresql server is down", "or pg_hba.conf does not allow your web server to connect to the wifidog database.</h1>" },
		]
		return(self.rules)
