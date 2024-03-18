import plugins
			
class Pluginpodpress_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<cite>Podcast Powered by <a href="http:\/\/www.mightyseek.com\/podpress\/" title="podPress", "the dream plugin for podcasting with WordPress"><strong>podPress \(v([\d\.]+)\)<\/strong><\/a><\/cite>/" },
			{ "version" : "/<div id="podPress_footer">Podcast powered by <a href="http:\/\/wordpress.org\/extend\/plugins\/podpress\/" title="podPress", "a plugin for podcasting with WordPress"><strong>podPress v([\d\.]+)<\/strong><\/a><\/div>/" },
		]
		return(self.rules)
