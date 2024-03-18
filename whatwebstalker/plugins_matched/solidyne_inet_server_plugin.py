import plugins
			
class Pluginsolidyne_inet_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Solidyne iNET Server</title>" },
			{ "text" : "<frame name="frLeft" scrolling="NO" id="frLeft" src="QFrLeft.aspx">" },
			{ "text" : "<META HTTP-EQUIV="refresh" content="0; url=/hmi/">" },
			{ "url" : "/hmi/sysapp/QLogin.aspx", "text" : "<form name="form1" method="post" action="QLogin.aspx" id="form1">" },
		]
		return(self.rules)
