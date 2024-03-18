import plugins
			
class Plugincarel_data_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<script type="text/javascript" language="JavaScript" src="/MPwebCoreFn.js"></script>" },
			{ "text" : "<img style="position:absolute;left:0;top:0;" src=plv_primoLW.jpg zwidth="100%" zheight="100%">" },
			{ "url" : "/plv_primoLW.jpg", "md5" : "df1e885e87f6ab393a90b908b6ce5dc4" },
			{ "version" : "/^CarelDataServer\/([\d\.]{1,10})/", "search" : "headers[server]" },
		]
		return(self.rules)

