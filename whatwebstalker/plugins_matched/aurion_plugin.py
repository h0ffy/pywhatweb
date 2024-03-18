import plugins
			
class Pluginaurion_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<br/>Please enable JavaScript in your browser or refer to you internal IT support for assistance.<br/><br/></div>" },
			{ "text" : "<!-- Aurion Teal will be used as the login-time default. Shell layouts will replace these after login. -->" },
			{ "text" : "<!-- teal.css has stuff needed for div#loading-noscript -->" },
			{ "text" : "<meta http-equiv="X-UA-Compatible" content="chrome=1; IE=8; IE=7"> <!-- Stop Internet Explorer from using "Compatability Mode" -->" },
			{ "version" : "/<title>Aurion V([^\s^<]+)<\/title>[\s]+<link rel="shortcut icon" href="\.\/favicon\.ico" >/" },
		]
			return(self.rules)
