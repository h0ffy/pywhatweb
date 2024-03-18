import plugins
			
class Pluginsmartcds_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<img border=0 src="http://www.globaldawin.com/capcds/refresh.gif" width="13" height="16"" },
			{ "regexp" : "/^smartcds/", "search" : "headers[server]" },
			{ "version" : "/^smartcds\/([^\s]+)/", "search" : "headers[server]" },
			{ "version" : "/^Version:([^\s]+)$/", "search" : "headers[smartcds]" },
			{ "string" : /^(.*)$/", "search" : "headers[x-smartcds-error]" },
		]
	return(self.rules)
