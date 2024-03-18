import plugins
			
class Pluginx10media_mp3_search_engine_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "	<meta name="copyright" content="X10Media"/>", "certainty" : "75 },
			{ "text" : "	<meta name="contributor" content="X10Media"/>", "certainty" : "75 },
			{ "text" : "<title>x10media Mp3 Search Engine</title>" },
			{ "text" : "Powered by <a href="http://www.x10media.com">x10media.com</a> a <a href="http://www.x10media.com/mp3-script.php">MP3 Search Script</a>" },
			{ "text" : "Cannot connect to the database. Possibly", "the X10Media Mp3 Search engine is not installed. Click <a href="install/">here</a>", "to install it." },
			{ "version" : "/<meta name="publisher" content="x10media`s Mp3 Search Engine V\.([\d\.]+)"\/>/" },
			{ "version" : "/<meta name="dc\.rights" content="x10media`s Mp3 Search Engine V\.([\d\.]+)"\/>/" },
			{ "version" : "/<meta name="dc\.publisher" content="x10media`s Mp3 Search Engine V\.([\d\.]+)"\/>/" },
			{ "version" : "/<meta name="owner" content="x10media`s Mp3 Search Engine V\.([\d\.]+)"\/>/" },
			{ "version" : "/<title>x10media`s Mp3 Search Engine V\.([\d\.]+)[\ Installer]*<\/title>/" },
		]
	return(self.rules)

