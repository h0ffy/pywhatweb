import plugins
			
class Pluginvts_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "status" : "401", "regexp" : "/<html>\r\n<head>\r\n<title>Error Message<\/title>\r\n<link rel="stylesheet" href="\/VTS.css">\r\n\r\n<\/head>\r\n<body class=error>\r\n<h1>Error Message<\/h1>\r\n<p>Error Code 401.\r\n<p>Message: Unauthorized.\r\n<p>Description: 401 = No permission -- see authorization schemes./" },
			{ "regexp" : "/VTS /", "search" : "headers[server]" },
			{ "version" : "/VTS ([\d\.]+)/", "search" : "headers[server]" },
			{ "version" : "/^VTS=([\d\.]+)/", "search" : "headers[set-cookie]" },
		]
	return(self.rules)
