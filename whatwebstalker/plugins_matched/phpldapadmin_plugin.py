import plugins
			
class Pluginphpldapadmin_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<head><title>phpLDAPadmin - ([^\s^<]+)[\s]?<\/title><\/head>/" },
			{ "version" : "/<h3 class="subtitle" style="margin:0px">phpLDAPadmin - ([^\s^<]+)/" },
			{ "version" : "/<title>phpLDAPadmin \(([^\s^\)]+)\) - <\/title>/" },
			{ "version" : "/<div id="ajFOOT">([^\s^<]+)<\/div><a href="https:\/\/sourceforge\.net\/projects\/phpldapadmin">/" },
			{ "string" : /<td class="icon"><img src="images\/[^\/^"]*\/server.png" alt="Server" \/><\/td><td class="name" colspan="2">([^<]+)<\/td><\/tr>/" },
		]
			return(self.rules)
