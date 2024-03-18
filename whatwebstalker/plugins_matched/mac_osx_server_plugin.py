import plugins
			
class Pluginmac_osx_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<title>Mac OS X Server</title>" },
			{ "version" : "/<div class="page_footer_appversion">Mac OS X Server Web Services Server ([\d\.]+)<\/div>/", "os" : "Mac OSX" },
			{ "account" : "/<li><a href="\/users\/([^\/]+)\/"><span class="img"><img src="\/collaboration\/images\/user\.jpg" alt=" width="32" height="32"><\/span><span class="title">[^<]+<\/span><span class="description"><\/span><\/a><\/li>/", "os" : "Mac OSX" },
			{ "text" : "<iframe id="webmail_frame" src="/webmail/src/"><!-- this frame will enable the webmail link if webmail is active --></iframe>", "os" : "Mac OSX" },
			{ "text" : "<link rel="stylesheet" type="text/css" media="screen", "projection" href="/collaboration/css/required_compressed.css">", "os" : "Mac OSX" },
		]
	return(self.rules)
