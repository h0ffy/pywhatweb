import plugins
			
class Pluginpligg_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered [Bb]y:? <a href="http:\/\/www.pligg.com\/?"( target="_blank")?>(Powered By )?Pligg( CMS)?<\/a>/" },
			{ "text" : "jQuery.jTwitter('pligg", "function (userdata) {" },
			{ "md5" : "7c548077f2a8cc6099858eb1bf9201b4", "url" : "/favicon.ico" },
		]
	return(self.rules)
