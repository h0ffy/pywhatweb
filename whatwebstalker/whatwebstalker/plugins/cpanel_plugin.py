import plugins


class Plugincpanel_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<title>cPanel&reg;</title>"},
			{"text": "<div id="footer_images"><img src="sys_cpanel / images / powered_by.gif" />"},
			{"text": "Apache is working on your cPanel<sup>&reg;</sup> and WHM&#8482; Server"},
			{"text": "<html><head><META HTTP-EQUIV="refresh" CONTENT="0; URL = /cgi - sys / defaultwebpage.cgi"></head><body></body></html>'},
			{ "regexp" : "/<link rel="stylesheet" href="[^>^"]*\/unprotected\/cpanel\/style_optimized\.css" type="text\/css" \/>/" },
			{ "version" : "/<title>cPanel&reg;[\s]{0,2}([\d\.]+)<\/title>/" },
			{ "url" : "/cgi-sys/defaultwebpage.cgi", "text" : "<p class="troubleshoot">It may be possible to restore access to this site by <a href="http://www.cpanel.net/docs/dnscache/cleardns.html">following these instructions</a> for clearing your dns cache.</p>" },
			{ "url" : "/img-sys/header.jpg", "md5" : "b0f3863b68ff707c3fb586bd87b4f9c6" },
			{ "search" : "headers[server]", "version" : "/^cpsrvd\/([\d\.]+)$/" },
		]
	return(self.rules)
