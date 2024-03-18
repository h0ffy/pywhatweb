import plugins
			
class Pluginactiveweb_content_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<!--[\s]+page generated with activeWeb contentserver R([\d\.]+)/" },
			{ "version" : "/<!--[\s]+activeWeb cache extension R([\d\.]+)/" },
			{ "text" : "<!-- AWNOCACHEBEGIN__AWNOCACHEBEGIN__AWNOCACHEBEGIN__AWNOCACHEBEGIN__AWNOCACHEBEGIN -->" },
			{ "name" : "X-AwCache-FollowUp Header", "text" : "", "search" : "headers[x-awcache-followup]" },
			{ "name" : "X-AwCache-Command Header", "text" : "", "search" : "headers[x-awcache-command]" },
			{ "name" : "X-AwCache-ScriptTechnology Header", "string" : /^.*$/ ,"search" : "headers[x-awcache-scripttechnology]" },
		]
			return(self.rules)
