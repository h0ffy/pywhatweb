import plugins
			
class Pluginsyndeocms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by <a href="http:\/\/www.syndeocms.org[\/]?" target="_blank">/i },
			{ "regexp" : "/Powered by <a href="http:\/\/www.syndeocms.org[\/]?" title="SyndeoCMS">/i },
			{ "regexp" : "/Powered by <a href="http:\/\/www.syndeocms.org[\/]?"[^>]*>SyndeoCMS<\/a>/i },
			{ "regexp" : "/Site created with <a href="http:\/\/www.syndeocms.org[\/]?">SyndeoCMS<\/a>/" },
			{ "version" : "/<div class="meta"><center>Powered by <a href="http:\/\/www.syndeoCMS.org\/" target="_blank">SyndeoCMS ([\d\.]+)<\/a>/" },
			{ "text" : "<!-- Please don't remove my credits! I worked hard to create this theme and distribute it freely. Thanks! -->" },
		]
	return(self.rules)
