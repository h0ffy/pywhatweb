import plugins
			
class Plugindell_kace_appliance_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/common/about.php", "version" : "/<b>K1000 Systems Management Appliance<\/b> <b>v([^\s^<]+)<\/b>/" },
			{ "search" : "headers[x-dellkace-version]", "version" : "/^(.+)$/" },
			{ "search" : "headers[x-dellkace-host]", "string" : /^(.+)$/" },
			{ "search" : "headers[x-dellkace-appliance]", "model" : "/^(.+)$/" },
			{ "search" : "headers[x-kbox-version]", "version" : "/^(.+)$/" },
			{ "search" : "headers[x-kbox-webserver]", "string" : /^(.+)$/" },
		]
		return(self.rules)

