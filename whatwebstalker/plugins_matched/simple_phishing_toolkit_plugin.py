import plugins
			
class Pluginsimple_phishing_toolkit_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="browser_warning">You are running a web browser that has not been tested...Try the latest version of <a href="http://google.com/chrome">Google Chrome</a>", "<a href="http://microsoft.com/ie">Microsoft Internet Explorer</a> or <a href="http://mozilla.org/firefox">Mozilla Firefox</a></div>" },
			{ "text" : "<meta name="description" content="welcome to spt - simple phishing toolkit.  spt is a super simple but powerful phishing toolkit." />" },
			{ "certainty" : "75", "text" : "<title>spt - simple phishing toolkit</title>" },
			{ "version" : "/<span id="spt"><a href="http:\/\/www\.sptoolkit\.com\/download\/" target="_blank">v([^\s^<]+)/" },
		]
		return(self.rules)
