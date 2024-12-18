import plugins


class Pluginmicrosoft_iis_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<html><head><title>Site Not Found</title></head>.<body>No web site is configured at this address.</body></html>",
			    "module": "Site Not Found"},
			{"text": "<id id="Comment1"><!--Problem--></id><id id="errorText">Under Construction</id></h1>", "module": "Under Construction"},
			{"text": "<P ID=Comment1><!--Problem--><P ID="errorText">Under Construction</h1>", "module": "Under Construction"},
			{"text": "If you are the Web site administrator and feel you have received this message in error", "please see &quot;Enabling and Disabling Dynamic Content&quot; in IIS Help.", "module": "Under Construction"},
			{"text": "<a href="http: // go.microsoft.com / fwlink / ?linkid = 66138 & amp; clcid = 0x409"><img src="welcome.png" alt="IIS7" width="571" height="411" /></a>", "module": "Under Construction"},
			{"text": "<a href="http: // go.microsoft.com / fwlink / ?linkid = 66138 & amp; clcid = 0x409"><img src="iis - 85.png" alt="IIS" width="960" height="600" /></a>", "module": "Under Construction"},
			{"status": "404", "text": "<h1 style="COLOR: 000000; FONT: 13pt / 15pt verdana"><!--Problem-->The page cannot be found</h1>"},
			{"status": "404", "version": "/<a href="http: \/\/www\.microsoft\.com\/ContentRedirect\.asp\?prd=iis&sbp=&pver=([\d\.]+)&pid=&ID=404&cat=web&os=&over=&hrd=&Opt1=&Opt2=&Opt3=" target="_blank">Microsoft Support<\/a>/" },
			{ "status" : "404", "text" : "<li>Go to <a href="http://go.microsoft.com/fwlink/?linkid=8180">Microsoft Product Support Services</a> and perform a title search for the words <b>HTTP</b> and <b>404</b>.</li>" },
			{ "status" : "403", "text" : "<li>Go to <a href="http://go.microsoft.com/fwlink/?linkid=8180">Microsoft Product Support Services</a> and perform a title search for the words <b>HTTP</b> and <b>403</b>.</li>" },
			{ "search" : "headers[server]", "version" : "/Microsoft-IIS\/([\d\.]+)/i },
		]
	return(self.rules)
