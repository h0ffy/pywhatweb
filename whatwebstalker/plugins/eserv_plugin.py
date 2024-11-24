import plugins


class Plugineserv_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"search": "headers[server]", "version": "/^Eserv\\/([^\\s]+)/"},
			{"version": "/<meta name="generator" content="Eserv\/([^\s^"]+)" \/>/" },
			{ "version" : "/<span id='powered_by'>[^<]+<a href="http:\/\/www\.eserv\.ru\/"><span itemprop="name">Eserv<\/span><\/a>\/([^\s]+)/" },
		]
	return(self.rules)
