import plugins
			
class Plugintestlink_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<meta name="author" content="Martin Havlat" />" },
			{ "version" : "/\.png" \/>[\s]*<br \/>TestLink ([^\s^<]+)/" },
			{ "text" : "TestLink project <a href="http://testlink.sourceforge.net/docs/testLink.php">Home</a><br />" },
			{ "regexp" : "/<html><head><\/head><body><script type='text\/javascript'>location\.href='https?:\/\/[^\'^\?]+\/login\.php\?note=expired';<\/script><\/body><\/html>/" },
		]
	return(self.rules)

