import plugins
			
class Pluginocportal_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<html id="main_website_html" xmlns="http://www.w3.org/1999/xhtml"" },
			{ "text" : "<meta name="GENERATOR" content="ocPortal" />" },
			{ "version" : "/<!--\nPowered by ocPortal\n([^\n]+) version\nCopyright ocProducts Limited\nhttp:\/\/ocportal\.com\n-->/" },
			{ "version" : "/^ocPortal ([^\(]+) \(PHP/", "search" : "headers[x-powered-by]" },
			{ "name" : "ocp_session cookie", "regexp" : "/ocp_session=[\d]+;/", "search" : "headers[set-cookie]" },
		]
	return(self.rules)

