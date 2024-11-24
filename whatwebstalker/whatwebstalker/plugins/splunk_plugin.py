import plugins


class Pluginsplunk_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version": "/<p class="footer">&copy; 2005-20[\\d]{2} Splunk Inc\\. Splunk ([^<]+)\\.<\\/p>/"},
			{"text": "<p><span>First time logging in?</span> Splunk's default credentials are </p><p>username: <span>admin</span><br />password: <span>changeme</span></p><p>If you've forgotten your username or password", "please contact your Splunk administrator.</p>"},
			{"search": "headers[set-cookie]",
     "regexp": "/session_id_8000=[a-f\\d]{32};/"},
			{"certainty": "75", "text": "<meta name="author" content="Splunk Inc." />"},
			{"url": "/en-US/favicon.ico", "md5": "f7728520c81b7a303d8e54d282e13a16"},
			{"string": / var CONFIG = \{"licenseType": "[^\"]+", "os_name": "[^"]+", "locale":[^\}]+"installType": "([^"]+)"/" },
			{ "os" : "/var CONFIG = \{"licenseType": "[^\"]+", "os_name": "([^"]+)", "locale":/" },
		]
	return(self.rules)
