import plugins
			
class Pluginfluxbb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "Powered by", "regexp" : "/>P(owered by|ropuls&#233; par) (<strong>)?<a href="http:\/\/fluxbb\.org\/">FluxBB<\/a>/" },
			{ "version" : "/>P(owered by|ropuls&#233; par) <a href="http:\/\/fluxbb\.org\/">FluxBB<\/a> ([\d\.]+)</", "offset" : "1 },
			{ "certainty" : "25", "regexp" : "/<link rel="stylesheet" type="text\/css" href="style\/(Cobalt|Lithium|Mercury|Oxygen|Radium|Sulfur)\.css" \/>/" },
			{ "certainty" : "75", "text" : "<li id="navlogin"><a href="login.php">" },
			{ "certainty" : "75", "regexp" : "/<div id="brdwelcome" class="inbox">[\s]+<p>[^<]+<\/p>[\s]+<\/div>/" },
		]
			return(self.rules)
