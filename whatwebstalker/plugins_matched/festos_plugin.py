import plugins
			
class Pluginfestos_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by[\ FestOS,]* <a href="http:\/\/[festengine.org\/|www.festengine.org\/|skypanther.com\/festos.php]+" title="FestOS", "[the\ festival\ engine|the\ Festival\ Engine|the\ web\-based\ festival\ manager]+"[\ target="_blank"]*>[FestOS|FestOS&trade;|www.festengine.org]+<\/a>/" },
			{ "text" : "	<meta name="author" content="FestOS by Skypanther Studios">" },
			{ "text" : "	<meta name="author" content="Skypanther Studios">", "certainty" : "75 },
		]
		return(self.rules)
