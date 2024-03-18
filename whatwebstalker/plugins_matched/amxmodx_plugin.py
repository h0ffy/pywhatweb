import plugins
			
class Pluginamxmodx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "// *NOTE* amx_sql_type specifies the DEFAULT database type which admin.sma will use." },
		]
		return(self.rules)
