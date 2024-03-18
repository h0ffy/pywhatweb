import plugins
			
class Pluginrackstar_server_appliance_os_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/<A HREF='http:\/\/www.rackstar.net\/' TITLE='This server is powered by the RackStar Server Appliance OS'>RACKSTAR<\/A>/" },
			{ "search" : "headers[server]", "regexp" : "/\(<A HREF=http:\/\/www.rackstar.net\/>RACKSTAR<\/A>\)/" },
		]
	return(self.rules)
