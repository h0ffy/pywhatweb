import plugins


class Plugintribiq_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"md5": "1d334359c5d0f68de91f33c78581f25c", "url": "/favicon.ico"},
			{"text": "Powered by <a href="http: // tribiq.com / " target="_blank">Tribiq CMS</a>"},
			{"text": "Designed &amp; Powered by <a alt="Tribiq CMS" target="_blank" title="Tribiq CMS" href="http: // www.tribiq.com">Tribiq CMS</a>"},
			{"regexp": "/Designed &amp; Powered by <a href="http: \/\/www.tribiq.com[\/]*[^>]+>Tribiq CMS<\/a>/" },
			{ "text" : "Powered by <a href="http://tribiq.com" title="TRIBiQ Content Management System" target="_blank">Tribiq</a>" },
			{ "text" : "<a href="http://tribiq.com">Powered by Tribiq CMS</a>" },
			{ "text" : "Powered by <a href="http://tribiq.com" target="_blank">TRIBiQ</a>" },
			{ "text" : "					document.location.href = "adminlogin.php?sk=" + (hash? hash : "tribiq__content");" },
			{ "text" : "				<p><a href="adminlogin.php">Please log in</a></p>" },
			{ "text" : "<title>Tribiq CMS Administrator Login</title>" },
		]
	return(self.rules)
