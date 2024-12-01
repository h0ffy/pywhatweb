import plugins
			
class Pluginnexusphp_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta name="generator" content="NexusPHP"[\s]?\/>/" },
			{ "text" : "<p><b>Note</b>: You need cookies enabled to log in or switch language.<br /> [<b>" },
			{ "text" : "<tr><td class="rowhead">SSL (HTTPS):</td><td class="rowfollow" align="left"><input class="checkbox" type="checkbox" name="ssl" value="yes"" },
			{ "string" : /<\/a> (20[\d]{2})-20[\d]{2} Powered by <a href="aboutnexus\.php">NexusPHP<\/a>/" },
		]
	return(self.rules)
