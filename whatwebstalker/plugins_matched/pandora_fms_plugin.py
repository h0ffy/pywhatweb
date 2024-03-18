import plugins
			
class Pluginpandora_fms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Pandora FMS - the Flexible Monitoring System</title>" },
			{ "text" : "<link rel="alternate" href="operation/events/events_rss.php" title="Pandora RSS Feed" type="application/rss+xml" />" },
			{ "version" : "/<img src="images\/pandora_logo\.png" style="border:0px;" alt="logo" \/><\/a><br \/>v([^<]+)<\/td><td class="f9b">/" },
		]
	return(self.rules)

