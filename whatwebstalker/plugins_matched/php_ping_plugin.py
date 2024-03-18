import plugins
			
class Pluginphp_ping_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "Enter ip" inurl:"php-ping.php"", "certainty" : "75 },
			{ "regexp" : "/<form methode="post" action="[^>]*>[\s]*Enter IP or Host[^<]*<[^<]*type="text" name="host" value="[\d\.]*"><\/input>[\s]*Enter Count[^>]*name="count" size="2" value="4"><\/input>[^>]*[\s]*<input type="submit"[^>]*name="submit" value="Ping!"><\/input><\/form><br><b><\/b>/" },
		]
		return(self.rules)

