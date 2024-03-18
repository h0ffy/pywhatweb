import plugins
			
class Pluginfastcgi_echo_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "SCRIPT_NAME=/fcgi-bin/echo" },
			{ "text" : "<title>FastCGI echo</title><h1>FastCGI echo</h1>" },
			{ "text" : "REQUEST_URI=/fcgi-bin/echo" },
			{ "version" : "/HTTP_ORACLE_CACHE_VERSION=([\d\.]+)/" },
			{ "version" : "/SERVER_SOFTWARE=([^\n]+)/" },
			{ "version" : "/SERVER_SIGNATURE=<ADDRESS>([^<]+)/" },
		]
			return(self.rules)
