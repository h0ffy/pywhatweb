import plugins
			
class Pluginposterous_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="Posterous" />" },
			{ "text" : "<div class="posterous_site_data" data-post-id="" },
			{ "account" : "/<meta property="og:site_name" content="([^"]+)'s posterous" \/>/" },
			{ "text" : "<li class="first"><a href="http://posterous.com/login?jumpto=http" },
			{ "regexp" : "/<html><body>You are being <a href="http:\/\/([^"]+)\.posterous\.com\/">redirected<\/a>\.<\/body><\/html>/" },
		]
		return(self.rules)
