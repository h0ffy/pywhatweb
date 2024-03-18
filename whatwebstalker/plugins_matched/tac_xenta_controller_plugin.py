import plugins
			
class Plugintac_xenta_controller_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<html><body><script>var url="https://"+location.hostname+"/www/index/Slogin.html";location.href=url;</script></body></html>" },
			{ "regexp" : "/^TAC\/Xenta/", "search" : "headers[server]" },
			{ "model" : "/^TAC\/Xenta([\d]{3}|[\d]{3}-[A-Z]{3}) [\d\.]{4}/", "search" : "headers[server]" },
			{ "firmware" : "/^TAC\/Xenta[^\ ]+ ([\d\.]{4})/", "search" : "headers[server]" },
		]
			return(self.rules)
