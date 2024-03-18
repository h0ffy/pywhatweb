import plugins
			
class Pluginmailman_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "inurl:mailman "Delivered by Mailman"'},
			{ "regexp" : "/<td><a[^>]+href="[^"]+\/listinfo\/[^"]+"><strong>[^<]+<\/strong><\/a><\/td>/" },
			{ "version" : "/<td><img src="[^"]+\/mailman.jpg" alt="Delivered by Mailman"[^>]+><br>version (\d.\d.[0-9a-z]+)/" },
			{ "version" : "/<td><a href="http:\/\/www.gnu.org\/software\/mailman\/index.html">Delivered by Mailman<br>version (\d.\d.[0-9a-z]+)<\/a>/" },
		]
		return(self.rules)

