import plugins
			
class Pluginunknown_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "model" : "'Arris Touchstone Device", "url" : "/favicon.ico", "md5" : "a8fe5b8ae2c445a33ac41b33ccc9a120" },
			{ "model" : "'ST 605", "url" : "/favicon.ico", "md5" : "d16a0da12074dae41980a6918d33f031" },
			{ "md5" : "d8d705cef8dbf67357ee908f42fd1baa", "url" : "/favicon.ico" },
			{ "md5" : "129f914b2570b50374ebeb8f1306617d", "url" : "/login/keys.png" },
		]
		return(self.rules)

