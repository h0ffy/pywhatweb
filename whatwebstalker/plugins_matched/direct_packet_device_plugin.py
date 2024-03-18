import plugins
			
class Plugindirect_packet_device_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/favicon.ico", "md5" : "ee6371b0db9369cf5a88e552bedeed19" },
			{ "text" : "<body bgcolor=#efefef link=# vlink=# text=#3f3f3f background=  >" },
			{ "text" : "<td height="30" class="login"><b><font color="ffffff" size="2" face="Arial", "Helvetica", "sans-serif">Password</font></b></td>" },
			{ "version" : "/^DPWebServer\/([\d\.]{1,3})/", "search" : "headers[server]" },
		]
			return(self.rules)
